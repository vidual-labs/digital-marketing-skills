---
name: instagram-organic
description: Use when developing Instagram organic strategy — auditing a profile, defining content pillars, choosing a Reels/carousel/story mix, setting a posting cadence, and planning follower and reach growth around Instagram's current ranking signals (watch time, likes, sends). Also use when someone asks "why did my reach drop", wants an Instagram content calendar, or asks how to grow an account from scratch. Don't use for Instagram paid ads (meta-ads-creative, meta-ads-diagnostics), influencer contracting, or Instagram Shop setup.
version: 1.2.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. Browsing is optional; when a profile cannot be fetched, the skill works from screenshots and Insights exports the user provides.
metadata:
  category: organic-social
  updated: 2026-11-17
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

Do not mix the two engagement formulas in one comparison, and never benchmark a reach-based rate against the follower-based table — reach-based rates run higher by construction.

### Step 2b: Signal ratios and per-post thresholds

Compute these per post, then average per format. They are the numbers the rest of the plan is built on.

| Ratio | Formula | Starting-point read (replace with the account's own median once 20+ posts exist) |
|-------|---------|------------------------------------------------------------------------------------|
| Sends per reach | shares ÷ reach × 100 | ≥ 1% strong, 0.3–1% normal, < 0.3% weak — content is not being forwarded |
| Saves per reach | saves ÷ reach × 100 | ≥ 1.5% strong (carousels), < 0.5% weak — no reason to keep it |
| Non-follower reach share (Reels) | non-follower reach ÷ reach | > 40% healthy for growth; < 20% means Reels are not leaving the follower base |
| Follows per 1,000 reach | follows ÷ reach × 1,000 | Use to compare formats and series; low with high reach = profile or topic mismatch |
| Profile visit → follow | follows ÷ profile visits × 100 | < 10% means the profile does not convert visitors (fix bio, name field, pinned posts) |

Per-post classification relative to the account's own **median reach for that format** (last 20–30 posts):

| Result | Rule | Action |
|--------|------|--------|
| Outlier winner | > 2× median reach, or top 10% on sends/reach | Make 2–3 variants (same topic, new hook) within 2 weeks; pin if it converts |
| Solid | 0.7–2× median | Keep in the rotation |
| Miss | < 0.5× median at 7 days | Check hook and topic; do not repost it unchanged |

Judge with at least 5 posts per format before calling a format "weak"; fewer than that, label the read as provisional. Evaluate Reels at 72 hours and again at 7 days, not at 24 hours.

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

Format decision rules (apply to the per-format averages from Step 2b):

| If… | Then… |
|-----|-------|
| Goal is growth and Reels are < 40% of posts | Shift toward Reels (target 50–60%) before changing anything else |
| A format has the lowest reach/post **and** the lowest sends + saves per reach | Cut it to ≤ 10% of posts or drop it |
| A format has low reach but the highest saves/reach (often carousels) | Keep it — it serves retention and sales; improve slide 1 instead of cutting it |
| Reels reach is high but follows per 1,000 reach is low | Topic or profile mismatch: tie Reels to the pillars and fix the profile before posting more |
| Goal is sales/retention | Weight carousels and Stories above their reach share; measure link clicks, DMs and profile actions |
| Fewer than 5 posts of a format in the sample | Treat as untested — schedule 4–6 posts before judging |

### Step 4: Pattern analysis

1. Which format has the highest reach per post, and which the highest saves + shares per reach?
2. Which topics generate comments and DMs (not only likes)?
3. What do the top 5 posts share — hook style, topic, length, caption structure, posting time?
4. Which posts drove profile visits and follows (Insights per post)?
5. Where do reach drops coincide with cadence gaps, reposts or format changes?

### Step 5: Reach-drop diagnosis

Locate the drop first, then pick the cause. Check **Account Status** (Settings → Account Status) for content that is not eligible to be recommended before anything else — it is the fastest way to confirm or rule out a recommendation problem.

| Symptom | Likely cause | Check | Fix |
|---------|--------------|-------|-----|
| Non-follower reach collapsed, follower reach stable | Lost recommendation eligibility: reposted or unoriginal content, watermarked clips from other apps, guideline issues | Account Status; count of reposts/recycled clips in the last 30 days | Stop reposting; publish only original Reels; remove or appeal flagged posts; expect recovery over weeks, not days |
| All reach down, cadence dropped or was erratic | Fewer posts, weaker velocity | Posts/week before vs after | Return to the sustainable cadence for 4+ weeks before judging |
| One format down, others stable | Creative fatigue or format shift in the account | Per-format reach and watch time | Refresh hooks/covers for that format; test with Trial Reels |
| Reach stable, engagement rate down | Audience mismatch or bought/inactive followers | Follower growth spikes, follows from off-niche content | Return to niche pillars; never buy followers or join engagement pods |
| Reach down across the whole niche at once | Seasonality or a platform change | Compare peers; note the date | Hold strategy; keep cadence; re-check in 2–3 weeks |
| Sudden drop after hashtag or caption changes | Usually coincidence — hashtags are labels, not reach | Timeline of changes | Revert to ≤ 5 topical hashtags and look for the real cause above |

Change one thing at a time during recovery so the cause stays readable.

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

### Testing protocol

| Rule | Why |
|------|-----|
| Test one variable at a time (hook, cover, length, topic) | Otherwise the winner teaches nothing |
| Use Trial Reels for hook tests; 2–3 variants of the same idea | Non-follower response without spending the followers' attention |
| Compare at the same age (72 h and 7 d) against the format median | Reels accumulate reach over days |
| Call a winner only on a clear gap (e.g. > 1.5× the other variant on sends/reach or watch time) | Small gaps are noise at organic sample sizes |
| Log every test (date, variable, result) | Patterns appear across 10+ tests, not one |

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

Label every number with its source: `[Insights]`, `[public]`, `[user-provided]` or `[assumption]`. Write `n/a` instead of estimating a figure you do not have.

```
INSTAGRAM AUDIT: @handle (URL)
Account type: [creator / business] | Goal: [..] | Stage: [follower tier] | Access: [fetched / screenshots / Insights export]

--- CURRENT STATE ---
Followers: X | Following: Y | Posts: Z [source]
Engagement rate: W% (by [reach/followers], formula: [..]) → [strong/average/weak] vs tier
Non-follower reach share: V% | Profile visit → follow: U% (or n/a)
Format mix (last N posts): Reels X% / Carousels Y% / Single Z%
Cadence: X posts/week, Stories Y days/week
Top performers: [3 posts — format, topic, why]

--- FORMAT SCORECARD ---
| Format | Posts | Avg reach | Sends/reach | Saves/reach | Verdict (scale / keep / fix / cut / untested) |
|--------|-------|-----------|-------------|-------------|-----------------------------------------------|
| Reels | .. | .. | ..% | ..% | .. |
| Carousels | .. | .. | ..% | ..% | .. |
| Single images | .. | .. | ..% | ..% | .. |

--- DIAGNOSIS ---
Primary constraint: [reach / recommendation eligibility / format mix / hook & watch time / profile conversion / cadence]
Evidence: [the 1–3 numbers that show it]

--- STRENGTHS ---
- [...]

--- GAPS ---
- [...]

--- PRIORITY ACTIONS ---
1. [Action] — [expected signal it moves] — [effort: low/med/high]
2. [...]
3. [...]

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
KPIs to track: [metric — current → target, review date] (non-follower reach share, sends/reach, saves/reach, profile visit → follow)

--- PROFILE OPTIMIZATION ---
Name field: [..] | Bio rewrite: [..] | Links: [..] | Pinned posts: [..] | Highlights: [..]

--- ASSUMPTIONS & MISSING DATA ---
[What was assumed, what to send next to firm up the plan]
```

For a narrow question (a reach drop, a single post review), keep CURRENT STATE, DIAGNOSIS, PRIORITY ACTIONS, GROWTH PLAN and ASSUMPTIONS & MISSING DATA, and drop the sections that do not apply.

## Common Pitfalls

1. **Reposting other accounts' content.** Original content gets more distribution; frequent reposting removes an account from recommendations.

2. **Optimising for likes.** Sends and saves move reach; design content to be forwarded and kept.

3. **Posting daily for two weeks, then nothing.** Consistency at a sustainable cadence beats intensity.

4. **Hook arrives late.** Watch time starts at zero; the first second decides whether the Reel is watched at all.

5. **Treating hashtags as reach.** Five topical hashtags help classification; thirty do nothing extra.

6. **Ignoring the grid crop.** Covers designed for 1:1 lose their text in the 3:4 grid.

7. **No reply strategy.** Comments and DMs in the first hour compound; a silent account trains people not to engage.

8. **Judging a Reel after 24 hours.** Reels gain distribution over days; evaluate at 72 hours and again at 7 days.

9. **Cross-posting clips with another app's watermark.** Recycled, watermarked video is treated as unoriginal. Export clean files and re-edit natively.

10. **Calling a format dead on three posts.** Organic results are noisy. Judge on 5+ posts per format against the account's own median, and label smaller samples as provisional.

11. **Mixing engagement formulas.** A reach-based rate compared with a follower-based benchmark looks great and means nothing. Name the formula and benchmark like with like.

12. **Buying followers or joining engagement pods.** Inactive or off-niche followers drag every rate down and confuse who the content is shown to. Grow through niche content, collabs and replies.

13. **Changing everything during a reach drop.** Five simultaneous changes hide the cause. Check Account Status first, then change one variable per week.

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
- [ ] Every number labelled with its source; nothing estimated for posts not seen
- [ ] Format scorecard filled with sends/reach and saves/reach per format, and a verdict per format
- [ ] Format calls based on 5+ posts each, or labelled provisional
- [ ] One primary constraint named with the evidence behind it
- [ ] For reach drops: Account Status check recommended and the drop located (follower vs non-follower, one format vs all)
- [ ] Benchmarks phrased as starting points; the account's own medians preferred where available
