---
name: competitor-research
description: Use when researching competitors in a market — identifying direct, indirect and adjacent players, auditing their websites, SEO, paid ads (Google Ads Transparency Center, Meta Ad Library, TikTok and LinkedIn ad libraries), social presence, content strategy and how AI assistants describe them, then running SWOTs and finding actionable market gaps. Also use when someone asks "who are we really competing with", wants a competitive landscape brief, or needs whitespace for a positioning or launch. Don't use for financial due diligence, patent or IP analysis, or pricing models.
version: 1.1.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. Browsing greatly improves results (ad libraries, profiles, SERPs); without it the skill structures the research plan and works from data the user collects.
metadata:
  category: competitive-intelligence
  updated: 2026-10-02
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

## Research Workflow

### Phase 1: Competitor discovery (three layers)

| Layer | Definition | Where to find them |
|-------|-----------|--------------------|
| Direct | Same solution, same audience, same price tier | Search the core buying keywords in the locale; look at who advertises on them; "alternatives to X" lists; G2/Capterra/app-store categories |
| Indirect | Different solution to the same problem | Reddit, niche forums, LinkedIn groups: "how do you handle X"; agencies, in-house tools, spreadsheets, doing nothing |
| Adjacent / aspirational | Brands that share the audience and could expand into the category | Partnerships, co-marketing, who the audience also follows, platform ecosystems |

Target: 8–15 names across layers; deep-dive the top 5 by overlap with the brand's segment. Also ask two AI assistants "what are the best [category] for [segment] in [locale]" — their answer is now part of how buyers discover the set.

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

--- MARKET OVERVIEW ---
[1–2 paragraphs: maturity, saturation, dominant players, how buyers discover (search, AI, social, referral)]

--- COMPETITOR TABLE ---
| # | Name | Layer | Website | Position | Key strength | Key weakness | Main channels | Paid active? |

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
1. [Type] — [Evidence] — [Action] — [Feasibility for the brand]
2. [..]
3. [..]

--- STRATEGIC RECOMMENDATIONS ---
1. Positioning: [..]
2. Channels: [..]
3. Content: [..]
4. Paid: [..]
5. Messaging / experience: [..]

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

8. **Invented numbers.** Traffic and spend estimates from tools are estimates. Say so, with the tool and date.

## Verification Checklist

- [ ] Competitors identified across direct, indirect and adjacent layers (8–15 total)
- [ ] Top 3–5 deep-dived across website, SEO, AI visibility, paid, social, content, reviews
- [ ] Paid activity checked in the relevant ad libraries with dates
- [ ] AI assistant recommendations for the category sampled or requested
- [ ] SWOT per deep-dived competitor with evidence and sources
- [ ] 4–6 market gaps, each quantified and feasibility-checked
- [ ] Recommendations across positioning, channels, content, paid and messaging/experience
- [ ] Estimates labelled with tool and date; no invented figures
- [ ] Research date and watchlist included
- [ ] Limitations and missing access stated
