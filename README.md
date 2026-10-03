
```
    ____  __  ___   _____ __ __ ______    __   _____
   / __ \/  |/  /  / ___// //_//  / /   / /  / ___/
  / / / / /|_/ /   \__ \/ ,<   / // /   / /   \__ \
 / /_/ / /  / /   ___/ / /| |_/ // /___/ /______/ /
/_____/_/  /_/   /____/_/ |_/___/_____/_____/____/
```
# Digital-Marketing-Skills


A collection of Agent Skills for digital marketing — paid ads, organic social, campaign diagnostics, tracking, competitive intelligence, brand positioning, and brand identity.

Each skill is a self-contained `SKILL.md`: a `description:` trigger, an **Inputs** section that says what data to ask for (and forbids inventing metrics), a decision framework with current platform facts, a fixed output format, common pitfalls, and a verification checklist. Every skill ships with `evals/evals.json` — realistic test prompts with assertions and machine checks — and the repo validates structure in CI.

The skills are agent-agnostic (Claude Code, Claude.ai, Cursor, Codex, Hermes, custom GPTs, pasted into any chat) and versioned: platform facts carry an `updated` date, and every change bumps the version (see [CHANGELOG.md](CHANGELOG.md)). **Current version: 1.1.0** (platform facts verified October 2026).

## Skills

### Paid & Search

| Skill | Description |
|-------|-------------|
| **[meta-ads-creative](skills/marketing/meta-ads-creative/SKILL.md)** | Creative concepts and copy for Meta (Facebook/Instagram) ads. Hook formulas, primary text, headlines, descriptions, CTA selection, and creative format guidance. |
| **[meta-ads-diagnostics](skills/marketing/meta-ads-diagnostics/SKILL.md)** | Analyze Meta Ads performance data and propose concrete campaign changes — budget allocation, targeting, lookalikes, bid strategy, learning phase, and placement optimization. |
| **[google-ads-keywords](skills/marketing/google-ads-keywords/SKILL.md)** | Keyword generation for Google Ads. Exact match `[keyword]` and phrase match `"keyword"` only — no broad match. Comma-separated, tightly themed ad groups with negative keywords. |
| **[google-ads-diagnostics](skills/marketing/google-ads-diagnostics/SKILL.md)** | Analyze Google Ads performance — keyword quality, search term negatives, Quality Score, bid strategy, ad copy, and budget optimization. |
| **[tiktok-ads](skills/marketing/tiktok-ads/SKILL.md)** | Native-first TikTok ad creatives and copy. Hook formulas, second-by-second scripts, in-app ad text, format guidance, and testing strategy. |

### Organic Social

| Skill | Description |
|-------|-------------|
| **[instagram-organic](skills/marketing/instagram-organic/SKILL.md)** | Profile audit, content pillars, posting schedule, and follower growth tactics — optimized for Reels, carousels, and the engagement flywheel. |
| **[linkedin-organic](skills/marketing/linkedin-organic/SKILL.md)** | Profile/page audit, writing-first strategy, comment flywheel, content pillars, and B2B thought leadership growth. |
| **[youtube-organic](skills/marketing/youtube-organic/SKILL.md)** | Channel audit, traffic source analysis, thumbnail/title strategy, retention optimization, and subscriber growth tactics. |
| **[pinterest-organic](skills/marketing/pinterest-organic/SKILL.md)** | Board structure, keyword-rich pin strategy, posting schedule, and visual search optimization — optimized for outbound clicks. |

### Conversion & Tracking

| Skill | Description |
|-------|-------------|
| **[geo-ai-seo](skills/marketing/geo-ai-seo/SKILL.md)** | Generative Engine Optimization — content structure and text formation for AI search (Google AI Overviews, Perplexity, ChatGPT). Answer-first architecture, data anchors, citation-signal optimization. |
| **[landing-page-funnel](skills/marketing/landing-page-funnel/SKILL.md)** | Landing page conversion optimization — funnel structure, ad-to-page congruence, form optimization, social proof, CRO testing, and copy analysis. |
| **[gtm-debugging](skills/marketing/gtm-debugging/SKILL.md)** | Diagnose and fix Google Tag Manager bugs — missing triggers, broken tags, data layer issues, consent mode, cross-domain tracking, and duplicate events. |

### Brand & Positioning

| Skill | Description |
|-------|-------------|
| **[branding](skills/marketing/branding/SKILL.md)** | Build a complete brand identity system — visual identity (colors, typography, imagery, layout), brand voice (attributes, tone matrix, vocabulary), copy standards by channel, and touchpoint consistency. |
| **[market-positioning](skills/marketing/market-positioning/SKILL.md)** | Define where your brand sits vs. competitors — perceptual mapping, distance-from-competition scoring, audience alignment, positioning statement, message house, and consistency audit. |

### Competitive Intelligence

| Skill | Description |
|-------|-------------|
| **[competitor-research](skills/marketing/competitor-research/SKILL.md)** | Identify competitors across 3 layers (direct, indirect, adjacent), audit their digital presence, run a SWOT, and find actionable market gaps. |

## Install & Use

### CLI install (recommended)

