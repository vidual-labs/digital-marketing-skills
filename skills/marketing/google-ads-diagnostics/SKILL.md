---
name: google-ads-diagnostics
description: Use when analyzing Google Ads performance data and suggesting optimizations — bid strategy, keyword quality, ad copy, search terms, structure, and budget allocation.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [google-ads, ppc, diagnostics, campaign-optimization, keywords, search-terms, ROAS, quality-score]
    related_skills: [google-ads-keywords, landing-page-funnel, meta-ads-diagnostics]
---

# Google Ads Performance Diagnostics

## Overview

Analyze Google Ads campaign data and produce actionable optimization recommendations across bidding strategy, keyword quality, ad copy performance, search term analysis, campaign structure, budget allocation, and quality score improvement.

## When to Use

- Reviewing Google Ads campaign performance data
- Diagnosing high CPC, low clicks, or poor conversion rates
- Optimizing keyword lists and match types
- Improving Quality Score and lowering CPC
- Analyzing search terms for negative keyword additions
- Restructuring campaigns or ad groups
- Adjusting bid strategies and budget allocation

Don't use for: Search keyword research (use `google-ads-keywords`), Google Shopping campaigns, display network, or video ads.

## Input Data Requirements

Request or receive these metrics at minimum:

| Level | Metric | Why |
|-------|--------|-----|
| Account | Total spend, total conversions, avg CPA, conversion rate | Account-level health |
| Campaign | Spend, clicks, CTR, avg CPC, conversions, CPA, conversion rate, ROAS | Campaign-level efficiency |
| Ad Group | Spend, impressions, CTR, avg CPC, Quality Score (1-10), avg position | Ad group relevance |
| Keyword | Impressions, clicks, CTR, avg CPC, conversions, conversion rate, CPA, Quality Score | Individual keyword performance |
| Search Terms | Query text, clicks, cost, conversions, CPA | Wasted spend, negative keyword candidates |
| Ad | Impressions, clicks, CTR, impression share (absolute + top) | Ad copy and ad strength |

### Benchmark Tables

| Metric | Excellent | Good | Average | Poor | Critical |
|--------|-----------|------|---------|------|----------|
| CTR (Search) | > 12% | 5-12% | 3-5% | 1.5-3% | < 1.5% |
| Quality Score | 8-10 | 6-7 | 4-5 | 2-3 | 1 |
| Imp. Share (Search) | > 90% | 70-90% | 50-70% | 30-50% | < 30% |
| Cost / Conv (vs target) | ≤ 0.8× target | ≤ target | 1.0-1.3× target | 1.3-2.0× target | > 2× target |
| Conversion Rate | > 10% | 5-10% | 3-5% | 1.5-3% | < 1.5% |

## Diagnostic Framework

### Phase 1: Account & Campaign Structure

| Check | Issue | Fix |
|-------|-------|-----|
| **Campaign types** | Search + Shopping + Performance Max in one account? | Separate objectives — Search for controlled keyword targeting, PMax for broad reach |
| **SKAGs vs STAGs** | Single Keyword Ad Groups create management overhead | Move to Single-Theme Ad Groups (5-15 tightly themed keywords per ad group) |
| **Too many campaigns** | Budget fragmented across 20+ campaigns | Consolidate related campaigns. Max 5-8 search campaigns for most accounts |
| **Shared audiences** | Audience overlap between campaigns wasting spend | Remove duplicate audiences, use exclusions |

### Phase 2: Keyword Health Audit

**Underperforming keywords** (spend > 2× target CPA, < 2 conversions):
- Action: Pause keyword or tighten match type (broad → phrase → exact)
- If phrase is underperforming: switch to exact or pause
- If exact is underperforming: either lower manual bid or pause

**Overperforming keywords** (CPA ≤ 0.8× target, CTR > 8%):
- Action: Increase bid or add similar long-tail variations
- Consider expanding match type: exact → phrase for controlled testing

**Zero-impression keywords** (2+ weeks, no data):
- Action: Pause. If you need those searches, broaden match type in a different ad group

**Keyword cannibalization:**
- Action: Same query triggering multiple keywords in same account? Keep the best-performing match type, pause duplicates

### Phase 3: Search Term Analysis

**Critical — review search terms weekly.** This is where most wasted spend hides.

Review process:

1. Export search terms report (last 14-30 days)
2. Sort by spend descending
3. Scan for irrelevant matches and add as negative keywords

**Negative keyword categories** (customize by business):

```
NEGATIVE KEYWORDS:
"free", "cheap", "jobs", "hiring", "career", "salary", "internship",
"tutorial", "how to make", "what is", "definition", "review",
"open position", "login", "signup", "download", "torrent",
[free trial], [how to], [what is a], [vs], [alternatives]
```

**Cannibalization check:**
- If your phrase match keyword `"buy running shoes"` is spending $200 on queries like "best running shoes for runners" — that's phrase match doing its job. But if it's triggering "running shoe repair" — add `"repair"` as a negative.

### Phase 4: Quality Score Optimization

Quality Score = Expected CTR × Ad Relevance × Landing Page Experience (each 1-10). QS directly impacts CPC.

**If QS is below 7:**

| Component | Diagnosis | Improvement |
|-----------|-----------|-------------|
| Expected CTR | CTR < industry average for the keyword | Rewrite ad to more directly match the query. A/B test stronger hooks. |
| Ad Relevance | Keywords don't tightly match the ad copy | Put the keyword or a close variant in the ad headline. STAG structure helps. |
| Landing Page XP | High bounce rate, slow load, or poor relevance | Improve page load speed, match LP headline to ad headline, add trust signals. |

