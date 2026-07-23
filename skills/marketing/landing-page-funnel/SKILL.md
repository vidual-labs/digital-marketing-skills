---
name: landing-page-funnel
description: Use when optimizing landing pages for conversion — funnel structure, CRO testing, headline/body analysis, form optimization, and social proof placement.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [landing-page, CRO, funnel-optimization, conversion, A-B-testing, copy]
    related_skills: [geo-ai-seo, meta-ads-creative, google-ads-keywords, gtm-debugging]
---

# Landing Page Funnel Optimization

## Overview

Optimize landing pages for maximum conversion through systematic copy analysis, funnel structure validation, CRO testing design, and evidence-based improvements. Every landing page should match the ad that brought the visitor, answer their intent within 3 seconds, and reduce friction on the conversion path.

## When to Use

- Auditing an existing landing page for conversion problems
- Writing or rewriting landing page copy to improve conversion rates
- Designing A/B or multivariate tests for landing page elements
- Aligning landing page messaging with ad creative (ad-to-page congruence)
- Optimizing form length, layout, or placement
- Structuring the landing page funnel from traffic to conversion

Don't use for: multi-page website copywriting, e-commerce product pages (different conversion model), or blog/SEO content (use `geo-ai-seo`).

## Landing Page Anatomy

### Above the Fold (Critical Zone)

Must answer within 3 seconds:
1. **What is this?** — clear headline that matches ad messaging
2. **Why does it matter to me?** — value proposition tied to the visitor's need
3. **What do I do next?** — visible CTA or form

| Element | Rule |
|---------|------|
| H1 headline | Must match the ad's promise. Word-for-word matching is a strength, not redundancy. |
| Sub-headline | One sentence supporting the claim with a specific benefit or number |
| Hero visual | Show the product/service in use, not abstract graphics |
| Primary CTA | Visible without scrolling. One action, one button. High-contrast color. |
| Trust signal | Near the CTA: "no credit card," "free for 14 days," or a brief testimonial |

### Body Section Order

1. **Problem** — 2-3 sentences. Name the visitor's pain in their words.
2. **Proof of understanding** — data, survey, or example that validates "we get it."
3. **Solution introduction** — your product/service as the answer. Not features — the transformation.
4. **How it works** — 3 steps max. Visual flow preferred over paragraphs.
5. **Social proof** — testimonials, logos, results, before/after data.
6. **Objection handling** — address the 2-3 real objections (price, time, risk).
7. **Secondary CTA** — repeat the conversion action, different angle (urgency or guarantee).

### Form Optimization

| Factor | Rule |
|--------|------|
| Field count | Each required field reduces conversion by ~5-10%. Collect only what you need now; defer the rest to post-conversion. |
| Inline validation | Show errors as the user types, not on submit. Red text on the specific field, not a banner above the form. |
| Smart defaults | Pre-fill what you know (country from IP, timezone). Autocomplete for email, phone, address. |
| Progress indicator | Multi-step forms must show "Step 1 of 3." Single-step forms never need it. |
| CTA button text | Action-oriented, not "Submit." Use "Get My Quote," "Start Free Trial," or the exact next step. |
| Below-form link | "Or book a call instead" / "Not ready? Get the free guide." Always offer a lower-commitment fallback. |

### Social Proof Hierarchy

| Type | Impact | When to Use |
|------|--------|-------------|
| Named client logos | High — builds immediate credibility | Homepage / first landing page |
| Star ratings with count | High — quantifiable trust | Product/offer pages |
| Specific testimonials | Very high — tells a micro-story | Decision pages, pricing sections |
| Case study links | High — shows depth | Consideration-stage pages |
| "X customers use this" | Medium | Anywhere, as a quick signal |
| Awards/certifications | Medium-High | Trust-sensitive offers (finance, health) |

### Specific testimonial formula

```
"[Specific result quote]"
— [Full Name], [Role] at [Company]
[Serving metric: revenue, time saved, units sold]
```

Vague: "This product changed our business."
Specific: "We cut customer onboarding time from 14 days to 2 days."

