---
name: pinterest-organic
description: Use when developing Pinterest organic strategy — profile audit, keyword-driven board structure, pin design and formats, fresh-pin cadence, Rich Pins and claimed-website setup, seasonal planning with Pinterest Trends, and growth measured in outbound clicks. Also use when someone asks "is Pinterest worth it for my business", wants a Pinterest content calendar, or needs pin titles and descriptions written for search. Don't use for Pinterest Ads, product catalog/shopping feeds, or Instagram-style engagement tactics.
version: 1.2.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. Browsing is optional; when a profile cannot be fetched, the skill works from screenshots and Pinterest Analytics exports the user provides.
metadata:
  category: organic-social
  updated: 2026-11-17
  tags: [pinterest, organic, visual-search, pin-strategy, boards, keywords, fresh-pins, content-calendar, traffic]
  related_skills: [instagram-organic, youtube-organic, linkedin-organic, competitor-research, geo-ai-seo, branding]
---

# Pinterest Organic Strategy

## Overview

Pinterest is a visual search and planning engine, not a social feed: pins are indexed by their text and image, surface for months, and are judged on saves and outbound clicks rather than likes. This skill audits a business profile, rebuilds boards around search keywords, sets a sustainable fresh-pin cadence, defines pin design and copy that rank, and plans content around Pinterest's seasonal demand curve. The success metric is traffic and conversions, not followers.

## When to Use

- Auditing a Pinterest business profile and boards
- Deciding whether Pinterest fits a niche and goal
- Planning boards, pin designs and a fresh-pin calendar
- Writing keyword-rich pin titles, descriptions and board descriptions
- Growing outbound clicks to a website, shop or lead magnet

Don't use for: Pinterest Ads (Promoted Pins, Ads Manager), product catalog ingestion and shopping feeds, or engagement-driven social tactics that assume a chronological audience.

## Inputs

Ask for (or extract from the conversation):

- **Profile URL** and whether it is a claimed business account
- **Goal**: traffic, email sign-ups, sales, brand awareness — and the destination URLs
- **Pinterest Analytics** (last 30–90 days): impressions, engagements, saves, outbound clicks, top pins, top boards, audience interests
- **Content inventory**: blog posts, products, guides, videos that pins can point to
- **Current boards and pin cadence**, or screenshots of the profile
- **Design capacity**: templates, brand kit, who produces pins
- **Seasonality** of the business

Data rules: if the profile cannot be fetched, say so and work from screenshots; do not estimate impressions or clicks. Keyword suggestions come from Pinterest's own search bar, Pinterest Trends and the user's analytics — if none are available, label suggested keywords as hypotheses to validate. Pinterest renames features (Idea Pins were folded into standard video/multi-image pins in 2023; scheduling is native); if the UI differs, follow the UI and note it.

## Audit Workflow

### Step 1: Profile and analytics

| Metric | Where | Why |
|--------|-------|-----|
| Followers | Header | Weak proxy; low weight |
| Monthly views | Header (public) | Vanity; use Analytics instead |
| Boards, pins per board | Boards tab | Coverage and depth (< 20 pins looks thin) |
| Impressions, saves, outbound clicks | Analytics → Overview | The metrics that matter, in that order of leading indicator |
| Top pins / top boards | Analytics | What ranks already |
| Audience interests and demographics | Analytics → Audience insights | Keyword and topic direction |
| Claimed website, Rich Pins | Settings | Attribution and richer pin data |
| Pin formats used | Recent pins | Static, video, multi-image (carousel), collages |
| Cadence | Recent activity | Consistency |

### Step 2: Content audit

| Check | Good | Problem |
|-------|------|---------|
| Aspect ratio | 2:3 vertical, 1000×1500 px | Horizontal or square gets cropped and buried |
| Pin title | ≤ 100 characters, keyword in the first 40 | Vague or missing |
| Pin description | 2–3 sentences, natural keywords, benefit, call to action; ≤ 500 characters, first ~50–60 visible | Empty or keyword-stuffed |
| Destination link | Every pin links to a relevant page | Dead links or homepage only |
| Text overlay | 3–6 words, large, high contrast | Tiny or absent text; readable only on desktop |
| Board titles and descriptions | Search phrases ("Small Bathroom Ideas") | Cute names ("Pretty things") |
| Freshness | Mostly new images and new URLs | Mostly re-saves of old pins |
| Cadence | Daily, steady | Bursts then silence |

### Step 3: Niche fit and keywords

