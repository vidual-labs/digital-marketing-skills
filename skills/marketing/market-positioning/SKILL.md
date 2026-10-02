---
name: market-positioning
description: Use when defining or sharpening market positioning — perceptual mapping against competitors, distance-from-competition scoring, whitespace validation, audience alignment scoring, positioning statement, message house and a cross-channel consistency audit, including how AI assistants currently describe the brand. Also use when someone says "we sound like everyone else", "what should we stand for", needs a positioning statement, or must align messaging before a launch or rebrand. Don't use for visual identity and voice (branding), for gathering competitor data (competitor-research) or for pricing strategy.
version: 1.1.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. No tools required; browsing helps for sampling customer language and AI-assistant descriptions but is optional.
metadata:
  category: brand
  updated: 2026-10-02
  tags: [market-positioning, positioning-statement, perceptual-mapping, differentiation, whitespace, message-house, target-audience, competitive-distance]
  related_skills: [competitor-research, branding, landing-page-funnel, geo-ai-seo, meta-ads-creative]
---

# Market Positioning

## Overview

Define where a brand sits relative to competitors and audience expectations, and make that position defensible and consistent. The output is a perceptual map, distance scores against each competitor, an audience alignment score, a positioning statement, a message house and a consistency audit of live touchpoints. Positioning is what the audience believes after every touchpoint — including what search engines and AI assistants say about you — not what the company says about itself.

## When to Use

- Launching a brand or product, or repositioning an existing one
- Before a major campaign, rebrand or website rewrite
- When traffic converts poorly because the audience does not "get it"
- When competitors crowd the current position or copy the messaging
- After competitor research reveals whitespace
- When messaging differs across channels

Don't use for: visual identity and voice (use `branding`), collecting competitor data (use `competitor-research`), pricing architecture, or product roadmap decisions.

## Inputs

Ask for (or extract from the conversation):

- **Brand / product**, category and current tagline or headline
- **Target market and segment** (industry, geography, company size or demographic)
- **Target audience** definition and any research (interviews, surveys, reviews, support tickets, sales call notes)
- **Competitor set** with their headlines and taglines (from `competitor-research` or the user)
- **Proof points**: data, customers, awards, technology, process
- **Current messaging** across homepage, ads, social bios, sales deck, app store listing
- **Constraints**: claims that legal will not allow, markets where the position must also work

Data rules: ground axes and scores in real audience language and real competitor copy. If no customer language is available, say so and use review sites, forums or sales notes the user can supply; do not invent quotes. When scoring overlap, show the words compared. If you can browse, sample how two AI assistants and Google describe the brand and its competitors; if you cannot, ask the user to paste those answers — they are now part of the perception the positioning must move.

## Positioning Workflow

### Phase 1: Perceptual mapping

Plot competitors on two axes that matter to the audience, derived from their language, not from internal preference.

| Axis pair | Fits | Poles |
|-----------|------|-------|
| Price vs quality | Most B2C | Budget ↔ premium |
| Simple vs powerful | SaaS, tools | Easy ↔ configurable |
| Generalist vs specialist | Crowded markets | All-purpose ↔ built for [niche] |
| Rational vs emotional | Lifestyle vs utility | Practical ↔ aspirational |
| Fast vs thorough | Services, media | Quick ↔ comprehensive |
| Human vs automated | Service and AI categories | Hands-on experts ↔ fully automated |
| Open vs curated | Platforms, content | Flexible ↔ opinionated |

Process:

1. Collect 30–100 snippets of audience language (reviews, forums, support, sales calls)
2. Find two dimensions that cluster competitors *and* that the audience uses when choosing
3. Plot each competitor from their own messaging and reviews
4. Plot the brand's **current** perceived position (from reviews and AI/search descriptions, not from the homepage)
5. Mark the **target** position: empty on the map *and* wanted by a viable segment

Whitespace validation: if a quadrant is empty, ask why. Absent competitors usually mean low demand, poor economics or a hard capability. State which it is and why the brand can hold it.

### Phase 2: Distance from competition

| Dimension | Measure | Target |
|-----------|---------|--------|
| Messaging overlap | Shared key words and promises across headline, tagline, top three claims | < 30% with the nearest competitor |
| Keyword overlap | Share of the top 20 organic/paid keywords in common | < 40% |
| Visual similarity | Palette, imagery, layout side by side | Distinguishable in a feed at a glance |
| Audience overlap | Shared follower interests (Meta Audience Overlap tool, social analytics) or customer profiles | < 50% with direct competitors |
| Channel overlap | Same platforms, same formats | At least one signature channel or format they do not own |
| AI/search description overlap | How assistants and search snippets describe each brand | The brand is described with a distinct attribute, not the category default |

Messaging overlap above 50% with any competitor means competing on execution alone; a point of difference is required, not a better adjective.

### Phase 3: Audience alignment (score 1–5 each)

| Dimension | Question | Evidence |
|-----------|----------|----------|
| Problem recognition | Does the position name a problem the audience feels and names themselves? | Review and forum language matches |
| Outcome desirability | Is the promised outcome one they will pay for? | Conversion on outcome-led pages, sales objections |
| Credibility | Can the brand prove it today? | Proof points, customer count, expertise |
| Emotional resonance | Does it make them feel relief, confidence, pride? | Sentiment in comments, qualitative interviews |
| Category clarity | Does a stranger know what the product is in 3 seconds? | Homepage test with 5 outsiders |

| Total | Reading |
|-------|---------|
| 20–25 | Strong — proceed |
| 15–19 | Refine the weakest dimensions |
| 10–14 | Rework before investing |
| < 10 | Misaligned — revisit segment or promise |

### Phase 4: Positioning statement

