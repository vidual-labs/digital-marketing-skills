---
name: market-positioning
description: Use when defining or refining digital market positioning — map your brand against competitors, find whitespace, align messaging to target audience, and establish a defensible position with clear differentiation.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [market-positioning, competitive-distance, target-audience, positioning-statement, differentiation, whitespace, perceptual-mapping]
    related_skills: [competitor-research, branding, landing-page-funnel, geo-ai-seo]
---

# Market Positioning

## Overview

Define where your brand sits in the digital landscape relative to competitors and audience expectations. Produces a positioning statement, perceptual map, differentiation strategy, and audience alignment score. The goal: occupy a clear, distinctive, defensible position that's both desired by your target and credibly achievable.

Positioning is not what you say about your product — it's what your audience believes about you after every digital touchpoint (website, ads, social, reviews, PR, search results). This skill audits that perception gap and closes it.

## When to Use

- Launching a new brand or repositioning an existing one
- Before a major campaign, product launch, or rebrand
- When conversion is poor despite good traffic (audience doesn't "get it")
- When competitors are crowding your positioning space
- After competitor research reveals whitespace to claim
- When messaging is inconsistent across channels (positioning leak)

Input is typically:
- **Brand/product name**
- **Target market** (industry, locale, segment)
- **Target audience** (demographic, psychographic, or behavioral)
- **Current or desired positioning** (if any)
- **Competitor set** (from `competitor-research` or provided)

Don't use for: pure creative brand identity (use `branding`), competitor data gathering (use `competitor-research`), or pricing strategy.

## Positioning Workflow

### Phase 1: Perceptual Mapping

Plot the competitive landscape on 2 axes that matter to your audience. These aren't arbitrary — derive them from actual customer language (reviews, forum posts, social comments).

**Axis selection framework:**

| Axis Pair | Works for | Example |
|-----------|----------|---------|
| Price vs Quality | Most B2C markets | Budget ↔ Premium, Good ↔ Premium quality |
| Complexity vs Simplicity | SaaS, tools, services | Technical ↔ Simple |
| Mass vs Niche | Any crowded market | General-purpose ↔ Specialized |
| Emotional vs Rational | Lifestyle vs utility brands | Fun/Aspirational ↔ Logical/Practical |
| Speed vs Depth | Services, media, tools | Quick fix ↔ Comprehensive |
| Human vs AI/Automated | Growing relevant | Personal/Handmade ↔ Automated/At-scale |

**Process:**
1. Gather language from your target audience — reviews, Reddit threads, social comments, survey responses
2. Find 2 dimensions that naturally cluster competitors and separate opportunities
3. Plot each competitor as a point on the 2D map
4. Mark your brand's *current* position (where the audience perceives you, not where you want to be)
5. Mark your *target* position — the whitespace that's both empty and desirable

**Validation test:** Is the whitespace real? Check: would the target audience actually go there? If competitors *could* go there but don't, there's usually a reason — acknowledge it.

### Phase 2: Distance-from-Competition Analysis

Quantify how close your positioning is to each major competitor. High proximity = confusion, price competition, audience overlap.

| Metric | How to Measure | Target |
|--------|---------------|--------|
| **Messaging overlap** | Word/phrase similarity between your headline, tagline, and value prop vs. each competitor | < 30% overlap with nearest competitor |
| **Keyword overlap** | % of top 20 organic/paid keywords you share with each competitor | < 40% with closest competitor |
| **Visual similarity** | Do you look like them in ads? Color schemes, composition, style | Instantly distinguishable in a feed |
| **Audience overlap** | Shared follower/interest demographics (Audience Network, social analytics) | < 50% overlap with direct competitors |
| **Channel overlap** | Are you on the exact same platforms using the exact same content types? | At least 1 signature channel they don't dominate |

**Red flag:** If your messaging overlap with a competitor is > 50%, you're competing on execution quality alone. You need differentiation.

**White space opportunity:** If a quadrant on the perceptual map is empty AND language research confirms it's what the audience wants, that's your positioning target.

### Phase 3: Target Audience Alignment

Even the cleverest positioning fails if the audience doesn't feel it. Score alignment across 5 dimensions:

| Dimension | Score (1-5) | What to Check |
|-----------|-------------|---------------|
| **Problem recognition** | Does your positioning name a problem they feel deeply? | Reviews, forum posts, support tickets — does your language match theirs? |
| **Outcome desirability** | Is the promised outcome something they actually care about? | Landing page conversion, ad CTR, social engagement on outcome-focused content |
| **Credibility** | Can you credibly own this position? | Social proof count, expertise evidence, track record |
| **Emotional resonance** | Does the positioning make them feel something (relieved, excited, empowered)? | Sentiment of comments, engagement rate vs. competitor average |
| **Category clarity** | Is it instantly clear what category you belong to? | "3-second test" — ask a stranger to describe what you do based on your homepage |

**Alignment score interpretation:**
- 20-25: Strong alignment — proceed with confidence
- 15-19: Decent — refine the weakest dimensions
- 10-14: Weak — reconsider the position before investing
- < 10: Misaligned — the audience doesn't connect with this positioning

### Phase 4: Positioning Statement Construction

Condense the work into a single, disciplined statement:

```
For [target segment],
[brand] is the [frame of reference]
that [point of difference]
because [reason to believe].
```

**Rules:**
- **Target segment**: specific enough to be differentiated, broad enough to be viable
- **Frame of reference**: the category you compete in (e.g., "project management tool," "meal delivery service")
- **Point of difference**: the one thing you own that competitors can't easily copy
- **Reason to believe**: the evidence (data, endorsement, process, technology)

**Anti-pattern:** "We are the best [X] for [everyone]." — This is not positioning, it's aspiration.

**Example:**
```
For mid-market SaaS companies in Europe,
Acme Analytics is the business intelligence platform
that turns raw data into boardroom-ready strategy in hours, not weeks,
because our AI-native engine is purpose-built for European compliance and data patterns.
```

### Phase 5: Message House

Translate the positioning statement into a practical messaging architecture:

| Level | Content | Source |
|-------|---------|--------|
| **Brand promise (1 line)** | The core positioning — what you deliver and for whom | Derived from positioning statement |
| **Key messages (3-4)** | Supporting pillars — each maps to an audience need | Derived from perceptual map + alignment scoring |
| **Proof points (per key message)** | Specific evidence, data, testimonials, features | From research, case studies, product capabilities |
| **Signature phrases (2-3)** | Ownable language that becomes your brand's vocabulary | Created to fill the whitespace — competitors don't use these words |

**Completion criterion:** Each key message, if swapped with a competitor's version, must be recognizable as *yours*. If not, the differentiation is too thin.

### Phase 6: Consistency Stress Test

Positioning degrades through inconsistency. Audit the planned positioning against every touchpoint:

| Touchpoint | Check | Fix |
|------------|-------|-----|
| **Homepage headline** | Does it match the positioning statement? | Rewrite if mismatched within 24h |
| **Ad copy** | Do all active ads express the same position? | Align or retire inconsistent ads |
| **Social bios** | Do profile descriptions reinforce the position? | Update bios to mirror key messages |
| **Email sign-off / footer** | Does the tagline match? | Standardize signature line |
| **Support / FAQ** | Does the language match? | Align help docs with positioning tone and framing |
| **SEO meta titles** | Do they express the position? | Update if generic or off-position |
| **Reviews / ratings** | Do customer reviews confirm the position? | If not, the audience perception is different — revisit Phase 3 |

## Output Format

```
MARKET POSITIONING REPORT: [Brand Name]
Date: [Date]
Target Market: [Market / Segment / Locale]

--- PERCEPTUAL MAP ---
Axes: [Axis A] ↔ [Axis B]
[Text-based scatter description showing all competitors and your position]

Current position: [Where you are]
Target position: [Where the whitespace is]

--- DISTANCE FROM COMPETITION ---

|| Brand | Messaging | Keywords | Visual | Audience | Channel |
|-------|---------|----------|---------|--------|---------|---------|
|[Competitor 1] | [X%] | [X%] | [Close/Far] | [X%] | [Same/Different] |

Nearest competitor: [Name] at [overall overlap]
Whitest quadrant: [Description]

--- AUDIENCE ALIGNMENT ---
Problem recognition: [X/5] — [Justification]
Outcome desirability: [X/5] — [Justification]
Credibility: [X/5] — [Justification]
Emotional resonance: [X/5] — [Justification]
Category clarity: [X/5] — [Justification]
Total: [X]/25 [Interpretation]

--- POSITIONING STATEMENT ---
For [target segment],
[brand] is the [frame of reference]
that [point of difference]
because [reason to believe].

--- MESSAGE HOUSE ---
BRAND PROMISE: [One line]
KEY MESSAGE 1: [Statement] → Proof: [Evidence]
KEY MESSAGE 2: [Statement] → Proof: [Evidence]
KEY MESSAGE 3: [Statement] → Proof: [Evidence]
SIGNATURE LANGUAGE: [2-3 ownable phrases]

--- CONSISTENCY AUDIT ---
[Table of touchpoints with pass/fail and fixes]

--- RECOMMENDATION ---
[Final call: proceed / refine / pivot — with 1-3 specific actions]
```

## Common Pitfalls

1. **Positioning based on internal wishful thinking.** The perceptual map must use real audience language and competitor data — not internal hypotheses. Always ground the axes in research.

2. **Claiming a whitespace that doesn't exist.** Just because a quadrant is empty doesn't mean customers want it. Validate with actual audience feedback before committing.

3. **Multiple points of difference.** Pick one. "Fastest AND cheapest AND most personal" is not credible. Trade-offs are what make positioning defensible.

4. **Positioning that's too similar to rebranding.** If the position requires a complete visual identity change, new product features, and a new name — that's a rebrand, not positioning. Positioning is messaging-driven.

5. **Forgetting the "reason to believe."** A position without proof is an opinion. Every claim needs evidence the audience trusts.

6. **Positioning once and never updating.** Markets shift. Re-audit every 6-12 months or when a new competitor enters with a different angle.

7. **Confusing price position with value position.** "Cheaper" as a positioning is fragile — anyone can underprice you. "More value for the price" is a position; "cheapest" is a race to the bottom.

## Verification Checklist

- [ ] Perceptual map uses audience-derived axes (not arbitrary dimensions)
- [ ] At least 5 competitors plotted on the map
- [ ] Distance-from-competition measured across 5 dimensions for each major competitor
- [ ] Audience alignment scored (1-5) across all 5 dimensions
- [ ] Positioning statement follows the template with all 4 elements filled
- [ ] Point of difference is singular and credible (one thing, backed by proof)
- [ ] Message house has 1 brand promise, 3 key messages, and proof for each
- [ ] 2-3 signature phrases created that competitors do not use
- [ ] Consistency audit covers at least 5 touchpoints with pass/fail
- [ ] Clear recommendation: proceed / refine / pivot with specific next actions
