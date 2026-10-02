---
name: instagram-organic
description: Use when developing Instagram organic strategy — auditing a profile, defining content pillars, choosing a Reels/carousel/story mix, setting a posting cadence, and planning follower and reach growth around Instagram's current ranking signals (watch time, likes, sends). Also use when someone asks "why did my reach drop", wants an Instagram content calendar, or asks how to grow an account from scratch. Don't use for Instagram paid ads (meta-ads-creative, meta-ads-diagnostics), influencer contracting, or Instagram Shop setup.
version: 1.1.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. Browsing is optional; when a profile cannot be fetched, the skill works from screenshots and Insights exports the user provides.
metadata:
  category: organic-social
  updated: 2026-10-02
  tags: [instagram, organic, social-media, content-strategy, reels, carousels, growth, engagement]
  related_skills: [tiktok-ads, linkedin-organic, youtube-organic, pinterest-organic, competitor-research, branding]
---

# Instagram Organic Strategy

## Overview

Build a data-informed organic plan for an Instagram account: audit the profile and recent posts, read the engagement pattern, define content pillars, choose a format mix and cadence the team can sustain, and set growth tactics for the account's current stage. Instagram ranks each format separately and, for reach beyond followers, weights **watch time, likes and sends (shares to DMs)** most heavily; the plan is built around those signals.

## When to Use

- Auditing an Instagram profile and its last 20–30 posts
- Planning a content calendar or relaunching a stalled account
- Deciding the Reels / carousel / single image / Stories mix
- Diagnosing a reach or follower drop
- Setting growth targets and tactics by follower stage

Don't use for: paid Instagram ads (use `meta-ads-creative` / `meta-ads-diagnostics`), influencer sourcing and contracts, Instagram Shop and catalog setup, or crisis/community management policies.

## Inputs

Ask for (or extract from the conversation):

- **Profile URL or handle** and whether it is a personal brand, business or creator account
- **Goal**: followers, reach, leads, sales, community — and the timeframe
- **Insights export or screenshots** (last 30–90 days): reach by content type, followers vs non-followers reach, watch time/plays for Reels, saves, shares, profile visits, follows, audience active times
- **Last 20–30 posts**: format, topic, date, likes, comments, shares, saves
- **Team capacity**: who creates, how many hours per week, can they film
- **Brand constraints**: voice, visual identity, topics to avoid

Data rules: if you can fetch the profile, record what is publicly visible (followers, following, post count, bio, formats, recent engagement counts); if you cannot, say so and ask for screenshots — do not estimate engagement for posts you have not seen. Benchmarks are starting points; the account's own Insights always win. Instagram changes features often (hashtag following removed, Reels length extended, grid ratio changed); if the UI differs from what is written here, follow the UI and note it.

## Audit Workflow

### Step 1: Profile and public data

| Metric | Where | Why |
|--------|-------|-----|
| Followers / following / posts | Header | Baseline; following ≫ followers looks like follow-for-follow |
| Bio, name field, category | Header | Searchable keywords and clear value proposition |
| Links (up to 5 native links) | Bio | Conversion path |
| Pinned posts (up to 3) | Grid top | Are the best converters pinned? |
| Highlights | Below bio | Evergreen proof and offers |
| Grid preview (3:4 crops since 2025) | Grid | Are covers legible when cropped? |
| Last 20–30 posts | Grid / Reels tab | Format mix, cadence, themes |
| Engagement per post | Likes, comments (shares/saves only via Insights) | Pattern of what resonates |

### Step 2: Engagement rate and benchmarks

Engagement rate by reach (preferred when Insights are available): `(likes + comments + saves + shares) ÷ reach × 100`.
Engagement rate by followers (public fallback): `(likes + comments) ÷ followers × 100`.

| Followers | Strong (by followers) | Average | Weak |
|-----------|----------------------|---------|------|
| < 10K | > 5% | 2–5% | < 2% |
| 10K–100K | > 3% | 1–3% | < 1% |
| 100K–1M | > 2% | 0.7–2% | < 0.7% |
| > 1M | > 1% | 0.4–1% | < 0.4% |

Also read: **non-follower share of reach** (growth accounts want > 40% on Reels), **sends per reach** and **saves per reach** (the strongest signals for distribution), **average watch time** and **replays** on Reels, and **profile visits → follows** conversion.

