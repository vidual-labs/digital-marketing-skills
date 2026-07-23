# digital-marketing-skills

```
    ____  __  ___   _____ __ __ ______    __   _____
   / __ \/  |/  /  / ___// //_//  / /   / /  / ___/
  / / / / /|_/ /   \__ \/ ,<   / // /   / /   \__ \
 / /_/ / /  / /   ___/ / /| |_/ // /___/ /______/ /
/_____/_/  /_/   /____/_/ |_/___/_____/_____/____/
```

A collection of Hermes Agent skills for digital marketing — designed for AI-powered content creation, ad copy, and search optimization.

## Skills

| Skill | Description |
|-------|-------------|
| **[geo-ai-seo](skills/marketing/geo-ai-seo/SKILL.md)** | Generative Engine Optimization — content structure and text formation for AI-powered search (Google AI Overview, Perplexity, ChatGPT Search). Answer-first architecture, data anchors, citation-signal optimization. |
| **[meta-ads-creative](skills/marketing/meta-ads-creative/SKILL.md)** | Creative concepts and copy for Meta (Facebook/Instagram) ads. Hook formulas, primary text, headlines, descriptions, CTA selection, and creative format guidance for A/B testing. |
| **[google-ads-keywords](skills/marketing/google-ads-keywords/SKILL.md)** | Keyword generation for Google Ads. Exact match `"keyword"` and phrase match `[keyword]` only — no broad match. Comma-separated output, organized into tightly themed ad groups with negative keywords. |

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
└── google-ads-keywords/
    └── SKILL.md
```
