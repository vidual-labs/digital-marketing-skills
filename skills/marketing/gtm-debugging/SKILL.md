---
name: gtm-debugging
description: Use when diagnosing and fixing Google Tag Manager or tracking bugs — tags not firing, triggers misconfigured, data layer variables undefined, GA4 events missing or duplicated, Google Ads or Meta Pixel conversions not recording, Conversions API deduplication, consent mode v2 blocking tags, cross-domain tracking, single-page-app pageviews, and server-side GTM forwarding. Also use when someone says "my conversions stopped", "GA4 shows nothing", "events fire twice" or shares a Tag Assistant screenshot. Don't use for analytics reporting questions or for campaign optimization (google-ads-diagnostics, meta-ads-diagnostics).
version: 1.1.0
author: vidual-labs
license: MIT
compatibility: Works in any agent that reads SKILL.md. Needs the user to run Tag Assistant / browser DevTools and report back, or to paste container exports, data layer snippets and console output; no direct site access required.
metadata:
  category: conversion-tracking
  updated: 2026-10-02
  tags: [gtm, google-tag-manager, debugging, ga4, datalayer, event-tracking, consent-mode, conversions-api, server-side-tagging, cross-domain]
  related_skills: [landing-page-funnel, google-ads-diagnostics, meta-ads-diagnostics]
---

# Google Tag Manager Debugging

## Overview

Find, reproduce and fix tracking bugs in Google Tag Manager setups: container loading, triggers, variables, tags (GA4, Google Ads, Meta Pixel and others), consent mode, duplicate events, cross-domain and single-page-app tracking, and server-side GTM. The output is a diagnosis with exact configuration changes, data layer code where needed, and verification steps a developer can follow.

## When to Use

- Events or conversions not firing, firing late, or firing twice
- GA4, Google Ads or Meta Pixel tags sending no data or wrong parameters
- Data layer variables returning `undefined` or stale values
- Tags working in Preview but not in production (usually consent)
- Session breaks across domains or on SPA route changes
- Server-side GTM not forwarding events, or Conversions API duplicates

Don't use for: interpreting analytics reports, campaign performance (use `google-ads-diagnostics` / `meta-ads-diagnostics`), SEO audits, or landing page conversion rate (use `landing-page-funnel`).

## Inputs

Ask for, in this order of usefulness:

1. **The symptom**, precisely: which tag, which page, which action, what is expected vs observed, since when
2. **Tag Assistant Preview output**: for the action in question, the event list, the tag's "Fired / Not fired" status and reason, trigger conditions, variable values, and the **Consent** tab
3. **Browser console errors** and the Network tab filtered for `collect`, `gtm.js`, `gtag/js`, `fbevents`, `tr?`
4. **Data layer code** as implemented on the page (copy of the `dataLayer.push` calls)
5. **Container export (JSON)** or screenshots of the tag, trigger and variable configuration
6. **Consent setup**: which CMP, whether consent mode v2 is on, default state
7. **Environment facts**: SPA framework, server-side GTM, CDN/WAF, Shopify/WordPress plugins that also inject tags

Data rules: do not guess what the container contains — ask for the export or screenshots. If you cannot access the site, walk the user through Tag Assistant step by step and reason from what they report. Mark any fix that depends on an unverified assumption. Google renames things (the GA4 Configuration tag is now the **Google tag**, Tag Assistant replaced the legacy extension) — map old names to current ones when the user's screenshots differ.

## Diagnostic Framework

### Phase 1: Is the container loading?

1. View page source: the GTM snippet (`GTM-XXXXXXX`) should be high in `<head>`, once
2. Network tab: `gtm.js?id=GTM-...` returns 200
3. Console: no `dataLayer is not defined` or CSP errors

| Symptom | Cause | Fix |
|---------|-------|-----|
| Snippet absent or on some pages only | Template/theme omits it | Add through the site's global layout, not per page |
| `gtm.js` blocked | CSP, ad blocker, corporate proxy, country-level block | Add `https://www.googletagmanager.com` to `script-src`/`connect-src`; consider first-party serving via server-side GTM or Google tag gateway |
| Two containers or duplicate snippet | Plugin plus hard-coded snippet | Remove one; duplicates double-fire everything |
| Data layer pushes before snippet lost | `dataLayer` defined after GTM | Declare `window.dataLayer = window.dataLayer || [];` **before** the snippet and push initial data there |

