---
name: branding
description: Use when defining or refreshing brand identity — visual identity, brand voice, tone guidelines, copy standards, naming, and the cohesive system that makes every output recognizable as "yours" before people read the logo.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [branding, brand-identity, visual-identity, brand-voice, tone-of-voice, brand-guidelines, copywriting, naming, design-system]
    related_skills: [market-positioning, competitor-research, landing-page-funnel, instagram-organic, linkedin-organic, youtube-organic]
---

# Branding

## Overview

Build a cohesive brand identity system — visual, verbal, and experiential — that makes every piece of content instantly recognizable as yours. Covers visual identity, brand voice, tone calibration, copy standards, naming conventions, and the practical guidelines that keep output consistent across channels and creators.

A brand is not a logo. It's the pattern of associations the audience builds after every touchpoint. This skill ensures that pattern is intentional, consistent, and distinctive.

## When to Use

- Creating a new brand identity from scratch (startup, new product, new market entry)
- Refreshing an existing brand that feels stale or inconsistent
- Standardizing output across multiple channels, team members, or agencies
- Preparing brand guidelines for a team, freelancer, or AI-generated content workflows
- Defining brand voice before launching a content strategy or campaign
- Naming a new product, feature, or sub-brand
- Ensuring AI-generated content matches human brand standards

Input is typically:
- **Brand name** (or naming direction if still in development)
- **Target audience** (who this brand is for)
- **Positioning** (from `market-positioning`; if not done, this skill includes positioning validation)
- **Existing brand assets** (logo, colors, voice notes — or absence thereof)

Don't use for: tactical copywriting for a single ad (too narrow), market research for positioning (use `market-positioning`), or competitor analysis (use `competitor-research`).

## Brand System Architecture

A complete brand system has four pillars. Address all of them — not just the visual.

| Pillar | Components | Output |
|--------|-----------|--------|
| **Visual** | Logo, color palette, typography, imagery style, iconography, layout principles | Visual identity guide |
| **Verbal** | Brand voice, tone matrix, vocabulary, naming conventions, tagline | Voice & tone guide |
| **Strategic** | Positioning, brand promise, key messages, brand values | Brand strategy document |
| **Experiential** | Touchpoint standards, content templates, interaction patterns | Touchpoint playbook |

## 1. Visual Identity

### 1.1 Logo

| Decision | Guidance |
|----------|---------|
| **Type** | Wordmark (text-only), lettermark (initials), pictorial (icon + text), abstract (symbol), combination mark. Choose based on memorability and scalability. |
| **Scalability** | Must be recognizable at 16px (favicon), 64px (social avatar), 500px (website header), and 2000px (billboard). |
| **Variants** | Create: primary (full), secondary (text-only for horizontal), tertiary (icon/lettermark for square). |
| **Clear space** | Minimum padding = height of the tallest letter in the logo. Never shrink, stretch, or recolor outside approved variants. |
| **Background** | Define acceptable and unacceptable backgrounds. Dark variant needed for light backgrounds and vice versa. |

### 1.2 Color Palette

| Role | Count | Purpose |
|------|-------|---------|
| **Primary color** | 1 | Brand anchor — used in logo, primary CTAs, key visual elements. Drives instant recognition. |
| **Secondary colors** | 2-3 | Supporting palette — used for hierarchy, cards, backgrounds, secondary actions. |
| **Accent colors** | 1-2 | Highlights, notifications, interactive states. Should create contrast, not compete. |
| **Neutrals** | 3-5 | Text, backgrounds, borders, dividers. Specify exact hex for dark text, body text, light text, surface, and border. |

**Color rules:**
- Specify exact hex codes — no "close enough" colors
- Always include both accessible (WCAG AA) and non-accessible combinations with guidance
- Define the single most important color → this is the one the audience should associate with your brand
- Test colors in grayscale to confirm they produce enough contrast hierarchy without relying on hue

### 1.3 Typography

