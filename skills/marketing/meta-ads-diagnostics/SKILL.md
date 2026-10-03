---
name: meta-ads-diagnostics
description: Use when analyzing Meta Ads (Facebook/Instagram) performance data and proposing concrete campaign changes — structure, budget allocation, Advantage+ vs manual setup, audiences, learning phase, creative fatigue, bid strategy, placements and attribution. Also use when the user pastes an Ads Manager export or screenshot and asks why CPA rose, ROAS fell, or how to scale without breaking delivery. Don't use for writing ad copy (meta-ads-creative), pixel/CAPI/consent bugs (gtm-debugging) or landing page fixes (landing-page-funnel).
version: 1.1.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. Needs performance data from the user (export, screenshot or pasted table); no Marketing API access required.
metadata:
  category: paid-social
  updated: 2026-10-02
  tags: [meta-ads, facebook-ads, instagram-ads, diagnostics, campaign-optimization, learning-phase, advantage-plus, budget, bid-strategy, placements]
  related_skills: [meta-ads-creative, landing-page-funnel, gtm-debugging, google-ads-diagnostics]
---

# Meta Ads Performance Diagnostics

## Overview

Translate Meta Ads performance data into specific configuration changes with expected impact and a safe implementation order. Covers campaign structure, Advantage+ versus manual setups, budget allocation and scaling, audience strategy, learning phase, creative fatigue, bid strategies, placements and attribution settings. The output is a prioritized change list, not a description of the dashboard.

## When to Use

- Reviewing campaign, ad set or ad level performance
- Diagnosing rising CPA/CPM, falling ROAS or stalled delivery
- Deciding how to scale winners or when to kill losers
- Fixing "Learning limited" ad sets
- Choosing between Advantage+ sales/leads/app campaigns and manual campaigns
- Choosing a bid strategy or attribution setting

Don't use for: ad copy and creative concepts (use `meta-ads-creative`), pixel, Conversions API or consent problems (use `gtm-debugging`), landing page conversion rate (use `landing-page-funnel`), or competitor analysis.

## Inputs

Request at least 7 days of data (14–28 preferred) at these levels, with the attribution setting shown:

| Level | Metrics | Why |
|-------|--------|-----|
| Account | Spend, results, cost per result, ROAS, attribution setting (e.g. 7-day click / 1-day view), CAPI status, Event Match Quality | Baseline and data trust |
| Campaign | Type (Advantage+ sales / leads / app, manual sales, traffic, engagement), budget type (campaign vs ad set), spend, results, CPA/ROAS, frequency | Structure and budget |
| Ad set | Audience type (broad, Advantage+ audience, interests, lookalike, custom), audience size, placements, optimization event, bid strategy, learning status, spend, CPM, CTR (link), CPC, results, CPA, frequency | Targeting and learning health |
| Ad | Creative type, spend, impressions, CPM, link CTR, hook rate (3-second plays ÷ impressions), hold rate (ThruPlays ÷ 3-second plays), results, CPA, first run date | Creative fatigue |
| Funnel | Link clicks → landing page views → add to cart / lead → purchase; rates between steps | Where drop-off happens |

Data rules: work only from the user's numbers and name the attribution window when quoting results. Benchmarks are starting points — the account's own history wins. Use the account's currency. Meta renames things often (Advantage+ shopping became Advantage+ sales; "lowest cost" is now "highest volume"); map labels to the nearest concept and say so.

### Funnel benchmarks (starting points)

| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| Link CTR | > 1.0% | 0.5–1.0% | < 0.5% |
| Hook rate (video) | > 30% | 20–30% | < 20% |
| Hold rate (video) | > 15% | 8–15% | < 8% |
| Landing page views ÷ link clicks | > 75% | 55–75% | < 55% (slow page or bot clicks) |
| Frequency (7-day, prospecting) | < 2.5 | 2.5–4 | > 4 |
| Frequency (7-day, retargeting) | < 6 | 6–10 | > 10 |
| CPA vs target | ≤ 1.0× | 1.0–1.5× | > 1.5× |

## Diagnostic Framework

### Phase 0: Can the data be trusted?

- Is the **Conversions API** sending the same events as the pixel with matching `event_id` for deduplication? Double counting inflates results; missing CAPI under-reports after consent denial.
- Is **Event Match Quality** ≥ 6 on the optimization event? Low quality means weaker optimization and attribution.
- Did the **attribution setting** change? 7-day click/1-day view vs 1-day click changes reported CPA by 20–50%.
- Compare Ads Manager purchases against the shop's actual orders for the same window. A gap over ~20% needs `gtm-debugging` before optimization.

