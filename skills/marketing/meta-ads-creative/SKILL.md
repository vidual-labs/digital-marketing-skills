---
name: meta-ads-creative
description: Use when writing or brainstorming Meta ads (Facebook, Instagram, Messenger, Threads, Audience Network) — primary text, headlines, descriptions, CTA choice, creative concepts, hooks, video scripts, carousel storyboards and A/B variations. Also use when someone asks for "Facebook ad copy", "Instagram ad ideas", "Advantage+ creative variations" or needs to adapt an offer into ad angles. Don't use for Google Search ads (google-ads-keywords), TikTok (tiktok-ads), landing pages (landing-page-funnel) or diagnosing a running Meta campaign (meta-ads-diagnostics).
version: 1.2.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. No tools or Meta API access required.
metadata:
  category: paid-social
  updated: 2026-11-17
  tags: [meta-ads, facebook-ads, instagram-ads, creative-concepts, ad-copy, hooks, direct-response, advantage-plus]
  related_skills: [meta-ads-diagnostics, tiktok-ads, landing-page-funnel, branding]
---

# Meta Ads Creative Concepts & Copy

## Overview

Create scroll-stopping creative concepts and copy for Meta placements: Facebook and Instagram feeds, Reels, Stories, Messenger, Threads and Audience Network. The skill covers angle selection, hook writing, every text field, format-specific creative direction and a testable set of variations. Meta's delivery system now does most of the audience targeting; creative is the main lever advertisers still control, so each variation must be a distinct hypothesis.

## When to Use

- Writing primary text, headlines and descriptions for Meta ads
- Developing creative concepts for a new campaign or offer
- Producing 3+ variations with different angles for testing
- Writing short video scripts or carousel storyboards for Reels and feed
- Adapting an existing offer, landing page or email into ad angles

Don't use for: Google Search ad copy (use `google-ads-keywords` for keywords and the RSA guidance in `google-ads-diagnostics`), TikTok creative (use `tiktok-ads`), landing page copy (use `landing-page-funnel`), or performance analysis (use `meta-ads-diagnostics`).

## Inputs

Ask for (or extract from the conversation):

- **Offer**: product/service, price or price anchor, the one transformation it delivers
- **Audience**: who buys, what they have tried, the objection that stops them
- **Funnel stage**: cold prospecting, warm (engaged / site visitors), retargeting (cart, leads)
- **Proof**: numbers, reviews, logos, guarantees that can legally be used
- **Brand voice** and any banned claims (health, finance, employment and housing have policy limits)
- **Formats available**: can they shoot video, do they have UGC, product photos, a catalog?
- **Landing page** the ad points to (the ad must promise what the page delivers)
- **Existing ad results** when iterating: per-ad hook rate, hold rate, link CTR, CPA/ROAS and frequency (export or screenshot). With these, diagnose before writing (step 0b)
- **Special Ad Category**: whether the campaign is declared as financial products and services, employment, housing, or social issues, elections or politics (it changes who the copy must speak to)

Data rules: never invent testimonials, statistics or reviews — write `[insert proof]` placeholders if none are provided and say so. Keep claims within Meta's advertising policies (no before/after body images, no personal attributes like "Are you diabetic?", no implied knowledge of the viewer's health or finances). If a character limit or feature below has changed in the user's Ads Manager, follow the UI and mention the discrepancy. Count characters rather than estimating, and show the count next to every hook and headline so the user can check it.

## Meta Ad Text Fields (2026)

| Field | Where it shows | Visible before truncation | Hard limit | Job |
|-------|---------------|---------------------------|-----------|-----|
| **Primary text** | Above the creative (FB), caption (IG) | ~125 characters before "See more" | 2,200 (shorter is better) | The hook and the argument |
| **Headline** | Below creative next to CTA (FB); below creative (IG feed) | ~27 characters on most placements | 40 | Restate the offer or add urgency; not shown on Reels/Stories |
| **Description** | Below the headline (FB feed and right column only) | ~27 characters | 30 | Optional proof or offer detail; hidden on mobile often |
| **CTA button** | Fixed list | — | — | Match funnel stage |
| **Display link** | Under headline | — | — | Clean domain |

