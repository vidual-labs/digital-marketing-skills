---
name: gtm-debugging
description: Use when diagnosing and fixing Google Tag Manager (GTM) bugs — missing triggers, broken tags, variable misconfiguration, event tracking failures, and data layer issues.
version: 1.0.0
author: Hermes Agent
license: MIT
metadata:
  hermes:
    tags: [GTM, google-tag-manager, debugging, analytics, datalayer, event-tracking, GA4]
    related_skills: [landing-page-funnel, google-ads-diagnostics, meta-ads-diagnostics]
---

# Google Tag Manager Debugging

## Overview

Diagnose and fix GTM bugs — from missing triggers and broken tags to data layer misconfigurations and event tracking failures. This skill gives you a systematic approach to finding, reproducing, and resolving GTM issues with concrete fix instructions.

## When to Use

- Events not firing (page views, clicks, form submissions, e-commerce)
- GA4, Meta Pixel, or conversion tags not sending data
- Data layer variables returning wrong values or "undefined"
- Triggers not firing at the expected moment
- Duplicate events firing multiple times
- Cross-domain or subdomain tracking issues
- Server-side GTM configuration problems

Don't use for: Analytics reporting (use platform-specific diagnostics), campaign performance analysis, or SEO technical audits.

## Diagnostic Framework

### Phase 1: Is the GTM Container Loading?

First and fastest check — if GTM itself isn't on the page, nothing else matters.

**Check:**
1. Open browser DevTools → Console tab → reload page
2. Look for `Google Tag Manager` in console (silent load) or check for errors
3. Inspect page source — search for `GTM-XXXXXX`
4. Check Network tab → filter "googletagmanager.com" — should see gtm.js load

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| `GTM-XXXXXX` not in source | GTM snippet not installed or broken | Add GTM container snippet immediately after `<head>` open tag |
| `gtm.js` in Network but errors | Script blocked by CSP, ad blocker, or DNS | Check Content-Security-Policy header; whitelist `googletagmanager.com` |
| Snippet present, but no tags firing | Data layer not defined before snippet | Add `window.dataLayer = window.dataLayer || [];` before GTM snippet |

**Critical rule:** The data layer must be declared *before* the GTM snippet:

```html
<head>
  <script>
    window.dataLayer = window.dataLayer || [];
    dataLayer.push({
      'userId': '12345',
      'isMember': true
    });
  </script>
  <!-- Google Tag Manager -->
  <script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
  new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
  j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
  'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
  })(window,document,'script','dataLayer','GTM-XXXXXX');</script>
  <!-- End Google Tag Manager -->
</head>
```

### Phase 2: Debug with GTM Preview Mode

GTM's built-in debug mode is the single most useful tool. Run it before any fix.

**Activate:** `https://tagassistant.google.com/snippet/gtm-XXXXXX` or use the GTM Chrome extension.

**Preview shows (3-column layout):**
- **Page:** The live site
- **Tags:** Which tags fired / didn't fire on this page/event
- **Triggers:** Which triggers fired / didn't fire (this is where 80% of bugs live)
- **Variables:** Current values of all variables at the moment of firing

**Debug workflow:**
1. Open preview on the relevant page
2. Perform the action (click button, submit form, scroll 50%)
3. Right panel → Triggers tab → check which should-have-fired triggers are marked "Not fired"
4. For a fired trigger → click it → inspect the conditions, variable values, and event type
5. For a tag that didn't fire → check which trigger was blocking it, and which variables it needed

### Phase 3: Trigger Diagnostics

| Problem | Diagnostic | Fix |
|---------|-----------|-----|
| **Custom Event trigger** — event not firing | Check if `dataLayer.push({'event': 'yourEvent'})` is actually called on the page. Add `console.log` before the push. | Ensure event name in GTM trigger matches exact string in dataLayer push (case-sensitive, including spacing) |
| **Click All Elements** — not capturing click | Check if clicked element is removed/replaced by JS before GTM processes it. | Switch to "DOM Elements Only" or "Just Clicked Element" — or use "Event Listener" mode |
| **Form Submission** — not firing | Google's "Form Submission" has specific element selection logic. AJAX forms often skip it. | Use "Click — All Elements" with a filter on form submit buttons, or implement custom JS listener |
| **Scroll Depth** — not firing at expected point | Scroll threshold calculation uses document height, which may be wrong for dynamically loaded content. | Recalculate scroll depth with JS that accounts for dynamic content. Use IntersectionObserver for accuracy |
| **Page View** — firing on wrong pages | Page URL trigger condition too loose or wrong operator | Use "Matches Regex" for complex patterns. Test against the actual URL pattern |
| **History Change** — SPA navigation | SPA routing that doesn't fire `historyChange` | Add custom trigger: use `pushState`/`replaceState` observer or push `{'event': 'pageView'}` on route change |
| **Timer trigger** — not reliable | Timer uses `setTimeout` which may be blocked or delayed | Switch to `setInterval`-based approach if reliability is critical |