Pinterest skews toward planning intent: home, food, fashion, beauty, wellness, parenting, weddings, travel, personal finance, DIY, crafts, business and marketing education, and increasingly men's interests and Gen Z. If the audience plans or shops for the category, Pinterest can be a top traffic source; if the product is impulse or B2B enterprise, expectations should be modest.

Keyword research sources: the Pinterest search bar (autocomplete and guided-search chips), Pinterest Trends (seasonality and related terms), top-performing pins of competitors, and the user's Analytics. Build a list of 15–30 keywords grouped by board.

Make the niche-fit call explicit — it decides how much effort the rest of the plan deserves:

| Verdict | When | What to recommend |
|---------|------|-------------------|
| **Go** | Audience plans, saves or shops for the category; the business has 20+ linkable pages (posts, products, guides) | Full plan: keyword boards, daily fresh pins, seasonal calendar |
| **Test** | Partial fit (B2B to small businesses, niche services, local with a planning angle) or fewer than 20 linkable pages | Bounded 90-day test: 3–5 boards, a fixed number of fresh pins per week, a pre-agreed decision rule (e.g. "continue if Pinterest outbound clicks reach [n] or [n] sign-ups by day 90", with the user setting [n] from their own channel economics) |
| **Deprioritize** | Impulse or enterprise purchase with no visual planning behaviour, no content to link to, or no capacity to make fresh pins | Say so plainly; at most claim the site and publish a few evergreen pins; point the effort to a better-fit channel |

### Step 4: Diagnose the analytics funnel

Pinterest's funnel is impressions → saves/engagements → outbound clicks → conversions. Find the first stage that breaks and fix that before anything downstream. Compute ratios from the user's export (save rate = saves ÷ impressions, outbound click rate = outbound clicks ÷ impressions) and compare them with the account's own top pins and its trailing 90 days — there is no universal benchmark worth quoting, so do not invent one.