Advantage+ creative may rewrite text, generate variations, adjust brightness, add music or crop images. Write copy that still works if the system shows a different headline/primary text pairing — each field must stand alone.

## Creative Framework

### 0a. Match the angle to the audience's awareness

Pick angles from where the audience is, not from what the brand wants to say. Funnel stage and awareness usually move together; when they disagree, awareness wins.

| Audience state | Typical audience | Lead with | Avoid |
|----------------|------------------|-----------|-------|
| Unaware of the problem | Broad / Advantage+ audience, new category | Question → Answer, educational, pattern-interrupt UGC | Price-first direct offers; jargon |
| Problem-aware | Broad prospecting, interest seeds | Problem → Solution, myth-busting | Brand history, feature lists |
| Solution-aware, comparing | Engaged, video viewers, competitor-curious | Contrarian, demo, specific social proof | Generic "best quality" claims |
| Product-aware | Site visitors, IG/FB engagers | Social proof, objection handling, offer | Re-explaining the problem from zero |
| Most aware | Add to cart, initiate checkout, open leads | Direct offer, risk reversal (returns, guarantee), real urgency | Long education, new claims the page does not back |

### 0b. When iterating, diagnose the existing ad first

If the user shares results, name the weak step before writing. Compare each ad with the account's own median for the same funnel stage; the bands below are fallbacks when no history exists.

| Signal (vs account median) | Starting-point fallback | Diagnosis | What the next variation changes |
|----------------------------|------------------------|-----------|---------------------------------|
| Low hook rate (3-s plays ÷ impressions) | < ~20–25% | The first 1–2 seconds do not stop the scroll | Opening frame and first line only; keep body and offer |
| Good hook, low hold rate (ThruPlays ÷ 3-s plays) | < ~8–10% | The middle stalls or the promise is not paid off | Cut setup, show the product earlier, shorten |
| Good hold, low link CTR | < ~0.8–1% | No reason to click now | Offer framing, on-screen CTA, headline, risk reversal |
| Good CTR, poor post-click conversion | Below account norm | Ad promises something the page does not deliver | Align the promise with the page; send page issues to `landing-page-funnel` |
| All steps healthy but CTR falling as frequency rises | Frequency > ~3 (7-day, prospecting) | Fatigue | New angle or format around the same insight; account-level fixes in `meta-ads-diagnostics` |

Iteration rule: when an ad wins, change one element per variation (hook, format, speaker or offer framing) and keep the winning angle. When nothing has won, change the angle.

### 1. Pick one angle per variation

| Angle | Best for | Structure |
|-------|----------|-----------|
| **Problem → Solution** | Pain-driven offers | Name the problem in their words, agitate briefly, present the fix |
| **Social proof** | Trust-building, warm audiences | Lead with a specific result or review, then the offer |
| **Educational / how-to** | Authority, cold audiences | Teach one useful thing, position the product as the next step |
| **Before → After** | Transformation offers | Contrast the two states; the product is the bridge (no body-image before/afters) |
| **Question → Answer** | Curiosity | Ask the question they are already asking |
| **Myth-busting / contrarian** | Differentiated products | "Stop doing X" and explain the better way |
| **Urgency / scarcity** | Conversion events, retargeting | A real deadline and a reason for it |
| **Direct offer** | Bottom funnel | Offer, terms, CTA — nothing else |
| **UGC / creator testimony** | Cold and warm | A real customer's phone video, first person, lightly edited |

### 2. Write the hook

The first ~125 characters of primary text, and the first 1–2 seconds of a video, decide everything. Everything after is conditional on the hook winning.

Hook formulas:

- "Stop [common mistake]. [Better approach] instead."
- "[Specific result] in [specific timeframe] — without [common objection]."
- "The [number] mistakes [persona] make with [topic]."
- "How [persona] got [result] (no [thing they dread])."
- "[Unexpected, true statement about the category]."
- "We asked [n] [persona] why they switched. Here's what they said."

Hook rules: no greetings, no "I'm excited to announce", front-load the specific value, and make the hook amplify the visual rather than describe it.

### 3. Primary text structure

```
[HOOK — 1 line, ≤ 125 characters, works alone]

[BODY — 2–4 short lines: the problem, the mechanism, the transformation]

[PROOF — 1 line: a specific number, review or guarantee]

[LEAD-IN — 1 line that hands off to the headline/CTA]
```

Body rules: sentences under ~20 words, line breaks every 1–2 sentences for mobile, concrete numbers, address the real objection, write at an everyday reading level, speak to "you" not "we".

### 4. Headline rules

Complement the primary text rather than repeat it; put the offer or the outcome in the first 27 characters; never duplicate the CTA button text; write at least two alternative headlines per variation for Advantage+ and manual testing.

### 5. Description

Optional. Use it for one proof point or offer term: "Free shipping over 50", "4.8★ from 12,000 reviews", "Cancel anytime". Assume it may not render.

### 6. CTA button by funnel stage

| Stage | CTA options |
|-------|-------------|
| Cold / awareness | Learn more, Watch more |
| Consideration | Learn more, Sign up, Get quote, Download |
| Conversion | Shop now, Book now, Subscribe, Get offer |
| Retargeting | Shop now, Get offer, Buy now |
| Messaging objectives | Send message, Send WhatsApp message |
| Lead forms | Sign up, Apply now, Get quote |

### 7. Make the set diverse enough to learn from

Meta's delivery tends to treat near-identical ads as one and concentrates spend on a few ads quickly, so variations must differ in ways a viewer would notice.

| Set type | Rule |
|----------|------|
| Launch set (no winner yet) | ≥ 3 different angles; when production allows, ≥ 2 formats (e.g. static + video) and ≥ 2 speakers or visual worlds |
| Iteration set (from a winner) | Same angle; each variation changes exactly one element and names it |
| Hook test | Same body, CTA and offer; only the first line / first 2 seconds differ |

### 8. Policy-safe rewrites

Meta reviews the ad and the landing page. These patterns cause most rejections; rewrite instead of hoping review misses them.

| Risky pattern | Why it fails | Compliant direction |
|---------------|-------------|---------------------|
| "Are you struggling with debt?" / "Still anxious at night?" | Asserts or implies a personal attribute (finances, health, mental state) of the viewer | Talk about the situation or the product: "A debt plan built around a real monthly budget" / "Wind-down routines for nights that run long" |
| Before/after body or face comparisons | Prohibited for health, weight and appearance claims | Product in use, routine, texture or packaging shots; describe progress without contrasting bodies |
| "Lose 10 kg in 30 days", "cures", "guaranteed income" | Unrealistic or unsubstantiated outcome claims | Substantiated, specific terms or `[insert substantiated claim]` |
| Fake UI (play buttons, notification badges, fake "close" buttons) | Misleading interface elements | Real product screenshots only |
| Narrow-audience copy in a Special Ad Category ("For women over 50 in Leeds") | The category limits targeting and the copy must not discriminate | Write for anyone eligible; describe the offer, not the viewer |

Flag every risky element the user asked for, explain the risk in one line, and supply the compliant version instead of silently dropping it.

## Creative Formats and Specs

Meta's placement-level rules changed: the old "20% text" rule is gone, but text-heavy images still get less distribution. Design for the placement.

### Image

