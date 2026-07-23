---
name: competitor-research
description: Use when researching competitors in a given market — identify key players, analyze their digital presence, strengths, weaknesses, content strategy, ad spend, and find actionable market gaps.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [competitor-research, market-analysis, competitive-intelligence, gap-analysis, positioning, SEO-competition]
    related_skills: [geo-ai-seo, instagram-organic, linkedin-organic, youtube-organic, pinterest-organic, google-ads-diagnostics]
---

# Competitor Research

## Overview

Identify and analyze competitors in a specific market segment and locale. Produces a structured competitive landscape with each competitor's digital footprint, content strategy, ad presence, strengths, weaknesses, and — most importantly — **actionable gaps** your client or brand can exploit.

## When to Use

- Market entry research for a new product, service, or campaign
- Competitive analysis to inform positioning and messaging
- Identifying content or distribution gaps in the market
- Preparing a competitive brief for a marketing strategy
- Auditing ad space: what competitors are spending on and where

The input is always:
- **Market/locale** (e.g., "SaaS marketing tools in the US")
- **Segment** (e.g., "mid-market", "luxury", "DTC activewear")
- **Optional:** list of known competitors if the user already has some

Don't use for: due diligence / financial competitive analysis, patent IP analysis, or pricing strategy modeling.

## Research Workflow

### Phase 1: Competitor Discovery

Identify the competitive set in layers:

#### Layer 1: Direct Competitors
Same product/service, same target audience, same price segment.

**Discovery methods:**
- Google the primary use-case keywords in the target locale
- Check Google Ads transparent reporting for active advertisers
- Check Meta Ad Library for brands advertising in the segment
- Search LinkedIn, Instagram, YouTube for brands posting about the niche
- Review industry reports and "top X alternatives" blog posts

#### Layer 2: Indirect Competitors
Different product/service, same customer problem, same audience.

**Discovery methods:**
- "Alternative to [direct competitor]" searches
- Browse Reddit, LinkedIn groups, industry forums for "what tools do you use for X"
- Check G2, Capterra, ProductHunt for categories

#### Layer 3: Adjacent / Aspirational
Brands in different segments that could expand into yours or already cross-pollinate audiences.

**Discovery methods:**
- Check social media followers overlap between direct competitors
- Browse brand partnerships and sponsorship mentions

**Target:** Identify 8-15 competitors total, then focus deep-dive on the top 5.

### Phase 2: Digital Presence Audit

For each of the top 5 competitors, document:

| Channel | Metric to Capture | Tool / Method |
|---------|------------------|---------------|
| **Website** | Traffic estimate (monthly), top pages, content volume, design quality | SEMrush / SimilarWeb (if available), manual browse |
| **SEO** | Domain authority, top-ranking keywords, organic traffic share | Manual Google search for core keywords, check position |
| **Google Ads** | Active ads? Search keywords? Display? Video? | Search target keywords and note ad presence |
| **Meta Ads** | Active campaigns? Creative style? Target audience signals? | Meta Ad Library (facebook.com/ads/library) — search competitor name |
| **TikTok** | Organic presence? Ad presence? Content style? | TikTok search + TikTok Ad Library |
| **Instagram** | Followers, posts/month, engagement rate, content mix | Manual profile visit |
| **LinkedIn** | Followers (page) / Connections (personal), posting frequency, content type | Manual page visit |
| **YouTube** | Subscribers, video count, upload frequency, top videos | Manual channel visit |
| **Pinterest** | Followers, monthly impressions, board structure, pin frequency | Manual profile visit |
| **Social overall** | Which platforms are they investing in vs. ignoring? | Cross-reference all above |

### Phase 3: Content Strategy Analysis

| Dimension | Questions |
|-----------|-----------|
| **Content pillars** | What 3-5 topics/categories dominate their content? |
| **Content format** | Heavy on video, long-form writing, image? |
| **Tone & voice** | Corporate, casual, edgy, educational, inspirational? |
| **Publication consistency** | Daily, 3x/week, sporadic? |
| **Signature content** | Do they have a recognizable recurring series or format? |
| **Content quality** | High production value or scrappy/authentic? |
| **Distribution** | Do they cross-promote across platforms or silo by channel? |

### Phase 4: Ad Strategy Analysis

| Question | Where to Investigate |
|----------|---------------------|
| Are they running paid ads? | Meta Ad Library, Google Ads transparency, TikTok Creative Center |
| How much creative variation do they have? | Count of unique ads in their ad library |
| What angles do they use? | Problem→solution, social proof, direct offer, educational? |
| Who are they targeting? | Inferred from ad copy, creative style, audience targeting language |
| What offers do they lead with? | Free trial, demo, lead magnet, discount, direct purchase? |
| How often do they refresh creative? | Date range of ads in libraries |

### Phase 5: SWOT per Competitor

For each of the top 5:

```
COMPETITOR: [Name]
Website: [URL]
Market Position: [Brief — e.g., "Premium, direct-to-consumer, US/EU"]

STRENGTHS:
- [Specific strength 1 — e.g., "Highest organic traffic in niche (200K/mo)"]
- [Specific strength 2]

WEAKNESSES:
- [Specific weakness 1 — e.g., "No Meta ad presence, 0 TikTok following"]
- [Specific weakness 2]

OPPORTUNITIES (for them / gaps):
- [e.g., "Not targeting [locale/language]"]
- [e.g., "Low engagement on Instagram despite 50K followers"]

THREATS (to them):
- [e.g., "Newer competitor X growing 3× faster on TikTok"]
```