## CRO Testing Framework

### What to Test (Priority Order)

| Element | Expected Lift | Test Type |
|---------|--------------|-----------|
| Headline | 10-30% | A/B |
| CTA text or color | 5-15% | A/B |
| Hero image vs video | 5-20% | A/B |
| Form field count | 10-25% | A/B |
| Page layout (1-column vs 2-column) | 5-15% | A/B |
| Social proof placement | 5-10% | A/B |
| Offer (pricing, guarantee type) | 15-40% | A/B |
| Full page variant | 10-30% | A/B or multivariate |

### Test Design Rules

**Sample size:** Minimum 100 conversions per variant for statistical significance (95% confidence). Below 50 conversions, the test is essentially a guess.

**Test duration:** Minimum 2 full weeks (captures weekday/weekend patterns). Never stop mid-week.

**One variable:** Change one element at a time. A/B tests with multiple changes are not actionable — you can never tell what moved the needle.

**Hold constant:** Same traffic source, same audience, same ad creative between variants.

### Test Analysis

```
CONTROL:  baseline = X% conversion
VARIANT:  result = Y% conversion
LIFT:     (Y - X) / X * 100 = Z%
P-VALUE:  must be ≤ 0.05
CONV COUNT:  at least 100 per variant
```

## Ad-to-Page Congruence

The single biggest leverage point. Landing page must match the ad in:

| Ad Element | Landing Page Match |
|------------|-------------------|
| Headline / hook | H1 must use the same words or concept |
| Offer (price, discount, guarantee) | Identical on the page — no surprises kill conversion |
| Visual style / colors | Similar color palette and imagery style |
| Tone (formal, casual, urgent, warm) | Body copy matches the ad's voice |

Scoring: Rate congruence 1-5. Below 4 and you're leaking conversions.

## Funnel Stages to Landing Pages

| Funnel Stage | Page Type | Goal | CTA |
|-------------|-----------|------|-----|
| Awareness | Educational / blog-adjacent | Capture email for nurturing | Download, watch video |
| Consideration | Feature-overview / comparison | Schedule demo or trial | Book a call, start trial |
| Decision | Offer / pricing | Convert to purchase | Buy, sign up |
| Retargeting | Objection-handling / testimonial-heavy | Overcome last barrier | Limited-time offer |

## Common Pitfalls

1. **Multiple CTAs per section.** Each extra action is a "no" to your primary goal. One CTA per above-the-fold. Below the fold, repeat the same CTA or a lower-commitment variant.

2. **Writing for your product, not their problem.** "Our platform leverages AI-driven automation..." tells nothing about the visitor. "Cut reporting time from 4 hours to 15 minutes" — now they care.

3. **Ignoring post-fold.** Half your visitors scroll. If the body section is weak, you've wasted the ad spend that got them to the page.

4. **Form-first thinking.** The value proposition must come before the form. Show the benefit, then ask for contact info — never the reverse.

5. **Mobile as an afterthought.** 50-70% of landing page traffic is mobile. Test your page on actual phones, not just responsive previews. Buttons must be 44px+ tap targets.

6. **Slow load time.** Each additional 100ms of load time reduces conversion by 7%. Above-the-fold must render in under 1.5 seconds.

7. **Testing vanity metrics.** Bounce rate and time-on-page are not conversion proxies. Conversion rate and revenue per visitor are the only metrics that matter.

## Verification Checklist

- [ ] H1 matches the ad the visitor clicked
- [ ] Value clear within 3 seconds (what, why, what next)
- [ ] Primary CTA visible without scrolling
- [ ] Form fields minimized to only-what-you-need-now
- [ ] Social proof placed before and at the second CTA
- [ ] Body follows Problem → Proof → Solution → Steps → Proof → Objections → CTA flow
- [ ] Mobile view tested on real device
- [ ] Page loads under 1.5s for above-the-fold
- [ ] One primary CTA in the hero, one at the bottom
- [ ] No more than 2 conversion paths total on the page
