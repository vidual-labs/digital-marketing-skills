---
name: landing-page-funnel
description: Use when auditing, writing or testing landing pages for conversion — above-the-fold structure, ad-to-page message match, body section order, form optimization, social proof, objection handling, mobile and page speed (Core Web Vitals), and A/B test design with proper sample sizes. Also use when someone says "traffic is fine but nobody converts", asks for a landing page teardown, or needs CRO test ideas. Don't use for full website copywriting, e-commerce product detail pages, blog/SEO content (geo-ai-seo) or tracking bugs (gtm-debugging).
version: 1.2.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. Browsing is optional; when the page cannot be fetched, the skill works from a pasted copy, screenshots or a description.
metadata:
  category: conversion-tracking
  updated: 2026-11-17
  tags: [landing-page, cro, conversion-rate-optimization, funnel, ab-testing, forms, social-proof, message-match, core-web-vitals]
  related_skills: [meta-ads-creative, google-ads-keywords, gtm-debugging, branding, geo-ai-seo]
---

# Landing Page Funnel Optimization

## Overview

Audit and improve landing pages so paid and organic traffic converts: match the page to the ad that brought the visitor, answer "what, why me, what next" within seconds, order the body to build belief, remove friction from the form, and prove claims with specific social proof. Includes a test design framework so improvements are measured rather than assumed.

## When to Use

- Auditing an existing landing page that gets traffic but few conversions
- Writing or rewriting landing page copy for a campaign
- Designing A/B tests and prioritizing what to test first
- Aligning landing pages with ad creative (message match)
- Optimizing lead forms, trial sign-ups or booking flows
- Choosing the right page type for each funnel stage

Don't use for: multi-page website copy, e-commerce product detail pages and checkout (different model), blog or AI-search content (use `geo-ai-seo`), or diagnosing why conversions are not *recorded* (use `gtm-debugging`).

## Inputs

Ask for (or extract from the conversation):

- **The page**: URL (fetch it if you can) or pasted copy plus screenshots of desktop and mobile
- **Traffic source and the ad/email** that sends visitors (headline, offer, visual)
- **Conversion goal** and current conversion rate, visitors per week, device split
- **Audience and offer**: who, what they get, price or commitment, guarantee
- **Proof available**: testimonials, numbers, logos, reviews, certifications
- **Form fields** currently required, and which are actually needed to fulfil
- **Speed data**: PageSpeed Insights / Core Web Vitals if available
- **Analytics**: scroll depth, form abandonment, heatmaps if available

Data rules: if you cannot fetch the page, say so and work from what the user provides; do not describe elements you have not seen. Never invent testimonials or numbers — use `[insert proof]`. Benchmarks are starting points; the page's own history and the business's unit economics decide what "good" is. Use the account's currency.

## Diagnose Where the Page Leaks

Before rewriting anything, find the stage where visitors drop. Use the user's analytics (scroll depth, form-start and form-submit events, heatmaps, session recordings); compare segments (mobile vs desktop, each traffic source, each ad) against each other and against the page's own history rather than an industry average.

| Symptom | Likely cause | First fix | Evidence to request if missing |
|---------|--------------|-----------|-------------------------------|
| Most visitors leave without scrolling, worst on paid traffic | Message mismatch or weak above the fold | Message match and H1/offer rewrite | Ad creative, scroll depth by source |
| One device converts far below the other | Mobile layout, speed or form usability | Mobile hero, Core Web Vitals, tap targets, keyboards | Device split of CVR, field data from PageSpeed Insights |
| Visitors scroll, few start the form | Belief or offer: weak proof, unanswered objections, commitment too high | Specific proof near CTA, objection section, lower-commitment option | Heatmap, click map, on-page poll answers |
| Many start the form, few finish | Form friction: too many or sensitive fields, validation errors | Cut or defer fields, multi-step, inline validation | Field-level abandonment, error logs |
| Form CVR fine, leads do not close | Qualification, or the offer attracts the wrong people | Add one qualifying field or price signal; check the ad targeting | CRM outcome per lead source |
| CVR changed suddenly with no page change | Tracking or traffic mix, not the page | Verify the conversion event (`gtm-debugging`); compare sources | Tag change log, source mix by week |

Fix the earliest leaking stage first: improving the form does little for visitors who never reach it.

## Landing Page Anatomy

### Above the fold (first screen on mobile and desktop)