### Phase 1: Campaign structure

| Issue | Symptom | Fix |
|-------|---------|-----|
| Too many ad sets | Results spread thin, several "Learning limited" | Consolidate to 1–3 ad sets per campaign; let the algorithm allocate |
| Audience overlap | Rising frequency and CPM across ad sets | Use the Audience Overlap tool; merge or exclude; prefer one broad ad set |
| Manual campaign where Advantage+ would win | Mature account, ≥ 50 purchases/week, stable creative pipeline | Test an Advantage+ sales campaign with the same creative; cap the existing-customer budget share |
| Advantage+ where control is needed | New brand, strict geo/age rules, B2B lead quality problems | Manual campaign with broad or Advantage+ audience and lead-quality filters |
| Prospecting and retargeting mixed | Retargeting share drives CPA down while prospecting starves | Separate by intent or use the existing-customer budget cap in Advantage+ |
| Budget too low per ad set | Daily budget < 5× target CPA | Fewer ad sets, higher budget each, or a cheaper optimization event |
| Wrong optimization event | Optimizing for add to cart because purchases are few | Only step down the funnel while purchases < ~30/week; step back up as volume grows |

### Phase 2: Creative fatigue

| Signal | Meaning | Action |
|--------|---------|--------|
| Frequency > 3 (7 days) on prospecting | Same people seeing the ad repeatedly | New creative within 7 days |
| Link CTR down > 20% week over week with stable CPM | Attention is fading | New hook or angle |
| CPM up > 30% with stable CTR | Auction pressure, seasonality or audience saturation | Broaden, add creative diversity, check the calendar |
| Hook rate down, hold rate stable | Thumbnail/first second is tired | Re-cut the first 2 seconds only |
| First run date > 4–6 weeks and CPA creeping | Natural decay | Rotate in 2–4 new concepts; keep the winner running until it is beaten |

Plan creative refresh on a schedule (new concepts every 1–2 weeks for accounts spending meaningful budgets). Diversity across formats (static, video, UGC, carousel) extends the life of a campaign more than more variants of one format.

### Phase 3: Learning phase

An ad set needs about **50 optimization events within 7 days** to exit learning. Below that it shows "Learning limited" and delivery is less stable.

| Status | Read | Action |
|--------|------|--------|
| Learning | Normal for new or recently edited ad sets | Do not edit; wait for 50 events or 7 days |
| Learning limited | Budget, audience or event too small | Raise budget, broaden audience, consolidate ad sets, or optimize for a higher-volume event |
| Active | Stable | Edit sparingly; scale ≤ 20% per day |

Edits that **reset learning**: changing targeting, placements, optimization event, bid strategy or amount; budget changes above ~20%; pausing for 7+ days then resuming; adding a new ad to the ad set (resets that ad set). Edits that **do not**: pausing an individual ad, budget nudges under ~20%. Editing an existing ad's creative or copy effectively creates a new ad (and drops its accumulated social proof), so treat creative changes as new ads rather than edits.

### Phase 4: Budget allocation and scaling

- Campaign budget (Advantage+ campaign budget) lets Meta shift spend between ad sets; use ad set budgets only when you must guarantee spend per audience.
- Tiering: top ad sets by CPA/ROAS get 50–60% of budget, middle 30–40%, test budget 10–15%.
- Scale winners by **≤ 20% per day** or duplicate at a higher budget and let the duplicate learn.
- Kill rule: an ad set that has spent 2× target CPA with zero results, or 3× with results far above target, is paused.
- Minimum viable daily budget per ad set ≈ 5× target CPA, otherwise it cannot exit learning.

### Phase 5: Bid strategy (current names)

| Strategy | Formerly | Use when |
|----------|----------|----------|
| **Highest volume** | Lowest cost | Default. Learning, prospecting, most accounts |
| **Cost per result goal** | Cost cap | Known acceptable CPA; set at 1.1–1.3× target; expect lower volume |
| **Highest value** | Value optimization | Purchase values vary and ≥ 30 value events/week |
| **ROAS goal** | Minimum ROAS | Stable e-commerce with value data; set slightly below the true target |
| **Bid cap** | Bid cap | Rare: experienced buyers controlling auction bids directly |

A goal set below what the account has achieved makes the ad set under-deliver. Start at reality and tighten by ≤ 10–20% per change.

### Phase 6: Schedule and attribution

