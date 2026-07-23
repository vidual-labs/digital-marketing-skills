---
name: meta-ads-creative
description: Use when creating creative concepts, ad copy, and campaign ideas for Meta (Facebook/Instagram) ads — primary text, headlines, descriptions, and creative strategy.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [meta-ads, facebook-ads, instagram-ads, creative-concepts, ad-copy, direct-response]
    related_skills: [geo-ai-seo, google-ads-keywords]
---

# Meta Ads Creative Concepts & Copy

## Overview

Create high-converting creative concepts and ad copy for Meta ads (Facebook, Instagram). This skill covers the full creative process: concept development, copywriting for all ad text fields, creative format recommendations, and hook strategies that stop the scroll.

## When to Use

- Writing primary text, headlines, and descriptions for Meta ads
- Developing ad creative concepts for Facebook or Instagram
- Creating A/B test variations of ad copy
- Adapting existing creative for the Meta ecosystem
- Brainstorming concepts for a new Meta campaign

Don't use for: Google Ads copy (use `google-ads-keywords`), LinkedIn or Twitter ads, or landing page copy.

## Meta Ad Text Fields

| Field | Placement | Character Limit | Purpose |
|-------|-----------|----------------|---------|
| **Primary Text** | Above/below creative (FB), caption (IG) | 125 chars visible (1651 max) | Main message, value prop, story |
| **Headline** | Next to CTA button (FB), below creative (IG) | 40 chars visible (60 max) | Reinforce offer, add urgency |
| **Description** | Below headline, above link (FB only) | 30 chars visible (95 max) | Supplementary detail, social proof |
| **CTA Button** | Below headline | Fixed set | Drive action (Shop Now, Learn More, etc.) |

## Creative Framework

### 1. Identify the Angle

Choose one angle per ad variation. Do not mix angles.

| Angle | Use Case | Structure |
|-------|----------|-----------|
| **Problem → Solution** | Pain-driven offers | State the problem, agitate it, present the solution |
| **Social Proof** | Trust-building | Customer result, testimonial, or data point as the hook |
| **How-To / Educational** | Authority positioning | Teach something, then position the offer as the next step |
| **Before → After** | Transformation offers | Show the contrast vividly, attribute it to your offer |
| **Question → Answer** | Curiosity hook | Ask the exact question the audience is thinking |
| **Myth-Busting** | Differentiated offers | "Stop doing X" then explain the better way |
| **Urgency / Scarcity** | Conversion events | Time-bound offer with specific deadline and reason |
| **Direct Offer** | Bottom-funnel, retargeting | State the offer clearly, remove friction |

### 2. Write the Hook

The first 125 characters of primary text are all users see before "See More." Everything that follows is conditional on the hook winning.

**Hook formulas:**
- "Stop [common mistake]: [better approach]"
- "[Specific result] in [specific timeframe]"
- "The [number] [people] use [topic] wrong:"
- "How [target persona] achieved [result] without [common objection]"
- "[Unexpected statement about industry/competitor]"
- "We helped [target] get [result] — here's exactly how"

**Hook rules:**
- No greeting ("Hi," "Hey," "So,")
- No filler ("I'm excited to share," "Here's the thing")
- Make the first line scannable — front-load the value
- Match the hook to the creative — text and visual should amplify each other

### 3. Primary Text Structure

```
[HOOK — 1 line, 125 chars max]

[BODY — 2-4 lines addressing the problem, showing transformation, or explaining the method]

[PROOF — 1 line with specific data, testimonial, or social proof]

[CTLEAD — 1 line that naturally leads to the headline/CTA]
```

**Body rules:**
- Use short sentences (max 20 words per line)
- Include specific numbers (time saved, money earned, percentage better)
- Address the real objection, not the surface one
- Write at a 6th-grade reading level for maximum reach
- Use line breaks every 1-2 sentences for mobile scanning

### 4. Headline Rules

- Complement (not repeat) the primary text
- Add a different angle or create urgency
- Include the offer when applicable
- Max 40 chars for full visibility
- Never repeat the CTA button text