Within ~5 seconds the visitor must know **what this is**, **why it matters to them**, and **what to do next**.

| Element | Rule |
|---------|------|
| H1 | Restates the ad's promise in the visitor's words. Word-for-word match with the ad headline is a feature. |
| Sub-headline | One sentence with a specific benefit, number or mechanism |
| Hero visual | The product or outcome in use; no abstract stock imagery |
| Primary CTA | One action, one button, visible without scrolling on mobile; verb-first label |
| Risk reducer near CTA | "No credit card", "Cancel anytime", "Free 15-min call", a star rating with count |
| Navigation | Removed or minimal; every exit link is a leak |

### Body order

1. **Problem** — name the pain in the visitor's language (2–3 sentences)
2. **Proof of understanding** — a data point, example or quote that shows you get it
3. **Solution** — the transformation, not the feature list
4. **How it works** — 3 steps, visual
5. **Social proof** — specific testimonials, logos, results
6. **Objections** — the 2–3 real ones (price, time, risk, "will it work for me")
7. **Offer recap and CTA** — the same action, plus a lower-commitment alternative
8. **FAQ** — remaining objections in question form (also helps AI and search extraction)

### Form optimization

| Factor | Rule |
|--------|------|
| Fields | Ask only what is needed to deliver the next step; every extra required field costs conversions. Enrich later. |
| Multi-step | For 5+ fields, split into steps starting with the easiest (interest), ending with contact details; show "Step 1 of 3" |
| Validation | Inline, as the user types; message on the field, not a banner |
| Defaults and autofill | Correct `autocomplete` attributes; prefill country/timezone |
| Button label | The outcome: "Get my quote", "Start free trial", "Book the call" — never "Submit" |
| Privacy line | One sentence under the button: what happens with the data, no spam |
| Fallback | A lower-commitment option under the form: "Not ready? Get the guide" |
| Mobile | Tap targets ≥ 44×44 px; correct keyboard types (`type="email"`, `type="tel"`) |
| Consent | Checkbox only where legally required; pre-ticked boxes are not consent in the EU/UK |

### Social proof hierarchy

| Type | Strength | Where |
|------|----------|-------|
| Specific testimonial with name, role, company, result | Very high | Near the first CTA and in the proof section |
| Star rating with count and platform | High | Hero, near CTAs |
| Recognisable logos | High (B2B) | Below hero |
| Case study link with headline number | High | Consideration pages |
| "[n] customers / [n] downloads" | Medium | Anywhere as a quick signal |
| Awards, certifications, security badges | Medium–high in regulated or payment contexts | Near form/payment |

Testimonial formula: `"[Specific result in numbers or concrete change]" — [Name], [Role], [Company]`. "Changed our business" is weak; "cut onboarding from 14 days to 2" is proof.

## Ad-to-Page Message Match

The largest single lever for paid traffic. Score each element 1–5; the overall score is the **lowest** element score, because one broken promise (for example a missing price) loses the visitor however well the rest matches. Any element under 4 is leaking.

| Score | Meaning |
|-------|---------|
| 5 | Same words and same offer, visible above the fold on mobile |
| 4 | Same promise in different words; offer visible above the fold |
| 3 | Related topic, but the specific promise or offer appears only below the fold |
| 2 | Generic page (brand or category) that does not repeat the promise |
| 1 | Contradicts the ad (different price, offer or audience) or is missing it entirely |


| Ad element | Page must match |
|------------|-----------------|
| Headline / hook | H1 uses the same words or the same promise |
| Offer (price, discount, guarantee, free trial) | Identical, visible above the fold |
| Audience named in the ad | Page names the same audience |
| Visual style and colour | Same palette, same imagery style |
| Tone | Same voice |
| Keyword (Search ads) | Appears in H1 or sub-headline |

Dynamic text replacement (by ad group or UTM) is the practical way to keep match high across many ads.

## Speed and Mobile

Most paid traffic is mobile. Test on a real phone, not only a responsive preview.

| Metric | Target (Core Web Vitals, 75th percentile) |
|--------|-------------------------------------------|
| Largest Contentful Paint (LCP) | ≤ 2.5 s |
| Interaction to Next Paint (INP) | ≤ 200 ms |
| Cumulative Layout Shift (CLS) | ≤ 0.1 |