### Phase 4: Variable Misconfiguration

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Data layer variable returns "undefined" | Variable name in GTM doesn't match exact string in data layer | Check case and spacing. `userId` ≠ `userid`. Use GTM preview to see what data layer actually contains |
| DOM element variable is null | Element not yet in DOM when GTM evaluates | Switch to "Wait for tags" or add a delay. Or switch to a click-specific trigger |
| 1st-party cookie variable empty | Cookie domain / path misconfigured | Check cookie path is `/` and domain matches (or use `.` for all subdomains) |
| URL variable returning full URL | You selected "Page URL" but need path, hostname, or query | Switch variable type to the specific part: "Hostname", "Page Path", "Query" |
| Auto Event — Click ID always empty | Clicked element has no `id` attribute | Use Click Classes, Click Text, or Click URL instead. Or add IDs to the element. |

**Data layer variable naming convention:**
- Always use `{{DLV - variableName}}` — be explicit it's a data layer variable
- Use dot notation for nested objects: `{{DLV - product.price}}`

### Phase 5: Tag Firing Issues

| Problem | Diagnostic | Fix |
|---------|-----------|-----|
| **GA4 config tag** not firing on all pages | Trigger set to "Some Page Views" with wrong condition, or missing entirely | Set to "All Pages" trigger |
| **GA4 event tag** firing duplicate events | Multiple triggers attached (e.g., "All Pages" + custom event that also fires on page load) | Remove redundant triggers. Ensure mutual exclusivity |
| **Meta Pixel** not firing | Pixel ID wrong, or trigger not matching, or consent blocker active | Verify pixel ID in tag config. Check trigger in preview. Verify consent mode status |
| **Server-side GTM** — events not forwarded | Server container not listening, or macro variable misconfigured | Check server container tags → "Forwarding Request" tag is firing. Verify cloud logs for errors |
| **Enhanced E-commerce** — product data missing | `ecommerce` or `event` data layer structure incorrect | Validate the data layer against the GA4 e-commerce spec (`items` array, `item_id`/`item_name`, event-scoped `ecommerce` object) |

### Phase 6: Consent & Ad Blockers

Consent management is the #1 silent cause of "nothing is tracking."

