---
name: market-positioning
description: Use when defining or sharpening market positioning — perceptual mapping against competitors, distance-from-competition scoring, whitespace validation, audience alignment scoring, positioning statement, message house and a cross-channel consistency audit, including how AI assistants currently describe the brand. Also use when someone says "we sound like everyone else", "what should we stand for", needs a positioning statement, or must align messaging before a launch or rebrand. Don't use for visual identity and voice (branding), for gathering competitor data (competitor-research) or for pricing strategy.
version: 1.2.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. No tools required; browsing helps for sampling customer language and AI-assistant descriptions but is optional.
metadata:
  category: brand
  updated: 2026-11-17
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

**How to compute messaging overlap** (so scores are reproducible): take the headline, sub-headline, tagline and top three claims of each brand; reduce each to its key terms (nouns, outcome verbs and promise words — drop stop-words and the bare category noun if every brand uses it, and say so); overlap = shared key terms ÷ all distinct key terms across the two brands. Always list the shared terms next to the percentage. Treat the thresholds in the table as starting points; if the user has their own benchmark (e.g. from a previous audit), use it.

| Overlap with nearest competitor | Reading | Do |
|---------------------------------|---------|----|
| < 30% | Distinct wording | Check the difference is one the audience values (Phase 3) |
| 30–50% | Blurred | Replace shared promise words with signature language; keep shared category words |
| > 50% | Interchangeable | Find a new point of difference (Phase 4a); rewording alone will not fix it |

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

Blocker rule: any single dimension at 1–2 caps the reading at "Refine", whatever the total — a position the brand cannot prove (Credibility 2) or that strangers cannot place (Category clarity 2) fails in market even when the other scores are high. Score from evidence; where a score is inferred, write "(inferred)" next to it.

### Strategy diagnosis (distance × alignment)

Combine Phase 2 and Phase 3 before writing anything. "Distinct" = messaging overlap < 30% with the nearest competitor and a distinct AI/search description; "aligned" = alignment ≥ 15/25 with no blocker.

| | Aligned | Not aligned |
|---|---------|-------------|
| **Distinct** | **PROCEED** — the position works; fix consistency (Phase 6) | **RE-SEGMENT** — distinct but unwanted: whitespace nobody values, or the wrong audience. Revisit Phase 1 whitespace validation |
| **Not distinct** | **DIFFERENTIATE** — the audience wants this, but so do competitors' customers. Keep the segment, find a new point of difference (Phase 4a) | **PIVOT** — neither different nor wanted. Restart from audience language |

In the Recommendation, DIFFERENTIATE and RE-SEGMENT map to REFINE. With fewer than ~30 audience snippets or no competitor copy, mark the diagnosis "provisional" and name the research that would confirm it.

### Phase 4a: Choosing the point of difference

Generate 2–4 candidate points of difference from the map, the gaps and the proof. Score each 1–3 on four tests:

| Test | Question | 3 | 1 |
|------|----------|---|---|
| Desired | Does the audience name this when choosing? | Appears repeatedly in their own language | Only the company says it |
| Deliverable | Can the brand prove it today? | Hard proof: data, customers, process | Roadmap or aspiration |
| Distinctive | Do competitors already claim it? | None of the set claims it | Two or more claim it |
| Durable | How hard is it to copy within ~12 months? | Structural (data, network, regulation, expertise, cost base) | A feature or a price cut |

Pick the highest total (max 12). Reject any candidate scoring 1 on Deliverable or Distinctive regardless of total; a 1 on Durable is acceptable only with a plan to deepen the moat. Price is a valid point of difference only when it rests on a structural cost advantage *and* is framed as value per outcome; otherwise it belongs in proof or packaging.

### Frame of reference

| Situation | Frame | Example |
|-----------|-------|---------|
| Buyers already search and budget for the category | Existing category | "the project management tool…" |
| The category exists but the segment is underserved | Subcategory: category + for [segment] | "the project management tool built for architecture practices" |
| No existing frame describes the job, and there is budget and time to educate the market | New category, with a one-line explainer that names the old alternative | "decision memos, not dashboards" |

Default to an existing category or subcategory; a new category costs years of education and loses buyers who search for the old one.

### Phase 4b: Positioning statement