- One focal point; faces looking toward the headline or product
- Feed: 1:1 (1080×1080) or 4:5 (1080×1350) — 4:5 takes more screen on mobile
- Stories/Reels: 9:16 (1080×1920); keep the top ~14% and bottom ~20–35% free of text and logos (UI overlays)
- Upload both ratios so Advantage+ placements use the right one, or let the system crop only if you have checked the crops
- On-image text: a short headline (≤ 5 words) is fine; paragraphs are not

### Video

| Length | Use | Structure |
|--------|-----|-----------|
| 6–15 s | Awareness, Reels, Stories | Hook (0–2 s) → one benefit → CTA |
| 15–30 s | Consideration, most conversion ads | Hook → problem → solution/demo → proof → CTA |
| 30–60 s | Complex offers, retargeting, UGC testimonials | Hook → story → mechanism → proof → objection → CTA |

Video rules: hook in the first 1–2 seconds with movement or a bold on-screen line; captions always (most feed video plays muted); show the product in use by second 5; on-screen CTA matching the button; vertical 9:16 for Reels/Stories plus a 4:5 or 1:1 cut for feed. Reels now runs as a placement in Advantage+ and often has cheaper CPMs than feed for the same creative — shoot native-looking vertical first.

### Carousel

- 2–10 cards, each with its own image, headline and link
- Card 1 is the hook, the last card is the CTA, middle cards carry one point each
- Use for: feature walkthroughs, product ranges, step-by-step processes, multiple testimonials
- Dynamic/catalog carousels: write the primary text so it works with any product shown

### Collection and catalog (Advantage+ catalog ads)

- Cover image or video plus products from the catalog, opens an Instant Experience
- Best for e-commerce with a product feed; the cover should set the mood or show the range, not one SKU

### Flexible format and Partnership ads

- **Flexible ad format**: upload up to 10 images/videos and let Meta choose the format per person; still write copy that stands alone
- **Partnership ads** (formerly branded content): run a creator's post as an ad from both handles — brief the creator on the hook, not the script

## Output Format

```
CAMPAIGN: [Name]
OBJECTIVE: [Sales / Leads / Traffic / Engagement / Awareness / App]
AUDIENCE: [Who] | STAGE: [Cold / Warm / Retargeting] | AWARENESS: [Unaware / Problem / Solution / Product / Most aware]
OFFER: [One line] → LANDING PAGE: [URL or page theme]
PROOF USED: [Facts the user supplied, or "none supplied — placeholders used"]
POLICY NOTES: [Risky elements requested → compliant replacement, or "None"]
ITERATION READ: [Only when results were shared: weak step + metric vs account median → what changes; otherwise "n/a — new set"]

--- Ad Variation A (Angle: [angle]) ---
Changes vs control: [Launch set: "new angle" | Iteration: the one element changed]
Format: [Image 4:5 + 9:16 / Video 15s / Carousel 5 cards / Catalog]
CTA button: [Text]

Primary text:
Hook ([n] chars): [Hook line ≤ 125 chars]

[Body]

[Proof]

[Lead-in]

Headline options (≤ 40 chars, key words in first 27): 1) [..] ([n] chars) 2) [..] ([n] chars)
Description (≤ 30 chars, optional): [..]

Creative direction:
[Visual concept, on-screen text, first-2-second action, safe-zone notes]
[For video: timestamped script | For carousel: card-by-card]

Hypothesis: If [what this variation does differently], then [primary metric] beats [control / other variations] because [audience insight].
Primary metric: [Hook rate / link CTR / CPA / ROAS — chosen by stage]

--- Ad Variation B (Angle: [different angle]) ---
[...]

--- Ad Variation C (Angle: [different angle]) ---
[...]

TEST PLAN
Variable isolated: [Angle / hook / format / offer framing]
Setup: [Ads in one ad set / A/B test / separate ad sets — and why]
Launch first: [Variation] because [reason]
Judge on: [Metric] after [minimum data, e.g. spend ≥ 1–2× target CPA per variation]
Next step: [What to build if the winner is A / B / C]
```