| Symptom (from the user's data) | Likely cause | First fix |
|--------------------------------|--------------|-----------|
| Low impressions overall, or impressions concentrated on a few old pins | Weak keywords, vague board names, low fresh-pin volume, site not claimed | Keyword titles/descriptions, rename or merge boards, steady fresh pins |
| Impressions fine, save rate well below the account's own top pins | Creative: unclear overlay, wrong ratio, image does not signal the topic | New designs for the same URL; test overlay wording and image angle |
| Saves fine, outbound clicks low | Pin answers the need in-image (nothing left to click for), weak call to action, pin-to-page mismatch | Overlay that promises more than the pin shows ("Full recipe + printable"), CTA in description, link to the exact matching page |
| Outbound clicks fine, few conversions | Landing page or offer, not Pinterest | Hand over to landing page work; add a Pinterest-specific lead magnet; check UTM tagging |
| All metrics falling together | Seasonality, posting gap, or a broken claimed domain / Rich Pins | Compare with the same period last year and Trends; check settings before changing strategy |

Rule: judge a pin after 30+ days and a board after 90; earlier numbers mostly reflect the distribution ramp, not quality.

## Strategy Formulation

### Board structure

Boards are how Pinterest understands what an account is about. One board = one search topic.

| Rule | Detail |
|------|--------|
| Count | 8–15 active boards covering the keyword clusters; archive off-topic boards |
| Titles | Keyword phrases people search |
| Descriptions | 1–2 sentences with related keywords |
| Sections | 2–4 per board for sub-topics when a board exceeds ~50 pins |
| Order | Most important boards first; set a strong cover |
| Secret boards | For staging and testing before making public |

### Pin formats

| Format | Use |
|--------|-----|
| Static pin (2:3) | Core evergreen content; most of the volume |
| Video pin (6–15 s, vertical) | Process, before/after, quick demo; strong in home feed |
| Multi-image / carousel pin | Step-by-step, multi-angle product; high engagement, lower click-out per image |
| Infographic / long pin (up to 1:2.1) | Checklists and data people save |
| Product pins (from claimed site/catalog) | Live price and availability |
| Collages | Trend-led, younger audience; link to products |

Design rules: brand colours and fonts for recognition, a face or hands when the category allows, subtle logo or URL at the bottom, text that survives the mobile crop, and 3–5 distinct designs per destination URL over time.

### Cadence (quality over volume)

Pinterest now rewards fresh, original pins and penalises spammy volume. Starting points:

| Account | Fresh pins per day |
|---------|-------------------|
| New (< 500 followers or < 10K impressions) | 1–3, every day |
| Established | 3–5 |
| Content-rich publishers | 5–10 at most, only if each pin is a new image or URL |

Fresh = a new image, even for an existing URL. Re-saving your own pins to other boards is acceptable in small doses; mass re-pinning of others' content no longer drives reach. Schedule with Pinterest's native scheduler (up to 30 days ahead) or a tool like Tailwind so posting is steady.

Timing: evenings and weekends in the audience's time zone are typical peaks, but pins live for months, so consistency matters more than the hour.

### Seasonal planning

Pinners plan 45–90 days ahead. Use Pinterest Trends and the Pinterest Predicts annual report to schedule seasonal pins 2–3 months before the event (holidays, back to school, weddings, summer). Evergreen content fills the rest of the calendar.

### Growth tactics

| Tactic | Effort | Impact | Why |
|--------|--------|--------|-----|
| Keyword-first titles, descriptions, boards | Low | Very high | Pinterest ranks text plus image understanding |
| Daily fresh pins | Medium | Very high | Fresh content is prioritised |
| Multiple designs per URL | Medium | High | Each design is a new chance to rank; test overlays and angles |
| Claimed website + Rich Pins | Low | High | Attribution, richer metadata, trust |
| Video and multi-image pins | Medium | High | Extra distribution in home feed |
| Seasonal pins 60–90 days early | Low | High | Matches planning behaviour |
| Alt text and image SEO | Low | Medium | Accessibility and visual search signals |
| Cross-link from site and newsletter | Low | Medium | Seeds early saves |
| Group boards | Low | Low–medium | Diminished since the fresh-pin shift; only niche, active ones |

### Growth stages

| Stage | Focus |
|-------|-------|
| < 10K monthly impressions | Claim site, Rich Pins, 8–10 keyword boards, 1–3 fresh pins daily, templates |
| 10K–100K | 3–5 fresh pins daily, video pins, seasonal calendar, 3+ designs per top URL |
| 100K–1M | Batch design monthly, analytics-driven pruning of weak boards, lead magnets per board |
| > 1M | Team or outsourcing, catalog/product pins, consider ads on proven organic winners |

### Board consolidation and pin pruning

| Situation | Action | Why |
|-----------|--------|-----|
| Two or more boards target the same keyword | Merge into the stronger board (move pins), then archive the empty one | Splitting a topic splits relevance signals |
| Board with a cute or vague name but on-topic pins | Rename to the keyword phrase and rewrite the description; do not recreate | Keeps the pins and their history |
| Off-topic board (personal, old niche) | Archive, or make secret | Dilutes what the account is about; deleting loses pins permanently |
| Pin with impressions but almost no outbound clicks after 30+ days | Leave it live; make a new design for the same URL with a stronger click reason | Saves still feed distribution; the fix is a fresh pin, not deletion |
| URL whose pins all underperform after 90 days | Check the keyword and the page; try 2 new designs before dropping the URL | Usually a topic or design problem, not a channel problem |
| Pin or URL clearly winning | Make 3+ new designs and add it to the seasonal calendar | Scale what already ranks |

## Profile Optimization Checklist

- [ ] Business account, website claimed, Rich Pins validated
- [ ] Profile name includes the main keyword ("Brand | Topic")
- [ ] Bio: value proposition + keywords + call to action (≤ 160 characters)
- [ ] Profile photo recognisable (logo or face)
- [ ] Board covers set; boards ordered by priority; off-topic boards archived
- [ ] Featured boards selected for the profile header
- [ ] Analytics connected and reviewed monthly

## Output Format

Use every heading below in this order. Write "not provided" rather than estimating a missing number; label every hypothesis-level keyword with `(hypothesis)`.

```
PINTEREST AUDIT: [Profile] (URL)
Goal: [traffic / leads / sales] | Access: [fetched / screenshots / analytics export / description only]
Followers: X | Boards: Y | Pins: Z | Monthly impressions: A | Saves: B | Outbound clicks: C
NICHE FIT: [Go / Test / Deprioritize] — [one-sentence reason]

--- FUNNEL DIAGNOSIS ---
Save rate: [saves ÷ impressions = x% or "not provided"] | Outbound click rate: [x% or "not provided"]
Breaking stage: [impressions / saves / outbound clicks / conversions] — [evidence]
First fix: [one action]

--- CURRENT STATE ---
Pin mix: Static X% / Video Y% / Multi-image Z%
Cadence: X fresh pins/day | Fresh vs re-save: ..
Board quality: [keyword-optimised? coverage? thin boards?]
Setup: [claimed site / Rich Pins / business account]
Top performers: [up to 3 pins — why]

--- STRENGTHS ---
- [...]

--- GAPS ---
- [...]

--- KEYWORD LIST (15–30, grouped by board; source noted) ---
[Board A]: kw, kw, kw — Source: [Pinterest search / Trends / Analytics / hypothesis]
[Board B]: kw, kw, kw — Source: [...]

--- BOARD STRUCTURE (8–15) ---
BOARD: [Keyword title] | Action: [keep / rename from "..." / merge "..." into this / new]
  Description: [1–2 sentences]
  Sections: [..]
Archive: [boards to archive or make secret]

--- PIN STRATEGY ---
Formats: [mix] | Designs per URL: [n]
Design direction: [2:3, 1000×1500 px, overlay style, colours, fonts, branding]
PIN 1: Title ([n] chars): [..] | Description ([n] chars): [..] | Overlay: [3–6 words] | Link: [URL]
[Repeat PIN n for each pin written]

--- CADENCE & SEASONAL CALENDAR ---
Fresh pins/day: X | Scheduler: [native / tool]
Seasonal pushes: [event → start pinning on date (60–90 days ahead)]

--- GROWTH PLAN ---
0–30 days: [3 actions]
30–90 days: [3 actions]
90+ days: [3 actions]
KPIs: Primary — outbound clicks; Secondary — saves, impressions on priority boards, conversions from Pinterest traffic (UTM-tagged)
Decision rule: [what result by which date means continue, change or stop]

--- PROFILE OPTIMIZATION ---
Name: [..] | Bio: [..] | Claimed site / Rich Pins: [..] | Featured boards: [..]

--- ASSUMPTIONS & MISSING DATA ---
[...]
```

For a narrow request (pin copy only, or a yes/no on fit), output only the relevant blocks — header line, `NICHE FIT`, `PIN STRATEGY` or `BOARD STRUCTURE` — plus `ASSUMPTIONS & MISSING DATA`.

## Common Pitfalls

1. **Horizontal or square images.** They are cropped and under-served. Fix: 2:3 vertical (1000×1500 px) as the default; long pins only for checklists and infographics.

2. **No keywords.** Titles, descriptions and board names are how Pinterest indexes content; "Inspo" ranks for nothing. Fix: keyword phrase first in titles and as the board name, natural related terms in descriptions.

3. **Keyword stuffing and hashtag lists.** Comma-separated keyword dumps read as spam and hashtags carry little weight. Fix: 2–3 natural sentences that a person would want to read.

4. **Volume spam.** Twenty re-pins a day used to work; now it is flagged. Fix: fewer, fresh, original pins at the stage-appropriate cadence.

5. **Treating Pinterest like Instagram.** Engagement loops, posting-time chasing and follower counts do not drive distribution. Fix: plan around search intent and shelf life.

6. **Pinning without a destination, or to the homepage.** A pin that lands on a generic page loses the click. Fix: link every pin to the exact page it promises, tagged with UTM parameters.

7. **Judging results after a week.** Pins ramp over weeks and months. Fix: judge pins at 30+ days, boards at 90, and prune quarterly.

8. **Deleting boards to "clean up".** Deleting a board deletes its pins and their history. Fix: rename, merge or archive instead.

9. **Diagnosing the wrong stage.** Redesigning pins when the real problem is a landing page that does not convert wastes effort. Fix: run the funnel diagnosis and fix the first breaking stage only.

10. **Ignoring seasonality.** Posting Christmas content in December is too late; pinners planned in October. Fix: seasonal pins 60–90 days ahead, checked against Pinterest Trends.

11. **Promising traffic numbers.** Forecasting impressions or clicks without data sets expectations the channel may not meet. Fix: state a decision rule with targets the user sets from their own data.

## Verification Checklist

- [ ] Profile and analytics reviewed from fetched data or screenshots; no invented or forecast metrics
- [ ] Niche fit given as Go / Test / Deprioritize with a reason; Test includes a 90-day decision rule
- [ ] Funnel diagnosis names the first breaking stage, using ratios from the user's own data (or "not provided")
- [ ] Keyword list of 15–30 terms grouped by board, with the source named and hypotheses labelled
- [ ] Board structure of 8–15 keyword boards with an action per board (keep / rename / merge / new); nothing deleted that could be archived
- [ ] Pin specs: 2:3 ratio, title ≤ 100 chars with keyword first, description ≤ 500 chars with CTA, character counts shown
- [ ] Fresh-pin cadence set by account stage (1–3 / 3–5 / ≤ 10 per day), not volume spam
- [ ] Claimed website, Rich Pins and UTM tagging addressed
- [ ] Seasonal calendar planned 60–90 days ahead using Pinterest Trends
- [ ] Growth plan split 0–30 / 30–90 / 90+ days with outbound clicks as the primary KPI
- [ ] Profile optimisation checklist applied
