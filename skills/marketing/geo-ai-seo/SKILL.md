---
name: geo-ai-seo
description: Use when optimizing content to be cited by AI search and answer engines — Google AI Overviews and AI Mode, ChatGPT search, Perplexity, Gemini, Copilot and Claude — through Generative Engine Optimization (GEO). Covers answer-first structure, data anchors, source attribution, entity clarity, FAQ and comparison templates, AI-crawler access and measuring AI referrals. Also use when someone asks about "AEO", "LLM SEO", "showing up in ChatGPT", "AI Overviews" or "why AI doesn't mention our brand". Don't use for paid search keywords (google-ads-keywords), social copy, or landing page conversion (landing-page-funnel).
version: 1.2.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. No tools required; browsing helps for checking robots.txt and live AI answers but is optional.
metadata:
  category: conversion-tracking
  updated: 2026-11-17
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

- `robots.txt` allows the **search and user-fetch** agents you want, and decides separately about **training** agents. Blocking training does not have to block search:

| Operator | Search / answer retrieval | User-initiated fetch | Model training |
|----------|---------------------------|----------------------|----------------|
| OpenAI | `OAI-SearchBot` | `ChatGPT-User` | `GPTBot` |
| Perplexity | `PerplexityBot` | `Perplexity-User` | — |
| Anthropic | `Claude-SearchBot` | `Claude-User` | `ClaudeBot` |
| Google | `Googlebot` (AI Overviews and AI Mode use the normal Search crawl) | — | `Google-Extended` (a control token; blocking it does not remove pages from AI Overviews) |
| Microsoft | `Bingbot` | — | — |
| Common Crawl | — | — | `CCBot` |

  Example for "cite us, don't train on us": `User-agent: GPTBot` / `Disallow: /` and the same for `ClaudeBot`, `Google-Extended` and `CCBot`, while `OAI-SearchBot`, `Claude-SearchBot`, `PerplexityBot`, `Googlebot` and `Bingbot` stay allowed. Operators add and rename agents; confirm names against each operator's current crawler documentation before shipping.
- CDN/WAF (Cloudflare and similar) is not challenging or rate-limiting those agents.
- No `noindex`, `nosnippet` or `max-snippet:0` on pages you want cited.
- Key content is server-rendered HTML, not injected by JavaScript after load.
- Pages are indexed in Google and Bing (AI Overviews and Copilot only cite indexed pages).
- Basic schema.org markup present where it fits: `Article` with `author` and `dateModified`, `FAQPage`, `HowTo`, `Product` with `offers`, `Organization` with `sameAs` links to official profiles.
- `llms.txt` is an unproven convention; harmless to add, do not expect ranking effects, and Google has said it does not use it.

## Why Are We Not Cited? (diagnostic order)

Work through the layers in order and stop at the first one that fails — fixing content does nothing if the engine cannot read the page, and new pages do nothing if the brand is unknown as an entity.

| Layer | Test | If it fails | Fix |
|-------|------|-------------|-----|
| 1. Access | robots.txt, WAF logs/settings, `noindex`/`nosnippet`, rendered HTML without JavaScript | Engine cannot fetch or quote the page | Technical Access Checklist |
| 2. Index | `site:` / URL inspection in Google Search Console and Bing Webmaster Tools | Not in the index the engine draws on | Fix indexing, sitemaps, internal links; submit to Bing |
| 3. Passage match | Does one section answer the exact question (and each fan-out sub-question) in its first 40–80 words? | Page is about the topic but has no liftable answer | Answer-first rewrite, question H2s, fan-out map |
| 4. Evidence | Does the passage carry numbers, dates, named sources or original data the competitor lacks? | Competitor's passage is more specific | Data anchors, attribution, original contribution |
| 5. Entity | Do engines describe the brand correctly when asked directly ("What is [Brand]?")? | Brand unknown or confused with another | Brand entity block, `Organization` schema with `sameAs`, consistent names across profiles, Wikidata where eligible |
| 6. Third-party presence | Unaided prompt ("best [category] for [segment]"): which domains are cited? | Citations come from review sites, Reddit, YouTube or directories where the brand is absent | Earn presence on those sources (reviews, genuine community answers, listings, videos) |

Mentioned but not linked → the entity is known but no page of yours wins the passage: work layers 3–4. Linked for brand queries but absent for category queries → work layers 5–6.

### Query fan-out map

AI Mode and other engines split a question into sub-queries. For each target question, list the 3–6 sub-questions a complete answer needs (cost, steps, comparison, eligibility, risks, alternatives) and map each to one self-contained section. A sub-question without a section is a passage a competitor will supply.

### Page type → template

| Query intent | Page type | Template to use |
|--------------|-----------|-----------------|
| "What is / how does" | Explainer or glossary | Definition block + numbered steps |
| "How much / pricing" | Pricing guide | Dated price table + "as of" + drivers |
| "[A] vs [B]" / "alternatives to" | Comparison page | Comparison block with verdict per use case |
| "Best [X] for [segment]" | Category or roundup page | Option table with "best for" + selection criteria + honest inclusion of competitors |
| "[Brand] reviews / is [Brand] legit" | About, proof, third-party reviews | Brand entity block + linked review profiles |
| Local / service ("near me", city) | Service page | FAQ block with hours, prices, location facts + `LocalBusiness` schema |

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
- **Citation log**: answers vary between runs, users and days. Run each question at least 3 times per engine (fresh session, no personalisation where possible) and record each run, not just the best one. Citation rate = runs where the brand is cited ÷ runs checked. Compare against the user's own baseline month, not a market benchmark.
- **Brand mention tracking**: prompts that describe the category without the brand name ("best [category] for [segment]") test unaided recall in the model.