```
For [target segment]
who [situation or need],
[brand] is the [frame of reference]
that [single point of difference]
because [reason to believe].
Unlike [primary alternative], [brand] [key contrast].
```

Rules: one point of difference (the winner from Phase 4a); a frame of reference the audience already understands (or a deliberately new category with a plan to explain it); a reason to believe that is evidence, not adjectives; the "unlike" line is internal unless legal clears comparative claims. Anti-pattern: "the best [X] for everyone".

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

Mark each touchpoint **PASS** (expresses the position), **PARTIAL** (right category, missing the point of difference) or **FAIL** (generic or contradicting). Consistency score = (PASS + 0.5 × PARTIAL) ÷ touchpoints audited. Fix order: homepage, then the highest-spend paid ads, then sales materials, then everything else; AI/search descriptions follow the source fixes because they lag them.

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
| [..] | [x% — shared: term, term] | [x% or "no data"] | [close/far] | [x% or "no data"] | [same/different] | [same/distinct] |
Nearest competitor: [..] | Overlap reading: [Distinct / Blurred / Interchangeable] | Risk: [..]

--- AUDIENCE ALIGNMENT ---
Problem recognition [x/5] — [evidence]
Outcome desirability [x/5] — [evidence]
Credibility [x/5] — [evidence]
Emotional resonance [x/5] — [evidence]
Category clarity [x/5] — [evidence]
Total: [x/25] → [reading] | Blockers: [dimensions scored 1–2, or none]

--- STRATEGY DIAGNOSIS ---
Distinct: [yes/no] × Aligned: [yes/no] → [PROCEED / DIFFERENTIATE / RE-SEGMENT / PIVOT]

--- CANDIDATE POINTS OF DIFFERENCE ---
| Candidate | Desired | Deliverable | Distinctive | Durable | Total /12 | Verdict |
| [..] | [1–3] | [1–3] | [1–3] | [1–3] | [x] | [chosen / rejected — reason] |
Frame of reference: [existing category / subcategory / new category] — [why]

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
| Touchpoint | Current copy | Status (PASS/PARTIAL/FAIL) | Rewrite / fix | Owner/when |
Consistency score: [x%]

--- RECOMMENDATION ---
Decision: [PROCEED / REFINE / PIVOT] — [1–3 actions, in order]

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

9. **Averaging away a blocker.** A 19/25 with Credibility at 2 is not "nearly strong"; it is a claim the brand cannot prove. Apply the blocker rule and fix proof first.

10. **Overlap scores without the words.** "45% overlap" cannot be checked or argued with. List the shared terms, and say which category words were excluded.

11. **Inventing a category by default.** New categories need education budget and time; most brands win faster as "[category] for [segment]".

12. **Choosing the point of difference by vote.** The founder's favourite claim often fails Deliverable or Distinctive. Score every candidate on the four tests and show the losing candidates and why.

## Verification Checklist

- [ ] Axes derived from documented audience language, with the sources named
- [ ] At least 5 competitors plotted, plus current and target positions
- [ ] Whitespace validated (why empty, why defensible)
- [ ] Distance scored on all six dimensions for each major competitor, with the shared terms listed next to each messaging overlap % ("no data" where a dimension could not be measured)
- [ ] Audience alignment scored 1–5 on five dimensions with evidence, a total reading and any blockers (dimensions at 1–2) named
- [ ] Strategy diagnosis stated (PROCEED / DIFFERENTIATE / RE-SEGMENT / PIVOT) from distance × alignment
- [ ] 2–4 candidate points of difference scored on Desired, Deliverable, Distinctive, Durable; the chosen one has no 1 on Deliverable or Distinctive
- [ ] Frame of reference chosen (existing / subcategory / new) with the reason
- [ ] Positioning statement complete, with a single point of difference and an evidence-based reason to believe
- [ ] Message house: promise, 3–4 key messages with proof, 2–3 signature phrases, never-say list
- [ ] Swap test applied to key messages
- [ ] Consistency audit covers at least 6 touchpoints including AI/search descriptions, each PASS/PARTIAL/FAIL with a rewrite, plus a consistency score
- [ ] Recommendation (PROCEED / REFINE / PIVOT) with ordered actions
- [ ] Assumptions and research gaps stated; no invented customer quotes
