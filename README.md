# digital-marketing-skills

```
    ____  __  ___   _____ __ __ ______    __   _____
   / __ \/  |/  /  / ___// //_//  / /   / /  / ___/
  / / / / /|_/ /   \__ \/ ,<   / // /   / /   \__ \
 / /_/ / /  / /   ___/ / /| |_/ // /___/ /______/ /
/_____/_/  /_/   /____/_/ |_/___/_____/_____/____/
```

A collection of Hermes Agent skills for digital marketing — AI-powered content creation, ad copy, campaign optimization, and tracking diagnostics.

## Skills

| Skill | Description |
|-------|-------------|
| **[geo-ai-seo](skills/marketing/geo-ai-seo/SKILL.md)** | Generative Engine Optimization — content structure and text formation for AI-powered search (Google AI Overview, Perplexity, ChatGPT Search). Answer-first architecture, data anchors, citation-signal optimization. |
| **[meta-ads-creative](skills/marketing/meta-ads-creative/SKILL.md)** | Creative concepts and copy for Meta (Facebook/Instagram) ads. Hook formulas, primary text, headlines, descriptions, CTA selection, and creative format guidance. |
| **[meta-ads-diagnostics](skills/marketing/meta-ads-diagnostics/SKILL.md)** | Analyze Meta Ads performance data and propose concrete campaign changes — budget allocation, targeting, scheduling, LLA management, bid strategy, segments, and placement optimization. |
| **[google-ads-keywords](skills/marketing/google-ads-keywords/SKILL.md)** | Keyword generation for Google Ads. Exact match `"keyword"` and phrase match `[keyword]` only — no broad match. Comma-separated output, organized into tightly themed ad groups with negative keywords. |
| **[google-ads-diagnostics](skills/marketing/google-ads-diagnostics/SKILL.md)** | Analyze Google Ads performance and suggest optimizations — bid strategy, keyword quality, ad copy, search term negatives, Quality Score, and budget allocation. |
| **[landing-page-funnel](skills/marketing/landing-page-funnel/SKILL.md)** | Landing page conversion optimization — funnel structure, ad-to-page congruence, form optimization, social proof placement, CRO testing frameworks, and copy analysis. |
| **[gtm-debugging](skills/marketing/gtm-debugging/SKILL.md)** | Diagnose and fix Google Tag Manager bugs — missing triggers, broken tags, variable misconfiguration, data layer issues, consent mode, cross-domain tracking, and duplicate event fires. |

## Install

Copy the `skills/marketing/` folder into your Hermes skills directory:

```bash
cp -r skills/marketing ~/.hermes/skills/
```

Or install as a git submodule:

```bash
git submodule add https://github.com/vidual-labs/digital-marketing-skills.git ~/.hermes/skills/digital-marketing-skills
```

## Structure

```
skills/marketing/
├── geo-ai-seo/
│   └── SKILL.md
├── meta-ads-creative/
│   └── SKILL.md
├── meta-ads-diagnostics/
│   └── SKILL.md
├── google-ads-keywords/
│   └── SKILL.md
├── google-ads-diagnostics/
│   └── SKILL.md
├── landing-page-funnel/
│   └── SKILL.md
└── gtm-debugging/
    └── SKILL.md
```