Reference snippet order:

```html
<head>
  <script>
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({ 'user_type': 'member', 'page_type': 'product' });
  </script>
  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-XXXXXXX');</script>
  <!-- End Google Tag Manager -->
</head>
```

### Phase 2: Reproduce in Tag Assistant Preview

Preview (tagassistant.google.com → Connect) is the primary tool. Reproduce before fixing.

Workflow:

1. Connect Preview to the page, perform the action
2. Left panel: find the event (`Consent Initialization`, `Initialization`, `Container Loaded`, `DOM Ready`, `Window Loaded`, custom events, `Click`, `Form Submit`, `History`)
3. **Tags** tab: is the tag under "Fired" or "Not fired"? Click it to see which trigger condition failed
4. **Variables** tab at that event: are the values what the tag needs?
5. **Data Layer** tab: what did the push actually contain?
6. **Consent** tab: what consent state did the tag see, and does the tag require consent?
7. **Errors** tab: JavaScript errors inside custom HTML tags

Preview does **not** bypass consent. A tag with built-in or additional consent checks stays "Not fired" when the state is denied, and the Consent tab shows why.

### Phase 3: Trigger problems

| Problem | Diagnostic | Fix |
|---------|-----------|-----|
| Custom Event trigger never fires | Event name in Data Layer tab ≠ trigger name (case, spacing) or push happens before GTM loads | Match the exact string; for early pushes make sure `dataLayer` exists before the snippet |
| Click trigger misses the click | Element is re-rendered on click, or click target is a child `<span>` | Use "Click – All Elements" with `matches CSS selector` and a selector ending in `, selector *`; enable "Wait for tags" only when navigation follows |
| Form Submission trigger silent | AJAX/React form, no native `submit` event | Push a custom `form_submit` event from the form's success callback; or use the Element Visibility trigger on the thank-you message |
| Scroll Depth fires at wrong time | Content loads after page load | Fire the trigger on a later event (e.g. `DOM Ready` or a custom "content_loaded" push) |
| Page View on wrong pages | URL condition too loose | Use "Page Path" with `matches RegEx`; test the regex against real URLs |
| SPA route change not tracked | No History Change trigger, or the router uses neither `pushState` nor hash | Add a History Change trigger; if the framework bypasses History API, push `{'event':'virtual_pageview', 'page_path': ...}` from the router |
| Element Visibility never fires | Element inside an iframe or shadow DOM | Track inside the iframe/component, or push an event from the component code |

### Phase 4: Variable problems

| Symptom | Cause | Fix |
|---------|-------|-----|
| Data Layer Variable `undefined` | Key mismatch (`userId` vs `userid`), nested path wrong, or value pushed *after* the event | Copy the exact key from the Data Layer tab; use dot notation `ecommerce.items.0.item_id`; push data in the same object as the event or before it |
| Variable shows the previous value | Data layer merges objects; stale `ecommerce` from the last event | Push `{ ecommerce: null }` before each new ecommerce push |
| DOM Element variable `null` | Element not yet rendered when the tag fires | Fire on `DOM Ready`/Element Visibility, or read the value from the data layer instead |
| Cookie variable empty | Cookie set on another path/domain or HttpOnly | Set path `/` and the apex domain; HttpOnly cookies cannot be read client-side |
| URL variable wrong component | "Page URL" selected instead of Path/Hostname/Query | Choose the component type explicitly |

Naming convention: prefix variables with type — `DLV - ecommerce.items`, `JS - Page Type`, `CJS - Clean URL`, `Const - GA4 ID` — so Preview is readable.

### Phase 5: Tag problems

