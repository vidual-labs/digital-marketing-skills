---
name: meta-ads-creative
description: Use when writing or brainstorming Meta ads (Facebook, Instagram, Messenger, Threads, Audience Network) — primary text, headlines, descriptions, CTA choice, creative concepts, hooks, video scripts, carousel storyboards and A/B variations. Also use when someone asks for "Facebook ad copy", "Instagram ad ideas", "Advantage+ creative variations" or needs to adapt an offer into ad angles. Don't use for Google Search ads (google-ads-keywords), TikTok (tiktok-ads), landing pages (landing-page-funnel) or diagnosing a running Meta campaign (meta-ads-diagnostics).
version: 1.1.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. No tools or Meta API access required.
metadata:
  category: paid-social
  updated: 2026-10-02
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

Data rules: never invent testimonials, statistics or reviews — write `[insert proof]` placeholders if none are provided and say so. Keep claims within Meta's advertising policies (no before/after body images, no personal attributes like "Are you diabetic?", no implied knowledge of the viewer's health or finances). If a character limit or feature below has changed in the user's Ads Manager, follow the UI and mention the discrepancy.

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
AUDIENCE: [Who, funnel stage]
OFFER: [One line] → LANDING PAGE: [URL or page theme]
POLICY NOTES: [Any claims to avoid or substantiate]

--- Ad Variation A (Angle: [angle]) ---
Format: [Image 4:5 + 9:16 / Video 15s / Carousel 5 cards / Catalog]
CTA button: [Text]

Primary text:
[Hook line ≤ 125 chars]

[Body]

[Proof]

[Lead-in]

Headline options (≤ 40 chars, aim for ≤ 27): 1) [..] 2) [..]
Description (≤ 30 chars, optional): [..]

Creative direction:
[Visual concept, on-screen text, first-2-second action, safe-zone notes]
[For video: timestamped script | For carousel: card-by-card]

Hypothesis: [What this variation tests and what result would confirm it]

--- Ad Variation B (Angle: [different angle]) ---
[...]

--- Ad Variation C (Angle: [different angle]) ---
[...]

TESTING NOTE: [Which variable differs between variations; which to launch first]
```

Always produce at least three variations with genuinely different angles. Different adjectives are not a test.

## Common Pitfalls

1. **Burying the point.** If the first 125 characters do not carry the value, the "See more" fold hides it. Write the hook last, after you know the argument.

2. **Talking about yourself.** "We", "our company", "since 1998" underperform "you", "your", and the customer's outcome.

3. **Mixing angles in one ad.** Educate, prove and pressure in one piece of copy and none of it lands. One angle per variation.

4. **Invented proof.** A made-up "4.9 stars" is a policy violation and a trust breach. Placeholder it and tell the user.

5. **Ignoring policy.** Personal attribute phrasing ("Struggling with debt?"), before/after bodies, or unsubstantiated health claims get ads rejected and accounts flagged.

6. **Designing one square image for everything.** Stories and Reels crop the top and bottom; feed shows 4:5 larger than 1:1. Supply the right ratios.

7. **Treating headline and primary text as a pair.** Advantage+ can recombine them. Each must make sense alone.

8. **Variations that are not hypotheses.** Three ads with the same angle and a different emoji teach nothing. Change the angle, the format or the hook mechanism.

## Verification Checklist

- [ ] At least 3 variations, each with a different angle and a stated hypothesis
- [ ] Each hook is ≤ 125 characters and conveys the value by itself
- [ ] Headlines ≤ 40 characters with the key words in the first 27; at least 2 options per variation
- [ ] Descriptions ≤ 30 characters and optional
- [ ] CTA button matches the funnel stage and is not repeated in the headline
- [ ] Copy is customer-focused ("you") with concrete numbers or `[insert proof]` placeholders — nothing invented
- [ ] No policy-risky phrasing (personal attributes, before/after bodies, unverifiable claims)
- [ ] Creative direction specifies ratio(s), first-2-second action and safe zones
- [ ] Video scripts are timestamped and include on-screen text/captions
- [ ] The ad promises only what the named landing page delivers
- [ ] Testing note explains which variable each variation isolates
