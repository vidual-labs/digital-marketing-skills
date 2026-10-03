---
name: branding
description: Use when defining, refreshing or documenting a brand identity system — visual identity (logo, colour, typography, imagery, layout), brand voice and tone matrix, vocabulary, copy standards by channel, naming conventions, touchpoint consistency and brand guidelines for humans and AI content tools. Also use when someone asks for "brand guidelines", "tone of voice", "a style guide for our content", "our brand feels inconsistent" or needs a brand brief for designers or AI writing. Don't use for one-off ad copy (meta-ads-creative, tiktok-ads), competitive positioning (market-positioning) or competitor analysis (competitor-research).
version: 1.1.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. No tools required; a contrast checker or browsing helps for colour accessibility checks but is optional.
metadata:
  category: brand
  updated: 2026-10-02
  tags: [branding, brand-identity, visual-identity, brand-voice, tone-of-voice, brand-guidelines, copywriting, naming, design-system, accessibility]
  related_skills: [market-positioning, competitor-research, landing-page-funnel, instagram-organic, linkedin-organic, youtube-organic, meta-ads-creative]
---

# Branding

## Overview

Build a cohesive brand identity system — visual, verbal, strategic and experiential — so every output is recognisable before the logo is seen. Covers visual identity, voice and tone, vocabulary, copy standards per channel, naming, touchpoint consistency and the practical guidelines that keep humans, agencies and AI tools producing the same brand. A brand is the pattern of associations an audience builds across touchpoints; this skill makes that pattern deliberate.

## When to Use

- Creating a brand identity from scratch (startup, product, market entry)
- Refreshing a brand that feels stale, inconsistent or dated
- Writing brand guidelines for a team, agency, freelancers or AI content workflows
- Defining voice and tone before a content or campaign programme
- Naming a product, feature or sub-brand
- Auditing touchpoints for consistency

Don't use for: single ad or post copy (use `meta-ads-creative`, `tiktok-ads`), competitive positioning and messaging architecture (use `market-positioning`), or competitor analysis (use `competitor-research`).

## Inputs

Ask for (or extract from the conversation):

- **Brand or working name**, what it sells, to whom, and the price tier
- **Positioning statement** or point of difference (run `market-positioning` first if none exists; otherwise capture a one-line hypothesis)
- **Existing assets**: logo files, colours, fonts, templates, past guidelines
- **Audience and context**: where the brand is encountered (web, app, social, retail, print, packaging)
- **Competitor look and feel** to differentiate from
- **Constraints**: accessibility requirements, legal (trademarks, regulated claims), languages and scripts, budget for fonts and photography
- **Personality cues**: 3–5 adjectives the team uses, and 3 they reject

Data rules: do not invent hex codes for an existing brand — ask for them or mark values as proposals. Check trademarks and domains only if you can; otherwise flag them as to-do items. Where this skill cites standards (WCAG levels, platform safe zones) the versions are current as of `metadata.updated`; confirm against the platform if it matters legally.

## Brand System Architecture

| Pillar | Components | Deliverable |
|--------|-----------|-------------|
| Strategic | Positioning, promise, values, personality | Brand foundation (one page) |
| Verbal | Voice attributes, tone matrix, vocabulary, naming, tagline | Voice & tone guide |
| Visual | Logo, colour, typography, imagery, iconography, layout, motion | Visual identity guide |
| Experiential | Touchpoint standards, templates, content and AI usage rules | Touchpoint playbook |

Build in that order. Visual decisions made before the strategic and verbal ones get redone.

## 1. Strategic Foundation

- **Promise**: one sentence of what the audience can always expect
- **Personality**: 3–4 adjectives with "is / is not" boundaries (used again in voice)
- **Values**: 3–5, each with a behaviour that proves it
- **Positioning**: from `market-positioning` — the frame of reference and point of difference the identity must express

## 2. Visual Identity

### 2.1 Logo

