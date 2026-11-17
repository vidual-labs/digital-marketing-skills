---
name: competitor-research
description: Use when researching competitors in a market — identifying direct, indirect and adjacent players, auditing their websites, SEO, paid ads (Google Ads Transparency Center, Meta Ad Library, TikTok and LinkedIn ad libraries), social presence, content strategy and how AI assistants describe them, then running SWOTs and finding actionable market gaps. Also use when someone asks "who are we really competing with", wants a competitive landscape brief, or needs whitespace for a positioning or launch. Don't use for financial due diligence, patent or IP analysis, or pricing models.
version: 1.2.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. Browsing greatly improves results (ad libraries, profiles, SERPs); without it the skill structures the research plan and works from data the user collects.
metadata:
  category: competitive-intelligence
  updated: 2026-11-17
  tags: [competitor-research, competitive-intelligence, market-analysis, gap-analysis, swot, ad-library, positioning, seo-competition]
  related_skills: [market-positioning, branding, geo-ai-seo, instagram-organic, linkedin-organic, youtube-organic, pinterest-organic, google-ads-diagnostics, meta-ads-diagnostics]
---

# Competitor Research

## Overview

Identify and analyse the competitive set for a market, segment and locale, then turn it into decisions: who the real competitors are across three layers, how they show up on web, search, paid, social and in AI answers, what they do well and badly, and — the valuable part — which gaps the brand can credibly claim. Every finding is dated and sourced because competitive data expires quickly.

## When to Use

- Market entry or launch research
- Competitive input for positioning, messaging or creative
- Finding channel, content, audience or offer gaps
- Auditing competitors' paid activity and creative angles
- Preparing a competitive brief for leadership or a client

Don't use for: financial due diligence, patent/IP analysis, pricing elasticity modelling, or legal competitive conduct questions. Hand positioning decisions to `market-positioning` and brand decisions to `branding`.

## Inputs

Ask for (or extract from the conversation):

- **Market and locale** (e.g. "B2B payroll software, DACH")
- **Segment and price tier** (e.g. "SMB, 10–200 employees, mid-price")
- **The brand's own offer** in one line, so gaps are judged against something the brand can execute
- **Known competitors** and any the user suspects
- **Channels in scope** and the brand's capacity (video team? budget for paid?)
- **Access**: can the user export Similarweb/Semrush/Ahrefs data, or share screenshots?