| Element | Specification |
|---------|-------------|
| **Primary font** | 1 typeface for headings and body. Prefer free/available fonts (Google Fonts) for practicality. |
| **Secondary font** | Optional — use only if primary is weak for a specific use (e.g., monospace for code). |
| **Scale** | Define a type scale: h1, h2, h3, body, caption, button. Use a ratio (1.25, 1.333, or 1.618). |
| **Weights** | Specify which weights to use (e.g., Regular 400 for body, Bold 700 for headings). Limit to 2-4 weights. |
| **Line height** | Body text: 1.5-1.75. Headings: 1.1-1.25. |
| **Fallback** | Always specify a system font fallback. |

**Typography decision framework:**

| Brand Personality | Font Style | Examples |
|------------------|-----------|----------|
| Modern, clean | Geometric sans-serif | Inter, Montserrat, Poppins |
| Trustworthy, professional | Humanist sans-serif | Source Sans 3, Lato, Open Sans |
| Creative, playful | Rounded or display | Quicksand, Comfortaa, Fredoka |
| Premium, sophisticated | Serif | Playfair Display, Lora, IBM Plex Serif |
| Technical, precision | Monospace | JetBrains Mono, Fira Code, IBM Plex Mono |

### 1.4 Imagery Style

Define what images, photos, illustrations, and graphics look like:

| Element | Decision |
|---------|---------|
| **Photo style** | Lifestyle (real people, natural light), product-focused (clean backgrounds), abstract (shapes, textures), or mixed |
| **Illustration style** | Flat, line art, 3D, hand-drawn, geometric, or no illustrations |
| **Color filter / treatment** | Do all photos get the same color grading? Consistent treatment = consistency. |
| **Image composition** | Rule of thirds? Centered? Negative space for text overlays? |
| **People** | Diversity guidelines, candid vs. posed, real users vs. stock photography |
| **Screenshots** | Device mockups, browser frames, floating cards? Define the style. |

**Rule:** Every image should feel like it belongs on the same page as every other image. If you can't instantly recognize a brand from a single image, the imagery style isn't distinctive enough.

### 1.5 Layout & Spacing

| Element | Guideline |
|---------|-----------|
| **Grid** | Define a base grid (e.g., 12-column for web, 4-column for mobile). |
| **Spacing scale** | Use a consistent spacing scale: 4, 8, 16, 24, 32, 48, 64px. Every margin and padding should be a multiple of 4 or 8. |
| **Border radius** | 0px (sharp), 4px (subtle), 8px (rounded), 16px+ (pill). Pick one and stay consistent. |
| **Shadows** | If used, define 2-3 levels for hierarchy. If not, don't. |
| **Max-width** | Content max-width for readability (680px for reading, 1200px for layout). |

## 2. Brand Voice

### 2.1 Voice Definition

Brand voice is how your brand *permanently* communicates — it doesn't change by channel, campaign, or post. Define it with 3-4 voice attributes:

| Attribute | What it means | What it isn't |
|-----------|-------------|---------------|
| *Example: Conversational* | Write like you talk to a colleague — direct, natural, no jargon | Casual slang, unprofessional, dismissive |
| *Example: Expert* | Lead with knowledge and confidence without being a know-it-all | Academic, condescending, dense |
| *Example: Optimistic* | Frame problems as solvable; lead with what's possible | Naive, unrealistic, ignoring real challenges |
| *Example: Direct* | Say what you mean in fewer words; skip the preamble | Blunt, rude, missing nuance |

**Each attribute needs a "what it means" and a "what it isn't."** This prevents drift — every writer knows the boundary.

### 2.2 Tone by Context

Tone is how voice flexes based on context. Voice is constant; tone adapts.

| Context | Tone | Example shift |
|---------|------|---------------|
| **Announcement / product launch** | Energetic, confident | Upbeat headlines, action-oriented copy |
| **Error / failure message** | Helpful, calm | "Something went wrong — here's how to fix it" |
| **Educational / tutorial** | Encouraging, clear | "Let's walk through this step by step" |
| **Sales / conversion page** | Persuasive, direct | Benefit-first language, clear next step |
| **Customer support response** | Empathetic, solution-focused | "I'm sorry you hit that — let me help" |
| **Social media comment** | Conversational, engaging | Short, warm, reactive |
| **Crisis communication** | Transparent, accountable | "Here's what happened, what we're doing, what to expect" |

### 2.3 Vocabulary