| Decision | Guidance |
|----------|---------|
| Type | Wordmark, lettermark, pictorial, abstract or combination; choose for memorability and scalability |
| Variants | Primary, horizontal, stacked, icon/lettermark, monochrome, reversed |
| Sizes | Legible at 16 px (favicon), 48–64 px (avatars), 500 px (web), large format |
| Clear space | At least the height of the main letterform around the logo |
| Don'ts | No stretching, recolouring outside the palette, effects, or placing on busy imagery |
| Files | SVG master, PNG with transparency, dark and light versions |

### 2.2 Colour

| Role | Count | Purpose |
|------|-------|---------|
| Primary | 1 | The colour the brand owns: logo, primary actions |
| Secondary | 2–3 | Hierarchy, sections, illustration |
| Accent | 1–2 | Highlights and interactive states |
| Neutrals | 4–6 | Text, backgrounds, borders, surfaces (define light and dark mode sets) |
| Semantic | 4 | Success, warning, error, info — must not clash with brand colours |

Rules: exact hex (and optionally OKLCH/HSL for design systems); every text/background pairing meets **WCAG 2.2 AA** (4.5:1 body, 3:1 large text and UI components); check the palette in greyscale for hierarchy; define which pairings are allowed; never rely on colour alone to convey meaning.

### 2.3 Typography

| Element | Specification |
|---------|-------------|
| Primary typeface | One family for headings and body; variable fonts simplify weights |
| Secondary | Optional (display or monospace) only with a defined job |
| Scale | Named steps (display, h1–h4, body, small, caption) on a ratio (1.2–1.333) with rem values |
| Weights | 2–4 maximum |
| Line height | Body 1.5–1.7; headings 1.1–1.25 |
| Fallbacks | System stack per platform; test with fallbacks active |
| Licensing | Confirm web, app and desktop licences; open-source fonts avoid the problem |

| Personality | Typeface direction | Open-source examples |
|-------------|-------------------|----------------------|
| Modern, clean | Geometric sans | Inter, Manrope, Outfit |
| Trustworthy, human | Humanist sans | Source Sans 3, Nunito Sans, Figtree |
| Playful, creative | Rounded or display | Fredoka, Quicksand, Bricolage Grotesque |
| Premium, editorial | Serif | Playfair Display, Lora, Fraunces |
| Technical | Monospace / grotesk | JetBrains Mono, IBM Plex Mono, Space Grotesk |

### 2.4 Imagery and illustration

| Element | Decide |
|---------|--------|
| Photography | Lifestyle, product, documentary, abstract; lighting, colour grading, composition rules |
| Illustration | Flat, line, 3D, hand-drawn, or none; stroke, palette, perspective |
| People | Representation guidelines, candid vs posed, real customers vs stock |
| Screenshots / UI | Device frames, shadows, background treatment |
| AI-generated imagery | Allowed or not; required disclosure; style prompts and a do-not list; licence and model policy |
| Alt text | Part of the voice; descriptive, no "image of" |

Test: shuffle brand images with competitors' — if yours are not identifiable at a glance, the style is not distinctive enough.

### 2.5 Layout, spacing, motion

| Element | Guideline |
|---------|-----------|
| Grid | 12-column web, 4-column mobile, consistent gutters |
| Spacing scale | 4/8 px base (4, 8, 12, 16, 24, 32, 48, 64) |
| Radius | One system (0 / 4 / 8 / 16 px / pill) |
| Elevation | 2–3 shadow levels or none |
| Max width | ~65–75 characters per line for reading; 1200–1440 px layouts |
| Motion | Durations (150–300 ms UI), easing, what animates and what never does; respect reduced-motion settings |
| Dark mode | Palette mapping defined, not inverted automatically |

## 3. Brand Voice

### 3.1 Voice attributes (constant)

Define 3–4 attributes, each with what it means and what it is not:

| Attribute (example) | Means | Is not |
|---------------------|-------|--------|
| Plain-spoken | Short words, concrete nouns, no jargon | Dumbed down, slangy |
| Expert | Leads with evidence and specifics | Academic, condescending |
| Warm | Addresses the reader, acknowledges effort | Gushing, emoji-heavy |
| Direct | Says the point first | Blunt, dismissive |

"Friendly" and "professional" alone are table stakes, not attributes; the attribute is *how* the brand is friendly differently.

### 3.2 Tone matrix (adapts by context)

