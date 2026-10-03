---
name: geo-ai-seo
description: Use when optimizing content to be cited by AI search and answer engines — Google AI Overviews and AI Mode, ChatGPT search, Perplexity, Gemini, Copilot and Claude — through Generative Engine Optimization (GEO). Covers answer-first structure, data anchors, source attribution, entity clarity, FAQ and comparison templates, AI-crawler access and measuring AI referrals. Also use when someone asks about "AEO", "LLM SEO", "showing up in ChatGPT", "AI Overviews" or "why AI doesn't mention our brand". Don't use for paid search keywords (google-ads-keywords), social copy, or landing page conversion (landing-page-funnel).
version: 1.1.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. No tools required; browsing helps for checking robots.txt and live AI answers but is optional.
metadata:
  category: conversion-tracking
  updated: 2026-10-02
  tags: [geo, ai-seo, aeo, generative-search, llm-citations, ai-overviews, ai-mode, answer-engine, content-optimization, structured-content]
  related_skills: [market-positioning, competitor-research, landing-page-funnel, youtube-organic]
---

# Generative Engine Optimization (GEO)

## Overview

GEO is optimization for AI-generated answers. Traditional SEO targets a ranking; GEO targets **citation probability** — the chance that an LLM-based engine pulls a passage from your page and names you as a source or recommends your brand. The engines read, chunk and extract; the winning content is answer-first, specific, attributed, fresh, crawlable and about clearly identified entities. This skill structures, rewrites and audits content for that, and tells you how to check whether it worked.

## When to Use

- Creating or rewriting pages that should be cited in AI answers
- Structuring FAQ, how-to, comparison, pricing or "best X" content
- Auditing why competitors appear in AI answers and you do not
- Checking technical access for AI crawlers and search bots
- Setting up measurement for AI referral traffic and brand mentions

Don't use for: Google Ads keyword work (use `google-ads-keywords`), social media copy, landing page CRO (use `landing-page-funnel`), or deep schema markup engineering beyond the basics listed here.

## Inputs

Ask for (or extract from the conversation):

- **Target queries / questions** the content should answer, in the user's words
- **The page or draft** (URL or text) and its purpose (inform, compare, sell)
- **Proof assets**: original data, customer numbers, studies, expert authors
- **Entity facts**: exact brand/product names, category, founding facts, locations, pricing
- **Competitors** that currently get cited (if known) or the AI answers the user has seen
- **Access** to robots.txt, CDN/WAF settings and analytics, or someone who has it

Data rules: never fabricate statistics, studies or quotes to "add data anchors" — insert `[add verified stat + source]` placeholders and explain. If you can browse, test the target query in at least two engines and report what they cite; if you cannot, ask the user for screenshots of the answers. Engine behaviour changes monthly; treat the landscape table as a snapshot dated by `metadata.updated`.

## AI Search Landscape (snapshot)

| Engine | How it sources | What it rewards |
|--------|---------------|-----------------|
| Google AI Overviews / AI Mode | Google's index; AI Mode runs several sub-queries ("fan-out") and stitches passages | Pages already indexed and crawlable, passages that answer one sub-question completely, E-E-A-T signals, freshness |
| ChatGPT (search) | Live web via OAI-SearchBot plus Bing-derived index | Clear definitions, step lists, named sources, recently updated pages |
| Perplexity | Own crawler (PerplexityBot) and live search | Dense facts, numbers, recent dates, comparison tables |
| Gemini | Google index | Same as AI Overviews; strong on structured, entity-rich content |
| Microsoft Copilot | Bing index | Structured Q&A, schema markup, freshness |
| Claude (web search) | Partner search index plus live fetch | Precise, well-attributed passages; readable HTML |

Common pattern across engines: a handful of large domains (Reddit, Wikipedia, YouTube, major publishers, review platforms) take a large share of citations. Being present on those — answering in relevant Reddit threads, maintaining accurate Wikipedia/Wikidata facts, publishing on YouTube — is part of GEO, not only your own pages.

## Technical Access Checklist

Content cannot be cited if the engine cannot read it.

- `robots.txt` allows the **search** agents you want: `OAI-SearchBot`, `PerplexityBot`, `ClaudeBot`/`Claude-SearchBot`, `Googlebot`, `Bingbot`. Decide separately about **training** agents (`GPTBot`, `Google-Extended`, `CCBot`, `anthropic-ai`); blocking training does not have to block search.
- CDN/WAF (Cloudflare and similar) is not challenging or rate-limiting those agents.
- No `noindex`, `nosnippet` or `max-snippet:0` on pages you want cited.
- Key content is server-rendered HTML, not injected by JavaScript after load.
- Pages are indexed in Google and Bing (AI Overviews and Copilot only cite indexed pages).
- Basic schema.org markup present where it fits: `Article` with `author` and `dateModified`, `FAQPage`, `HowTo`, `Product` with `offers`, `Organization` with `sameAs` links to official profiles.
- `llms.txt` is an unproven convention; harmless to add, do not expect ranking effects, and Google has said it does not use it.

## Content Structure for GEO

1. **Answer first.** The first 40–80 words under the title (and under each H2) state the direct answer. No throat-clearing.
2. **One question per section.** H2/H3 headings are the questions people ask, phrased naturally. Each section is self-contained so it can be lifted as a passage.
3. **Data anchors.** Numbers, dates, ranges, named entities. "Costs 500–2,000 EUR depending on X (as of Sept 2026)" beats "costs vary".
4. **Attribution.** "According to [named source], [year]" — link it. Engines weigh sourced claims; unsourced claims look like opinion.
5. **Definition blocks.** "X is [one-sentence definition]. [elaboration]."
6. **Lists and tables for procedures and comparisons.** Numbered steps are extracted verbatim; tables are parsed as structured evidence.
7. **Entity clarity.** Use the full brand/product name on first mention in each section; keep names consistent with your Organization schema and official profiles.
8. **Author and experience signals.** Byline with credentials, first-hand observations ("we tested 12 units for 30 days"), an updated date that is true.
9. **Freshness.** Update facts, change the visible "Updated" date only when content actually changed, and keep `dateModified` honest.
10. **Original contribution.** Something not on competing pages: your data, a survey, a benchmark, a decision framework. Paraphrases of the top results do not get cited.

