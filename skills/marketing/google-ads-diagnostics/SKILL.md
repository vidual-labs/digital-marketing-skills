---
name: google-ads-diagnostics
description: Use when analyzing Google Ads performance data and recommending optimizations — Search campaign structure, keyword health, search terms and negatives, Quality Score, responsive search ad strength, assets, Smart Bidding strategy and budget scaling. Also use when the user shares a Google Ads export, screenshot or report and asks why CPC is high, conversions dropped, or how to scale. Don't use for generating keyword lists (google-ads-keywords), landing page fixes (landing-page-funnel), or conversion tag bugs (gtm-debugging).
version: 1.1.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. Needs performance data from the user (export, screenshot or pasted table); no Google Ads API access required.
metadata:
  category: paid-search
  updated: 2026-10-02
  tags: [google-ads, ppc, diagnostics, campaign-optimization, search-terms, negative-keywords, quality-score, smart-bidding, performance-max]
  related_skills: [google-ads-keywords, landing-page-funnel, gtm-debugging, meta-ads-diagnostics]
---

# Google Ads Performance Diagnostics

## Overview

Turn Google Ads performance data into a prioritized list of concrete changes: structure fixes, keywords to pause or scale, negatives to add, Quality Score work, ad and asset improvements, bid strategy and budget moves. Every recommendation names the current state, the change and the expected effect, in an order that avoids resetting Smart Bidding learning.

## When to Use

- Reviewing campaign, ad group, keyword or search term reports
- Diagnosing high CPC, low CTR, falling conversions or rising CPA
- Deciding whether a campaign is ready for Target CPA / Target ROAS
- Planning budget increases without destabilizing delivery
- Reviewing Performance Max or Demand Gen campaigns at the level the reports allow

Don't use for: keyword list generation (use `google-ads-keywords`), landing page conversion problems (use `landing-page-funnel`), conversion tracking or consent bugs (use `gtm-debugging`), or Google Shopping feed issues.

## Inputs

Request at least 14 days of data (30 preferred) at these levels:

| Level | Metrics | Why |
|-------|--------|-----|
| Account | Spend, conversions, conversion value, CPA/ROAS, conversion-tracking status | Health and trust in the data |
| Campaign | Type (Search / PMax / Demand Gen / Shopping), bid strategy, budget, spend, impressions, clicks, CTR, CPC, conversions, CPA, ROAS, Search impression share, "Limited by budget" status | Efficiency and headroom |
| Ad group | Spend, CTR, CPC, conversions, CPA | Theme relevance |
| Keyword | Match type, impressions, clicks, CTR, CPC, conversions, CPA, Quality Score with its three components | Individual performance |
| Search terms | Query, match type that triggered it, clicks, cost, conversions | Wasted spend, negative candidates |
| Ads | Ad strength, impressions, CTR, conversions, asset performance labels | Copy quality |
| Conversions | Which actions are "primary", attribution model, whether values are imported | Whether optimization targets are right |

Data rules: work only from the user's numbers. If a level is missing, say which phase you could not evaluate rather than guessing. Benchmarks below are industry starting points; the account's own history beats them. Use the account's currency. Google renames features often (extensions became assets, Enhanced CPC was retired, Dynamic Search Ads are migrating into AI Max) — if a report label differs, map it to the nearest concept and note it.

### Benchmarks (Search, starting points only)

| Metric | Strong | Average | Weak |
|--------|--------|---------|------|
| CTR | > 8% | 4–8% | < 3% |
| Quality Score | 8–10 | 6–7 | ≤ 5 |
| Search impression share | > 80% | 50–80% | < 50% |
| Absolute top impression share | > 50% | 25–50% | < 25% |
| Conversion rate | > 8% | 3–8% | < 2% |
| CPA vs target | ≤ 0.8× | 0.8–1.2× | > 1.5× |

Industry averages differ widely (legal and B2B SaaS convert at 2–4%; e-commerce brand terms at 10%+). Prefer the account's own trend over these numbers.

## Diagnostic Framework

### Phase 0: Trust the data first