| Context | Tone | Example shift |
|---------|------|---------------|
| Launch / announcement | Energetic, confident | Benefit-led headline, active verbs |
| Error / outage | Calm, specific, accountable | What happened, what to do, when it is fixed |
| Education / help | Patient, step-by-step | Numbered steps, no assumed knowledge |
| Sales / conversion | Clear, evidence-led | Outcome, proof, one next step |
| Support reply | Empathetic, solution-first | Acknowledge, resolve, confirm |
| Social reply | Conversational, brief | Human, in-joke aware, never corporate |
| Legal / policy | Plain, precise | Short sentences, defined terms |
| Crisis | Transparent, measured | Facts, responsibility, next update time |

### 3.3 Vocabulary

A use / avoid list makes writing recognisable and keeps product terms consistent.

| Use | Avoid | Why |
|-----|-------|-----|
| "Free trial" | "Complimentary period" | One name for one offer |
| "Get started" | "Begin your journey" | Cliché |
| "You / your" | "Users / customers" (in copy) | Direct address |
| Product term list | Synonyms for the same feature | Searchability and clarity |

Minimum 10 pairs; 25+ for teams. Add spelling conventions (sentence case, serial comma, numerals, date and currency formats, localisation notes).

### 3.4 Sentence style

Average 12–20 words; vary rhythm; active voice; one idea per paragraph; headlines lead with the benefit or action; ban list of filler ("leverage", "seamless", "cutting-edge", "we're excited to announce"); prefer specific numbers and named examples; inclusive language by default.

## 4. Copy Standards by Channel

| Channel | Length | Pattern | Goal |
|---------|--------|---------|------|
| Homepage headline | 5–10 words | Outcome for whom | Communicate position in 3 seconds |
| Ad headline | ≤ 27–40 characters (Meta) / 30 (Google RSA) | Offer or outcome | Stop the scroll |
| Ad primary text | ≤ 125 characters before the fold | Hook → proof → CTA | Click |
| Landing page body | 200–600 words | Problem → proof → solution → steps → proof → objections → CTA | Convert |
| Social post | 1–3 short paragraphs; first line carries the idea | Native to each platform | Engagement, saves, sends |
| Email subject | 3–7 words | Specific benefit or curiosity, no bait | Open |
| Email body | 80–250 words | One idea, one CTA | Click |
| Product description | 50–150 words | Feature → benefit → spec | Decide |
| Help article | As long as needed, scannable | Answer first, steps, screenshots | Resolve |
| Alt text | ≤ 125 characters | Describe content and function | Accessibility |

### CTA rules

One primary CTA per screen; verb first ("Get", "Start", "Book"); specific ("Get the pricing sheet" beats "Download"); primary CTA uses the accent/action colour, secondary is outline or text; minimum 44×44 px tap target.

## 5. Naming Conventions

| Asset | Convention |
|-------|-----------|
| Products / sub-brands | Pronounceable, memorable, available (domain, handles, trademark search); max 3 syllables preferred; architecture decided (branded house vs house of brands) |
| Features | Functional and benefit-oriented ("Smart Search"); avoid invented words users cannot search |
| Campaigns | Internal `YYYY-channel-campaign`; external emotional or benefit-led |
| Files | `brand_channel_asset_version_YYYY-MM-DD.ext` |
| Design tokens | `color.brand.primary`, `space.4`, `font.heading` |

## 6. Touchpoint Consistency and AI Usage

| Touchpoint | Check | Standard |
|------------|-------|---------|
| Website / app | Colours, type, imagery, voice, CTA | Design tokens in code |
| Social profiles | Avatar, banner, bio voice, pinned content | Template per platform with safe zones |
| Ads | Palette, type, copy voice, imagery style | Ad template library |
| Email | Header, signature, voice, button style | Master template |
| Decks and documents | Template, charts, type | Master templates |
| Help and docs | Voice, formatting, screenshots | Writing guide for contributors |
| Packaging / physical | Logo placement, colour matching (Pantone/CMYK), type | Print guide |
| AI content tools | System prompt with voice, vocabulary, banned words, examples; review step before publishing; disclosure policy | Brand prompt pack |

