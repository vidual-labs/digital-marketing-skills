# digital-marketing-skills

```
    ____  __  ___   _____ __ __ ______    __   _____
   / __ \/  |/  /  / ___// //_//  / /   / /  / ___/
  / / / / /|_/ /   \__ \/ ,<   / // /   / /   \__ \
 / /_/ / /  / /   ___/ / /| |_/ // /___/ /______/ /
/_____/_/  /_/   /____/_/ |_/___/_____/_____/____/
```

A collection of Hermes Agent skills for digital marketing — paid ads, organic social, campaign diagnostics, tracking, and competitive intelligence.

## Skills

### Paid & Search

| Skill | Description |
|-------|-------------|
| **[meta-ads-creative](skills/marketing/meta-ads-creative/SKILL.md)** | Creative concepts and copy for Meta (Facebook/Instagram) ads. Hook formulas, primary text, headlines, descriptions, CTA selection, and creative format guidance. |
| **[meta-ads-diagnostics](skills/marketing/meta-ads-diagnostics/SKILL.md)** | Analyze Meta Ads performance data and propose concrete campaign changes — budget allocation, targeting, LLA, bid strategy, segments, and placement optimization. |
| **[google-ads-keywords](skills/marketing/google-ads-keywords/SKILL.md)** | Keyword generation for Google Ads. Exact match `"keyword"` and phrase match `[keyword]` only — no broad match. Comma-separated, tightly themed ad groups with negative keywords. |
| **[google-ads-diagnostics](skills/marketing/google-ads-diagnostics/SKILL.md)** | Analyze Google Ads performance — keyword quality, search term negatives, Quality Score, bid strategy, ad copy, and budget optimization. |
| **[tiktok-ads](skills/marketing/tiktok-ads/SKILL.md)** | Native-first TikTok ad creatives and copy. Hook formulas, second-by-second scripts, in-app ad text, format guidance, and testing strategy. |

### Organic Social

| Skill | Description |
|-------|-------------|
| **[instagram-organic](skills/marketing/instagram-organic/SKILL.md)** | Profile audit, content pillars, posting schedule, and follower growth tactics — optimized for Reels, carousels, and engagement flywheel. |
| **[linkedin-organic](skills/marketing/linkedin-organic/SKILL.md)** | Profile/page audit, writing-first strategy, comment flywheel, content pillars, and B2B thought leadership growth. |
| **[youtube-organic](skills/marketing/youtube-organic/SKILL.md)** | Channel audit, traffic source analysis, thumbnail/title strategy, retention optimization, and subscriber growth tactics. |
| **[pinterest-organic](skills/marketing/pinterest-organic/SKILL.md)** | Board structure, keyword-rich pin strategy, posting schedule, and visual search optimization — optimized for outbound clicks. |

### Conversion & Tracking

| Skill | Description |
|-------|-------------|
| **[geo-ai-seo](skills/marketing/geo-ai-seo/SKILL.md)** | Generative Engine Optimization — content structure and text formation for AI search (Google AI Overviews, Perplexity, ChatGPT). Answer-first architecture, data anchors, citation-signal optimization. |
| **[landing-page-funnel](skills/marketing/landing-page-funnel/SKILL.md)** | Landing page conversion optimization — funnel structure, ad-to-page congruence, form optimization, social proof, CRO testing, and copy analysis. |
| **[gtm-debugging](skills/marketing/gtm-debugging/SKILL.md)** | Diagnose and fix GTM bugs — missing triggers, broken tags, data layer issues, consent mode, cross-domain tracking, and duplicate events. |

### Competitive Intelligence

| Skill | Description |
|-------|-------------|
| **[competitor-research](skills/marketing/competitor-research/SKILL.md)** | Identify competitors across 3 layers (direct, indirect, adjacent), audit their digital presence, SWOT analysis, and find actionable market gaps. |

## Install & Use

### In Hermes Agent

The native home — skills auto-load by trigger:

```bash
cp -r skills/marketing ~/.hermes/skills/
```

Each skill has a `description:` frontmatter field that acts as a trigger. The agent loads the skill automatically when the trigger matches your prompt (e.g., "write TikTok ad copy" → loads `tiktok-ads`).

### In Claude (Claude.ai / Desktop App)

Claude doesn't have a skill system, so paste the skill content directly as instructions.

**Method A: Direct paste (one-off)**

1. Open Claude
2. Paste the full content of the SKILL.md you need (skip the YAML frontmatter between `---`)
3. Add your request below it

**Method B: Custom Instructions (reusable, recommended)**

1. Go to Claude Settings → Custom Instructions
2. In "Always include these instructions..." paste **all 13 SKILL.md files** (without YAML frontmatter) concatenated together
3. Add this instruction at the top:

```
You are a digital marketing strategist. When I give you a marketing task, reference the skill framework below to guide your response. Follow the structure, output format, and verification checklist from the relevant skill section.
```

4. Click Save — every new conversation will now have full marketing skill context

**Method C: Upload as a file (for a single conversation)**

1. Combine all SKILL.md files into a single `marketing-skills.md`
2. Upload the file in your chat
3. Tell Claude: "Read this file — it contains my marketing workflow. Follow its structure for all marketing tasks in this conversation."

### In ChatGPT (GPT-4 / GPT-4o)

**Method A: Custom Instructions (simplest, partial)**

1. Go to Settings → Custom Instructions
2. In the "Instruct GPT..." box, paste the skills most relevant to your work (GPT-4 Custom Instructions allow ~4K chars, so pick your top 3-5 skills)
3. Add this instruction at the top:

```
You are a digital marketing strategist. When I give you a marketing task, reference the skill framework below to guide your response.
```

4. Save — every new chat starts with those skill contexts loaded

**Method B: Upload a file (for one conversation)**

1. Combine all SKILL.md files into `marketing-skills.md`
2. Upload the file in your GPT chat
3. Prompt: "Read this file — it contains my marketing workflow framework. Follow its instructions for all marketing tasks in this conversation."

**Method C: Build a custom GPT (permanent, sharable)**

1. Go to https://chatgpt.com/gpts (or Settings → My GPTs → Create)
2. Name it: "Digital Marketing Strategist"
3. In the **Instructions** field, paste all SKILL.md content (minus YAML frontmatter)
4. In **Knowledge**, upload the combined `marketing-skills.md` file as backup
5. Enable "Always use these files"
6. Configure Capabilities: Web Browsing (for competitor research), Code Interpreter (for data analysis)
7. Click **Create**
8. This gives you a dedicated, permanently-skilled GPT you can share with your team

## Structure

```
skills/marketing/
├── competitor-research/
├── geo-ai-seo/
├── google-ads-diagnostics/
├── google-ads-keywords/
├── gtm-debugging/
├── instagram-organic/
├── landing-page-funnel/
├── linkedin-organic/
├── meta-ads-creative/
├── meta-ads-diagnostics/
├── pinterest-organic/
├── tiktok-ads/
└── youtube-organic/
```