Before optimizing, confirm the conversion data is real:

- Are the right actions set as **primary** conversions? Micro-conversions (page views, button clicks) set as primary inflate volume and mislead Smart Bidding.
- Is **enhanced conversions** or offline conversion import in place for lead-gen? Without it, Smart Bidding optimizes toward form fills, not sales.
- Did conversion counts change suddenly on a date that matches a tag or consent change? If so, route to `gtm-debugging` before touching bids.

### Phase 1: Account and campaign structure

| Check | Problem | Fix |
|-------|---------|-----|
| Campaign types mixed | Search, Shopping and PMax competing for the same queries | Keep Search for controlled keywords; let PMax cover Shopping/Display/YouTube; use brand exclusions and campaign-level negatives in PMax so it does not cannibalize brand Search |
| Too many campaigns | Budget fragmented, most campaigns limited by budget | Consolidate to 3–8 Search campaigns grouped by goal, geography or margin |
| SKAGs | Single-keyword ad groups create management overhead with no Quality Score benefit under close variants | Move to single-theme ad groups of 5–20 related keywords |
| Brand and non-brand together | Brand CPA masks weak non-brand performance | Separate brand campaign with its own budget and bid strategy |
| Location / language mismatch | Spend in regions the business does not serve | Check location options ("Presence" vs "Presence or interest"), exclude unserved regions |
| Search partners / Display expansion on | Low-quality traffic on Search campaigns | Turn off unless the report shows profitable partner conversions |

### Phase 2: Keyword health

| Segment | Definition (30 days) | Action |
|---------|---------------------|--------|
| Wasted spend | Spend > 2× target CPA, 0–1 conversions | Pause, or tighten match type and add negatives if the search terms show salvageable intent |
| Underperformers | CPA > 1.5× target with ≥ 3 conversions | Lower bids (manual) or move to a separate campaign with a looser target; check landing page match |
| Winners | CPA ≤ 0.8× target and ≥ 5 conversions | Add exact-match variants from their search terms; ensure not limited by budget or low impression share |
| Zero impressions | 30+ days, no impressions | Pause; the query space is empty or bids too low — do not keep for "completeness" |
| Low Quality Score (≤ 5) | Any spend | Diagnose component (Phase 4) before pausing |
| Cannibalization | Same query served by multiple keywords / ad groups | Keep the best-performing keyword, add cross-ad-group negatives |

### Phase 3: Search terms and negatives

Review search terms weekly; this is where budget leaks. Note that Google hides low-volume queries for privacy, so the report only shows part of spend — if "Other search terms" is a large share, phrase match and broad match are the usual cause.

Process:

1. Sort last 30 days by cost descending
2. Flag irrelevant intent (jobs, DIY, free, unrelated products, wrong location)
3. Add as negatives at the right level — account shared list for universal junk, campaign for topic, ad group for cross-theme routing
4. Promote converting search terms that are not yet keywords to exact match

Negative keyword behaviour: negatives match misspellings automatically but **not** plurals or synonyms — add those yourself. Negatives work at campaign and account level for Performance Max too; use them when PMax captures brand or junk queries.

### Phase 4: Quality Score

Quality Score (1–10) is a diagnostic built from Expected CTR, Ad Relevance and Landing Page Experience, each rated Below average / Average / Above average. It is not used directly in the auction, but the same components drive Ad Rank, so low scores mean higher CPC for the same position.

| Component below average | Likely cause | Fix |
|------------------------|--------------|-----|
| Expected CTR | Ad does not match the query's wording or promise | Put the keyword theme in at least two headlines; add a concrete benefit or number; test a stronger offer |
| Ad relevance | Ad group too broad for one ad | Split ad groups by theme; tighten keywords to the ad's wording |
| Landing page experience | Slow page, weak relevance, poor mobile, thin content | Match H1 to the ad, pass Core Web Vitals, make the next step obvious — hand off to `landing-page-funnel` |

Prioritize Quality Score work by spend: a QS 4 keyword spending 30% of budget matters more than ten QS 4 keywords spending nothing.

