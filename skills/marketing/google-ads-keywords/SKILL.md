---
name: google-ads-keywords
description: Use when the user needs keyword lists for Google Ads Search campaigns — building, expanding or restructuring keywords, grouping them into ad groups, or writing negative keyword lists. Always outputs exact match ([keyword]) and phrase match ("keyword") in comma-separated lines, never broad match, never bullet points. Also use when someone asks for "PPC keywords", "search terms to bid on" or "Google Ads Editor import". Don't use for SEO/organic keyword research (geo-ai-seo) or for diagnosing a running account (google-ads-diagnostics).
version: 1.1.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. No tools, browsing or API access required; keyword volume data is optional and must be labelled as estimates when unavailable.
metadata:
  category: paid-search
  updated: 2026-10-02
  tags: [google-ads, keywords, exact-match, phrase-match, search-ads, ppc, negative-keywords, ad-groups]
  related_skills: [google-ads-diagnostics, landing-page-funnel, geo-ai-seo, meta-ads-creative]
---

# Google Ads Keyword Lists

## Overview

Generate structured keyword lists for Google Ads Search campaigns using only exact match and phrase match. Every keyword carries its match-type delimiter, lists are comma-separated so they can be pasted straight into Google Ads or Google Ads Editor, and every campaign ships with a negative keyword list. The goal is control: tightly themed ad groups that map to one ad and one landing page.

## When to Use

- Building keyword lists for a new Search campaign or account
- Expanding research from a seed product, service or topic
- Reorganizing an existing account into tightly themed ad groups
- Writing negative keyword lists (campaign, account or shared list level)
- Producing a Google Ads Editor import sheet

Don't use for: SEO or AI-search keyword research (use `geo-ai-seo`), diagnosing live campaign performance (use `google-ads-diagnostics`), Shopping or Performance Max feeds, or Display/YouTube audience targeting.

## Inputs

Ask for (or extract from the conversation):

- **Product / service** and the 2–5 core things it does
- **Campaign objective** (sales, leads, traffic) and funnel stage
- **Target locations and language** — keyword wording changes by locale
- **Landing pages** available (one ad group per landing page theme)
- **Brand names** (own and competitors) and whether competitor bidding is wanted
- **Existing keywords or search terms report**, if the account is live
- **Monthly search volume data**, if the user has Keyword Planner access

Data rules: do not invent search volumes or CPCs. If the user has no volume data, say so and rank keywords by intent instead. Use the account's language; do not translate brand names. Google renames features regularly — if a match-type or UI name differs from what is written here, use the closest current equivalent and say so.

## Match Types

| Match Type | Syntax | Behaviour (2026) |
|-----------|--------|----------|
| **Exact match** | `[keyword]` | Searches with the *same meaning or intent* as the keyword, including misspellings, plurals, reordered words and implied words. Tightest control available. |
| **Phrase match** | `"keyword"` | Searches that *include the meaning* of the keyword; extra words before, after or in between are allowed as long as intent is preserved. Phrase match absorbed broad match modifier in 2021. |
| **Broad match** | `keyword` (no delimiter) | Any search Google considers related, informed by landing page, other keywords and the user's signals. Only sensible together with Smart Bidding, strong conversion tracking and a mature account. **Not produced by this skill.** |

Why exact and phrase only: this skill exists for advertisers who want predictable spend and clean reporting. Broad match hands the matching decision to Google's models, which can work with high conversion volume but wastes budget on thin accounts. If the user explicitly wants broad match for a Smart-Bidding campaign, tell them it is outside this skill's output and that the keywords below can be converted by removing the delimiters.

> Syntax check: square brackets `[ ]` = exact, quotation marks `" "` = phrase. A naked word is broad match and must not appear in the output.

**Technical limits:** a keyword is at most 80 characters and 10 words. Keywords are not case-sensitive. The same keyword cannot exist twice in one ad group with the same match type.

## Output Format

All keywords are comma-separated. Each keyword is wrapped in its match-type delimiters. No bullets, no numbering, no line breaks inside a group.

```
[exact match keyword], [another exact], "phrase match keyword", "another phrase"
```

### Full template

```
CAMPAIGN: [Campaign Name]
OBJECTIVE: [Sales / Leads / Traffic]
LOCATION & LANGUAGE: [e.g. Germany, German]
TARGET AUDIENCE: [One line]

AD GROUP: [Ad Group 1 Name] → Landing page: [URL or page theme]
[exact keyword 1], [exact keyword 2], [exact keyword 3], "phrase keyword 1", "phrase keyword 2"

AD GROUP: [Ad Group 2 Name] → Landing page: [URL or page theme]
[exact keyword 1], [exact keyword 2], "phrase keyword 1", "phrase keyword 2", "phrase keyword 3"

NEGATIVE KEYWORDS (campaign level):
"free", "cheap", "jobs", "login", "career", "salary", [free trial], [how to make], [what is]

NEGATIVE KEYWORDS (cross-ad-group, to stop cannibalization):
AD GROUP [Name A] excludes: "term that belongs to group B"
AD GROUP [Name B] excludes: "term that belongs to group A"

NOTES: [Assumptions, missing data, keywords to validate in Keyword Planner]
```

### Google Ads Editor CSV (on request)

When the user wants a bulk upload, add this block. Match type is written in the column, so the keyword column has no delimiters here — this is the one place naked keywords are correct.

```
Campaign,Ad Group,Keyword,Match Type
[Campaign],[Ad Group 1],buy running shoes online,Exact
[Campaign],[Ad Group 1],buy running shoes,Phrase
```

### Negative keywords

