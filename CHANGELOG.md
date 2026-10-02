# Changelog

All notable changes to the skills in this repository. Versions follow [semver](https://semver.org/) per skill; a repo-wide release bumps every skill that changed. See [CONTRIBUTING.md](CONTRIBUTING.md) for the bump rules.

## 1.1.0 — 2026-10-02

Repo-wide release: every skill bumped from 1.0.0 to 1.1.0. Platform facts verified as of 2026-10-02.

### Repository

- **Added** `scripts/validate_skills.py` — structural tests for frontmatter, section order, cross-references, README links and eval schema (standard library only, PyYAML optional).
- **Added** `scripts/run_evals.py` — runs each skill's eval prompts through any stdin→stdout LLM command (Claude Code CLI by default) and applies machine checks.
- **Added** `evals/evals.json` to every skill: 3 realistic prompts each with human-judged assertions and deterministic checks (45 prompts total).
- **Added** `.github/workflows/validate.yml` — CI runs the validator on every push and pull request.
- **Added** `CONTRIBUTING.md` with the skill contract (frontmatter, body sections, eval schema, versioning).
- **Changed** README: agent-agnostic install instructions, Testing section, updated structure tree.

### All skills (universal changes)

- Frontmatter made agent-neutral: `author: vidual-labs` (was an agent name), new `compatibility` field, `metadata` flattened to generic `category`, `updated`, `tags`, `related_skills` (was nested under one agent's key).
- Descriptions rewritten to state triggers explicitly ("Use when … Also use when … Don't use for …") for more reliable skill selection.
- New **Inputs** section in every skill: what to ask the user for, and data rules — never invent metrics, label estimates and benchmarks, say when a URL cannot be fetched, use the account's currency, map renamed platform features to current names.
- Output formats gained `Data confidence` / `Access` / `Assumptions & missing data` lines so answers state their evidence base.
- Benchmarks reframed as starting points that defer to the account's own data.
- Cross-references between skills checked and fixed.

### Per-skill updates

- **google-ads-keywords** — Exact/phrase behaviour as of 2026; broad match explained and explicitly excluded; negatives now documented as matching misspellings but not plurals/synonyms; keyword limits (80 chars / 10 words); cross-ad-group negatives; optional Google Ads Editor CSV block; locale and volume-data rules.
- **google-ads-diagnostics** — New Phase 0 (conversion tracking trust: primary conversions, enhanced/offline conversions); removed retired concepts (average position, Enhanced CPC, "extensions" → assets); RSA guidance (15 headlines / 4 descriptions, pinning, asset labels); current bid strategies and conversion-volume thresholds; Performance Max brand exclusions and negatives; AI Max / automatically created assets review; search terms privacy threshold; impression share diagnostics.
- **meta-ads-creative** — Field limits updated (headline ~27 visible / 40 max, description 30, primary text 125 visible / 2,200 max); removed the obsolete "20% text" rule; Reels/Stories safe zones; Advantage+ creative implications (fields must stand alone); flexible format, Partnership ads, catalog ads; policy rules (personal attributes, before/after); hypothesis per variation; no invented proof.
- **meta-ads-diagnostics** — Phase 0 data trust (CAPI dedup, Event Match Quality, attribution window, order reconciliation); current bid strategy names (highest volume, cost per result goal, highest value, ROAS goal); Advantage+ sales/leads/app vs manual decision table; corrected dayparting (requires lifetime budget); removed Google-only "ad rotation" content; hook/hold rate metrics; Threads placement; learning-phase reset rules clarified.
- **tiktok-ads** — Corrected in-app fields (single 100-char ad text, 20-char display name, no headline/description pair for in-feed video); added Spark Ads, Smart+, Search Ads, GMV Max/Video Shopping, TikTok One and Symphony; commercial music licensing; safe zones; hook formats incl. stitch/reply style; testing matrix incl. Spark vs dark post.
- **gtm-debugging** — Consent mode v2 corrected: defaults via `gtag('consent','default')` on Consent Initialization (the old data layer object was wrong); Preview does **not** bypass consent (Consent tab explained); GA4 Configuration tag → Google tag; cross-domain configured in GA4 Admin, `_gl` parameter; `ecommerce: null` reset; CAPI `event_id` dedup; server-side GTM checks; SPA duplicate pageview pattern; removed the incorrect timer/`setInterval` advice; root-cause confidence in output.
- **geo-ai-seo** — Landscape updated (Google AI Mode with query fan-out, ChatGPT search, Perplexity, Gemini, Copilot, Claude); technical access checklist (search vs training crawlers, WAF, snippets, rendering, schema); `llms.txt` positioned as unproven; third-party surfaces (Reddit, YouTube, review sites); brand entity block; measurement plan (GA4 AI referrals, citation checks, Search Console); no fabricated data anchors.
- **landing-page-funnel** — Core Web Vitals targets (LCP ≤ 2.5 s, INP ≤ 200 ms, CLS ≤ 0.1) replace the old load-time claim; sample-size guidance replaces fixed thresholds; Google Optimize sunset noted with alternatives; FAQ section; consent/privacy line in forms; message-match scoring table; quick wins vs tests split.
- **instagram-organic** — Ranking signals (watch time, likes, sends), non-follower reach share, saves/sends per reach; Reels up to 3 min, carousels up to 20 slides, 3:4 grid, up to 5 native links, Trial Reels, original-content preference vs reposts; hashtags capped at 5 and reframed as classification; cadence tied to team capacity; fixed time table replaced by Insights-first guidance.
- **linkedin-organic** — Creator Mode retirement reflected (Follow as primary button via settings); native video weight raised (dedicated video feed); engagement rate by impressions; page hashtags removed; employee advocacy; newsletters; link-in-first-comment and engagement-bait rules; realistic cadence table.
- **youtube-organic** — Shorts up to 3 minutes; thumbnail Test & Compare; CTR read with impressions; retention-curve interpretation; Shorts→long-form bridge via related video link; Posts (community), auto-dubbing, altered/synthetic content disclosure; tags de-emphasised; cadence by stage incl. Shorts and Posts.
- **pinterest-organic** — Fresh-pin cadence (1–3 / 3–5 / ≤ 10 per day) replaces the old 5–25 pins/day volume advice; Idea Pins folded into standard pins; native scheduler; title/description limits (100 / 500 chars); seasonal planning with Pinterest Trends 60–90 days ahead; collages, product pins; outbound clicks as the primary KPI; group boards de-emphasised.
- **branding** — WCAG 2.2 AA pairings, dark mode, motion and reduced-motion rules; AI-generated imagery policy and a brand prompt pack for AI content tools; design tokens; Twitter → X and current ad field limits in copy standards; strategic foundation before visual work; proposals labelled when hex codes are not provided.
- **market-positioning** — Added AI/search description as a sixth distance dimension and a consistency-audit touchpoint; "who [situation]" and "unlike" lines in the positioning statement; fixed the incorrect "Audience Network" reference (Meta Audience Overlap tool); evidence-base line in output.
- **competitor-research** — Tool names updated (Google Ads Transparency Center, LinkedIn Ad Library, TikTok Commercial Content Library, Meta Ad Library EU data); AI assistant recommendations as a discovery and visibility channel; reviews, email and hiring as evidence; watchlist and limitations in output; estimates must be labelled with tool and date.

## 1.0.0

Initial release of 15 skills.