### Phase 5: Ads and assets

Responsive search ads (RSAs) are the only standard Search ad type. One strong RSA per ad group, two at most.

| Check | Standard | Fix |
|-------|----------|-----|
| Ad strength | "Good" or "Excellent" | Add headlines (up to 15) and descriptions (up to 4); vary length and angle; include keyword themes |
| Pinning | Minimal | Pin only legally required text; heavy pinning lowers Ad strength and limits combinations |
| Asset performance labels | "Best" / "Good" over "Low" | Replace "Low" assets after they have ~5,000 impressions |
| Sitelinks | ≥ 4 with descriptions | Add deep links to pricing, categories, reviews, contact |
| Callouts | ≥ 4 | Short proof points: free shipping, 24h response, certified |
| Structured snippets | ≥ 1 | Types, brands, services |
| Other assets | Call, location, image, price, promotion, lead form where relevant | Add where the funnel supports it |
| Automatically created assets / AI Max | Understand what is on | If the account uses AI Max for Search or automatically created assets, review the generated headlines and final-URL expansions and exclude pages that should not receive paid traffic |

CTR diagnostics: headline does not mirror the query → put the theme in H1; no differentiator → add a number or proof; weak CTA → replace "Learn more" with the specific next step; no assets → add sitelinks and callouts first (cheapest CTR win).

### Phase 6: Bid strategy

Current strategies: **Manual CPC**, **Maximize clicks**, **Maximize conversions** (optionally with a Target CPA), **Maximize conversion value** (optionally with a Target ROAS), **Target impression share**. Enhanced CPC was retired in 2024–2025; accounts still showing it were moved to Manual CPC.

| Situation | Recommended | Why |
|-----------|-------------|-----|
| New campaign, < 15 conversions / 30 days | Maximize conversions without target, or Manual CPC if budget is very small | Smart Bidding needs conversion signal before a target is useful |
| 15–30 conversions / 30 days, CPA roughly known | Maximize conversions with Target CPA set at or 10–20% above recent actual CPA | A target below recent reality throttles delivery |
| 30–50+ conversions / 30 days, values tracked | Maximize conversion value with Target ROAS | Volume is enough for value-based bidding |
| Lead quality varies | Import offline conversions or assign conversion values; then value-based bidding | Otherwise the system optimizes toward cheap, low-quality leads |
| Visibility goal (brand defence) | Target impression share | Only for brand campaigns |
| Pure traffic goal | Maximize clicks with a max CPC limit | Rarely right for conversion accounts |

Smart Bidding hygiene:

- Change targets in steps of ≤ 20% and wait 1–2 weeks between changes
- Budget changes under ~20–30% do not reset learning; large changes, target changes and conversion action changes do
- Seasonality adjustments exist for short, predictable spikes (sales, launches) — use them instead of yanking targets
- Portfolio bid strategies let you set max CPC limits on Target CPA / ROAS campaigns

### Phase 7: Budget and scaling

| Scenario | Read | Action |
|----------|------|--------|
| "Limited by budget" and CPA at or below target | Profitable headroom | Raise budget 20–30% per week; watch CPA |
| Search impression share < 50%, lost IS (rank) high | Bids or quality too low | Fix Quality Score; loosen target 10–20% |
| Search impression share < 50%, lost IS (budget) high | Budget is the cap | Raise budget or cut waste first |
| Budget not spent, CPA fine | Target too tight or audience small | Loosen target; add phrase variants; widen location |
| High spend, poor ROI | Waste | Negatives, pause wasted-spend keywords, restructure before adding budget |

Scaling rule: increase budgets by at most ~30% per week on Smart Bidding so the system adapts without re-entering learning.

### Phase 8: Performance Max and Demand Gen (when present)

- Check asset group performance by **channel** (Search, Shopping, Display, YouTube, Discover, Gmail, Maps) in the campaign report and search themes insights
- Add **brand exclusions** so PMax does not buy your brand queries at inflated cost
- Add campaign-level **negative keywords** for junk queries surfaced in the search terms insights
- Confirm the final URL expansion is allowed only for pages that should convert
- Demand Gen: judge on view-through and engaged-view conversions, not last-click alone; use lookalike segments from first-party lists

