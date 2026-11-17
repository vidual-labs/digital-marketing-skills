---
name: youtube-organic
description: Use when developing YouTube organic strategy — channel audit, traffic-source diagnosis, title and thumbnail strategy, retention and hook structure, upload cadence, Shorts-to-long-form funnel and subscriber growth. Also use when someone asks "why aren't my videos getting views", wants a content plan for a channel, or needs help choosing video length and series formats. Don't use for YouTube Ads, live-event production, or monetization and sponsorship deals.
version: 1.2.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. Browsing is optional; when the channel cannot be fetched, the skill works from YouTube Studio screenshots (traffic sources, CTR, retention) the user provides.
metadata:
  category: organic-social
  updated: 2026-11-17
  tags: [youtube, organic, video, shorts, thumbnails, retention, search, subscriber-growth, content-strategy]
  related_skills: [instagram-organic, linkedin-organic, pinterest-organic, tiktok-ads, competitor-research, geo-ai-seo]
---

# YouTube Organic Strategy

## Overview

Build a data-informed plan for a YouTube channel: audit the channel and its recent uploads, diagnose where views come from, fix the two levers that gate distribution (click-through rate from title + thumbnail, and retention), define pillars and series, set a sustainable cadence, and decide how Shorts feed long-form. YouTube is a recommendation engine and a search engine; it rewards videos that get clicked by the people shown them and then keep them watching.

## When to Use

- Auditing a channel and its last 20–30 videos
- Diagnosing low views, low CTR or poor retention
- Planning series, cadence and video length
- Building a Shorts strategy that supports long-form
- Optimising titles, thumbnails, descriptions and channel pages

Don't use for: YouTube Ads campaigns, live-stream production, monetisation policy, sponsorship negotiation, or editing software tutorials.

## Inputs

Ask for (or extract from the conversation):

- **Channel URL** and goal (subscribers, watch time, leads, product sales, authority)
- **YouTube Studio screenshots** (last 28–90 days): traffic sources, impressions and CTR, average view duration and percentage viewed, audience retention curves of 3–5 recent videos, returning vs new viewers, subscribers gained per video, Shorts vs long-form breakdown
- **Last 20–30 uploads**: title, length, publish date, views, and whether Shorts or long-form
- **Production capacity**: how many videos per month can realistically be made at what quality
- **Niche and competitors** the user watches or benchmarks against

Data rules: if you can fetch the channel, record the public data (subscribers, video count, titles, view counts, upload dates, thumbnails as described); if not, say so and ask for screenshots — never estimate CTR or retention. Benchmarks are starting points; Studio's own "typical performance" comparison beats them. YouTube changes limits and features (Shorts up to 3 minutes since Oct 2024, thumbnail Test & Compare, Communities, Hype); if the UI differs, follow the UI and note it.

## Audit Workflow

### Step 1: Channel analysis

| Metric | Where | Why |
|--------|-------|-----|
| Subscribers, total views, video count | Channel home / About | Baseline |
| Banner, trailer, About, links | Home | Clarity of promise to a new visitor |
| Last 20–30 uploads | Videos / Shorts tabs | Cadence, formats, topics |
| Views per video vs subscriber count | Videos tab | Health: long-form views at 10–30% of subscribers within a week is normal |
| Top 10 videos all time | Popular sort | What already resonates |
| Playlists and sections | Home layout | Session guidance |

From Studio: **traffic sources**, **impressions CTR**, **average view duration (AVD)** and **average percentage viewed**, **retention curves**, **returning viewers**, **subscribers per video**.

### Step 2: Traffic source diagnosis (the most important read)

| Dominant source | Meaning | Action |
|-----------------|---------|--------|
| Browse features (home, subscriptions) > 40% | YouTube is recommending to a warm audience; CTR and retention are strong | Protect cadence and series; raise production on hooks |
| Suggested videos > 30% | Videos sit next to related content | Make sequels and playlists; mirror topics that drive suggestions |
| YouTube search > 40% | Found by intent | Double down on searchable titles, chapters and descriptions; evergreen library |
| Shorts feed dominant | Reach without loyalty unless funnelled | Build the Shorts → long-form bridge (below) |
| External > 20% | Growth depends on other platforms | Fine as a start; build internal discovery so the channel stands on its own |

### Step 3: CTR and retention

