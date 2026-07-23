---
name: google-ads-keywords
description: Use when generating keyword lists for Google Ads campaigns. Always outputs exact match ("keyword") or phrase match ([keyword]) — never broad match, never bullet points.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [google-ads, keywords, exact-match, phrase-match, search-ads, ppc]
    related_skills: [meta-ads-creative, geo-ai-seo]
---

# Google Ads Keyword Lists

## Overview

Generate structured keyword lists for Google Ads search campaigns using only exact match and phrase match operators. Every keyword is formatted with proper match-type syntax — no broad match, no bullet points, and always machine-ready for direct copying into Google Ads.

## When to Use

- Building keyword lists for Google Ads search campaigns
- Expanding keyword research from a seed topic or product
- Creating negative keyword lists
- Organizing keywords into tightly themed ad groups
- Preparing keyword sets for a new Google Ads account

Don't use for: SEO keyword research (use `geo-ai-seo`), shopping campaigns, or display audience targeting.

## Match Types

Only two match types are used:

| Match Type | Syntax | Behavior |
|-----------|--------|----------|
| **Exact Match** | `"keyword"` | Matches the keyword or close variants (misspellings, plurals, reordering, removed stop words) with the same intent |
| **Phrase Match** | `[keyword]` | Contains the keyword or close variants with the same intent. Can have additional words before or after |

**Never use broad match** (no quotes or brackets). Broad match wastes budget on irrelevant traffic and destroys campaign quality score.

## Output Format

All keywords are output as comma-separated values. Each keyword is wrapped in its match-type delimiters. No bullet points, no numbering, no line breaks between keywords within a group.

```
"exact match keyword", "another exact", [phrase match keyword], [another phrase]
```

### Ad Group Structure

When organizing by ad group, output:

```
AD GROUP: [Ad Group Name]
"exact 1", "exact 2", [phrase 1], [phrase 2]
```

### Negative Keywords

```
NEGATIVE KEYWORDS:
"free", "cheap", "jobs", "login", [free trial], [open position]
```

## Keyword Research Process

### 1. Seed Extraction

From the product/service, extract core seed terms representing the primary intent.

### 2. Variations

For each seed, generate:

- **Synonyms:** "shoes", "footwear", "sneakers"
- **Commercial intent modifiers:** "buy [product]", "[product] near me", "[product] store"
- **Transactional modifiers:** "[product] price", "[product] deal", "[product] discount"
- **Question-based for phrase match:** [what is [product]], [how to choose [product]]
- **Brand-adjacent:** "[competitor] alternative", "[competitor] vs [your brand]"
- **Long-tail specific:** "[product] for [use case]", "[product] with [feature]"

### 3. Quality Filtering

Exclude keywords that:

- Have no commercial intent (informational only, unless that's the campaign goal)
- Are too broad (single generic word, use phrase or exact instead)
- Conflict with brand positioning
- Target a different product/use case than the campaign

### 4. Grouping

Organize into tightly themed ad groups (5-20 keywords each). Each ad group should match a specific ad variation and landing page.

Ad group naming convention: `[product]-[modifier]-[location-if-relevant]`

### 5. Match Type Assignment

Use this decision framework:

| Intent | Match Type | Example |
|--------|-----------|---------|
| High-intent commercial | Exact | "buy running shoes online" |
| Commercial with variation | Phrase | [buy running shoes] |
| Brand-specific | Exact | "[brand] running shoes" |
| Long-tail specific | Exact | "waterproof running shoes for trail" |
| Broader search patterns | Phrase | [running shoes for wide feet] |
| Competitor comparison | Exact | "[brand] vs [competitor]" |

## Keyword Density Rules

| Campaign Type | Exact Match % | Phrase Match % | Max Keywords/Ad Group |
|--------------|--------------|----------------|----------------------|
| Bottom-funnel conversion | 80% | 20% | 10 |
| Middle-funnel consideration | 50% | 50% | 15 |
| Top-funnel awareness | 20% | 80% | 20 |
| Retargeting | 90% | 10% | 10 |

## Output Template

When generating a keyword list, output in this exact format:

```
CAMPAIGN: [Campaign Name]
OBJECTIVE: [Conversions/Leads/Sales/Traffic]
TARGET AUDIENCE: [Description]

AD GROUP: [Ad Group 1 Name]
"exact keyword 1", "exact keyword 2", "exact keyword 3", [phrase keyword 1], [phrase keyword 2]

AD GROUP: [Ad Group 2 Name]
"exact keyword 1", "exact keyword 2", "exact keyword 3", [phrase keyword 1], [phrase keyword 2]

AD GROUP: [Ad Group 3 Name]
"exact keyword 1", "exact keyword 2", [phrase keyword 1], [phrase keyword 2], [phrase keyword 3]

NEGATIVE KEYWORDS:
"free", "cheap", "jobs", "login", "hire", "career", "internship", "salary", [free trial], [how to make], [what is], [tutorial]
```

## Common Pitfalls

1. **Using broad match.** Every keyword must be wrapped in `"quotes"` or `[brackets]`. No exceptions.

2. **Bullet points or numbered lists.** Output is always comma-separated keywords. Never use bullets, numbers, or line breaks within a keyword group.

3. **Ad groups that are too broad.** If a keyword's search intent doesn't match the ad and landing page for that group, move it to a different group. Tightly themed groups give better quality scores and lower CPC.

4. **Forgetting negative keywords.** Always include a negative keyword section. Even a basic set saves budget from unqualified clicks.

5. **Duplicate keywords with different match types.** Having both "keyword" and [keyword] for the same root can cause internal competition. Use exact for precise targeting and phrase for broader intent capture — but not identical phrases in both.

6. **Keyword stuffing without relevance.** More keywords do not mean more conversions. 10 tightly matched keywords outperform 100 loosely related ones.

7. **Ignoring search volume signals.** For very niche keywords (under 100 monthly searches), group them into one ad group with similar low-volume keywords to accumulate sufficient data.

## Verification Checklist

- [ ] Every keyword is wrapped in `"exact"` or `[phrase]` match syntax
- [ ] No broad match keywords (naked words without delimiters)
- [ ] No bullet points, numbers, or line breaks within keyword groups
- [ ] Keywords are comma-separated
- [ ] Ad groups are tightly themed (all keywords in a group match the same ad/landing page)
- [ ] Each ad group has 5-20 keywords
- [ ] Negative keywords section is included
- [ ] Exact match dominates for bottom-funnel campaigns
- [ ] Phrase match used for broader intent patterns
- [ ] No duplicate keywords across match types for the same root term