Create a do/don't word list. This is what makes your writing unmistakably yours.

| Use | Don't use | Reason |
|-----|---------|--------|
| *Example: "Free trial"* | *"14-day pass"* | Consistent offer language across all channels |
| *Example: "Get started"* | *"Begin your journey"* | Avoids corporate cliché |
| *Example: "We"* | *"The company"* | Reinforces conversational voice |

**Minimum:** 10 pairs. **Recommended:** 25+ for teams producing regular content.

### 2.4 Sentence Style

| Rule | Guideline |
|------|-----------|
| **Sentence length** | Average 15-20 words for web. Vary for rhythm — follow a short sentence with a longer one. |
| **Active voice** | "We built this for you" not "This was built for you." Always prefer active. |
| **Paragraph length** | 1-3 sentences for web. No wall of text. |
| **Headlines** | Start with the benefit or the action, not the product name. |
| **Avoid** | Corporate filler words: leverage, synergy, ecosystem, robust, cutting-edge, best-in-class. |
| **Use** | Concrete nouns, specific numbers, real examples. |

## 3. Copy Standards

### 3.1 Copy by Channel

| Channel | Length | Style | Primary goal |
|---------|--------|-------|-------------|
| **Homepage headline** | 6-10 words | Clear, benefit-driven | Communicate position in 3 seconds |
| **Ad headline** | 6-12 words | Attention-grabbing, relevant | Stop the scroll / capture attention |
| **Ad body copy** | 15-40 words | Benefit → proof → CTA | Drive click |
| **Landing page body** | 200-500 words | Persuasive, scannable | Convert the click into action |
| **Social post** | 1-2 sentences (Twitter/X), 3-5 (LinkedIn/Instagram) | Conversational, value-forward | Drive engagement |
| **Email subject line** | 3-7 words | Curiosity or benefit | 40%+ open rate |
| **Email body** | 100-300 words | Personal, focused | Drive the single CTA |
| **Blog intro** | 50-100 words | Hook → promise | Keep reader past the first 3 lines |
| **Product descriptions** | 50-150 words | Feature → benefit, scannable | Support purchase decision |

### 3.2 CTA Guidelines

| Rule | Detail |
|------|-------|
| **One CTA per page** | If there are two, prioritize. Secondary CTAs can be de-emphasized. |
| **Action verb first** | "Get," "Start," "Book," "See" — not "Click here" or "Submit." |
| **Specific, not generic** | "Get your free report" > "Download now" > "Click here." |
| **Color** | Primary CTA uses the accent/action color. Secondary CTA uses outline or text link. |
| **Size** | Large enough to be a clear focal point (min width 200px on desktop, full width on mobile). |

### 3.3 Naming Conventions

| Asset | Convention |
|-----|---------|
| **Product names** | Memorable, pronounceable, available (URL + social handle). Check 3 domains minimum. |
| **Feature names** | Benefit-oriented if possible ("Smart Search") or functional ("Filter by date"). |
| **Campaign names** | Internal: `[YYYY]-[channel]-[campaign-name]`. External: emotional or benefit-aligned. |
| **File naming** | `brand-name_channel_component_date.ext` (e.g., `acme_instagram_story_v1_2026-07-24.png`) |

## 4. Touchpoint Consistency

Every time the audience encounters the brand, it should feel like an extension of the same entity. Audit and standardize:

| Touchpoint | What to check | Standard |
|------------|-------------|---------|
| **Website** | Colors, fonts, imagery, headline voice match brand guide | Pass/fail per section |
| **Social profiles** | Bio, avatar, cover image, pinned post follow brand | Bio uses brand voice keywords |
| **Email signatures** | Name, title, color, CTA link, signature line | Matches brand promise |
| **Presentation decks** | Template uses brand colors, fonts, imagery style | Master template available |
| **Docs / help center** | Same voice and formatting conventions | Style guide for writers |
| **Ad creative** | Colors, fonts, copy, imagery all consistent | Ad library audit |
| **Packaging** (if physical) | Colors, typography, logo placement, unboxing experience | Brand guide extended to physical |

## Output Format