Data rules: if you can browse, fetch what is public (sites, ad libraries, profiles, search results, AI answers) and record the date; if you cannot, produce the research plan with exact places to look and fill in only what the user provides. Never invent traffic, follower or spend figures — label third-party estimates as estimates with the tool name. Ad libraries and platform tools change names and coverage (the EU Digital Services Act expanded ad transparency; Google's is the Ads Transparency Center; TikTok and LinkedIn have ad libraries); if a tool differs, say which one you used.

### Evidence labels

Tag every figure and factual claim in the output so a reader can tell what was seen from what was guessed:

| Tag | Meaning | Example |
|-----|---------|---------|
| `[OBS]` | Observed directly, with date | "14 active Meta ads [OBS 2026-11-17]" |
| `[USER]` | Supplied by the user or their exports | "Churn complaints in 3 of 5 [USER]" |
| `[EST]` | Third-party estimate — name the tool | "~40k visits/month [EST Similarweb, Oct 2026]" |
| `[INF]` | Inferred from other evidence — say from what | "Likely scaling paid [INF: 30 new ads in 2 weeks]" |

Decisions resting only on `[INF]` items are hypotheses: say so in the recommendation and name the check that would confirm them.

## Research Workflow

### Phase 1: Competitor discovery (three layers)

| Layer | Definition | Where to find them |
|-------|-----------|--------------------|
| Direct | Same solution, same audience, same price tier | Search the core buying keywords in the locale; look at who advertises on them; "alternatives to X" lists; G2/Capterra/app-store categories |
| Indirect | Different solution to the same problem | Reddit, niche forums, LinkedIn groups: "how do you handle X"; agencies, in-house tools, spreadsheets, doing nothing |
| Adjacent / aspirational | Brands that share the audience and could expand into the category | Partnerships, co-marketing, who the audience also follows, platform ecosystems |

Target: 8–15 names across layers. Also ask two AI assistants "what are the best [category] for [segment] in [locale]" — their answer is now part of how buyers discover the set.

### Phase 1b: Threat ranking (who gets a deep dive)

Score every identified competitor 1–3 on four factors, then deep-dive the top 3–5 by total. Do not pick deep dives by fame or follower count.

| Factor | 3 | 2 | 1 |
|--------|---|---|---|
| Audience overlap | Same segment, size and locale | Partial (adjacent size or region) | Different segment |
| Offer overlap | Same job, similar price tier | Same job, different tier or model | Different solution (indirect) |
| Discovery presence | Shows up where buyers look: core keywords, ads, AI answers, review categories | Present in one or two | Rarely encountered |
| Momentum | Rising: new ads, hiring, launches, review volume growing | Stable | Shrinking or dormant |

Rules (starting points — adjust if the user knows their win/loss data, which beats any proxy):

- **Total 10–12**: deep-dive. **7–9**: deep-dive if fewer than 3 competitors score 10+, otherwise watchlist. **≤ 6**: list only.
- **Always deep-dive the competitor the brand loses deals to most often**, if the user knows it, whatever its score.
- **Include at least one indirect substitute** (spreadsheet, agency, in-house, doing nothing) in the table even if not deep-dived; it often explains lost deals better than any direct rival.
- **If a factor cannot be scored** (no data), score it 2 and mark it `[INF]` rather than dropping the competitor.

### Phase 2: Digital presence audit (top 5)

| Channel | Capture | Where |
|---------|---------|-------|
| Website | Offer, pricing visibility, proof, design quality, speed, languages | Site, PageSpeed Insights |
| SEO | Rankings for 10 core keywords, content volume, estimated traffic (labelled) | Manual SERPs, Semrush/Ahrefs/Similarweb if available |
| AI search | Whether they are cited or recommended for category queries | Google AI Overviews/AI Mode, ChatGPT, Perplexity |
| Google Ads | Active search/display/video ads, how long running | Google Ads Transparency Center |
| Meta Ads | Active ads, count, formats, angles, start dates, EU reach data | Meta Ad Library |
| TikTok | Organic presence, ad presence and top ads | TikTok profile, TikTok Creative Center, TikTok Commercial Content Library (EU) |
| LinkedIn | Page followers, cadence, formats; active ads | Page, LinkedIn Ad Library |
| Instagram / YouTube / Pinterest | Followers, cadence, formats, engagement pattern | Profiles |
| Reviews | Rating, volume, recurring complaints and praise | G2, Capterra, Trustpilot, app stores, Google Business |
| Email / lifecycle | Welcome flow, cadence, offers | Subscribe with a test address |
| Hiring | Open roles reveal strategy (video, paid, new markets) | Careers page, LinkedIn jobs |

### Phase 3: Content strategy

| Dimension | Questions |
|-----------|-----------|
| Pillars | Which 3–5 topics dominate? |
| Formats | Video-first, long-form text, carousels, podcasts? |
| Voice | Corporate, founder-led, edgy, educational? |
| Cadence | Daily, weekly, sporadic? |
| Signature | A recurring series or format people recognise? |
| Distribution | Cross-platform or siloed? Native or link-outs? |
| Proof | Case studies, numbers, named customers? |

### Phase 4: Paid strategy

| Question | Evidence |
|----------|----------|
| Are they running paid, where, since when? | Ad libraries, Transparency Center, start dates |
| How many distinct creatives are live? | Count unique ads; many variants signal testing budget |
| Which angles and offers? | Problem→solution, proof, discount, demo, lead magnet |
| Who do they target? | Copy, language, EU audience data in Meta Ad Library |
| Creative refresh rate | Start dates spread over weeks vs one old batch |
| Landing pages | Where ads land; offer match |

Reading ad-library evidence (heuristics, not proof — label conclusions `[INF]`):

| Signal | Likely meaning | Caveat |
|--------|----------------|--------|
| An ad live for a long time (roughly 60–90+ days) while others were switched off | A performer worth studying | Some advertisers leave ads running by neglect; check whether spend or impressions data is shown (EU/political ads) |
| Many variants launched on the same date | Structured creative test | Count variants per concept, not just ads |
| Steady stream of new start dates every week or two | Active creative refresh, likely meaningful budget | Count only distinct creatives |
| One batch of old ads, nothing new | Paid on autopilot or deprioritised | — |
| No ads found | Not running paid *in that library, region and date range* | Check country filter, advertiser name variants and the other libraries before concluding "no paid" |
| Same angle across many competitors | Category convention — a message gap may sit beside it | Convention can also mean it works; test, do not just avoid |

Review mining: sample the most recent ~50 reviews (or the last 12 months) per deep-dived competitor; count a theme only when it recurs (e.g. in at least ~10% of the sample or 3+ reviews, whichever is larger); report counts ("onboarding: 11 of 50"), not adjectives.

### Phase 5: SWOT per competitor

```
COMPETITOR: [Name] — [URL] — [Position in one line]
STRENGTHS: [specific, evidenced — "ranks #1–3 for 7 of 10 core keywords"]
WEAKNESSES: [specific — "no video; 3.6★ with recurring complaints about support"]
OPPORTUNITIES (gaps they leave): [..]
THREATS (to them): [..]
Sources and dates: [..]
```

### Phase 6: Market gap analysis

| Gap type | Look for | Example |
|----------|----------|---------|
| Channel | Platforms nobody uses well | "No competitor publishes on YouTube; all are Instagram-first" |
| Format | Formats absent from the set | "Nobody does document carousels or founder video" |
| Audience | Segments ignored | "All target enterprise; 10–50-employee teams have no dedicated content" |
| Locale / language | Underserved geography or language | "No German-language help content despite DACH sales" |
| Voice | Personalities missing | "All corporate; a plain-spoken expert voice is open" |
| Message / offer | Overused claims | "Everyone says AI-powered; nobody says done-for-you" |
| Price / packaging | Missing tiers | "No free tier or monthly plan" |
| Proof | Weak evidence | "No one shows named customer results" |
| AI visibility | Not cited by assistants | "Only two of five are recommended by ChatGPT for the category" |
| Experience | Review complaints | "Onboarding and support are the top complaints for three of five" |

Quantify gaps ("five competitors average 80 YouTube subscribers between them") and check feasibility against the brand's capacity.

Before claiming a gap, ask **why it is empty**: no demand, poor economics, hard capability, or simply overlooked. Only "overlooked" and "hard capability the brand has" are attractive.

Score each gap 1–3 on three factors and multiply (max 27):

| Factor | 3 | 2 | 1 |
|--------|---|---|---|
| Evidence | Counted across the set, `[OBS]` or `[USER]` | Partial or mixed | Single observation or `[INF]` only |
| Demand | Audience asks for it (reviews, forums, search, sales calls) | Plausible, indirect signals | No sign anyone wants it |
| Feasibility | Brand can start within ~30 days with current team and budget | Needs a hire, budget or partner | Needs a product change or capability it lacks |

| Score | Priority |
|-------|----------|
| 18–27 | **Act now** — lead recommendation |
| 8–17 | **Test** — small experiment with a success metric |
| ≤ 7 | **Park** — note on the watchlist |

A gap with Feasibility 1 that is really a product or pricing decision (new tier, new feature) is routed to the owner of that decision, not presented as a marketing action.

### Phase 7: Recommendations (3–5)

| Type | Form |
|------|------|
| Positioning | "Own [attribute] against [dominant claim]" → hand to `market-positioning` |
| Channel | "Lead with [channel] where no competitor is credible" |
| Content | "Build [format/series] nobody offers" |
| Paid | "Test [angle] in [market] where ad libraries show no competitor activity" |
| Messaging | "Lead with [gap message]; avoid [overused claim]" |
| Experience | "Fix [common complaint] and make it a proof point" |

## Output Format

```
COMPETITIVE LANDSCAPE: [Market / Segment / Locale]
Date: [Research date] | Competitors identified: [n] | Deep-dived: [n]
Method: [browsed / user-provided data / mixed] | Tools: [names]
Evidence tags: [OBS date] observed · [USER] user-supplied · [EST tool] estimate · [INF] inferred

--- MARKET OVERVIEW ---
[1–2 paragraphs: maturity, saturation, dominant players, how buyers discover (search, AI, social, referral)]

--- COMPETITOR TABLE ---
| # | Name | Layer | Website | Position | Key strength | Key weakness | Main channels | Paid active? |

--- THREAT RANKING ---
| Name | Audience | Offer | Discovery | Momentum | Total /12 | Decision (DEEP DIVE / WATCHLIST / LIST) |

--- DEEP DIVE: [Competitor 1] ---
Website & offer: [..]
SEO & AI visibility: [..]
Paid: [platforms, # creatives, angles, since]
Social: IG [..] | LinkedIn [..] | YouTube [..] | TikTok [..] | Pinterest [..]
Content pillars & voice: [..]
Reviews: [rating, volume, themes]
SWOT: S [..] W [..] O [..] T [..]
Sources & dates: [..]

[Repeat for top 3–5]

--- MARKET GAPS (quantified, feasibility-checked) ---
| # | Gap type | Evidence (count + tag) | Why empty | Evidence × Demand × Feasibility = Score | Priority (ACT NOW / TEST / PARK) | Action |
[4–6 rows, highest score first]

--- STRATEGIC RECOMMENDATIONS ---
1. Positioning: [..]
2. Channels: [..]
3. Content: [..]
4. Paid: [..]
5. Messaging / experience: [..]
[Each: action — gap # it addresses — success metric — owner; mark hypotheses that rest on [INF] evidence]

--- WATCHLIST ---
[What to re-check in 60–90 days and where]

--- LIMITATIONS ---
[Estimates, missing access, unverified items]
```

## Common Pitfalls

1. **Direct competitors only.** The real threat is often the indirect substitute or the "do nothing" option.

2. **Follower counts as strength.** Check engagement and reviews; large dormant audiences are weak.

3. **Skipping ad libraries.** Organic may look quiet while paid is heavy. Libraries show it in minutes.

4. **Snapshot thinking.** Ad start dates, hiring and cadence changes tell the trend; capture dates.

5. **Unquantified gaps.** "They don't do video much" is an opinion; "five competitors, 1 video in 90 days" is a decision.

6. **Gaps the brand cannot execute.** Flag feasibility against team and budget.

7. **Too many deep dives.** Fifteen SWOTs are noise; five with evidence are a strategy.

8. **Invented numbers.** Traffic and spend estimates from tools are estimates. Say so, with the tool and date, and tag every figure.

9. **"No ads found" read as "no paid".** Libraries differ by region, name variant and date filter. Check all relevant libraries and countries before concluding a competitor is not advertising.

10. **Gaps nobody asked for.** An empty space may be empty because there is no demand or no margin. Record "why empty" and score Demand before recommending.

11. **Deep dives chosen by fame.** The best-known brand is not always the biggest threat. Rank by audience, offer, discovery and momentum, and override only with real win/loss data.

12. **Product decisions disguised as marketing.** A missing pricing tier or feature is a product call; route it to its owner instead of listing it as a campaign.

## Verification Checklist

- [ ] Competitors identified across direct, indirect and adjacent layers (8–15 total), including at least one indirect substitute
- [ ] Threat ranking scored for every competitor; top 3–5 by total (or by known win/loss) deep-dived
- [ ] Deep dives cover website, SEO, AI visibility, paid, social, content, reviews; review themes reported as counts
- [ ] Paid activity checked in the relevant ad libraries with dates
- [ ] AI assistant recommendations for the category sampled or requested
- [ ] SWOT per deep-dived competitor with evidence and sources
- [ ] 4–6 market gaps, each quantified, with "why empty", an Evidence × Demand × Feasibility score and a priority
- [ ] Ad-library conclusions labelled as inferences, and "no ads" checked across libraries and regions
- [ ] Recommendations across positioning, channels, content, paid and messaging/experience
- [ ] Every figure carries an evidence tag ([OBS], [USER], [EST], [INF]); estimates name tool and date; no invented figures
- [ ] Research date and watchlist included
- [ ] Limitations and missing access stated