### Step 3: Format mix (last 20–30 posts)

| Format | Role in 2026 | Notes |
|--------|-------------|-------|
| Reels (up to 3 min; 15–45 s sweet spot for reach) | Reach to non-followers | Ranked on watch time and sends; the first second decides |
| Carousels (up to 20 slides) | Saves, shares, depth | Instagram re-serves carousels with the next slide if the first was skipped; strong for education |
| Single image | Followers' feed | Lower reach; fine for announcements and visual brands |
| Stories (24 h) | Retention and conversion | Polls, questions, links; distribution only to followers |
| Live, Broadcast channels, Notes | Community | Low effort retention tools |
| Collabs | Shared distribution | Post appears on up to 5 accounts with pooled engagement |
| Trial Reels | Testing | Shown to non-followers first; use to test hooks before the followers see them |

Diagnostic: if Reels are under ~40% of posts and the goal is growth, reach is being left on the table; if the goal is retention and sales, carousels and Stories carry more weight than their reach suggests.

### Step 4: Pattern analysis

1. Which format has the highest reach per post, and which the highest saves + shares per reach?
2. Which topics generate comments and DMs (not only likes)?
3. What do the top 5 posts share — hook style, topic, length, caption structure, posting time?
4. Which posts drove profile visits and follows (Insights per post)?
5. Where do reach drops coincide with cadence gaps, reposts or format changes?

## Strategy Formulation

### Content pillars (3–5)

| Pillar type | Examples | Formats |
|-------------|----------|---------|
| Educational | "3 steps to X", "why Y happens", myth-busting | Reels, carousels |
| Proof / results | Client outcomes, before/after (policy-safe), data | Carousels, Reels |
| Behind the scenes / process | How it is made, team, founder day | Reels, Stories |
| Point of view / opinion | Industry takes, trends decoded | Reels (talking head), text carousels |
| Community / conversation | Questions, polls, user content, replies | Stories, Notes, comments-driven Reels |

Each pillar gets a recurring, recognisable format (a series) so the audience knows what to expect and the algorithm can categorise the account.

### Format and cadence

Sustainable cadence beats bursts. Starting points by capacity:

| Capacity | Cadence |
|----------|---------|
| Solo, few hours/week | 3 posts/week (2 Reels + 1 carousel) + Stories 3–5 days/week |
| Small team | 4–5 posts/week (3 Reels + 1–2 carousels) + daily Stories |
| Content team | 1–2 posts/day, no more; extra effort goes to quality and replies |

Mix for growth accounts: ~50–60% Reels, 30–40% carousels, ≤ 10% single images; Stories daily as retention layer. Mix for sales/retention accounts: 40% carousels, 40% Reels, 20% Stories-led offers.

### Timing

Post when the audience is active (Insights → Audience → Most active times), roughly 15–30 minutes before the peak. Generic windows (weekday late morning and early evening local time) are a fallback, not a rule. Consistency of slot matters more than the exact hour.

### Reels craft

- Hook in the first second: movement, on-screen line that states the payoff, or a visual contrast
- On-screen captions always; a share-worthy line near the end ("send this to…")
- Original audio or trending audio with the small arrow icon; original content gets a distribution boost, reposts are penalised
- Cover image with legible text for the 3:4 grid crop
- Keyword-rich caption first line and on-screen text — Instagram search and Google indexing read them
- Hashtags: max 5, treat as topic labels, not reach

### Growth tactics

| Tactic | Effort | Impact | Why it works |
|--------|--------|--------|--------------|
| Send-worthy content | Medium | Very high | Sends per reach is the top non-follower signal; make content people forward to one person |
| Consistent series | Medium | Very high | Returning viewers raise watch time and follows |
| Collab posts with peers | Medium | High | Pooled audiences and engagement |
| Reply to every comment early and in DMs | Medium | High | Early engagement velocity and relationship signal |
| Trial Reels for hook testing | Low | High | Learn what non-followers respond to without burning followers |
| Carousel with a reason to save | Medium | High | Saves and re-serving extend lifetime |
| Profile conversion | Low | Medium | Clear name field keyword, bio promise, pinned proof, right link |
| Stories with polls/questions daily | Low | Medium | Keeps the account in followers' trays and feeds the ranking |
| Cross-post natively to other platforms | Low | Medium | Repurpose, but re-edit for each platform's safe zones and length |