```
BRAND IDENTITY GUIDE: [Brand Name]
Date: [Date]

--- VISUAL IDENTITY ---
PRIMARY COLOR: [Hex + name]
SECONDARY COLORS: [Hex list]
ACCENT: [Hex + usage]
NEUTRALS: [Dark text, body, light, surface, border]

TYPEFACE:
  Primary: [Font name] — weights: [400, 700, etc.]
  Scale: [h1: Xpx, h2: Xpx, h3: Xpx, body: Xpx, caption: Xpx] @ ratio [X]
  Fallback: [System font]

IMAGERY:
  Style: [Photo style, illustration style, treatment]
  Composition: [Rule]
  People: [Guideline]

LAYOUT:
  Grid: [X-col]
  Spacing: [4/8px scale]
  Border radius: [Xpx]
  Shadows: [If used]
  Max-width: [Xpx]

--- BRAND VOICE ---
ATTRIBUTES:
  [Attribute 1]: [What it means] (Not: [What it isn't])
  [Attribute 2]: [What it means] (Not: [What it isn't])
  [Attribute 3]: [What it means] (Not: [What it isn't])

TONE BY CONTEXT:
  [Context 1] → [Tone] — [Example]
  [Context 2] → [Tone] — [Example]

VOCABULARY:
  Use: [Words/phrases]
  Avoid: [Words/phrases]

--- COPY STANDARDS ---
[Channel-specific copy guidelines]

--- TOUCHPOINT AUDIT ---
[Current state: what matches, what doesn't, what to fix]

--- BRAND ASSETS CHECKLIST ---
[ ] Logo variants (primary, text-only, icon)
[ ] Color palette document
[ ] Font files / licensing
[ ] Image style examples (3-5 approved references)
[ ] Social media templates (LinkedIn, Instagram, Twitter)
[ ] Email template
[ ] Presentation template
[ ] File naming convention documented
[ ] Brand guide distributed to all creators
```

## Common Pitfalls

1. **Starting with a logo.** Logo is a symbol — voice, message, and experience create the actual brand. Build the verbal and strategic foundation first, then the visual.

2. **Too many colors.** 5+ accent colors doesn't make a brand "vibrant" — it makes it noisy. Pick one hero color and let everything else support it.

3. **Voice description that's too vague.** "Friendly" and "professional" are not voice attributes — they're expectations. Everyone should be friendly and professional. Your voice is *how* you're friendly and professional differently.

4. **Inconsistent tone across channels.** A brand that's playful on Instagram and corporate on LinkedIn confuses the audience. Tone can *adapt* to context, but the voice attributes stay constant.

5. **Font choice without practicality check.** Beautiful fonts are useless if they cost $500/year or only work on the designer's Mac. Always specify Google Fonts or system fallback.

6. **Writing a brand guide that nobody reads.** Make it scannable. Use examples more than rules. If your brand guide is 50 pages, it's not being used.

7. **Ignoring accessibility.** Brand colors must meet WCAG AA contrast. Fonts must be readable at small sizes. Alt text is part of brand voice, not an afterthought.

8. **Forgetting internal consistency.** If your team uses different vocabulary, different tone, or different formats in email vs. Slack vs. reports, the brand is already inconsistent internally. Fix that before worrying about external.

## Verification Checklist

- [ ] Visual identity defined: 1 primary color, 2-3 secondary, 1-2 accent, 3-5 neutrals with exact hex
- [ ] Primary typography specified with weights, scale, and fallback
- [ ] Imagery style documented: photo style, illustration style, composition, people guidelines
- [ ] Layout standards defined: grid, spacing scale, border radius, max-width
- [ ] 3-4 voice attributes defined with "what it is" and "what it isn't" for each
- [ ] Tone matrix covers at least 5 contexts with examples
- [ ] Vocabulary list has 10+ use/avoid pairs
- [ ] Copy standards defined for at least 5 channels
- [ ] CTA guidelines: single CTA, action verb, specific language
- [ ] Naming conventions documented for products, campaigns, and files
- [ ] Touchpoint audit completed for at least 5 channels with pass/fail status
- [ ] Brand assets checklist complete (logo variants, templates, guide distributed)
- [ ] WCAG AA contrast verified for primary color combinations
- [ ] Font availability confirmed (free/commercial license checked)
