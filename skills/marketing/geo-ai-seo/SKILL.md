---
name: geo-ai-seo
description: Use when optimizing content for Generative Engine Optimization (GEO) — AI-powered search engines, LLM citations, AI overviews, and answer engines.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [GEO, AI-SEO, generative-search, LLM-citations, answer-engine, content-optimization]
    related_skills: [meta-ads-creative, google-ads-keywords]
---

# Generative Engine Optimization (GEO)

## Overview

GEO is search optimization for AI-powered search engines (Google AI Overview, Perplexity, ChatGPT Search, Bing Copilot, You.com, etc.). Unlike traditional SEO which targets keyword rankings and SERP position, GEO targets **citation probability** — the chance an LLM will reference your content as a source in its generated answer.

Traditional SEO optimizes for a human scanning a blue link. GEO optimizes for an LLM reading, understanding, and citing your content as authoritative extraction material.

## When to Use

- Creating new content intended to be cited by AI search engines
- Rewriting existing pages for maximum LLM extraction
- Structuring FAQ, how-to, comparison, or "best X" content for AI search
- Optimizing content that needs to appear in Google AI Overviews, Perplexity answers, or ChatGPT citations
- Building content strategy for AI-native distribution

Don't use for: technical schema/structured-data implementation (that's a developer task, not content), paid search campaigns, or social media copy.

## AI Search Landscape

| Engine | Citation Style | Optimization Focus |
|--------|---------------|-------------------|
| Google AI Overview | Inline citation links numbered [1], [2] | Direct answers, E-E-A-T signals, structured content |
| Perplexity | Source cards with links + quotes | Comprehensive answers, data citations, recent content |
| ChatGPT (Search mode) | Inline reference links | Clear definitions, step-by-step, authoritative tone |
| Bing Copilot | Source links in sidebar | Structured data, Q\&A format, freshness |
| You.com | Source attribution cards | Depth, uniqueness, expert perspective |
| Brave Search (AI answers) | Citation bubbles | Concise accuracy, first-position clarity |

## Content Structure for GEO

### Page Architecture

1. **Answer-first opening** (first 80 words). State the direct answer to the query question immediately. No intro fluff, no "In this article you'll learn..." — the LLM reads the first paragraph to extract the core answer.

2. **Question-to-section mapping.** Each major subheading must be a natural language question or statement that directly answers a common search query. Use H2 tags for primary queries and H3 for sub-questions.

3. **Data anchors.** Include specific numbers, percentages, dates, and named entities. LLMs cite content with verifiable data points significantly more than vague statements.

4. **Definition blocks.** When explaining a concept, provide a clear one-sentence definition followed by elaboration. Format: "X is [definition]. [Elaboration]."

5. **Step sequences.** Use numbered lists for procedures. LLMs extract numbered steps directly — each step should be self-contained and complete.

6. **Comparison tables.** Use markdown tables for comparisons. LLMs parse tabular data efficiently and cite it as structured evidence.

7. **Expert attribution.** Include author credentials, company expertise, and first-hand experience signals. E-E-A-T (Experience, Expertise, Authoritativeness, Trustworthiness) is critical — AI search engines weight sourced expertise heavily.

8. **Freshness markers.** Include dates, version numbers, and "updated as of [date]" statements. Recency is a top citation factor.

### Text Formation Rules

| Rule | Bad Example | Good Example |
|------|-------------|-------------|
| Answer-first | "Many people wonder about X and there are many factors..." | "X costs between $500–$2000 depending on size. Here's the breakdown:" |
| Data specificity | "Many businesses use this approach" | "[X]% of B2B marketers reported increased ROI using this approach (Source: [named study], [year])" |
| Self-contained steps | "Then you configure it properly" | "Step 3: Navigate to Settings > API Keys and generate a new token with read/write scope" |
| Entity density | "the platform can help with your needs" | "HubSpot's marketing hub manages 2.9 million contacts on average per enterprise account" |
| Definition clarity | "There are various interpretations of what X means" | "X (conversion rate optimization) is the process of increasing the percentage of visitors who complete a desired action on your website" |