### Phase 6: Market Gap Analysis

The most valuable output. Identify what's **not** being done in the market — the whitespace your strategy can claim.

| Gap Category | What to Look For | Example |
|-------------|-----------------|---------|
| **Channel gaps** | Platforms no competitor is using or using poorly | "No competitor uses YouTube consistently. All are Instagram-focused." |
| **Content format gaps** | Formats competitors aren't using | "All competitors do polished video. Nobody does carousel or document content on LinkedIn." |
| **Audience gaps** | Demographics or segments being ignored | "All competitors target enterprise. Mid-market (10-50 employees) has no dedicated content." |
| **Locale/language gaps** | Geographic or language underserved | "No competitor produces Spanish-language content despite 15% Spanish-speaking audience." |
| **Tone/voice gaps** | Brand personalities not present | "All competitors are corporate/formal. A founder-led, personal brand angle is open." |
| **Offer/message gaps** | Angles or messaging not being used | "Every competitor leads with 'AI-powered.' Nobody leads with 'human-first.'" |
| **Price/positioning gaps** | Price points or tiers missing | "All offerings are $50+/month. A free-tier or freemium model could capture top-funnel." |
| **Educational gap** | Topics nobody covers | "No competitor has comprehensive beginner content. All assume mid-level expertise." |

### Phase 7: Strategic Recommendations

Based on gaps, recommend 3-5 actionable strategic moves:

| Recommendation Type | Output |
|--------------------|--------|
| **Positioning** | "Position as the [differentiator] alternative to [top competitor's positioning]" |
| **Channel strategy** | "Go all-in on [under-served channel] where no competitor has strong presence" |
| **Content format** | "Lead with [gap format] — every competitor uses [weak format]" |
| **Ad strategy** | "Run [ad type] ads in [locale] where no competitor is buying" |
| **Messaging** | "Lead with [gap message] — all competitors lead with [overused message]" |

## Output Format

```
COMPETITIVE LANDSCAPE: [Market / Segment / Locale]
Date: [Research Date]
Competitors Analyzed: [Number]

--- MARKET OVERVIEW ---
[1-2 paragraphs: size, saturation level, level of competition, dominant players]

--- COMPETITOR TABLE ---

| Rank | Name | Website | Key Strength | Key Weakness | Primary Channels |
|------|------|---------|-------------|-------------|-----------------|
| 1 | [Name] | [URL] | [Brief] | [Brief] | [Platforms] |

--- DEEP DIVE: [Competitor 1 — Top player] ---
WEBSITE: [Traffic, design, offer]
SEO: [Top keywords, organic strength]
ADS: [Active? Google/Meta/TikTok? Creative style?]
SOCIAL:
  Instagram: [Followers X | ER Y% | Content mix]
  LinkedIn: [Followers X | Frequency | Content type]
  YouTube: [Subs X | Uploads/month | Top content]
  TikTok: [Followers X | Content style]
  Pinterest: [Followers X | Pins/month]
CONTENT PILLARS: [List 3-5]
TONE: [Description]

SWOT:
  Strengths: [...]
  Weaknesses: [...]
  Opportunities: [...]
  Threats: [...]

[Repeat for top 3-5 competitors]

--- MARKET GAPS (Actionable whitespace) ---

1. [Gap type] — [Description] — [Recommended action]
2. [Gap type] — [Description] — [Recommended action]
3. [Gap type] — [Description] — [Recommended action]

--- STRATEGIC RECOMMENDATIONS ---

1. POSITIONING: [Recommendation]
2. CHANNELS: [Recommendation]
3. CONTENT: [Recommendation]
4. ADS: [Recommendation]
5. MESSAGING: [Recommendation]
```

## Common Pitfalls

1. **Only looking at direct competitors.** The biggest threat often comes from indirect competitors solving the same problem differently. Always research all three layers.

2. **Judging competitors by follower count only.** A competitor with 50K engaged followers is stronger than one with 200K ghost followers. Always check engagement rate.

3. **Missing Meta/TikTok ad libraries.** Competitors may look small on organic but are spending heavily on paid. Ad libraries (Meta Ad Library, TikTok Creative Center) reveal this instantly.

4. **Looking at a snapshot, not trends.** Take a 30-60 day view when possible. A competitor that was ad-heavy 60 days ago and has suddenly stopped tells a story.

5. **Not quantifying gaps.** "They don't do YouTube much" is weak. "Top 5 competitors average 80 subscribers between them" is actionable — it means YouTube is wide open.

6. **Recommending things the client can't execute.** A gap in TikTok is only useful if the client has the team and appetite for video content. Flag feasibility.

7. **Too many competitors.** Deep-diving 15+ competitors produces noise. Pick top 5 and use the rest as a landscape table.

## Verification Checklist

- [ ] At least 3 layers of competitors identified (direct, indirect, adjacent)
- [ ] Top 5 competitors deep-dived with full digital presence audit
- [ ] Ad presence checked via Meta Ad Library, Google Ads transparency, TikTok Creative Center
- [ ] All major social channels assessed for each competitor
- [ ] Content pillars and tone identified for each deep-dived competitor
- [ ] SWOT completed for top 5 competitors
- [ ] At least 4-6 actionable market gaps identified with type and recommended action
- [ ] Strategic recommendations provided across positioning, channels, content, ads, and messaging
- [ ] Recommendations include feasibility consideration
- [ ] Date of research noted (competitor data is time-sensitive)
