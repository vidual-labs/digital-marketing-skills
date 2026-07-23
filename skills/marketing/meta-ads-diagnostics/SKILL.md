---
name: meta-ads-diagnostics
description: Use when analyzing Meta Ads performance data and proposing concrete campaign changes — budget allocation, targeting, schedule, learning phase, lookalikes, segments, and structural fixes.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [meta-ads, facebook-ads, diagnostics, campaign-optimization, learning-phase, lookalike-audiences, budget, targeting, scheduling]
    related_skills: [meta-ads-creative, landing-page-funnel, google-ads-diagnostics]
---

# Meta Ads Performance Diagnostics

## Overview

Analyze Meta Ads campaign data and produce actionable change recommendations across budget, targeting, scheduling, learning phase, segment allocation, and campaign structure. This skill takes raw performance metrics and translates them into specific configuration changes with expected impact.

## When to Use

- Reviewing Meta Ads campaign performance data
- Diagnosing why a campaign is underperforming
- Optimizing budget allocation across ad sets and campaigns
- Adjusting targeting, audiences, or placement
- Fixing learning phase issues (getting an ad set out of "Learning" or "Learning Limited")
- Proposing bid strategy changes (lowest cost vs. cost cap)
- Scheduling optimization (dayparting, ad rotation)

Don't use for: writing ad creative (use `meta-ads-creative`), tracking/pixel setup (use `gtm-debugging`), or competitive research.

## Input Data Requirements

Request or receive these metrics at minimum:

| Level | Metric | Why |
|-------|--------|-----|
| Campaign | Budget, amount spent, conversions, CPA, frequency | Budget efficiency, saturation |
| Ad Set | CPC, CTR, frequency, audience size, placements, CPA | Targeting health, fatigue, placement value |
| Ad | Spend, impressions, CTR, CPC, engagement rate, CPA, thumbnail/creative | Creative performance, fatigue |
| Funnel | Link CTR (vs. CTR overall), landing page view rate, add-to-cart / purchase / lead rate | Post-click drop-off diagnosis |

### Funnel Drop-off Benchmarks

| Metric | Good | Warning | Critical |
|--------|------|---------|----------|
| CTR (all) | > 1.5% | 0.8-1.5% | < 0.8% |
| CTR (link) | > 1.0% | 0.5-1.0% | < 0.5% |
| Landing page view rate (vs. link click) | > 75% | 55-75% | < 55% |
| Frequency (7-day) | < 3 | 3-6 | > 6 |
| CPA vs. target | ≤ target | 1.0x-1.5x target | > 1.5x target |

## Diagnostic Framework

### Phase 1: Campaign Structure Health

Check these first — structural problems make optimization pointless.

| Issue | Symptom | Fix |
|-------|---------|-----|
| **Too many ad sets** | < 20 conversions/campaign/week spread thin | Consolidate to 3-5 ad sets max. Kill underperformers. |
| **Budget too low for learning** | Campaign stuck in "Learning Limited" or CPA wildly fluctuating | Increase daily budget to ≥ 5× target CPA |
| **Budget too high** | CPA creeping up, overspending on unprofitable clicks | Cap with cost-per-result cap or lower budget to target CPA × 2 |
| **Shared audiences overlap** | Frequency > 6, rising CPA over time | Use Advantage+ audience or exclude overlapping audiences. Check audience overlap tool. |
| **Ad set too narrow** | Audience < 50k, "Learning Limited" | Broaden targeting or switch to Advantage+ Placements + broad |
| **Ad set too broad for niche offer** | High spend, low conversion quality | Add interest/behavior layers or use lookalikes |

### Phase 2: Creative Fatigue Detection

| Signal | Meaning | Action |
|--------|---------|--------|
| Frequency > 3 (7 days) | Same people seeing the ad too often | Refresh creative within 7-10 days |
| CTR declining week-over-week > 20% | Creative losing attention | Test new hook, angle, or format |
| CPC rising > 30% while CTR stable | Bid war or auction competition increase | Consider cost caps or shift budget to lower-competition audiences |
| Impressions up, engagement flat | Audience is saturated | Pause or broaden targeting |

**Creative refresh cycle:** Plan new creative every 7-14 days. Do not wait for fatigue to set in — front-load refresh planning.

### Phase 3: Learning Phase Management

Meta's algorithm enters "learning" whenever a significant edit is made. An ad set needs ~50 optimization events in a 7-day window to exit learning and optimize efficiently. (Lookalike audiences are a separate lever — see targeting in Phase 1.)

| Status | Conversion count (7d) | Action |
|--------|----------------------|--------|
| **Learning** | < 50 | Do NOT edit. Wait. If budget allows, increase to get events faster. |
| **Learning Limited** | < 20 | Either increase budget, broaden targeting, or switch to a higher-funnel objective |
| **Active** | ≥ 50 | Safe to test, but minimize edits. Keep winning ads flying. |

**Rules:**
- Never edit a campaign below 20 weekly conversions unless fixing a blocker
- "Significant edits" that reset learning: budget changes > 20%, off/on, changing objective, changing optimization event, editing targeting
- "Non-learning-reset edits" (safe): disabling underperforming ads, adding new ads, minor budget tweaks < 20%
- When duplicating a campaign for testing, both enter learning — budget for reduced efficiency during the test

