# Changelog

All notable changes to the skills in this repository. Versions follow [semver](https://semver.org/) per skill; a repo-wide release bumps every skill that changed. See [CONTRIBUTING.md](CONTRIBUTING.md) for the bump rules.

## 1.2.0 — 2026-11-17

Repo-wide release: every skill bumped from 1.1.0 to 1.2.0 after a substantive review pass. Evals grow from 45 to 60 prompts (one new eval per skill).

### Repository

- **Added** `assets/`: static light/dark logo and two animated SVG visuals (`demo-workflow.svg`, `skill-map.svg`) for the README.
- **Changed** README header: centered logo, badges (CI, version, skills, evals, format, license, supported agents) and quick-nav links; replaced the ASCII banner.

### All skills (universal changes)

- Diagnostic skills now decompose the headline metric first and name a single **primary driver/constraint** before recommending changes.
- Thresholds are stated as starting points relative to the account's own median or baseline, with explicit minimum-data floors before pausing, scaling or calling winners.
- Output formats gained scorecards, diagnosis blocks and explicit "not evaluated" / assumptions lines so answers are comparable and gradeable.
- Common Pitfalls and Verification Checklists expanded; each skill gained a new eval (`evals/evals.json` id 4) and stricter machine checks on existing evals.

### Per-skill updates

- **meta-ads-creative** — Added awareness-level angle table, data-driven iteration table (hook rate, hold rate, link CTR, post-click CVR, frequency vs the account median) naming the one element to change, set-diversity rules, policy-safe rewrite table and test-design table (uneven spend is not a verdict); output gains AWARENESS, PROOF USED, ITERATION READ, "Changes vs control", character counts and a structured TEST PLAN; new eval 4 (iterate a fatigued winner).
- **meta-ads-diagnostics** — Added CPA decomposition triage (CPM × link CTR × CVR) routing the primary driver, minimum-data floors, data-confidence gating, Advantage+ vs manual rules, scaling table and change order by learning reset; output gains Baseline used, PRIMARY DRIVER, DO NOT CHANGE YET, NOT EVALUATED, `Learning reset:` per change and a health-score rubric; fixed the vague kill rule (spend ≥ 3× target CPA and CPA > 1.5× target, outside learning); new eval 4 (Q4 CPM spike, not creative).
- **google-ads-keywords** — Added 8-class intent classification with default actions, decision-rule tables (split ad group, exact vs phrase, search-term action with conversion-based click floor, negative level) and a negative-conflict check (e.g. "free" blocking [gluten free cake]); output gains SUMMARY, intent tags, NEGATIVE CONFLICTS and SEPARATE CAMPAIGNS blocks; fixed 80-character checklist rule; new eval 4.
- **google-ads-diagnostics** — Added metric-decomposition triage (CPA = CPC ÷ CVR) routing each driver to first checks, minimum-data floors, data-confidence gating, lost-IS (budget vs rank) reading and changes ordered by Smart Bidding learning risk; output gains Baseline used, PRIMARY DRIVER, `Learning risk:` per change, NOT EVALUATED and a health-score rubric; removed unverifiable industry CVR benchmarks; new eval 4.
- **tiktok-ads** — Added "Reading Creative Tests" (Scale / Iterate / Kill / Wait verdicts against the account's own median), hook-type selection table and Spark Ads authorization guidance; output gains TEST READ, "Builds on:", character counts, muted and safe-zone check and a structured TESTING PLAN; fixed inconsistent safe-zone guidance (bottom ~35% plus right-hand button column); new eval 4.
- **instagram-organic** — Added signal-ratio table (sends/saves per reach, non-follower share, follows per 1,000 reach) and per-format median classification (min 5 posts); "if X then Y" format-mix rules, reach-drop diagnosis starting with Account Status, Trial Reels testing protocol; output gains FORMAT SCORECARD, DIAGNOSIS with "Primary constraint:", PRIORITY ACTIONS and source-labelled numbers; 5 new pitfalls, new eval 4.
- **linkedin-organic** — Added quality/fit ratios (comments ÷ reactions, target-title audience share, profile views per post), median-based post classification and diagnostic rules (link suppression, applause-only posts, audience mismatch, no conversion path); hours-per-week plan table and 5-point pre-publish score; output gains FORMAT SCORECARD, DIAGNOSIS, PRIORITY ACTIONS; new eval 4 (high reach, no leads).
- **youtube-organic** — Added CTR × retention matrix naming the primary constraint, supporting ratios and median-based video classification at 7/28 days; Test & Compare rules; output gains DIAGNOSIS, VIDEO SCORECARD, PRIORITY ACTIONS, retention at 30 s, Shorts vs long-form split; new eval 4.
- **pinterest-organic** — Added Go/Test/Deprioritize niche-fit table, funnel diagnosis (impressions → saves → outbound clicks → conversions) against the account's own top pins, board/pin maintenance table (archive, don't delete); output gains NICHE FIT, FUNNEL DIAGNOSIS, per-board actions and `PIN n:` lines with character counts; 3 new pitfalls; new eval 4.
- **geo-ai-seo** — Fixed crawler classification (ClaudeBot is a training crawler; removed outdated `anthropic-ai`) with a per-company table of search, user-fetch and training crawlers, note that blocking Google-Extended doesn't remove AI Overviews eligibility, and a sample robots.txt; added six-layer "Why are we not cited?" diagnosis, sub-question map, query → page-type table, citation log with ≥3 runs; output gains DIAGNOSIS, robots.txt changes and ASSUMPTIONS & PLACEHOLDERS; new eval 4.
- **landing-page-funnel** — Added leak-diagnosis table (symptom → cause → first fix → evidence), 1–5 message-match scoring where the lowest element wins, sample-size math (16·p(1−p)/(p·MDE)²) with weeks-at-current-traffic feasibility check and ship/test/research table; output gains LEAK DIAGNOSIS, keep/defer/remove form fields, full test-plan lines and ASSUMPTIONS & MISSING DATA; new eval 4.
- **gtm-debugging** — Added first-broken-link triage, Network-tab reading guide (GA4 `/g/collect` incl. `gcs`, Google Ads, Meta `ev`/`eid`), evidence-based confidence levels, basic vs advanced consent mode, consent-loss vs bug rule, Pixel + CAPI dedup rules, ad-blocker and GA4 filter steps; output gains TRIAGE, OK/ISSUE/NOT CHECKED status, Confidence and Data impact lines; new eval 4 (Pixel + CAPI double purchases).
- **branding** — Added Scope Decision (new / enforce / evolve / rebrand) that keeps recognised assets by default, WCAG 2.2 AA contrast table (AAA target for tough conditions), 1–3 voice check for copy and AI output, touchpoint consistency score; output gains `Scope:`, contrast matrix and touchpoint audit with owners; fixed tap-target guidance (WCAG 2.2 AA = 24×24 px, 44×44 kept as brand standard); new eval 4 (rebrand request with recognised assets).
- **market-positioning** — Added repeatable messaging-overlap calculation with Distinct/Blurred/Interchangeable bands, blocker rule, strategy diagnosis (PROCEED / DIFFERENTIATE / RE-SEGMENT / PIVOT), Phase 4a point-of-difference scoring (want / prove / claimed / copyable) and category-choice table; output gains Strategy Diagnosis, Candidate Points of Difference, scored consistency audit and `Decision:`; new eval 4.
- **competitor-research** — Added evidence tags ([OBS]/[USER]/[EST]/[INF]), Phase 1b threat ranking, ad-library pattern reading, review-sampling method, "why is this gap empty" check and gap scoring (ACT NOW / TEST / PARK); output gains Threat Ranking, scored Market Gaps and recommendations with metric and owner; new eval 4.

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