These skills follow the open [Agent Skills](https://github.com/vercel-labs/skills) format, so you can install them straight from this repo with the community `skills` CLI — no cloning, no copy-pasting into your agent's config:

```bash
npx skills add vidual-labs/digital-marketing-skills
```

It detects which coding agents you have installed (Claude Code, Cursor, and 70+ others) and asks where to put the skills. A few useful flags:

```bash
npx skills add vidual-labs/digital-marketing-skills -l               # list skills without installing
npx skills add vidual-labs/digital-marketing-skills -s tiktok-ads meta-ads-creative   # install specific skills only
npx skills add vidual-labs/digital-marketing-skills -g               # install globally instead of per-project
npx skills update vidual-labs/digital-marketing-skills               # pull the latest versions later
```

`skills` is a third-party open-source tool (not built or maintained by this repo or by Anthropic) — reasonable to run for a quick install, but read [its source](https://github.com/vercel-labs/skills) first if you'd rather not run an unfamiliar `npx` package. Everything below is the manual alternative for anyone who prefers that, or who's on a platform the CLI doesn't cover.

### In any Agent Skills runtime (Cursor, Codex, Hermes, …)

The files follow the [Agent Skills specification](https://agentskills.io/specification): only `name` and `description` are required, and runtimes ignore frontmatter they don't know. Copy the skill folders into whatever directory your agent reads skills from, for example:

```bash
cp -r skills/marketing/* ~/.hermes/skills/        # Hermes Agent
cp -r skills/marketing/* .cursor/skills/           # Cursor (project)
cp -r skills/marketing/* ~/.codex/skills/          # Codex
```

Each skill's `description:` acts as the trigger: the agent loads the skill when your request matches (e.g., "write TikTok ad copy" → `tiktok-ads`).

### In Claude

Claude supports the same Agent Skills format these files use (`SKILL.md` with a `description:` trigger), so you can use them directly.

**Claude Code (auto-loading)**

Drop the skills into a skills directory Claude Code reads — a project-level `.claude/skills/` or your personal `~/.claude/skills/`:

```bash
cp -r skills/marketing ~/.claude/skills/
```

Claude Code discovers each skill by its `description:` and loads it automatically when your request matches.

**Claude apps (Settings → Capabilities → Skills)**

If your plan exposes Skills in the Claude apps, add each `SKILL.md` as a skill there. Claude invokes it when your prompt matches the trigger.

**Manual paste (works everywhere, one conversation)**

1. Open any Claude conversation
2. Paste the content of the SKILL.md you need (the framework below the `---` frontmatter is enough)
3. Add your request below it

For a reusable setup, paste the skills you use most into Claude Settings → Custom Instructions (or a Project's instructions), prefaced with:

```
You are a digital marketing strategist. When I give you a marketing task, use the skill framework below to guide your response — follow its structure, output format, and verification checklist.
```

### In ChatGPT

**Custom Instructions (simplest)**

1. Go to Settings → Personalization → Custom Instructions
2. Paste the skills most relevant to your work (custom instructions have a length cap, so pick your top 3–5 skills)
3. Preface them with:

```
You are a digital marketing strategist. When I give you a marketing task, use the skill framework below to guide your response.
```

**Upload a file (one conversation)**

1. Combine the SKILL.md files you need into a single `marketing-skills.md`
2. Upload it in your chat
3. Prompt: "Read this file — it's my marketing workflow framework. Follow its structure for all marketing tasks in this conversation."

**Build a custom GPT (reusable, shareable)**

1. Create a new GPT (Explore GPTs → Create)
2. Name it "Digital Marketing Strategist"
3. Paste the SKILL.md content (minus frontmatter) into **Instructions**
4. Upload the combined `marketing-skills.md` into **Knowledge** as backup
5. Enable Web Search (for competitor research) and Code Interpreter (for data analysis)
6. Save — you get a dedicated, permanently-skilled GPT you can share with your team

## Testing

Two layers, both agent-independent:

```bash
# 1. Structural tests (no model, no network, standard library only) — also runs in CI
python3 scripts/validate_skills.py

# 2. Behavioural tests — pipes each eval prompt plus the skill into any LLM command
python3 scripts/run_evals.py --skill tiktok-ads                   # Claude Code CLI by default
python3 scripts/run_evals.py --all --runner "ollama run llama3"  # any stdin → stdout command
python3 scripts/run_evals.py --skill tiktok-ads --dry-run        # just print the prompts
```

The validator checks frontmatter, section order, cross-references, README links and the eval schema. The eval runner saves each model answer to `eval-results/` with its machine-check results and the human-judged assertions. See [CONTRIBUTING.md](CONTRIBUTING.md) for the full skill contract and versioning rules.

## Structure

```
.github/workflows/validate.yml   # CI: structural validation on every push/PR
scripts/
├── validate_skills.py           # frontmatter, sections, evals, README checks
└── run_evals.py                 # run eval prompts through any LLM and grade
skills/marketing/<skill>/
├── SKILL.md                     # the skill
└── evals/evals.json             # 3+ test prompts with assertions + checks

skills/marketing/
├── branding/
├── competitor-research/
├── geo-ai-seo/
├── google-ads-diagnostics/
├── google-ads-keywords/
├── gtm-debugging/
├── instagram-organic/
├── landing-page-funnel/
├── linkedin-organic/
├── market-positioning/
├── meta-ads-creative/
├── meta-ads-diagnostics/
├── pinterest-organic/
├── tiktok-ads/
└── youtube-organic/
```