Usual fixes: compress and size the hero image, lazy-load below-the-fold media, remove unused scripts and heavy chat widgets, load the consent banner without blocking render, avoid layout shifts from late-loading fonts and banners.

## Funnel Stage to Page Type

| Stage | Page type | Goal | CTA |
|-------|-----------|------|-----|
| Cold / awareness | Educational, guide, quiz | Capture email, qualify | Download, Take the quiz |
| Consideration | Feature overview, comparison, demo | Trial or call | Start trial, Book a demo |
| Decision | Offer / pricing | Purchase or sign-up | Buy, Sign up |
| Retargeting | Objection-handling, testimonial-heavy, offer | Overcome last barrier | Claim offer |

## CRO Testing Framework

### What to test first

| Element | Typical effect size | Why first |
|---------|--------------------|-----------|
| Offer (price framing, guarantee, trial length) | Largest | Changes the value equation |
| Headline / message match | Large | Decides whether people read on |
| Form length and steps | Large on lead gen | Direct friction |
| Hero visual (image vs product video) | Medium | Comprehension |
| Social proof placement and specificity | Medium | Belief |
| CTA label | Small–medium | Clarity |
| Colour and layout tweaks | Small | Test last |

### Test design rules

- **One hypothesis per test**: "Adding a specific testimonial next to the form will raise form completion because trust is the blocker."
- **Sample size**: calculate it before launching (baseline rate, minimum detectable effect, 95% confidence, 80% power). A quick approximation for two variants: visitors per variant ≈ 16 × p × (1 − p) ÷ (p × MDE)², where p is the baseline conversion rate and MDE the relative lift to detect. Example: p = 3%, MDE = 20% → 16 × 0.03 × 0.97 ÷ 0.006² ≈ 12,900 visitors per variant. Use a proper calculator for the final number; below ~100 conversions per variant results are mostly noise.
- **Feasibility**: weeks needed = (visitors per variant × number of variants) ÷ weekly visitors to the page. Starting point: if that exceeds ~8 weeks, do not run a classic A/B test — raise the MDE with a bolder change, test on a higher-traffic page or step (e.g. form start), or ship and monitor.
- **Duration**: full weeks (2+), never stop early on a peak, run through at least one business cycle.
- **Hold constant**: traffic sources, campaigns and offers between variants; split traffic randomly at the page level.
- **Guardrails**: watch lead quality and down-funnel conversion, not only the form rate.
- **Tooling**: Google Optimize is gone; use the testing tool the team has (VWO, Optimizely, AB Tasty, Convert, Unbounce/Instapage built-ins, or a server-side split). Low-traffic pages: run sequential, bolder changes and judge on direction plus qualitative feedback rather than p-values.

### Ship, test or research?

| Change | Decision | Why |
|--------|----------|-----|
| Fixes a defect: broken element, "Submit" label, missing offer from the ad, slow hero, no mobile CTA, wrong keyboard type | **Ship** (quick win) and monitor | No plausible downside; testing wastes traffic |
| A trade-off: form length vs lead quality, price framing, trial length, gating content | **Test** if feasible, with a down-funnel guardrail | Could help or hurt; the answer depends on the audience |
| Unknown cause (data shows a leak but not why) | **Research** first: polls, recordings, customer interviews | Testing guesses burns weeks |
| Cosmetic: colours, button shape, minor layout | **Ship or skip**; test only on very high traffic | Effects are too small to detect on most pages |

### Reporting a test

```
HYPOTHESIS: [Change] will [effect] because [reason]
CONTROL: [n visitors] → [conversions] = [rate]
VARIANT: [n visitors] → [conversions] = [rate]
LIFT: [relative %] | CONFIDENCE: [%] | MDE planned: [%]
DOWN-FUNNEL CHECK: [lead quality / revenue per visitor]
DECISION: [Ship / iterate / discard] — [why]
```

## Output Format

Use every heading below in this order. When a number is not provided, write "not provided" instead of estimating it. For a copywriting request, replace `LEAK DIAGNOSIS` with the full page copy in body order and keep `MESSAGE MATCH`, `FORM` and `QUICK WINS`.