```
For [target segment]
who [situation or need],
[brand] is the [frame of reference]
that [single point of difference]
because [reason to believe].
Unlike [primary alternative], [brand] [key contrast].
```

Rules: one point of difference; a frame of reference the audience already understands (or a deliberately new category with a plan to explain it); a reason to believe that is evidence, not adjectives; the "unlike" line is internal unless legal clears comparative claims. Anti-pattern: "the best [X] for everyone".

Example:

```
For mid-market B2B SaaS teams in Europe
who need board-ready reporting without a data team,
Acme Analytics is the business intelligence platform
that turns raw product data into a decision memo in hours, not weeks,
because its models are pre-built for SaaS metrics and EU data residency.
Unlike general BI suites, Acme ships answers, not dashboards.
```

### Phase 5: Message house

| Level | Content | Source |
|-------|---------|--------|
| Brand promise (roof) | One line: outcome for whom | Positioning statement |
| Key messages (3–4 pillars) | Each answers one audience need | Alignment scoring, map |
| Proof points (per pillar) | Numbers, customers, features, process | Research, product |
| Signature language (2–3 phrases) | Ownable words competitors do not use | Created to claim the whitespace |
| Foundations | Values, tone cues, what we never say | Brand foundation |

Test: swap each key message into a competitor's site. If it still fits, it is not differentiated enough.

### Phase 6: Consistency stress test

| Touchpoint | Check | Fix |
|------------|-------|-----|
| Homepage headline and sub-headline | Express the positioning statement | Rewrite first |
| Paid ads (search and social) | Same promise and signature language | Align or retire |
| Social bios and pinned posts | Mirror a key message | Update |
| Sales deck and one-pager | Same pillars and proof | Rebuild slide 2 |
| App store / marketplace listing | Same frame of reference | Update |
| Help centre and onboarding | Same vocabulary | Align terms |
| SEO titles and meta descriptions | Carry the position, not generic category words | Update top pages |
| Reviews and testimonials | Confirm the position in customers' words | If not, perception lags — feed proof |
| AI assistant and search descriptions | Describe the brand with the intended attribute | Fix entity facts (About page, schema, Wikipedia/Wikidata, directories, press) — see `geo-ai-seo` |

Positioning degrades through inconsistency more than through weak wording. Re-audit every 6–12 months or when a new entrant changes the map.

## Output Format

```
MARKET POSITIONING REPORT: [Brand]
Date: [Date] | Market: [segment / geography] | Audience: [one line]
Evidence base: [n audience snippets, sources; competitors reviewed; AI/search descriptions sampled or not]

--- PERCEPTUAL MAP ---
Axes: [A-low ↔ A-high] × [B-low ↔ B-high] (why these axes)
[Text layout or table of competitor positions]
Current perceived position: [..] (evidence)
Target position: [..] | Whitespace validation: [why it is empty, why we can hold it]

--- DISTANCE FROM COMPETITION ---
| Competitor | Messaging | Keywords | Visual | Audience | Channel | AI/search description |
| [..] | [x% — shared words] | [x%] | [close/far] | [x%] | [same/different] | [same/distinct] |
Nearest competitor: [..] | Risk: [..]

--- AUDIENCE ALIGNMENT ---
Problem recognition [x/5] — [evidence]
Outcome desirability [x/5] — [evidence]
Credibility [x/5] — [evidence]
Emotional resonance [x/5] — [evidence]
Category clarity [x/5] — [evidence]
Total: [x/25] → [reading]

--- POSITIONING STATEMENT ---
For … who … [brand] is the … that … because … Unlike … 

--- MESSAGE HOUSE ---
Promise: [..]
Key message 1: [..] → Proof: [..]
Key message 2: [..] → Proof: [..]
Key message 3: [..] → Proof: [..]
Signature language: [phrase], [phrase], [phrase]
Never say: [..]

--- CONSISTENCY AUDIT ---
| Touchpoint | Status | Fix | Owner/when |

--- RECOMMENDATION ---
[Proceed / refine / pivot] — [1–3 actions, in order]

--- ASSUMPTIONS & GAPS ---
[What was inferred, what research would confirm it]
```

## Common Pitfalls

1. **Axes chosen internally.** If the audience does not use the dimension when choosing, the map is decoration.

2. **Claiming empty space nobody wants.** Validate demand before committing.

3. **Several points of difference.** "Fastest, cheapest and most personal" is not credible. Pick one; the others are proof or table stakes.

4. **Positioning that is really a rebrand or a roadmap.** If the position needs a new product and a new name, say so; positioning is a messaging commitment the brand can honour now.

5. **No reason to believe.** A claim without evidence is an opinion.

6. **Ignoring how AI and search describe you.** If assistants call you "a budget alternative", the market hears that regardless of your homepage. Fix entity facts and proof.

7. **Competing on price as the position.** Anyone can undercut; "more value per unit" is a position, "cheapest" is a race.

8. **One-time exercise.** Markets move; schedule the re-audit.

## Verification Checklist

- [ ] Axes derived from documented audience language, with the sources named
- [ ] At least 5 competitors plotted, plus current and target positions
- [ ] Whitespace validated (why empty, why defensible)
- [ ] Distance scored on all six dimensions for each major competitor, with the compared words shown for messaging overlap
- [ ] Audience alignment scored 1–5 on five dimensions with evidence and a total reading
- [ ] Positioning statement complete, with a single point of difference and an evidence-based reason to believe
- [ ] Message house: promise, 3–4 key messages with proof, 2–3 signature phrases, never-say list
- [ ] Swap test applied to key messages
- [ ] Consistency audit covers at least 6 touchpoints including AI/search descriptions
- [ ] Recommendation (proceed / refine / pivot) with ordered actions
- [ ] Assumptions and research gaps stated; no invented customer quotes