### Growth stages

| Followers | Focus |
|-----------|-------|
| < 1K | Reels only for reach, one series, reply to everything, test hooks with Trial Reels, engage genuinely with 20 accounts in the niche daily |
| 1K–10K | Add carousels and 3 pillars, start collabs, build the Stories habit, optimise profile conversion |
| 10K–50K | Double down on the two best formats, systematise series, test lead magnets via DM automation and links |
| 50K–200K | Raise production quality on hooks and editing, track saves/sends over followers, add Broadcast channel |
| > 200K | Team and templates, brand partnerships, protect quality over volume |

## Profile Optimization Checklist

- [ ] Profile photo recognisable at thumbnail size (face or simple logo)
- [ ] Name field includes the main keyword (e.g. "Ana | Running Coach")
- [ ] Bio: who it is for + outcome + proof + CTA, in under 150 characters
- [ ] Up to 5 native links ordered by priority (no third-party link page unless needed)
- [ ] 3 pinned posts: best proof, best explainer, current offer
- [ ] Highlights with covers: About, Results, Offers, FAQ, BTS
- [ ] Category set correctly; contact buttons on for business accounts
- [ ] Professional account enabled so Insights and Google indexing are available

## Output Format

```
INSTAGRAM AUDIT: @handle (URL)
Account type: [creator / business] | Goal: [..] | Access: [fetched / screenshots / Insights export]

--- CURRENT STATE ---
Followers: X | Following: Y | Posts: Z
Engagement rate: W% (by [reach/followers]) | Non-follower reach share: V% (if known)
Format mix (last N posts): Reels X%, Carousels Y%, Single Z%
Cadence: X posts/week, Stories Y days/week
Top performers: [3 posts — format, topic, why]

--- STRENGTHS ---
- [...]

--- GAPS ---
- [...]

--- CONTENT PILLARS (3–5) ---
1. [Pillar] — [Promise to audience] — [Series format] — [Frequency]
2. [...]

--- FORMAT MIX & CADENCE ---
Reels X% / Carousels Y% / Single Z% | Stories: [days/week]
Weekly plan: [Mon: Reel (pillar) …]
Posting windows: [from Insights or stated fallback]

--- GROWTH PLAN ---
0–30 days: [3 actions]
30–90 days: [3 actions]
90+ days: [3 actions]
KPIs to track: [reach from non-followers, sends/reach, saves/reach, profile visits→follows]

--- PROFILE OPTIMIZATION ---
Name field: [..] | Bio rewrite: [..] | Links: [..] | Pinned posts: [..] | Highlights: [..]

--- ASSUMPTIONS & MISSING DATA ---
[...]
```

## Common Pitfalls

1. **Reposting other accounts' content.** Original content gets more distribution; frequent reposting removes an account from recommendations.

2. **Optimising for likes.** Sends and saves move reach; design content to be forwarded and kept.

3. **Posting daily for two weeks, then nothing.** Consistency at a sustainable cadence beats intensity.

4. **Hook arrives late.** Watch time starts at zero; the first second decides whether the Reel is watched at all.

5. **Treating hashtags as reach.** Five topical hashtags help classification; thirty do nothing extra.

6. **Ignoring the grid crop.** Covers designed for 1:1 lose their text in the 3:4 grid.

7. **No reply strategy.** Comments and DMs in the first hour compound; a silent account trains people not to engage.

8. **Judging a Reel after 24 hours.** Reels gain distribution over days; evaluate at 72 hours and again at 7 days.

## Verification Checklist

- [ ] Last 20–30 posts analysed (or the limitation stated)
- [ ] Engagement rate calculated with the formula named and benchmarked by follower tier
- [ ] Format mix quantified and compared to the goal (growth vs retention)
- [ ] Sends, saves and watch time discussed as the primary signals, not likes alone
- [ ] 3–5 content pillars with a recurring series format each
- [ ] Cadence matched to stated team capacity
- [ ] Posting windows based on Insights, or the fallback labelled as such
- [ ] Growth plan split into 0–30 / 30–90 / 90+ days with KPIs
- [ ] Profile optimisation covers name field, bio, links, pinned posts, highlights
- [ ] Hashtag guidance limited to ≤ 5 topical tags
- [ ] Strategy tailored to the account's follower stage