The **brand prompt pack** (voice attributes, tone matrix, vocabulary, three good and three bad examples, visual style prompts) is now a standard deliverable: it is how the brand survives AI-assisted production.

## Output Format

```
BRAND IDENTITY GUIDE: [Brand]
Date: [Date] | Status: [proposal / approved] | Positioning: [one line]

--- STRATEGIC FOUNDATION ---
Promise: [..] | Personality: [adj (is / is not) ×3–4] | Values: [value → behaviour]

--- VISUAL IDENTITY ---
Logo: [type, variants, clear space, files]
Colour: Primary [hex] | Secondary [hex…] | Accent [hex] | Neutrals [hex…] | Semantic [hex…]
  Accessibility: [pairings checked, WCAG 2.2 AA pass/fail]
Typography: [family, weights, scale with ratio, fallbacks, licence]
Imagery: [photo, illustration, people, screenshots, AI policy, alt text]
Layout & motion: [grid, spacing, radius, elevation, max width, motion, dark mode]

--- BRAND VOICE ---
Attributes: [attribute — means — is not] ×3–4
Tone matrix: [context → tone → example] ×6+
Vocabulary: Use [..] / Avoid [..] (10+ pairs) | Conventions: [case, numerals, dates, currency]
Sentence style: [rules]

--- COPY STANDARDS ---
[Channel → length → pattern → goal] for the channels the brand uses
CTA rules: [..]

--- NAMING ---
[Products, features, campaigns, files, tokens]

--- TOUCHPOINT AUDIT ---
[Touchpoint → pass/fail → fix] ×5+

--- AI USAGE ---
Brand prompt pack: [voice, vocabulary, examples, visual prompts, review and disclosure rules]

--- ASSET CHECKLIST ---
[ ] Logo variants (SVG/PNG, dark/light)  [ ] Colour tokens  [ ] Font files/licences
[ ] Image references (3–5)  [ ] Social templates with safe zones  [ ] Email template
[ ] Deck template  [ ] Writing guide  [ ] Brand prompt pack  [ ] Guide distributed

--- OPEN ITEMS ---
[Trademark/domain checks, approvals, missing assets]
```

## Common Pitfalls

1. **Starting with the logo.** Strategy and voice first; the logo expresses them.

2. **Too many colours.** One hero colour; everything else supports it.

3. **Vague voice words.** "Friendly, professional" describe every brand. Define the *how* and the *is not*.

4. **Tone drift between channels.** Tone adapts, voice does not; a brand that is playful on Instagram and stiff on LinkedIn reads as two brands.

5. **Unchecked accessibility.** Pretty pairings that fail 4.5:1 exclude readers and fail audits. Check every pairing.

6. **Fonts nobody can use.** Confirm licences for web, app and desktop before specifying; open-source fonts avoid surprises.

7. **A 60-page guide nobody opens.** Lead with examples; keep the rules scannable; publish tokens and templates, not just PDFs.

8. **No rules for AI tools.** Without a prompt pack and a review step, AI output drifts off-brand fastest of all.

## Verification Checklist

- [ ] Strategic foundation stated (promise, personality with is/is-not, values, positioning line)
- [ ] Colour palette with exact hex for primary, secondary, accent, neutrals and semantic colours
- [ ] Text/background pairings checked against WCAG 2.2 AA with pass/fail noted
- [ ] Typography specified with weights, scale, fallbacks and licence status
- [ ] Imagery rules cover photography, illustration, people, screenshots, AI-generated media and alt text
- [ ] Layout, spacing, radius, motion and dark-mode rules defined
- [ ] 3–4 voice attributes each with "means" and "is not"
- [ ] Tone matrix covers at least 6 contexts with examples
- [ ] Vocabulary list has 10+ use/avoid pairs plus writing conventions
- [ ] Copy standards and CTA rules given for the channels the brand uses
- [ ] Naming conventions for products, features, campaigns, files and tokens
- [ ] Touchpoint audit of 5+ touchpoints with pass/fail and fixes
- [ ] Brand prompt pack for AI tools included
- [ ] Existing brand values not invented; proposals labelled as proposals; open items listed