## Output Format

Use every heading below in this order (for a pure writing request such as an FAQ block, `REWRITTEN SECTIONS`, `ASSUMPTIONS & PLACEHOLDERS` and a short `TECHNICAL ACCESS` note are enough). Never put an unverified number in rewritten copy; use `[add verified stat + source]`.

```
GEO AUDIT / BRIEF: [Page or topic]
Target questions: [list]
Engines checked: [engine — date — runs per question, or "not checked: no browsing / no screenshots"]
Currently cited: [domains/brands, or "unknown"]

--- DIAGNOSIS ---
Failing layer: [1 Access / 2 Index / 3 Passage match / 4 Evidence / 5 Entity / 6 Third-party] — [evidence]
Status per layer: Access [pass/fail/unknown] | Index [..] | Passage [..] | Evidence [..] | Entity [..] | Third-party [..]

--- TECHNICAL ACCESS ---
[robots.txt per agent: allow/block → recommended | WAF | indexing | rendering | snippet directives | schema]
robots.txt changes: [exact lines, or "none needed"]

--- STRUCTURE ---
Answer-first opening: [present / rewrite]
Fan-out map: [target question → sub-questions → section that answers each, or "missing"]
H2 question mapping: [current → recommended]
Lists / tables: [where to add]

--- CONTENT ---
Data anchors to add: [facts needed, with `[add verified stat + source]` placeholders]
Attribution gaps: [claims needing sources]
Entity clarity: [name consistency, schema]
Original contribution: [what unique data/perspective to add]
Freshness: [what to update, how to date it]
Third-party surfaces: [which sources the engines cite in this category → presence plan]

--- REWRITTEN SECTIONS ---
[Answer-first opening, FAQ block, comparison block as applicable]

--- MEASUREMENT PLAN ---
GA4: [AI referral channel/segment with source list]
Citation log: Question | Engine | Run | Mentioned (y/n) | Cited with link (y/n) | Recommended (y/n) | Cited instead
Baseline: [date, citation rate] | Review: [monthly]
Search Console: [question-query view]

--- PRIORITY ACTIONS ---
1. [Action] — Layer: [n] — Effort: [low/med/high] — Owner: [..]
2. [...]
3. [...]

--- ASSUMPTIONS & PLACEHOLDERS ---
[Unverified facts, placeholders to fill, data not provided]
```

## Common Pitfalls

1. **Writing for the model only.** Humans still read the page and convert. Fix: keep precision and readability together; test the rewrite on a human reader too.

2. **Burying the answer.** Context-building intros push the extractable passage down. Fix: answer in the first 40–80 words, then explain.

3. **Vague quantifiers.** "Many", "several", "a lot" give the engine nothing to quote. Fix: replace with a number, range or named entity, or delete.

4. **Fabricated data anchors.** An invented statistic that gets cited is a liability. Fix: `[add verified stat + source]` placeholder and a note on who verifies it.

5. **Blocking the bots you want.** Teams block training agents and accidentally block search agents (or a WAF challenges them). Fix: decide per agent using the operator table and check WAF bot rules.

6. **Skipping the diagnostic order.** Rewriting content for a page that is not indexed or is blocked changes nothing. Fix: work layers 1–6 in order and stop at the first failure.

7. **Duplicating the top results.** Engines favour pages that add something. Fix: original data, a survey, a benchmark or a distinct decision framework.

8. **Fake freshness.** Bumping the date without changing content is noticed when the facts are stale. Fix: change dates and `dateModified` only with real updates.

9. **Judging from one run.** A single answer is a sample of one; the next run may differ. Fix: 3+ runs per question per engine, logged, compared with the user's own baseline.

10. **Treating `llms.txt` or schema as a ranking switch.** Neither makes an unhelpful page citable. Fix: add them as hygiene after access, passages and evidence are right.

11. **Ignoring third-party surfaces.** If Reddit, YouTube and review sites carry most citations in your category, being absent there caps your GEO ceiling. Fix: a presence plan for the cited sources, with genuine contributions rather than spam.

## Verification Checklist

- [ ] Diagnosis names the first failing layer (Access → Index → Passage → Evidence → Entity → Third-party) with evidence or "unknown"
- [ ] Technical access checked per agent: search, user-fetch and training agents decided separately; WAF, indexing, rendering, snippet directives
- [ ] First 40–80 words of the page and of each H2 give the direct answer
- [ ] Each H2/H3 is a real question or statement users search for; fan-out sub-questions mapped to sections
- [ ] Every paragraph names at least one entity (brand, person, place, product)
- [ ] Vague quantifiers replaced; data anchors either verified with sources or marked as placeholders
- [ ] At least one table or numbered list where a comparison or procedure exists
- [ ] Author/experience signals and an honest updated date present
- [ ] One original contribution identified that competitors lack
- [ ] Brand entity facts consistent with schema and official profiles
- [ ] Measurement plan covers AI referrals, a multi-run citation log with baseline, and Search Console
- [ ] Engines, dates and runs of the citation check recorded, or stated as not checked