### 5. Description (Facebook only)

- Use for secondary social proof or offer reinforcement
- Examples: "⚡ 50% off ends tonight", "As seen on [media]", "#1 rated in [category]"

### 6. CTA Button

Match CTA to funnel position:

| Funnel Position | CTA |
|----------------|-----|
| Top (Awareness) | Learn More, Watch More |
| Middle (Consideration) | Learn More, Sign Up |
| Bottom (Conversion) | Shop Now, Book Now, Get Quote |
| Retargeting | Shop Now, Get Offer, Get Quote |

## Creative Formats

### Image Ads

- Single strong visual with clear focal point
- Human faces looking at (not away from) the CTA
- Text overlay: max 20% of image area
- Safe areas: avoid top 20%, right 20%, bottom 15% (UI overlap)
- 4:5 ratio (1080×1350) for maximum IG/FB placement

### Video Ads

| Format | Duration | Use |
|--------|----------|-----|
| Short-form | 5-15s | Awareness, rapid testing |
| Story | 15-30s | Education, social proof |
| Long-form | 30-60s | Consideration, detailed offers |

**Video script structure:**
1. **Hook (0-2s):** Visual + text hook that matches primary text
2. **Problem (2-5s):** Show or state the pain point
3. **Solution (5-15s):** Demonstrate the transformation
4. **Proof (15-20s):** Real result, testimonial, or data
5. **CTA (20-25s):** On-screen CTA matching button text

### Carousel Ads

- 2-10 cards, each with its own headline and CTA
- Each card tells one part of the story; the sequence is the argument
- Card 1: hook, Last card: CTA, Middle cards: supporting points
- Use for: feature lists, product showcases, step-by-step process

### Collection Ads

- Cover image + 4 product images below
- Best for: e-commerce catalogs, multiple products
- Cover should show the brand, not a single product

## Output Format

When creating Meta ad copy, always output in this format:

```
Campaign: [Campaign Name]
Objective: [Traffic/Conversions/Awareness/Engagement]
Target Audience: [Description]
Funnel Position: [Top/Middle/Bottom/Retargeting]

--- Ad Variation A (Angle: [_angle name_]) ---

Creative Format: [Image/Video/Carousel]
CTA: [Button text]

Headline: [Text]
Description: [Text] (if Facebook)
Primary Text:
[Text]

Visual Direction: [Brief description of recommended creative]

--- Ad Variation B (Angle: [angle name]) ---

[Same structure, different angle]

--- Ad Variation C (Angle: [angle name]) ---

[Same structure, different angle]
```

Always create at least 3 variations with different angles for A/B testing.

## Common Pitfalls

1. **Writing too long.** Primary text longer than 200 characters often gets "See More" — you just lost half your message. Front-load everything that matters.

2. **Speaking about yourself.** Meta ads that say "we," "our company," "since 2010" underperform. Talk about the customer's world, their problem, their transformation.

3. **Mixing angles.** A single ad trying to educate, build trust, and push urgency becomes a confusing message. One angle per variation.

4. **Generic hooks.** "Are you ready to change your life?" tells the user nothing. Every hook must be specific to the audience and offer.

5. **Ignoring the visual-copy relationship.** Copy that contradicts the visual, or says exactly what the visual already shows, wastes a communication channel.

6. **Feature-dumping.** Listing 10 features in primary text kills conversion. Pick the single most compelling benefit and make it the entire argument.

7. **Not adapting to placement.** Instagram-first creative works differently than Facebook-first. IG: visual-first, shorter copy. FB: copy-first, more text tolerated.

## Verification Checklist

- [ ] Hook is under 125 characters and conveys the full value alone
- [ ] At least 3 ad variations with different angles
- [ ] Primary text matches reading level of target audience
- [ ] Headline complements (not repeats) primary text
- [ ] CTA button matches funnel position
- [ ] Copy is customer-focused (you/your, not we/our)
- [ ] Specific proof points included (numbers, not vibes)
- [ ] Visual direction provided for each variation
- [ ] No filler openers or closers
- [ ] Each variation is testable as a standalone experiment