Always produce at least three variations with genuinely different angles (or, for an iteration set, three different single-element changes). Different adjectives are not a test. Fill every line; write "n/a — [reason]" rather than deleting one.

### Choosing the primary metric and minimum data

| Stage / test | Judge on | Minimum before calling it (starting point; use the account's own norms when known) |
|--------------|----------|-----------------------------------------------|
| Hook test | Hook rate, then link CTR | A few thousand impressions per variation |
| Cold prospecting concept | CPA or ROAS, with link CTR as the early read | Spend ≥ ~1–2× target CPA per variation |
| Retargeting | CPA and frequency | Spend ≥ ~1× target CPA; audiences are small, so read sooner but expect noise |
| Lead gen | Cost per qualified lead, not raw CPL | Enough leads for the sales team to grade quality |

Meta will spend unevenly across ads in one ad set. An ad that received little spend has not lost; it has not been tested. For a clean comparison use the A/B test feature or separate ad sets with equal budgets.

## Common Pitfalls

1. **Burying the point.** If the first 125 characters do not carry the value, the "See more" fold hides it. Write the hook last, after you know the argument.

2. **Talking about yourself.** "We", "our company", "since 1998" underperform "you", "your", and the customer's outcome.

3. **Mixing angles in one ad.** Educate, prove and pressure in one piece of copy and none of it lands. One angle per variation.

4. **Invented proof.** A made-up "4.9 stars" is a policy violation and a trust breach. Placeholder it and tell the user.

5. **Ignoring policy.** Personal attribute phrasing ("Struggling with debt?"), before/after bodies, or unsubstantiated health claims get ads rejected and accounts flagged. Use the rewrite table and explain the swap.

6. **Designing one square image for everything.** Stories and Reels crop the top and bottom; feed shows 4:5 larger than 1:1. Supply the right ratios.

7. **Treating headline and primary text as a pair.** Advantage+ can recombine them. Each must make sense alone.

8. **Variations that are not hypotheses.** Three ads with the same angle and a different emoji teach nothing. Change the angle, the format or the hook mechanism.

9. **Pitching the wrong awareness level.** A price-first offer to a cold audience that does not know it has the problem wastes the impression. Pick the angle from the awareness table first.

10. **Rewriting a winner from scratch.** Changing hook, angle and format at once loses what worked and teaches nothing. Iterate one element at a time on a winner; change the angle only when nothing has won.

11. **Fixing the wrong step.** A new hook will not fix a weak post-click conversion rate. Diagnose the weak step (step 0b) before writing iterations.

12. **Calling a test from uneven spend.** Low-spend ads have not lost. Judge only variations that reached the minimum data, or use an A/B test for an even split.

13. **Guessing character counts.** "About 120 characters" is how 140-character hooks ship. Count and print the number next to each hook and headline.

## Verification Checklist

- [ ] Header names stage and awareness level, and the angles fit the awareness table
- [ ] At least 3 variations, each with a different angle (launch) or one named element changed (iteration), and an if/then hypothesis
- [ ] If results were shared, ITERATION READ names the weak step with the metric before any copy is written
- [ ] Each hook is ≤ 125 characters, shows its character count and conveys the value by itself
- [ ] Headlines ≤ 40 characters with counts and the key words in the first 27; at least 2 options per variation
- [ ] Descriptions ≤ 30 characters and optional
- [ ] CTA button matches the funnel stage and is not repeated in the headline
- [ ] Copy is customer-focused ("you") with concrete numbers or `[insert proof]` placeholders — nothing invented; PROOF USED lists the source
- [ ] No policy-risky phrasing (personal attributes, before/after bodies, unverifiable claims); every risky request is flagged with its compliant replacement
- [ ] Creative direction specifies ratio(s), first-2-second action and safe zones
- [ ] Video scripts are timestamped and include on-screen text/captions
- [ ] The ad promises only what the named landing page delivers
- [ ] TEST PLAN names the isolated variable, setup, primary metric and minimum data before a call