Negative keywords also take a match type and behave differently from positive keywords:

- Negatives match **misspellings** automatically (since 2024) but **not** plurals, synonyms or close variants. Add plurals and synonyms yourself.
- Phrase negative `"repair"` blocks every query containing that word in that order. Exact negative `[running shoes]` blocks only that query.
- Use a shared **negative keyword list** at account level for universal exclusions (jobs, free, DIY) and campaign-level negatives for topic exclusions.

## Keyword Research Process

### 1. Seed extraction

From the product or service, list the core nouns a buyer would type: product type, category, problem solved, solution name.

### 2. Variations per seed

| Variation type | Examples (replace brackets) | Usual match type |
|---------------|-----------------------------|------------------|
| Synonyms | shoes / footwear / sneakers | exact |
| Commercial modifiers | buy [product], [product] online, [product] shop, [product] near me | exact |
| Transactional modifiers | [product] price, [product] cost, [product] deal, cheap [product]* | exact |
| Qualifier / long-tail | [product] for [use case], waterproof [product], [product] size 12 | exact |
| Comparison | best [product], [product] reviews, [brand] vs [competitor] | phrase |
| Question (consideration) | how to choose [product], which [product] for [use] | phrase, only for mid-funnel campaigns |
| Brand | [own brand], [own brand] [product] | exact, in a separate brand campaign |
| Competitor | [competitor], [competitor] alternative | exact, separate campaign, no trademark in ad copy |

\* "cheap" is a positive keyword only for discount positioning; otherwise it is a negative.

### 3. Quality filtering

Remove keywords that:

- have informational intent only (unless the campaign is explicitly mid-funnel)
- are single generic words (one-word exact match is still too broad in meaning)
- conflict with the offer (e.g. "free" for a paid product, "used" for a new-goods retailer)
- target a product or location the user does not serve

### 4. Grouping into ad groups

Each ad group = one search intent = one responsive search ad = one landing page. Google rewards relevance between query, ad and page with better Quality Score and lower CPC, so a tight theme is cheaper than a big one.

- 5–20 keywords per ad group; fewer is fine when volume is concentrated
- Name ad groups `[product]-[modifier]-[location if relevant]`
- Low-volume long-tails (under ~100 searches/month) are grouped together so they accumulate enough data

### 5. Match type assignment

| Situation | Match type | Example |
|-----------|-----------|---------|
| Clear buying intent, known phrasing | Exact | `[buy running shoes online]` |
| Buying intent, phrasing varies | Phrase | `"buy running shoes"` |
| Brand | Exact | `[acme running shoes]` |
| Specific long-tail | Exact | `[waterproof trail running shoes]` |
| Catch broader patterns to mine search terms | Phrase | `"running shoes for wide feet"` |
| Competitor | Exact | `[competitor brand]` |

Avoid `[keyword]` and `"keyword"` for the identical string in one campaign. Google picks one to serve, but the duplicate splits data and muddles reporting.

### Match type mix by campaign goal

| Campaign type | Exact | Phrase | Max keywords / ad group |
|--------------|-------|--------|------------------------|
| Bottom-funnel conversion | ~80% | ~20% | 10 |
| Mid-funnel consideration | ~50% | ~50% | 15 |
| Top-funnel awareness (rare for Search) | ~20% | ~80% | 20 |
| Brand | 100% | — | 10 |
| Remarketing (RLSA) | ~90% | ~10% | 10 |

These are starting ratios. Phrase match earns its place by discovering new exact-match winners in the search terms report; once a phrase keyword's best queries are known, add them as exact and tighten.

## Common Pitfalls

1. **A naked keyword slips in.** Every keyword must be wrapped in `[ ]` or `" "`. Scan the final output line by line.

2. **Delimiters swapped.** Brackets are exact, quotes are phrase. Reversing them changes targeting entirely.

3. **Bullets or line breaks inside a group.** Output is comma-separated so it pastes cleanly. Bulleted keyword lists have to be re-typed.

4. **Ad groups that mix intents.** "running shoes" and "running shoe repair" in one group means one ad and one page for two different needs. Split them.

5. **No negatives.** Every campaign ships with a negative list. Even ten generic negatives save real money in week one.

6. **Forgetting cross-ad-group negatives.** If group A has `"trail running shoes"` and group B has `"running shoes"`, add `"trail"` as a negative to group B so each query lands on the intended ad.

7. **Assuming negatives block variants.** Negatives block misspellings but not plurals or synonyms. Add `"job"` and `"jobs"`, `"free"` and `"for free"`.

8. **Invented volumes.** If you have no Keyword Planner data, rank by intent and say the numbers need validation. Fabricated volumes lead to bad budget decisions.

## Verification Checklist

- [ ] Every keyword is wrapped in `[exact]` or `"phrase"` syntax; no naked keywords outside the Editor CSV block
- [ ] Brackets = exact, quotes = phrase (not reversed)
- [ ] Keywords are comma-separated with no bullets, numbers or line breaks inside a group
- [ ] Each ad group has one clear intent and names its landing page theme
- [ ] Each ad group has 5–20 keywords (or a documented reason for fewer)
- [ ] No keyword is ≥ 80 characters or more than 10 words
- [ ] No identical string appears in both match types within one campaign
- [ ] Campaign-level negative list included, with plurals and synonyms spelled out
- [ ] Cross-ad-group negatives listed where themes overlap
- [ ] Exact match dominates bottom-funnel groups; phrase is used to capture variation
- [ ] Brand and competitor keywords are in separate campaigns (or flagged to be)
- [ ] Assumptions and missing data (volumes, locale) stated in NOTES