| Metric | Weak | Typical | Strong |
|--------|------|---------|--------|
| Impressions CTR (long-form) | < 3% | 4–6% | > 8% |
| Average percentage viewed (8–15 min video) | < 35% | 40–50% | > 55% |
| Retention at 30 s | < 60% | 65–75% | > 80% |
| Shorts: viewed vs swiped away | < 60% viewed | 65–75% | > 80% |

CTR is relative to who sees the impressions: a broad push lowers CTR without meaning the thumbnail got worse. Read CTR together with impressions and AVD.

Retention curve reading: a cliff in the first 30 seconds = intro problem; a steady slide = pacing; spikes = re-watched moments to repeat; a dip then recovery = a segment to cut.

Average percentage viewed falls as length grows, so compare videos of similar length, or compare absolute average view duration across lengths. Never compare Shorts and long-form CTR or retention with each other.

### Step 3b: Find the primary constraint

Read CTR and retention together for the last 10 long-form videos (each against the channel's own median, or the table above if there is no history):

| CTR | Retention (30 s and avg % viewed) | Primary constraint | First fix |
|-----|-----------------------------------|--------------------|-----------|
| Low | High | **Packaging** — the video is good, the title/thumbnail undersells it | Retitle and Test & Compare thumbnails on existing videos |
| High | Low | **Promise mismatch / retention** — packaging overpromises or the intro stalls | Match the first frame to the thumbnail; cut the intro; deliver the payoff earlier |
| Low | Low | **Topic** — the idea itself does not pull this audience | Re-select topics from top performers, search demand and comments before polishing |
| High | High, but impressions flat | **Discovery / volume** — too few uploads or too narrow a topic | Raise cadence within capacity; series and playlists; adjacent topics |
| High | High, impressions rising | **None** — scale | Protect slot and series; more of the same format |

Supporting ratios (starting points; prefer the channel's own medians):

| Ratio | Formula | Read |
|-------|---------|------|
| Subscribers per 1,000 views | subs gained ÷ views × 1,000 | Compare videos and formats; Shorts usually convert at a fraction of long-form — measure, don't assume |
| Returning viewer share | returning ÷ unique viewers | Low (< ~20%) with high views = one-off hits, no series pull |
| Impressions trend | impressions per video, last 10 vs previous 10 | Falling with stable CTR = YouTube testing it on fewer people; fix retention first |

Per-video classification against Studio's typical-performance range (or the median views of the last 10 uploads at the same age):

| Result | Rule | Action |
|--------|------|--------|
| Outlier | > 2× median at 7 days | Make a sequel or a series from it within a month; link it from older videos |
| On track | 0.5–2× median | Keep the format |
| Under | < 0.5× median at 7 days | Change the packaging (title, thumbnail) once, re-check at 28 days; don't delete and reupload |

Judge long-form at 7 and 28 days, Shorts at 7 days. Call a pattern only across 3+ comparable videos.

### Step 4: Title and thumbnail audit

| Element | Good | Fix |
|---------|------|-----|
| Title | Specific outcome or curiosity gap, ≤ 60 characters visible, no clickbait the video cannot pay off | Add the payoff, remove filler, front-load the keyword for search |
| Thumbnail | One focal subject, high contrast, ≤ 3 words of text, readable at 120 px | Remove clutter; face with emotion or object with contrast |
| Title + thumbnail | Complementary (title says what, thumbnail shows why or the stakes) | Never repeat the same words in both |
| Consistency | Recognisable style per series | Template per series |
| Testing | Use Test & Compare (up to 3 thumbnails) on new uploads | Test one variable at a time |

Testing rules: variants must differ in one idea (face vs object, text vs no text, stakes vs result), not in small tweaks; let the test finish rather than overriding early; log the winner and the losing idea so the series template improves. Studio picks the winner on watch time, not only clicks, so a "lower CTR" winner can be correct.

## Strategy Formulation

### Content pillars and series (3–5)

| Pillar type | Drives | Example formats |
|-------------|--------|-----------------|
| Evergreen how-to / tutorial | Search, library value | "How to X", "Complete setup" |
| Commentary / analysis | Suggested and browse | "Why X failed", "X explained" |
| Case study / experiment | Trust and watch time | "We tested X for 30 days" |
| Series with a recurring hook | Returning viewers | Weekly teardown, Q&A, ranking |
| Story / behind the scenes | Connection, community | "How I built X" |

Mix for most channels: ~50% searchable evergreen, 20% timely, 20% series for returning viewers, Shorts as a parallel track rather than a percentage of long-form.

### Cadence

Consistency and quality beat frequency. Choose the cadence the team can hold for 6 months.

| Stage | Long-form | Shorts | Posts (community) |
|-------|-----------|--------|-------------------|
| < 1K subs | 1/week | 2–4/week to test hooks and topics | Occasional |
| 1K–10K | 1–2/week | 3–5/week | Weekly poll or teaser |
| 10K–100K | 1–2/week plus a series slot | 3–7/week | 2–3/week |
| > 100K | 2+/week with a team | Daily if resourced | Regular |

Publish at a fixed slot; Studio's "when your viewers are on YouTube" beats generic time tables. Premieres and Posts can warm the slot.

### Video structure for retention

| Section | Rule |
|---------|------|
| Hook (0–15 s) | Show the payoff or the stakes; no "hi guys, welcome back"; the first frame should match the thumbnail's promise |
| Credibility (one line) | Why this video, why you — then move on |
| Body | A visual or structural change every 60–90 seconds; chapters in the description; deliver a concrete takeaway every 3–4 minutes |
| Open loops | Tease what is coming ("the third one is the one that broke") without stalling |
| Ending | One CTA to the next best video (end screen); do not stack subscribe/like/comment/follow |

### Video length by goal

| Goal / genre | Typical length | Why |
|--------------|---------------|-----|
| Tutorials | 8–15 min | Depth without drop-off |
| Commentary / analysis | 10–20 min | Argument needs runway |
| Deep dives / documentary | 20–40 min | High watch time per viewer if retention holds |
| News / timely | 6–12 min | Fast consumption |
| Shorts (reach) | 15–45 s | Highest completion and loops |
| Shorts (storytelling, up to 3 min) | 60–120 s | Only when the story holds; viewed-vs-swiped is the metric |

### Shorts → long-form funnel

- Each Short carries one idea from a long-form video and ends on a question the long video answers
- Use the "related video" link on Shorts to point to the long-form
- Match the Short's topic to the channel's long-form so the audience overlap is real
- Track subscribers and long-form views from Shorts viewers in Studio; Shorts audiences convert weakly unless the bridge is explicit

### Growth tactics

| Tactic | Effort | Impact | Why |
|--------|--------|--------|-----|
| Thumbnail Test & Compare on every upload | Low | Very high | Directly lifts the gatekeeper metric |
| Rewrite the first 30 seconds | Medium | Very high | Early retention decides distribution |
| Series with a recurring hook | Medium | Very high | Returning viewers and browse distribution |
| Playlists and end screens to the next video | Low | High | Session time and suggested traffic |
| Search-first titles for evergreen | Low | High | Compounding library views |
| Shorts bridge | Medium | High | Reach that converts |
| Collaborations with channels 2–5× your size | Medium | High | Audience transfer |
| Posts and polls between uploads | Low | Medium | Keeps subscribers warm, informs topics |
| Localisation (auto-dubbing, translated titles) | Low | Medium | New language markets at near-zero cost |

## Channel Page Checklist

- [ ] Banner states who the channel is for and the upload promise
- [ ] Trailer for new visitors (30–60 s "why watch") and a different featured video for returning subscribers
- [ ] About with keywords, links and a contact
- [ ] Handle set (youtube.com/@name)
- [ ] 4–8 playlists matching pillars, arranged as home sections
- [ ] End-screen and card templates
- [ ] Default upload settings: description template with chapters, links, disclosure where needed
- [ ] Altered or synthetic content disclosure set when AI-generated media is used

## Output Format

Label every number with its source: `[Studio]`, `[public]`, `[user-provided]` or `[assumption]`. Write `n/a` instead of estimating CTR, retention or traffic shares you have not seen.

```
YOUTUBE AUDIT: [Channel] (URL)
Goal: [..] | Stage: [subscriber tier] | Access: [fetched / Studio screenshots]
Subscribers: X | Videos: Y | Total views: Z | Avg views (last 20 long-form): W

--- CURRENT STATE ---
Format mix: Long-form X% / Shorts Y% / Live Z%
Cadence: X long-form/week, Y Shorts/week
Traffic sources: Browse X% / Suggested Y% / Search Z% / Shorts feed … / External …
CTR: X% → [weak/typical/strong] | Avg view duration: Y | Avg % viewed: Z% | Retention at 30 s: V% | Returning viewers: W%
Subs per 1,000 views: long-form X / Shorts Y
Top performers: [3 videos — why]

--- DIAGNOSIS ---
Primary constraint: [packaging / retention / topic / discovery / Shorts bridge / none — scale]
Evidence: [the CTR × retention read and 1–2 supporting numbers]
Dominant traffic source → implication: [..]

--- VIDEO SCORECARD (last 5–10 long-form) ---
| Video | Length | Views vs median | CTR | Avg % viewed | Verdict (outlier / on track / under) |
|-------|--------|-----------------|-----|--------------|--------------------------------------|
| .. | .. | ..× | ..% | ..% | .. |

--- STRENGTHS ---
- [...]

--- GAPS ---
- [...]

--- PRIORITY ACTIONS ---
1. [Action] — [metric it moves] — [effort: low/med/high]
2. [...]
3. [...]

--- CONTENT PILLARS & SERIES (3–5) ---
1. [Pillar] — [Series name/hook] — [Length] — [Frequency]
2. [...]

--- CADENCE ---
Long-form: [..] | Shorts: [..] | Posts: [..] | Slot: [from Studio or stated fallback]

--- TITLE & THUMBNAIL ---
[Current pattern] → [Recommended pattern]
Examples: [3 title rewrites (≤ 60 characters) with thumbnail concept (≤ 3 words)]
Testing: [Test & Compare plan — variable tested per video]

--- RETENTION FIXES ---
[Intro structure, pacing, chapters, open loops, ending]

--- SHORTS STRATEGY ---
[Bridge to long-form, cadence, metrics]

--- GROWTH PLAN ---
0–30 days: [3 actions]
30–90 days: [3 actions]
90+ days: [3 actions]
KPIs: [metric — current → target, review date] (CTR, AVD/%, returning viewers, subs per 1,000 views, browse + suggested share)

--- CHANNEL PAGE ---
[Banner, trailer, About, playlists, end screens]

--- ASSUMPTIONS & MISSING DATA ---
[What was assumed, which Studio screenshots to send next]
```

For a narrow request (title rewrites, a Shorts question), give the deliverable first, then DIAGNOSIS, PRIORITY ACTIONS and ASSUMPTIONS & MISSING DATA; skip sections that do not apply.

## Common Pitfalls

1. **Long intros.** The first 15–30 seconds lose a third of viewers on most channels. Start with the payoff.

2. **Thumbnail repeating the title.** They should carry different information: what vs why/stakes.

3. **Treating low CTR as a thumbnail failure in isolation.** Read CTR with impressions; a broader push lowers CTR naturally.

4. **Random uploads.** No series means no returning viewers; returning viewers are the browse engine.

5. **Shorts without a bridge.** Reach without conversion; make the link to long-form explicit.

6. **Ignoring Studio.** Traffic sources and retention curves are free, specific and actionable.

7. **Chasing frequency.** Two forgettable videos a week lose to one that keeps people watching.

8. **One CTA too many.** Stacked asks dilute; point to the next video.

9. **Comparing videos of different lengths on average percentage viewed.** A 25-minute video at 35% can hold viewers longer than an 8-minute one at 50%. Compare similar lengths or use absolute view duration.

10. **Deleting and reuploading underperformers.** It throws away the video's history and comments. Change title and thumbnail once, then judge at 28 days.

11. **Judging a video at 48 hours.** Search and suggested traffic build for weeks. Read at 7 and 28 days against the channel's own median.

12. **Polishing packaging on a topic nobody wants.** When CTR and retention are both low, the topic is the problem. Re-select topics from top performers, search and comments first.

13. **Mixing Shorts and long-form metrics.** Different feeds, different viewers, different benchmarks. Report them separately.

## Verification Checklist

- [ ] Last 20–30 uploads reviewed (or the limitation stated); no CTR/retention figures invented
- [ ] Traffic sources diagnosed and tied to actions
- [ ] CTR read together with impressions and AVD, benchmarked
- [ ] Retention curves interpreted (intro cliff, pacing, spikes) where provided
- [ ] 3–5 pillars with at least one recurring series
- [ ] Cadence matched to capacity for long-form, Shorts and Posts
- [ ] Title and thumbnail recommendations with concrete rewrites and a Test & Compare plan
- [ ] Shorts strategy includes an explicit bridge to long-form
- [ ] Channel page checklist applied
- [ ] Growth plan split 0–30 / 30–90 / 90+ days with KPIs
- [ ] Every number labelled with its source; `n/a` used instead of estimates
- [ ] One primary constraint named from the CTR × retention read, with evidence
- [ ] Video scorecard compares each video with the channel's own median, at a stated age
- [ ] Shorts and long-form reported separately (CTR, retention, subs per 1,000 views)
- [ ] Priority actions ranked; benchmarks phrased as starting points