| Problem | Diagnostic | Fix |
|---------|-----------|-----|
| GA4 events missing | No **Google tag** (`G-XXXX`) firing on `Initialization – All Pages`, or GA4 event tag fires before it | One Google tag on Initialization; GA4 Event tags reference the same Measurement ID |
| GA4 events duplicated | Both the Google tag's enhanced measurement and a GTM event tag send the same event; or two triggers on one tag | Disable the enhanced measurement feature for that event or remove the GTM tag; one trigger per behaviour |
| Ecommerce missing items | Data layer does not follow the GA4 schema (`ecommerce.items[]` with `item_id`/`item_name`), or "Send Ecommerce data" is off in the tag | Fix the schema; set the tag's data source to Data Layer |
| Google Ads conversion not counting | Conversion ID/label typo, conversion linker missing, consent denied for `ad_storage`, or landing page lost `gclid` | Add a Conversion Linker tag on all pages; check consent; keep `gclid` across redirects |
| Meta Pixel fires but Events Manager shows "no recent activity" | Wrong Pixel ID, blocked by consent/ad blocker, or test events only | Verify ID; check consent; compare browser vs server events |
| Pixel + Conversions API double counts | No shared `event_id` | Send the same `event_id` from browser and server for each event |
| Custom HTML tag errors | Syntax error, undefined variable, runs before dependency | Check the Errors tab; wrap in try/catch; sequence with tag sequencing |
| Server-side GTM silent | Client not claiming requests, wrong transport URL, missing server-side tag | Confirm the GA4 client claims `/g/collect`; set `server_container_url` on the Google tag; check server container Preview and cloud logs |

Reference data layer pushes (GA4 schema):

```javascript
// Always clear the previous ecommerce object first
dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: 'add_to_cart',
  ecommerce: {
    currency: 'EUR',
    value: 29.99,
    items: [{ item_id: 'SKU-123', item_name: 'Product Name', item_category: 'Category', price: 29.99, quantity: 1 }]
  }
});

dataLayer.push({ ecommerce: null });
dataLayer.push({
  event: 'purchase',
  ecommerce: {
    transaction_id: 'TX-98765',
    value: 59.98,
    tax: 5.00,
    shipping: 4.99,
    currency: 'EUR',
    items: [{ item_id: 'SKU-123', item_name: 'Product Name', price: 29.99, quantity: 2 }]
  }
});

dataLayer.push({ event: 'generate_lead', lead_source: 'contact_form', form_id: 'contact' });
```

### Phase 6: Consent mode v2

Consent is the most common cause of "works in Preview, not in production" and of conversion drops after a CMP change.