### Text formation rules

| Rule | Weak | Strong |
|------|------|--------|
| Answer-first | "Many factors influence the cost of X…" | "X costs 500–2,000 EUR; the main driver is Y. Breakdown:" |
| Specificity | "Many businesses see better ROI" | "[n]% of surveyed B2B teams reported higher ROI ([source], [year])" |
| Self-contained step | "Then configure it" | "Step 3: Settings → API keys → Create key with read/write scope" |
| Entity density | "the platform helps with this" | "[Brand]'s [Product] handles [specific capability] for [segment]" |
| Definition | "There are various views on X" | "X is [definition]. In practice it means [elaboration]." |
| No filler | "In this article we will explore…" | Delete; start with the answer |

## Section Templates

### FAQ block

```
## What is [topic]?
[Topic] is [one-sentence definition]. [Two sentences of elaboration with one named source.]

## How does [topic] work?
1. [Complete step — who, what, result]
2. [...]
3. [...]

## How much does [thing] cost?
As of [Month Year], [thing] costs:
- [Tier]: [price] — [what is included]
- [Tier]: [price] — [what is included]
Source: [official page], accessed [date].

## What are the best [things] for [use case]?
| Option | Best for | Key fact |
|--------|----------|----------|
| [Name] | [use case] | [specific metric] |
```

### Comparison block

```
## [A] vs [B]: which is better for [use case]?
| Criterion | [A] | [B] |
|-----------|-----|-----|
| [Metric]  | [value] | [value] |
| [Metric]  | [value] | [value] |

**Verdict:** [A] suits [use case] because [specific reason + data]. [B] wins for [use case] because [specific reason + data].
```

### Brand entity block (About / homepage)

```
[Brand] is a [category] for [who], founded [year] in [place]. It [one-sentence differentiator with a number]. [Brand] is used by [n] [customers] including [named examples].
```

## Measurement

- **AI referrals in GA4**: create a channel or segment for sessions whose source contains `chatgpt.com`, `perplexity.ai`, `copilot.microsoft.com`, `gemini.google.com`, `claude.ai`. Expect small volumes with high intent.
- **Citation checks**: monthly, run the 10–20 target questions in each engine (manually or with a monitoring tool) and log whether the brand is mentioned, cited (linked) or recommended, and which competitor passages are used instead.
- **Google Search Console**: AI Overview impressions are included in Search performance; watch impressions-without-clicks on question queries.
- **Brand mention tracking**: prompts that describe the category without the brand name ("best [category] for [segment]") test unaided recall in the model.

## Output Format

```
GEO AUDIT / BRIEF: [Page or topic]
Target questions: [list]
Engines checked: [which, date] | Currently cited: [who]

--- TECHNICAL ACCESS ---
[robots.txt / WAF / indexing / rendering / schema findings → fixes]

--- STRUCTURE ---
[Answer-first opening: present / rewrite]
[H2 question mapping: current → recommended]
[Lists / tables: where to add]

--- CONTENT ---
Data anchors to add: [facts needed, with `[add verified stat + source]` placeholders]
Attribution gaps: [claims needing sources]
Entity clarity: [name consistency, schema]
Original contribution: [what unique data/perspective to add]
Freshness: [what to update, how to date it]

--- REWRITTEN SECTIONS ---
[Answer-first opening, FAQ block, comparison block as applicable]

--- MEASUREMENT PLAN ---
[GA4 segment, monthly citation check list, Search Console view]

--- PRIORITY ACTIONS ---
1. [...]
2. [...]
3. [...]
```

## Common Pitfalls

1. **Writing for the model only.** Humans still read the page and convert. Precision and readability are compatible; dullness is not required.

2. **Burying the answer.** Context-building intros push the extractable passage below the fold of the model's attention. Answer, then explain.

3. **Vague quantifiers.** "Many", "several", "a lot" are replaced with numbers or removed.

4. **Fabricated data anchors.** An invented statistic that gets cited is a liability. Placeholder and verify.

5. **Blocking the bots you want.** Teams block `GPTBot` for training and accidentally block `OAI-SearchBot`. Separate the decisions.

6. **Duplicating the top results.** Engines favour pages that add something. Bring original data or a distinct framework.

7. **Fake freshness.** Bumping the date without changing content is noticed when the facts are stale.

8. **Ignoring third-party surfaces.** If Reddit, YouTube and review sites carry most citations in your category, being absent there caps your GEO ceiling.

## Verification Checklist

- [ ] Technical access checked: robots.txt agents, WAF, indexing, rendering, snippet directives
- [ ] First 40–80 words of the page and of each H2 give the direct answer
- [ ] Each H2/H3 is a real question or statement users search for
- [ ] Every paragraph names at least one entity (brand, person, place, product)
- [ ] Vague quantifiers replaced; data anchors either verified with sources or marked as placeholders
- [ ] At least one table or numbered list where a comparison or procedure exists
- [ ] Author/experience signals and an honest updated date present
- [ ] One original contribution identified that competitors lack
- [ ] Brand entity facts consistent with schema and official profiles
- [ ] Measurement plan covers AI referrals, citation checks and Search Console
- [ ] Engines and date of the citation check recorded