- **Ad scheduling (dayparting)** is available only with a **lifetime budget**. Use it when the data shows CPA 2–3× worse in specific hours (e.g. a call-based business overnight) — not on a hunch.
- **Attribution settings** can be set per ad set: 7-day click / 1-day view (default), 1-day click, or engaged-view for video. Report what the setting is; compare periods only with the same setting.
- **Incrementality**: for large accounts, run a conversion lift or geo holdout before trusting platform-reported ROAS for budget decisions.

### Phase 7: Placements

| Placement | Typical behaviour | Keep when |
|-----------|-------------------|-----------|
| Facebook & Instagram feeds | Core volume and conversions | Always |
| Instagram & Facebook Reels | Cheap reach, strong for vertical video | You have 9:16 creative |
| Stories | Mobile-native, time-limited | You have 9:16 creative with safe zones |
| Threads | New inventory, limited data | Testing with Advantage+ placements |
| Audience Network | Low CPM, weak quality, accidental clicks | Only if CPA on it is at or below campaign CPA |
| Marketplace, right column, search | Small volume | Leave on under Advantage+ unless the breakdown shows waste |
| Messenger inbox / sponsored messages | Messaging objectives | Conversation goals only |

Start with Advantage+ placements; after ~30 results, break down by placement and remove any placement whose CPA is more than 50% above the campaign average.

## Output Format

```
META ADS AUDIT: [Account / Campaign]
Date range: [Start] – [End] | Attribution: [setting] | Currency: [XXX]
Spend: [X] | Results: [Y] ([event]) | CPA: [Z] (target [T]) | ROAS: [R]
Data confidence: [High / Medium / Low — CAPI, EMQ, attribution, gaps]

--- HEALTH SCORE: X/10 ---
[One-line rationale]

0. TRACKING & ATTRIBUTION
   [CAPI / EMQ / attribution issues] → [Fix]

1. STRUCTURE
   [Issue] → [Change] → [Expected effect]

2. BUDGET & SCALING
   [Current allocation] → [Change, in ≤ 20%/day steps] → [Expected effect]

3. AUDIENCES
   [Overlap, size, broad vs targeted, exclusions] → [Change]

4. CREATIVE FATIGUE
   [Ad] — [signal: frequency / CTR / hook rate] → [Refresh plan and date]

5. LEARNING PHASE
   [Ad sets in learning / limited] → [Action or hold] → [Reasoning]

6. BID STRATEGY
   [Current] → [Recommended] → [Expected effect]

7. PLACEMENTS
   [Keep / remove, with CPA evidence]

PRIORITY CHANGES (implementation order, grouped so learning resets happen once)
1. [...]
2. [...]
3. [...]

ESTIMATED IMPACT: [Range with assumptions]
RE-CHECK DATE: [Usually 7 days]
```

## Common Pitfalls

1. **Editing daily.** Every structural edit restarts learning. Batch changes and let 7 days pass.

2. **Judging on 1–2 days.** Delivery is noisy and attribution lags. Decide on 7 days minimum, 14 for small budgets.

3. **Scaling by 100% overnight.** The ad set re-enters learning and CPA usually jumps. Scale ≤ 20% per day or duplicate.

4. **Treating "Learning limited" as a bug.** It is a volume problem. Consolidate, raise budget or move up the funnel event.

5. **Comparing periods with different attribution settings.** A switch from 7-day click to 1-day click "drops" results without anything changing.

6. **Reading platform ROAS as truth.** Check against actual orders; run lift tests at scale.

7. **Ignoring creative as the cause.** Most "targeting" problems in broad or Advantage+ campaigns are creative fatigue. Check Phase 2 before touching audiences.

8. **Over-segmenting audiences.** Ten interest ad sets split budget and compete. One broad ad set with strong creative usually wins.

## Verification Checklist

- [ ] Tracking trust checked first (CAPI dedup, Event Match Quality, attribution window, order reconciliation)
- [ ] Analysis uses ≥ 7 days of data or states the caveat
- [ ] Attribution setting named whenever results are quoted
- [ ] All seven phases evaluated; missing data called out
- [ ] Funnel drop-off point identified (impression → click → landing page → event)
- [ ] Creative fatigue assessed with frequency, CTR trend and hook/hold rates before structural changes
- [ ] Learning-phase status of each ad set considered and resets batched
- [ ] Budget changes stay within ~20%/day; kill rules applied with numbers
- [ ] Bid strategy named with current (not legacy) terminology and a realistic goal
- [ ] Placement recommendations backed by placement-level CPA
- [ ] Priority changes in implementation order with expected impact range
- [ ] Specific numbers cited from the user's data, not generic advice