**QS impact:** A QS of 3 can cost 200-500% more per click than a QS of 9 for the same keyword position. QS improvement has compound ROI.

### Phase 5: Ad Copy Performance

**Ad strength check:**
- If "Good" or lower: rewrite with responsive search ad best practices
- Use at least 3 headlines + 2 descriptions per RSA
- Make each headline self-contained (not a sentence split across headlines)

**CTR diagnostics:**
| Low CTR cause | Fix |
|--------------|-----|
| Headline doesn't match query | Put keyword in headline 1 |
| No differentiator | Add specific benefit, number, or proof |
| Weak CTA | Change "Learn More" to specific action ("Get Free Quote") |
| Ad extensions missing | Add sitelinks, callouts, structured snippets, call, image extensions |

**Sitelink strategy:**
- 4 sitelinks covering your top sub-pages
- Each sitelink has its own 2 descriptions
- This increases real estate + clicks + overall CTR

**Callout text (8 items max):**
- Short benefit statements
- "Free shipping over $50", "Same-day delivery", "Trusted by 10,000+ customers"

### Phase 6: Bid Strategy

| Situation | Strategy | When to Switch |
|-----------|----------|----------------|
| New campaign / < 30 conv. in 30 days | Manual CPC or Target CPA with high target | Once you hit 30 conversions, move to automated |
| Stable performance | Target CPA or Target ROAS | Monitor weekly, adjust target if reality shifts |
| Budget constraint | Maximize clicks with bid cap or Enhanced CPC | Only for top-funnel or brand awareness |
| E-commerce, stable data | Target ROAS | Requires 30+ conversions in 30 days for stable optimization |
| High-value leads | Target CPA with value optimization | Requires offline conversion import |

**Smart Bidding rules:**
- Target CPA: Set at your break-even CPA or 1.2-1.5× if scaling aggressively
- Budget changes < 50% won't reset learning
- At least 30 conversions per 30 days for any automated strategy to work properly

### Phase 7: Budget & Scaling

| Scenario | Action |
|----------|--------|
| Imp. Share (top) < 50% and budget not exhausted | Increase daily budget or bids |
| Budget exhausted, high impression share | Budget is constraining growth — increase it by 20-30% |
| Low conversion volume | Broaden match types, add new keyword themes, expand to new campaigns |
| High spend, low ROI | Audit search terms. Kill negative queries. Restructure underperforming ad groups. |

**Scaling rule:** Increase budget by max 30% per week to avoid algorithm destabilization.

### Phase 8: Search Term Negative Funnel

Maintain a running negative keyword list with these layers:

1. **Global negatives:** Apply to all campaigns (typo variants, competitor brand names you don't want, job-related terms)
2. **Campaign negatives:** Apply within campaign boundaries (irrelevant subtopics)
3. **Ad-group negatives:** Apply within ad groups (prevent good-but-not-right queries from triggering the wrong ad)

## Output Format

```
GOOGLE ADS AUDIT: [Campaign Name]
Date Range: [Start] to [End]
Budget: $X/day | Spent: $Y | Conversions: Z

--- HEALTH SCORE: X/10 ---

1. STRUCTURE
   [Issue found] → [Specific change] → [Expected impact]

2. KEYWORD HEALTH
   [Underperforming keywords to pause/lower]
   [Overperforming keywords to scale]
   [Cannibalization issues]

3. SEARCH TERMS (Negatives to add)
"neg 1", "neg 2", "neg 3", [neg phrase], [neg phrase 2]

4. QUALITY SCORE
   [Low-QS keywords and ad relevance issues]
   [Specific fix per keyword/ad group]

5. AD COPY
   [CTR issues]
   [Extension gaps]
   [Rewrite recommendations]

6. BID STRATEGY
   [Current] → [Recommended] → [Expected impact]

7. BUDGET & SCALING
   [Current allocation] → [Recommended changes]

PRIORITY CHANGES:
1. [Highest impact first — usually negatives + QS fixes]
2. [Second]
3. [Third]

ESTIMATED IMPACT: [X% CPC reduction / Y% CPA improvement / Z% conversion increase]
```

## Common Pitfalls

1. **Not reviewing search terms regularly.** Search terms are where budget leaks to irrelevant traffic. Review at least weekly.

2. **Setting target CPA too low.** If Google can't reach it at your current budget, you lose delivery. Work upward from achievable baseline, not downward from wishful thinking.

3. **Changing bid strategy too frequently.** Smart Bidding needs ~2-4 weeks to stabilize. Switching between strategies before that destroys historical data.

4. **Leaving phrase match keywords unmanaged.** Phrase match expands to queries you didn't intend. Review its search terms monthly and add negatives aggressively.

5. **Not enough ad extensions.** Missing sitelinks, callouts, and structured snippets is free CTR improvement. Every campaign should have 4+ sitelinks, 6+ callouts, 1 structured snippet.

6. **Optimizing for clicks, not conversions.** High CTR with zero conversions is just expensive curiosity. Always optimize downstream — conversion rate and CPA are your north stars.

## Verification Checklist

- [ ] Audit based on ≥ 7 days of data (14-30 days preferred)
- [ ] All 8 phases evaluated
- [ ] Search term negatives identified and listed
- [ ] Low QS keywords flagged with specific improvement plan
- [ ] Underperforming keywords marked for pause/bid reduction
- [ ] Overperforming keywords identified for scaling
- [ ] Bid strategy recommendation matches account maturity
- [ ] Budget scaling respects 30%/week rule
- [ ] Ad extensions gaps identified
- [ ] Priority changes ordered by impact
- [ ] Estimated impact quantified