### Phase 4: Budget Allocation

Use these rules for budget distribution:

**By performance tier:**
- Top 20% of ad sets by ROAS/CPA → 50-60% of budget
- Mid 50% by ROAS/CPA → 30-40% of budget
- Bottom 30% → 10-15% of budget (test budget)

**Scaling rules:**
- Scale winners by +20% per 24h — never more (avoids resetting learning)
- Kill losers after they spend 2× target CPA with zero conversions
- For accounts under $10k/mo: 1-2 campaigns max. Under $50k/mo: 3-5 campaigns.

### Phase 5: Bid Strategy

| Situation | Strategy | Rationale |
|-----------|----------|-----------|
| Standard / learning | Lowest cost, no cap | Maximum delivery, data collection |
| Stable winner, known CPA | Cost cap at 1.2× target CPA | Protects efficiency, caps waste |
| Bid cap | Only for extreme niches or very high-value leads | Requires deep bid data; rarely better than cost cap |
| Value optimization | When conversion value > amount varies significantly | Requires CAPI + value pixel |
| ROAS target | E-commerce with stable historical data | Requires minimum $50/day per ad set |

### Phase 6: Schedule and Ad Rotation

**Scheduling (dayparting):**
- Not available for lowest-cost in all contexts — only manual bidding supports ad scheduling
- Use only when you have data showing clear off-hours waste (CPA 3× worse on certain days/hours)
- Test before implementing: run 2 weeks of data by day/hour before cutting time slots

**Ad rotation:**
- Default: Rotate without repeating for 7 days. For campaigns where creative refresh is frequent, this wastes impressions.
- Recommended for most accounts: Rotate for 1 day so new ads get fair delivery testing
- When 1 ad clearly wins: leave it running, add new ads to test against it

### Phase 7: Placement Optimization

| Placement | Typical Performance | When to Keep |
|-----------|-------------------|-------------|
| Feed (FB + IG) | Strongest for most | Always keep |
| Reels | Growing fast, cheap CPMs | Keep for awareness, video formats |
| Stories | Good for mobile-first brands | Keep for mobile-native visuals |
| Audience Network | Lowest quality, high bounce | Kill unless CPA justifies it |
| Search | High intent, limited scale | Keep for branded searches |
| Marketplace | Low intent | Typically kill |

**Recommendation:** Start with Advantage+ Placements for learning. After 20+ conversions, look at placement-level CPA. Kill placements where CPA exceeds campaign CPA by > 50%.

## Output Format

When analyzing Meta Ads data, always output in this format:

```
CAMPAIGN AUDIT: [Campaign Name]
Date Range: [Start] to [End]
Budget: $X/day | Spent: $Y | Conversions: Z

--- HEALTH SCORE: X/10 ---

1. STRUCTURE
   [Issue found] → [Specific change] → [Expected impact]

2. BUDGET & SCALING
   [Current state] → [Recommended change] → [Expected impact]

3. TARGETING & AUDIENCES
   [Issue found] → [Specific change] → [Expected impact]

4. CREATIVE FATIGUE
   [Status] → [Recommendation] → [Timeline]

5. LEARNING PHASE
   [Status] → [Action or hold] → [Reasoning]

6. BID STRATEGY
   [Current] → [Recommended] → [Expected impact]

7. PLACEMENTS
   [Which to keep/kill] → [Why]

PRIORITY CHANGES:
1. [Highest impact change first]
2. [Second highest]
3. [Third]

IMPLEMENTATION ORDER: [Specific sequence to avoid resetting learning]
```

## Common Pitfalls

1. **Editing too aggressively.** Every significant edit resets learning. If you're tweaking budget daily, you're keeping the system in "learning" mode and burning money.

2. **Reading 1-day data.** Meta's delivery fluctuates day-to-day. Never make decisions based on less than 3 full days of data (7 full days ideal).

3. **Scaling too fast.** Increasing budget by 100% in one day resets learning and typically doubles CPA. Never scale more than +20% per day.

4. **Keeping dead ad sets alive.** "It might pick up..." is a budget leak. After 2× target CPA with zero conversions, kill it.

5. **Ignoring placement-level data.** Audience Network and sometimes Placements cost 2-3× more per conversion than Feed/Reels without the engagement quality.

6. **Changing creative and targeting at the same time.** You can never tell which change caused the result. Test one variable at a time.

## Verification Checklist

- [ ] Diagnostic based on ≥ 3 days of data (7 days preferred)
- [ ] All 7 phases evaluated (structure, budget, targeting, fatigue, learning phase, bid, placements)
- [ ] Priority changes listed in implementation order
- [ ] Changes that reset learning flagged and sequenced carefully
- [ ] Budget scaling respects 20%/day rule
- [ ] Creative fatigue identified before proposing structural changes
- [ ] Drop-off point diagnosed (ad → click → LP → conversion)
- [ ] Specific numbers cited, not vague "improve CTR"