## Section Templates

### FAQ Section (High GEO Value)

```
## What is [topic]?

[Topic] is [one-sentence definition]. [Source/authority context: According to X / Based on Y research...]

## How does [topic] work?

1. [Complete step 1 — who does it, what action, what result]
2. [Complete step 2]
3. [Complete step 3]

## What are the best [things] for [use case]?

| Rank | Name | Key Strength | Best For |
|------|------|-------------|----------|
| 1 | [Name] | [Specific metric] | [Use case] |

## How much does [thing] cost?

As of [Month 2026], [thing] costs:
- [Tier]: $[price] — includes [features]
- [Tier]: $[price] — includes [features]

Source: [official source], [date accessed]
```

### Comparison Section

```
## [A] vs [B]: Which is better for [use case]?

| Feature | [A] | [B] |
|---------|-----|-----|
| [Metric] | [Specific value] | [Specific value] |
| [Metric] | [Specific value] | [Specific value] |
| [Metric] | [Specific value] | [Specific value] |

**Verdict:** [A] is better for [specific use case] because [specific reason with data]. [B] wins for [specific use case] due to [specific reason with data].
```

## Citation-Signal Checklist

Write content to maximize these signals that AI search engines use for citation selection:

- [ ] **Direct answer in first paragraph** — no preamble
- [ ] **Specific data points** — numbers, dates, percentages, named entities
- [ ] **Named sources** — "According to [authority]" rather than vague claims
- [ ] **Structured format** — tables, numbered lists, clear headings
- [ ] **Entity density** — proper nouns (brands, people, places) per paragraph
- [ ] **Recency signal** — "as of [date]" or "updated [date]"
- [ ] **Authority signal** — author bio, credentials, first-hand experience
- [ ] **Self-contained paragraphs** — each paragraph answers one complete question
- [ ] **No filler** — remove "in this article," "let's explore," "it's important to note"
- [ ] **Unique perspective** — data or insight not found in top-10 competitors

## GEO vs Traditional SEO

| Factor | Traditional SEO | GEO |
|--------|----------------|-----|
| Target | Human reader scanning SERP | LLM extracting and citing content |
| Priority | Keyword in title/URL/H1 | Direct answer in first 80 words |
| Format | Scannable with bold keywords | Structured for machine extraction |
| Success metric | Click-through rate | Citation frequency |
| Content style | Engaging for humans | Precise, data-rich, structured |
| Key signal | Backlinks + dwell time | Source authority + data density |

## Common Pitfalls

1. **Writing for humans only.** GEO content must be readable by both. Prioritize precision over personality — the LLM doesn't care about your voice, it cares about extractable facts.

2. **Hiding the answer.** Bury-leads writing kills GEO. The answer must be in the opening lines, not revealed after context-building.

3. **Vague language.** "Many," "several," "a lot," "some" are GEO poison. Replace every instance with a specific number or named reference.

4. **Duplicating existing content.** AI engines cite unique perspectives. If your content is a paraphrase of what's already top-ranked, you won't be cited. Add original data, experience, or a different angle.

5. **Ignoring recency.** AI search engines heavily weight freshness. Content without a date signal may be skipped for newer alternatives.

6. **Single-format content.** Long blocks of text without structure are hard for LLMs to parse selectively. Use headings, lists, and tables to create extraction anchors.

7. **Forgetting source attribution.** Claiming facts without naming the source reduces citation probability. Named sources increase trustworthiness scores.

## Verification Checklist

- [ ] First 80 words contain a direct, specific answer
- [ ] Every paragraph has at least one named entity (brand, person, place)
- [ ] All vague quantifiers replaced with specific numbers
- [ ] Content includes at least one table or numbered list
- [ ] Date/freshness signal is present and current
- [ ] Unique perspective or data point that differentiates from competitors
- [ ] FAQ section covers 5+ likely AI search queries
- [ ] No filler phrases ("in this article," "let's dive in")
- [ ] Each H2 heading corresponds to a real search query