| Symptom | Cause | Fix |
|---------|-------|-----|
| Tags fire in preview but not in production | Consent mode blocking tags (user hasn't consented, or Consent Manager tag fires in wrong order) | Ensure Consent Mode v2 configuration. Check tag firing order — consent must resolve before any tracking tag fires |
| No data in GA4 during normal browsing | Ad blocker or Privacy Badger blocking `googletagmanager.com` or `google-analytics.com` | Test with ad blocker disabled. Consider consent-first deployment pattern |
| Meta Pixel fires but GA4 doesn't (or opposite) | Third-party cookies consent granted for one, blocked for another | Check both tags fire under the same consent trigger. Verify both have consent settings configured in GTM |
| Consent tag fires too late | Consent Manager loads after GTM container | Load consent script inline *before* GTM snippet, or use `cookieExists` check before GTM loads |

**Consent Mode v2 minimum config for GTM:**
```javascript
// Data layer push before GTM loads
window.dataLayer = window.dataLayer || [];
dataLayer.push({
  'consent': {
    'ad_storage': 'denied',      // or 'granted' based on consent
    'analytics_storage': 'denied',
    'ad_user_data': 'denied',
    'ad_personalization': 'denied',
    'functionality_storage': 'granted'
  }
});
```

### Phase 7: Common Patterns to Fix

#### E-commerce event tracking (Google Analytics 4)

```javascript
// Add to cart
dataLayer.push({
  'event': 'add_to_cart',
  'ecommerce': {
    'items': [{
      'item_id': 'SKU-123',
      'item_name': 'Product Name',
      'item_category': 'Category',
      'price': 29.99,
      'quantity': 1
    }]
  }
});

// Purchase
dataLayer.push({
  'event': 'purchase',
  'ecommerce': {
    'transaction_id': 'TX-98765',
    'value': 59.98,
    'currency': 'USD',
    'tax': 5.00,
    'shipping': 4.99,
    'items': [{
      'item_id': 'SKU-123',
      'item_name': 'Product Name',
      'item_category': 'Category',
      'price': 29.99,
      'quantity': 2
    }]
  }
});

// Generate lead
dataLayer.push({
  'event': 'generate_lead',
  'lead': {
    'source': 'contact_form',
    'plan': 'enterprise'
  }
});
```

**GTM tag config for these events:**
- Trigger: Custom Event, event = `add_to_cart` (or `purchase`, `generate_lead`)
- Tag type: GA4 Event, Event name = same as dataLayer event
- Enable enhanced measurement in the GA4 config tag

#### Cross-domain tracking (GA4)

**Linker configuration:**
1. In GA4 Config tag → Config Settings → Linker Domain Settings: add the second domain
2. On cross-domain links → fire a "Linker" tag with trigger on click that goes to the other domain
3. Verify both sites have the GA4 config tag with the linker domain configured

**Debugging cross-domain:**
- Check `__ga` parameter is appended to outbound links
- Check `_gl` parameter for session-level tracking
- In GA4 DebugView, verify user_id or client_id persists across domains

#### Fixing duplicate events

When the same event fires twice:

1. In GTM preview → check how many times the tag fires per action
2. Check all triggers attached to the tag — is there more than one?
3. Check if the dataLayer event fires multiple times (add `console.log` on the push)
4. If it's a click trigger — is it on "All Elements" but also on a parent element that shares classes?
5. Fix: make triggers mutually exclusive. Use the most specific trigger level (Click ID > Click Classes > All Elements)

### Phase 8: DebugView and Real-Time Verification

After implementing fixes in GTM:

1. **Publish** the container (or use unlisted version for testing)
2. Open GA4 → DebugView (left sidebar)
3. Perform the action on the site (with GTM preview mode active)
4. Verify the event appears in DebugView within 10-30 seconds
5. Check the event parameters are correct and complete

## Output Format

```
GTM DIAGNOSIS: [Site URL]
Container ID: GTM-XXXXXX
Issue Reported: [Description]

--- FINDINGS ---

1. CONTAINER LOAD: [OK / BROKEN — detail]

2. DATA LAYER:
   [Issues found — missing variables, wrong naming, structural problems]

3. TRIGGER ISSUES:
   [Trigger name] — [Problem] → [Fix]

4. TAG ISSUES:
   [Tag name] — [Problem] → [Fix]

5. CONSENT: [OK / Blocking — detail]

6. SPECIFIC FIXES:

   FIX 1: [Name]
   Where: [Tags / Triggers / Variables / Data Layer]
   Change: [Exact configuration change]
   Data layer code (if needed): [code block]

   FIX 2: [Name]
   ...

--- VERIFICATION STEPS ---
1. [Step to verify fix 1]
2. [Step to verify fix 2]
```

## Common Pitfalls

1. **Not using preview mode first.** Guessing at bugs without preview mode is blind debugging. Always start there.

2. **Publishing before verifying.** Edit, test in preview, THEN publish. Never publish and hope.

3. **Case sensitivity.** Data layer event names, variable names, and filter matching are all case-sensitive. `FormSubmit` ≠ `formsubmit`.

4. **Assuming the click is the element it looks like.** Shadow DOM, iframes, and SPA re-renders mean the actual clicked element may differ. Use "Just Clicked Element" to see the truth.

5. **Not checking consent mode.** Tags silently failing due to consent is the hardest to debug because preview mode *will* show them firing (consent is bypassed in preview). Production behavior differs.

6. **Not checking server console for GTM errors.** `window.dataLayer is not defined` or `dataLayer.push is not a function` errors in the browser console tell you exactly what's wrong. Always check console.

7. **Forgetting to publish.** Changes in GTM only exist in the working (unpublished) container until you publish. Preview shows the working container — production sees the published one.

## Verification Checklist

- [ ] Container loads correctly (snippet in source + gtm.js in network)
- [ ] Data layer defined before GTM snippet
- [ ] Preview mode used to diagnose (not guessing)
- [ ] Browser console checked for errors
- [ ] Event names match exactly (case-sensitive) between data layer and triggers
- [ ] Consents verified in real user context (not just preview mode)
- [ ] Changes tested in preview before publishing
- [ ] Published version verified against DebugView/analytics tool
- [ ] Specific data layer code provided when JS changes are needed
- [ ] Verification steps included for developer to confirm fix
