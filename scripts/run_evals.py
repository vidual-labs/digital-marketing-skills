#!/usr/bin/env python3
"""Run a skill's eval prompts through any LLM command and grade the output.

The runner is agent-agnostic: it pipes a prompt (skill body + task) to a shell
command on stdin and reads the model's answer from stdout. The default command
is the Claude Code CLI (``claude -p``), but anything that reads stdin and writes
stdout works, e.g. ``ollama run llama3`` or your own wrapper script.

Usage:
    python3 scripts/run_evals.py --skill google-ads-keywords
    python3 scripts/run_evals.py --all --runner "claude -p --output-format text"
    python3 scripts/run_evals.py --skill tiktok-ads --dry-run     # print prompts only
    python3 scripts/run_evals.py --skill tiktok-ads --grade-only  # re-grade saved outputs

Outputs land in ``eval-results/<skill>/<eval-id>-<name>.md`` plus a
``summary.json`` per skill. Machine checks (``checks`` in evals.json) are
evaluated automatically; the human/LLM ``assertions`` are printed next to each
output so a reviewer or grader model can judge them.

Exit code is 0 when every machine check passes, 1 otherwise.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"
RESULTS_ROOT = REPO_ROOT / "eval-results"

PROMPT_TEMPLATE = """You are an expert digital marketer. The following skill document defines how to
approach the task. Follow its workflow, output format and verification checklist
exactly. If the task lacks data the skill needs, say what is missing and proceed
with clearly labelled assumptions rather than inventing figures.

<skill>
{skill}
</skill>

<task>
{task}
</task>
"""


def find_skill_dir(name: str) -> Path:
    matches = [p.parent for p in SKILLS_ROOT.rglob("SKILL.md") if p.parent.name == name]
    if not matches:
        sys.exit(f"skill '{name}' not found under {SKILLS_ROOT}")
    return matches[0]


def skill_body(skill_dir: Path) -> str:
    text = (skill_dir / "SKILL.md").read_text(encoding="utf-8")
    end = text.find("\n---\n", 4)
    return text[end + 5 :] if text.startswith("---\n") and end != -1 else text


def run_check(check: dict, output: str) -> tuple[bool, str]:
    ctype = check["type"]
    flags = re.I | re.M
    if ctype == "contains":
        ok = check["value"].lower() in output.lower()
        return ok, f"contains {check['value']!r}"
    if ctype == "not_contains":
        ok = check["value"].lower() not in output.lower()
        return ok, f"does not contain {check['value']!r}"
    if ctype == "regex":
        ok = re.search(check["pattern"], output, flags) is not None
        return ok, f"matches /{check['pattern']}/"
    if ctype == "not_regex":
        ok = re.search(check["pattern"], output, flags) is None
        return ok, f"no match for /{check['pattern']}/"
    if ctype == "min_count":
        n = len(re.findall(check["pattern"], output, flags))
        ok = n >= check["count"]
        return ok, f"at least {check['count']} matches of /{check['pattern']}/ (found {n})"
    return False, f"unknown check type {ctype!r}"


def call_runner(runner: str, prompt: str, timeout: int) -> str:
    proc = subprocess.run(
        runner, shell=True, input=prompt, capture_output=True, text=True, timeout=timeout
    )
    if proc.returncode != 0:
        raise RuntimeError(f"runner exited {proc.returncode}: {proc.stderr.strip()[:500]}")
    return proc.stdout


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60]


def run_skill(name: str, args: argparse.Namespace) -> bool:
    skill_dir = find_skill_dir(name)
    evals_path = skill_dir / "evals" / "evals.json"
    data = json.loads(evals_path.read_text(encoding="utf-8"))
    body = skill_body(skill_dir)
    out_dir = RESULTS_ROOT / name
    out_dir.mkdir(parents=True, exist_ok=True)

    all_ok = True
    summary = {"skill": name, "version": data.get("version"), "runner": args.runner, "evals": []}
    print(f"\n=== {name} ({len(data['evals'])} evals) ===")

    for ev in data["evals"]:
        eid = ev["id"]
        label = f"{eid}-{slug(ev['name'])}"
        out_file = out_dir / f"{label}.md"
        prompt = PROMPT_TEMPLATE.format(skill=body, task=ev["prompt"])

        if args.dry_run:
            print(f"\n--- eval {eid}: {ev['name']} ---\n{ev['prompt']}\n")
            continue

        if args.grade_only:
            if not out_file.exists():
                print(f"  [{eid}] no saved output at {out_file}; skipping")
                continue
            output = out_file.read_text(encoding="utf-8").split("\n## Model output\n", 1)[-1]
        else:
            try:
                output = call_runner(args.runner, prompt, args.timeout)
            except Exception as exc:  # noqa: BLE001
                print(f"  [{eid}] runner failed: {exc}")
                all_ok = False
                summary["evals"].append({"id": eid, "name": ev["name"], "error": str(exc)})
                continue

        results = [run_check(c, output) for c in ev.get("checks", [])]
        passed = all(ok for ok, _ in results)
        all_ok = all_ok and passed
        status = "PASS" if passed else "FAIL"
        print(f"  [{eid}] {status}  {ev['name']}")
        for ok, desc in results:
            print(f"        {'ok ' if ok else 'XX '} {desc}")

        report = [
            f"# {name} — eval {eid}: {ev['name']}",
            "",
            "## Prompt",
            "",
            ev["prompt"],
            "",
            "## Expected",
            "",
            ev["expected_output"],
            "",
            "## Assertions (judge manually or with a grader model)",
            "",
            *[f"- [ ] {a}" for a in ev.get("assertions", [])],
            "",
            "## Machine checks",
            "",
            *[f"- {'PASS' if ok else 'FAIL'}: {desc}" for ok, desc in results],
            "",
            "## Model output",
            "",
            output.strip(),
            "",
        ]
        out_file.write_text("\n".join(report), encoding="utf-8")
        summary["evals"].append(
            {
                "id": eid,
                "name": ev["name"],
                "passed_checks": sum(1 for ok, _ in results if ok),
                "total_checks": len(results),
                "output_file": str(out_file.relative_to(REPO_ROOT)),
            }
        )

    if not args.dry_run:
        (out_dir / "summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    return all_ok


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--skill", help="skill directory name, e.g. tiktok-ads")
    group.add_argument("--all", action="store_true", help="run every skill")
    parser.add_argument(
        "--runner",
        default="claude -p --output-format text",
        help="shell command that reads the prompt on stdin and prints the answer (default: Claude Code CLI)",
    )
    parser.add_argument("--timeout", type=int, default=600, help="seconds per eval (default 600)")
    parser.add_argument("--dry-run", action="store_true", help="print prompts without calling the runner")
    parser.add_argument("--grade-only", action="store_true", help="re-run machine checks on saved outputs")
    args = parser.parse_args()

    names = (
        sorted(p.parent.name for p in SKILLS_ROOT.rglob("SKILL.md")) if args.all else [args.skill]
    )
    ok = True
    for name in names:
        ok = run_skill(name, args) and ok
    if not args.dry_run:
        print("\nAll machine checks passed." if ok else "\nSome machine checks failed.")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
