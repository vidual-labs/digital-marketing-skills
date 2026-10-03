#!/usr/bin/env python3
"""Structural validation for every skill in this repository.

Checks each ``skills/**/SKILL.md`` against the skill contract described in
CONTRIBUTING.md and each ``evals/evals.json`` against the eval schema.

Usage:
    python3 scripts/validate_skills.py            # validate everything
    python3 scripts/validate_skills.py --quiet    # only print failures
    python3 scripts/validate_skills.py skills/marketing/tiktok-ads

Exit code 0 when everything passes, 1 when any check fails.

Only the Python standard library is required. PyYAML is used when available;
otherwise a small parser handles the YAML subset used in our frontmatter.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"
README = REPO_ROOT / "README.md"

REQUIRED_FRONTMATTER = ["name", "description", "version", "license"]
REQUIRED_SECTIONS = [
    "## Overview",
    "## When to Use",
    "## Inputs",
    "## Output Format",
    "## Common Pitfalls",
    "## Verification Checklist",
]
MAX_BODY_LINES = 500
MAX_DESCRIPTION_CHARS = 1024
MAX_COMPATIBILITY_CHARS = 500
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
SEMVER_PATTERN = re.compile(r"^\d+\.\d+\.\d+$")
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")
VALID_CHECK_TYPES = {"contains", "not_contains", "regex", "not_regex", "min_count"}
FORBIDDEN_BODY_PATTERNS = [
    (re.compile(r"hermes", re.I), "agent-specific wording ('Hermes') — skills must stay agent-neutral"),
]


# --------------------------------------------------------------------------- #
# Frontmatter parsing
# --------------------------------------------------------------------------- #
def split_frontmatter(text: str) -> tuple[str, str]:
    """Return (frontmatter_yaml, body). Raises ValueError when malformed."""
    if not text.startswith("---\n"):
        raise ValueError("file must start with a '---' frontmatter block")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("frontmatter block is not closed with '---'")
    return text[4:end], text[end + 5 :]


def _parse_scalar(raw: str):
    raw = raw.strip()
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        if not inner:
            return []
        return [_parse_scalar(item) for item in inner.split(",")]
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    if raw in ("true", "false"):
        return raw == "true"
    return raw


def parse_simple_yaml(text: str) -> dict:
    """Parse the YAML subset used in frontmatter: scalars, flow lists, nested maps."""
    root: dict = {}
    stack: list[tuple[int, dict]] = [(-1, root)]
    for raw_line in text.splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue
        indent = len(raw_line) - len(raw_line.lstrip(" "))
        line = raw_line.strip()
        if ":" not in line:
            raise ValueError(f"cannot parse frontmatter line: {raw_line!r}")
        key, _, value = line.partition(":")
        key = key.strip()
        while stack and indent <= stack[-1][0]:
            stack.pop()
        parent = stack[-1][1]
        if value.strip() == "":
            child: dict = {}
            parent[key] = child
            stack.append((indent, child))
        else:
            parent[key] = _parse_scalar(value)
    return root


def parse_frontmatter(text: str) -> dict:
    try:
        import yaml  # type: ignore

        data = yaml.safe_load(text)
        if not isinstance(data, dict):
            raise ValueError("frontmatter must be a mapping")
        return data
    except ImportError:
        return parse_simple_yaml(text)


# --------------------------------------------------------------------------- #
# Checks
# --------------------------------------------------------------------------- #
class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.passed: list[str] = []

    def fail(self, where: str, msg: str) -> None:
        self.errors.append(f"{where}: {msg}")

    def ok(self, where: str) -> None:
        self.passed.append(where)


def discover_skill_dirs(targets: list[str]) -> list[Path]:
    if targets:
        dirs = [Path(t).resolve() for t in targets]
    else:
        dirs = sorted(p.parent for p in SKILLS_ROOT.rglob("SKILL.md"))
    return dirs


def all_skill_names() -> set[str]:
    return {p.parent.name for p in SKILLS_ROOT.rglob("SKILL.md")}


def check_skill(skill_dir: Path, known_names: set[str], report: Report) -> dict | None:
    rel = skill_dir.relative_to(REPO_ROOT)
    skill_md = skill_dir / "SKILL.md"
    where = str(rel / "SKILL.md")

    errors_before = len(report.errors)
    if not skill_md.exists():
        report.fail(where, "SKILL.md missing")
        return None

    text = skill_md.read_text(encoding="utf-8")
    try:
        fm_text, body = split_frontmatter(text)
        fm = parse_frontmatter(fm_text)
    except ValueError as exc:
        report.fail(where, f"frontmatter: {exc}")
        return None

    # Required keys
    for key in REQUIRED_FRONTMATTER:
        if key not in fm or fm[key] in ("", None):
            report.fail(where, f"frontmatter missing required field '{key}'")

    name = str(fm.get("name", ""))
    if name and not NAME_PATTERN.match(name):
        report.fail(where, f"name '{name}' must be lowercase letters, digits and single hyphens")
    if name and len(name) > 64:
        report.fail(where, "name exceeds 64 characters")
    if name and name != skill_dir.name:
        report.fail(where, f"name '{name}' does not match directory '{skill_dir.name}'")

    description = str(fm.get("description", ""))
    if description and len(description) > MAX_DESCRIPTION_CHARS:
        report.fail(where, f"description exceeds {MAX_DESCRIPTION_CHARS} characters")
    if description and not re.search(r"\b(use when|use this|trigger|load this)\b", description, re.I):
        report.fail(where, "description should state when to trigger (e.g. 'Use when ...')")

    version = str(fm.get("version", ""))
    if version and not SEMVER_PATTERN.match(version):
        report.fail(where, f"version '{version}' is not semver (MAJOR.MINOR.PATCH)")

    if "compatibility" in fm and len(str(fm["compatibility"])) > MAX_COMPATIBILITY_CHARS:
        report.fail(where, f"compatibility exceeds {MAX_COMPATIBILITY_CHARS} characters")

    metadata = fm.get("metadata") or {}
    if not isinstance(metadata, dict):
        report.fail(where, "metadata must be a mapping")
        metadata = {}
    for key in ("category", "updated", "tags", "related_skills"):
        if key not in metadata:
            report.fail(where, f"metadata.{key} missing")
    updated = str(metadata.get("updated", ""))
    if updated and not DATE_PATTERN.match(updated):
        report.fail(where, f"metadata.updated '{updated}' must be YYYY-MM-DD")
    for related in metadata.get("related_skills", []) or []:
        if related not in known_names:
            report.fail(where, f"related_skills references unknown skill '{related}'")
        if related == name:
            report.fail(where, "related_skills must not reference the skill itself")
    tags = metadata.get("tags", []) or []
    if isinstance(tags, list) and len(tags) < 3:
        report.fail(where, "metadata.tags should list at least 3 tags")

    # Body structure
    body_lines = body.splitlines()
    if len(body_lines) > MAX_BODY_LINES:
        report.fail(where, f"body is {len(body_lines)} lines; keep SKILL.md under {MAX_BODY_LINES}")
    if not re.search(r"^# \S", body, re.M):
        report.fail(where, "body must start with a '# Title' heading")
    last_index = -1
    for section in REQUIRED_SECTIONS:
        matches = [i for i, line in enumerate(body_lines) if line.strip() == section]
        if not matches:
            report.fail(where, f"missing required section '{section}'")
            continue
        if matches[0] < last_index:
            report.fail(where, f"section '{section}' is out of order")
        last_index = matches[0]

    if "```" in body and body.count("```") % 2 != 0:
        report.fail(where, "unbalanced ``` code fences")

    checklist = re.findall(r"^- \[ \] ", body, re.M)
    if len(checklist) < 5:
        report.fail(where, "Verification Checklist should contain at least 5 '- [ ]' items")

    for pattern, message in FORBIDDEN_BODY_PATTERNS:
        if pattern.search(body) or pattern.search(fm_text):
            report.fail(where, message)

    # Skill-to-skill references must resolve
    for ref in set(re.findall(r"`([a-z0-9]+(?:-[a-z0-9]+)+)`", body)):
        if ref in known_names or ref == name:
            continue
        # Only flag identifiers that look like one of our skill names (contain a known suffix)
        if ref.endswith(("-organic", "-ads", "-diagnostics", "-keywords", "-research", "-positioning", "-funnel", "-debugging", "-seo", "-creative")):
            report.fail(where, f"references unknown skill '{ref}'")

    if len(report.errors) == errors_before:
        report.ok(where)
    return fm


def check_evals(skill_dir: Path, fm: dict | None, report: Report) -> None:
    rel = skill_dir.relative_to(REPO_ROOT)
    evals_path = skill_dir / "evals" / "evals.json"
    where = str(rel / "evals" / "evals.json")
    errors_before = len(report.errors)
    if not evals_path.exists():
        report.fail(where, "missing evals/evals.json (every skill needs test prompts)")
        return
    try:
        data = json.loads(evals_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        report.fail(where, f"invalid JSON: {exc}")
        return

    if data.get("skill_name") != skill_dir.name:
        report.fail(where, f"skill_name must be '{skill_dir.name}'")
    if fm and data.get("version") != fm.get("version"):
        report.fail(where, f"version '{data.get('version')}' does not match SKILL.md version '{fm.get('version')}'")

    evals = data.get("evals")
    if not isinstance(evals, list) or len(evals) < 3:
        report.fail(where, "need at least 3 evals")
        return

    seen_ids: set = set()
    for ev in evals:
        eid = ev.get("id")
        label = f"eval {eid!r}"
        if eid in seen_ids:
            report.fail(where, f"{label}: duplicate id")
        seen_ids.add(eid)
        for key in ("id", "name", "prompt", "expected_output", "assertions"):
            if key not in ev:
                report.fail(where, f"{label}: missing '{key}'")
        if len(str(ev.get("prompt", ""))) < 60:
            report.fail(where, f"{label}: prompt is too short to be realistic (< 60 chars)")
        assertions = ev.get("assertions", [])
        if not isinstance(assertions, list) or len(assertions) < 2:
            report.fail(where, f"{label}: need at least 2 assertions")
        checks = ev.get("checks", [])
        if not isinstance(checks, list) or not checks:
            report.fail(where, f"{label}: need at least 1 machine check in 'checks'")
            continue
        for chk in checks:
            ctype = chk.get("type")
            if ctype not in VALID_CHECK_TYPES:
                report.fail(where, f"{label}: unknown check type {ctype!r}")
                continue
            if ctype in ("contains", "not_contains") and not chk.get("value"):
                report.fail(where, f"{label}: '{ctype}' check needs 'value'")
            if ctype in ("regex", "not_regex", "min_count"):
                pattern = chk.get("pattern", "")
                try:
                    re.compile(pattern, re.I | re.M)
                except re.error as exc:
                    report.fail(where, f"{label}: bad regex {pattern!r}: {exc}")
                if ctype == "min_count" and not isinstance(chk.get("count"), int):
                    report.fail(where, f"{label}: 'min_count' check needs integer 'count'")
    if len(report.errors) == errors_before:
        report.ok(where)


def check_readme(skill_names: set[str], report: Report) -> None:
    if not README.exists():
        report.fail("README.md", "missing")
        return
    text = README.read_text(encoding="utf-8")
    errors_before = len(report.errors)
    for name in sorted(skill_names):
        if f"/{name}/SKILL.md" not in text:
            report.fail("README.md", f"skill '{name}' is not linked in README")
    if len(report.errors) == errors_before:
        report.ok("README.md")


def main(argv: list[str]) -> int:
    quiet = "--quiet" in argv
    targets = [a for a in argv if not a.startswith("--")]
    report = Report()
    known = all_skill_names()
    dirs = discover_skill_dirs(targets)
    if not dirs:
        print("No skills found.")
        return 1
    for skill_dir in dirs:
        fm = check_skill(skill_dir, known, report)
        check_evals(skill_dir, fm, report)
    if not targets:
        check_readme(known, report)

    if not quiet:
        for item in report.passed:
            print(f"PASS  {item}")
    for err in report.errors:
        print(f"FAIL  {err}")
    print(f"\n{len(dirs)} skill(s) checked, {len(report.errors)} problem(s).")
    return 1 if report.errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