Correct order: consent default → consent update (after user choice) → tags. The default must be set with the `gtag('consent','default', …)` command (or the CMP's GTM template) on the **Consent Initialization – All Pages** trigger. A plain `dataLayer.push({consent: …})` object does nothing.

```html
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){ dataLayer.push(arguments); }
  gtag('consent', 'default', {
    'ad_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'analytics_storage': 'denied',
    'functionality_storage': 'granted',
    'security_storage': 'granted',
    'wait_for_update': 500
  });
</script>
<!-- GTM snippet follows -->
```

| Symptom | Cause | Fix |
|---------|-------|-----|
| Tags fire in Preview with consent granted but conversions dropped in production | Most real users deny; no consent update is sent after acceptance | Verify the CMP sends `gtag('consent','update', …)`; check the Consent tab shows "On-page Update" |
| Google Ads conversions missing entirely in the EEA | `ad_storage` / `ad_user_data` default denied and never updated | Fix the update call; enable modelling via consent mode (basic vs advanced) |
| Default set too late | CMP loads after GTM | Put the default inline before the snippet, or use the CMP template on Consent Initialization |
| Non-Google tags (Meta, TikTok) fire despite denial | They do not read Google consent signals | Set "Additional consent checks" on those tags to require `ad_storage` (or use a consent-aware trigger) |

### Phase 7: Cross-domain and duplicates

**Cross-domain (GA4)**: configure domains in GA4 Admin → Data streams → Configure tag settings → Configure your domains (not in a GTM linker tag). Verify the `_gl` parameter is appended to cross-domain links and that both sites load the same Google tag. Google Ads uses the Conversion Linker tag; enable "Link across domains" there.

**Duplicate events**: count fires per action in Preview; check for multiple triggers on one tag; check whether the data layer push itself happens twice (framework double-render, plugin plus hard-coded code); check enhanced measurement overlap; for click triggers, use the most specific selector so parent and child do not both match.

### Phase 8: Verify end to end

1. Fix in the workspace, test in Preview, then publish (changes are invisible to users until published)
2. GA4 → Admin → DebugView (enable with Preview or `debug_mode`): confirm the event and parameters arrive within ~30 seconds
3. Google Ads → Goals → Conversions: status "Recording conversions" within 24 hours (use Tag Assistant to see the conversion hit immediately)
4. Meta Events Manager → Test Events: browser and server events appear once each, deduplicated
5. Re-test with consent **denied** and **granted** in a fresh incognito session

## Output Format

```
GTM DIAGNOSIS: [Site]
Container: GTM-XXXXXXX | Environment: [web / server-side / both] | CMP: [name or none]
Issue reported: [Description, since when]

--- FINDINGS ---
1. CONTAINER LOAD: [OK / problem — evidence]
2. DATA LAYER: [Issues — key mismatches, timing, schema]
3. TRIGGERS: [Trigger] — [Problem] — [Evidence from Preview]
4. VARIABLES: [Variable] — [Problem] — [Evidence]
5. TAGS: [Tag] — [Problem] — [Evidence]
6. CONSENT: [Default/update state, which tags are blocked, evidence from Consent tab]
7. DUPLICATES / CROSS-DOMAIN / SPA: [Findings]

--- ROOT CAUSE ---
[One or two sentences; confidence High / Medium / Low and why]

--- FIXES (in order) ---
FIX 1: [Name]
  Where: [Tag / Trigger / Variable / Site code / CMP]
  Change: [Exact configuration or code]
  Code (if needed):
  [code block]

FIX 2: [...]

--- VERIFICATION ---
1. [Preview check: event, tag fired, variable value]
2. [DebugView / Events Manager / Ads conversion check]
3. [Consent denied and granted test]
4. [Publish and re-check production]

--- OPEN QUESTIONS ---
[Anything that needs the developer's confirmation]
```

## Common Pitfalls

1. **Fixing without reproducing.** Preview first. Guessing wastes a developer's afternoon.

2. **Assuming Preview bypasses consent.** It does not. Read the Consent tab; most "random" non-firing is denied consent.

3. **Setting consent defaults with a data layer object.** Only `gtag('consent','default', …)` or a CMP template on Consent Initialization works.

4. **Case and whitespace.** `formSubmit` ≠ `FormSubmit`. Copy event and key names from the Data Layer tab.

5. **Forgetting `ecommerce: null`.** Stale items from the previous event leak into the next one and inflate revenue.

6. **Debugging the wrong container version.** Preview shows the workspace; users see the published version. Check "Versions" and publish.

7. **Not checking for a second source of the same tag.** Shopify apps, WordPress plugins and hard-coded pixels fire alongside GTM and create duplicates.

8. **Treating a reporting drop as a tracking bug without checking consent and attribution changes first.** A new CMP banner can halve "conversions" without breaking any tag.

## Verification Checklist

- [ ] Container load confirmed (snippet once, `gtm.js` 200, no console errors)
- [ ] Data layer declared before the snippet; pushes copied as implemented
- [ ] Issue reproduced in Tag Assistant Preview with the specific event, tag status and failing condition
- [ ] Variable values at the moment of firing checked in Preview
- [ ] Consent tab reviewed; default and update calls verified; non-Google tags have consent checks
- [ ] Event/trigger names matched exactly (case-sensitive)
- [ ] Duplicate sources ruled out (second snippet, plugin, enhanced measurement, multiple triggers)
- [ ] Fixes list the exact place and change, with data layer or consent code where needed
- [ ] Verification steps cover Preview, DebugView/Events Manager/Ads, consent denied and granted, and published version
- [ ] Root cause stated with a confidence level and open questions listed