## Output Format

```
GOOGLE ADS AUDIT: [Account / Campaign name]
Date range: [Start] – [End] | Currency: [XXX]
Spend: [X] | Conversions: [Y] | CPA: [Z] (target [T]) | ROAS: [R] (if tracked)
Data confidence: [High / Medium / Low — what is missing]

--- HEALTH SCORE: X/10 ---
[One-line rationale]

0. CONVERSION TRACKING
   [Primary actions correct? Enhanced conversions? Anomalies?] → [Fix]

1. STRUCTURE
   [Issue] → [Change] → [Expected effect]

2. KEYWORDS
   Pause / reduce: [keywords with spend, conversions, CPA]
   Scale: [keywords with CPA ≤ 0.8× target]
   Cannibalization: [query → keywords competing]

3. SEARCH TERMS → NEGATIVES
   Account list: "term", "term", [exact term]
   Campaign [name]: "term", "term"
   Promote to exact: [converting search terms]

4. QUALITY SCORE
   [Keyword / ad group] — [component below average] → [Fix]

5. ADS & ASSETS
   [Ad strength, pinning, low assets] → [Rewrite / add]
   Missing assets: [sitelinks, callouts, snippets, ...]

6. BID STRATEGY
   [Current] → [Recommended] → [Why] → [When to change next]

7. BUDGET & SCALING
   [Current allocation] → [Change] → [Expected effect]

8. PMAX / DEMAND GEN (if applicable)
   [Channel mix, brand exclusions, negatives, URL expansion]

PRIORITY CHANGES (implementation order)
1. [Highest impact, lowest risk — usually negatives and tracking fixes]
2. [...]
3. [...]

ESTIMATED IMPACT: [Range, with assumptions stated]
RE-CHECK DATE: [Date, usually 14 days]
```

## Common Pitfalls

1. **Optimizing on broken conversion data.** A tracking change that doubled conversions makes every bid decision wrong. Verify Phase 0 before anything else.

2. **Setting Target CPA below what the account has ever achieved.** The system responds by not spending. Start at recent actual CPA and walk it down 10–20% at a time.

3. **Changing bid strategy every week.** Smart Bidding needs 1–2 weeks and enough conversions to settle. Decide on a cadence and stick to it.

4. **Reading the search terms report as if it were complete.** Low-volume queries are hidden. Large "other" spend means match types are too loose, not that the data is clean.

5. **Treating Quality Score as a KPI.** It is a diagnostic. Fix the component that is below average on keywords that spend; ignore QS on keywords with no traffic.

6. **Pinning every headline in an RSA.** It turns the RSA back into a fixed ad and caps Ad strength. Pin only what legal or brand rules require.

7. **Letting PMax eat brand queries.** Brand CPA looks great in PMax while non-brand Search starves. Use brand exclusions and compare blended results.

8. **Optimizing for clicks.** High CTR with no conversions is expensive curiosity. CPA, ROAS and conversion quality are the only north stars.

## Verification Checklist

- [ ] Conversion tracking sanity-checked (primary actions, enhanced/offline conversions, anomalies) before recommending bid changes
- [ ] Audit based on ≥ 14 days of data, or a stated caveat if less
- [ ] Every phase that had data was evaluated; missing data called out explicitly
- [ ] Negatives listed with match type and the level (account / campaign / ad group) to add them
- [ ] Keywords to pause/scale cited with their actual spend, conversions and CPA
- [ ] Quality Score fixes name the component that is below average
- [ ] RSA ad strength, pinning and missing assets reviewed
- [ ] Bid strategy recommendation matches conversion volume (15 / 30 / 50 thresholds) and includes a wait period
- [ ] Budget scaling stays within ~30% per week on Smart Bidding
- [ ] PMax brand exclusions and negatives addressed when PMax is present
- [ ] Priority changes ordered to avoid resetting learning
- [ ] Estimated impact given as a range with assumptions, in the account's currency
