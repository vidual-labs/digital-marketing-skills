# Contributing

Every skill in this repository follows one contract so that it stays **universal** (works in any agent that reads `SKILL.md`), **testable** (structure is machine-checked, behaviour has eval prompts) and **maintainable** (versioned, dated, changelogged).

## Skill layout

```
skills/marketing/<skill-name>/
├── SKILL.md            # the skill — frontmatter + instructions
└── evals/
    └── evals.json      # 3+ realistic test prompts with assertions and machine checks
```

## Frontmatter contract

```yaml
---
name: skill-name                      # lowercase, hyphens, must equal the directory name
description: Use when ... Also use when ... Don't use for ...   # ≤ 1024 chars, states the trigger
version: 1.1.0                        # semver — bump on every content change
author: vidual-labs
license: MIT
compatibility: ...                    # ≤ 500 chars, what the skill needs (usually nothing)
metadata:
  category: paid-search | paid-social | organic-social | conversion-tracking | brand | competitive-intelligence
  updated: YYYY-MM-DD                 # last date the platform facts were verified
  tags: [at, least, three]
  related_skills: [other-skill-names] # must exist in this repo
---
```

`name` and `description` are the only fields the [Agent Skills spec](https://agentskills.io/specification) requires; everything else is optional metadata that spec-compliant runtimes ignore. Never add fields that only one agent understands and never mention a specific agent in the body — the skills must read the same in Claude Code, Cursor, Codex, Hermes, a custom GPT or a pasted chat.

## Body contract (sections in this order)

| Section | Purpose |
|---------|---------|
| `# Title` | Human-readable name |
| `## Overview` | What the skill produces, in 2–4 sentences |
| `## When to Use` | Trigger scenarios and an explicit *Don't use for* line pointing to sibling skills |
| `## Inputs` | What to ask the user for, and the data-handling rules (no invented metrics, label assumptions, say when a URL can't be fetched) |
| *domain sections* | Frameworks, tables, decision rules — explain the *why*, prefer tables over prose |
| `## Output Format` | A fixed template in a code block so outputs are comparable and gradeable |
| `## Common Pitfalls` | Numbered, each with the fix |
| `## Verification Checklist` | `- [ ]` items (≥ 5) the agent ticks before answering |

Keep `SKILL.md` under 500 lines. If you need more, move reference material into `references/` and link to it.

### Writing rules

- Imperative voice, explain the reasoning, avoid shouting (`ALWAYS`, `NEVER`) except for genuine safety rails.
- Platform facts (limits, feature names, algorithm signals) go in tables and carry the `metadata.updated` date. When you change one, bump `version` and update `updated`.
- Benchmarks are *starting points*. Phrase them so the agent prefers the user's own data when available.
- Currency and locale neutral: use `$` only as an example unit, and tell the agent to use the account's currency.
- Never assume the agent can browse. Every audit skill must describe what to request from the user when a URL cannot be fetched.

## Eval contract (`evals/evals.json`)

```json
{
  "skill_name": "skill-name",
  "version": "1.1.0",
  "evals": [
    {
      "id": 1,
      "name": "short-kebab-case-name",
      "prompt": "A realistic user request, 60+ characters, with concrete details.",
      "files": [],
      "expected_output": "What a good answer contains.",
      "assertions": ["Human/LLM-judged statements about quality", "..."],
      "checks": [
        {"type": "contains", "value": "NEGATIVE KEYWORDS"},
        {"type": "regex", "pattern": "^AD GROUP:"},
        {"type": "not_regex", "pattern": "^\\s*[-*] "},
        {"type": "min_count", "pattern": "^--- Ad Variation", "count": 3}
      ]
    }
  ]
}
```

- `assertions` are judged by a human or a grader model.
- `checks` are deterministic and run automatically (`contains`, `not_contains`, `regex`, `not_regex`, `min_count`; regexes are case-insensitive and multiline).
- `version` must match the `SKILL.md` version so stale evals fail validation.

## Running the tests

```bash
# Structural tests — no model, no network, standard library only
python3 scripts/validate_skills.py

# Behavioural tests — pipes each eval prompt plus the skill into an LLM command
python3 scripts/run_evals.py --skill tiktok-ads                       # Claude Code CLI by default
python3 scripts/run_evals.py --all --runner "ollama run llama3"      # any stdin→stdout command
python3 scripts/run_evals.py --skill tiktok-ads --dry-run            # just print the prompts
```

Results are written to `eval-results/` (git-ignored) with the model output, machine-check results and the assertions to judge.

## Versioning

- **PATCH** (1.1.x): typo, clarification, no change in behaviour or facts.
- **MINOR** (1.x.0): updated platform facts, new section, new eval, changed benchmarks.
- **MAJOR** (x.0.0): changed output format or trigger scope in a way that breaks downstream prompts.

Record every bump in `CHANGELOG.md`.

## Pull requests

CI runs `scripts/validate_skills.py` on every push and PR. A PR that changes a skill must bump its version, update `metadata.updated` if facts changed, keep its evals in sync, and add a changelog line.