```
LANDING PAGE AUDIT: [Page / URL]
Traffic source: [Ad / email / organic] | Goal: [conversion] | Current CVR: [x% or not provided]
Traffic: [visitors/week] | Conversions/week: [n] | Devices: [mobile % / desktop %]
Access: [fetched / from screenshots / from copy — page not fetched]

--- LEAK DIAGNOSIS ---
Leaking stage: [above the fold / belief & offer / form / qualification / tracking] — [evidence or "assumed: data needed"]

--- MESSAGE MATCH SCORE: X/5 (lowest element) ---
Headline: [ad] ↔ [page H1] — [score] — [fix]
Offer: [ad] ↔ [page] — [score] — [fix]
Audience / visual / keyword: [score each] — [fix]

--- ABOVE THE FOLD ---
What / why / next: [pass or fail each, with the fix]
H1 rewrite: [..]
Sub-headline rewrite: [..]
CTA label: [current] → [recommended]
Risk reducer: [add ...]

--- BODY FLOW ---
[Current order] → [Recommended order]
Missing sections: [...]
Proof gaps: [`[insert proof]` placeholders and what to collect]
Objections unanswered: [...]

--- FORM ---
Fields: [current n] → [recommended n] | Keep: [..] | Defer: [..] | Remove: [..]
Steps / validation / label / privacy line / fallback: [changes]

--- SPEED & MOBILE ---
LCP / INP / CLS: [values or "not provided"] → [fixes]
Mobile issues: [...]

--- TEST PLAN (priority order) ---
1. Hypothesis: [change → effect because reason] | Metric: [..] | Guardrail: [..] | Baseline: [x%] | MDE: [x%] | Visitors per variant: [n] | Weeks at current traffic: [n] | Decision: [A/B test / sequential / research first]
2. [...]
3. [...]

--- QUICK WINS (ship without testing) ---
- [...]

--- ASSUMPTIONS & MISSING DATA ---
[...]
```

## Common Pitfalls

1. **Several competing CTAs.** Each extra action is a "no" to the main one. Fix: one primary action, repeated, plus one lower-commitment fallback.

2. **Product-first copy.** "Our AI-powered platform…" says nothing about the visitor. Fix: lead with their outcome in their words.

3. **Ignoring message match.** A page that does not repeat the ad's promise makes visitors feel they clicked wrong. Fix: match words, offer and visuals; score the weakest element.

4. **Form before value.** Asking for details before the benefit is clear raises abandonment. Fix: benefit and proof first, or a multi-step form that starts with an easy question.

5. **Desktop-first design.** Most paid traffic is mobile; a hero that needs two scrolls on a phone has no above-the-fold. Fix: design and review the mobile first screen first, on a real device.

6. **Fixing the wrong stage.** Rewriting the form when visitors leave in the hero wastes the effort. Fix: run the leak diagnosis and start at the earliest leaking stage.

7. **Underpowered tests.** Declaring a winner at 30 conversions per variant is a coin flip. Fix: calculate visitors per variant and weeks first; if infeasible, ship, go bolder or research.

8. **Peeking and stopping early.** Checking daily and stopping at the first significant reading inflates false positives. Fix: fix the sample and duration in advance, in full weeks.

9. **Testing on unverified tracking.** A conversion event that double-fires or misses mobile makes every result wrong. Fix: verify the event before the test (`gtm-debugging`).

10. **Optimizing vanity metrics.** Time on page and bounce rate are not conversion. Fix: judge on conversion rate, lead quality and revenue per visitor.

11. **Invented proof.** Placeholder testimonials shipped to production are a legal and trust problem. Fix: mark them `[insert proof]` and collect real ones.

## Verification Checklist

- [ ] Leak diagnosis names the earliest leaking stage, with evidence or a list of data needed
- [ ] Message match scored per element against the actual ad/email; overall score = lowest element
- [ ] Above the fold answers what / why me / what next on mobile without scrolling
- [ ] H1 and sub-headline rewritten with the visitor's words and a specific benefit
- [ ] One primary CTA, verb-first label, risk reducer beside it
- [ ] Body follows Problem → Proof → Solution → Steps → Social proof → Objections → CTA → FAQ
- [ ] Form fields split into keep / defer / remove; validation, label, privacy line and fallback specified
- [ ] Social proof is specific (name, role, result) or marked `[insert proof]`
- [ ] Core Web Vitals targets stated with fixes where data exists
- [ ] Each test has hypothesis, metric, guardrail, visitors per variant and weeks at current traffic; infeasible tests redirected
- [ ] Quick wins (defect fixes) separated from trade-offs that need a test
- [ ] Page not described beyond what was actually fetched or provided
