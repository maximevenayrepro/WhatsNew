---
description: Frontend rules for UI, accessibility, state, and DOM manipulation
globs: "public/**/*.js,public/**/*.html,public/**/*.css"
alwaysApply: true
---
# Frontend UI and Accessibility

## Overview
This rule promotes a clear, responsive UI with accessible interactions, minimal but structured JS state, and careful DOM updates.

## Rule: Accessible, performant frontend
1. **Always** provide keyboard accessibility (Esc to close modal, focus trap inside modal).
2. **Always** manage state explicitly (`selectedTopics`, `newsByTopic`, `isLoading`).
3. **Never** block the main thread; update DOM in batches where possible.
4. **Always** persist `selectedTopics` in `localStorage`.
5. **Always** show empty/error states with friendly messages.

## Common Violations and Solutions

### ❌ BAD: Modal without focus management
```html
<div id="modal"> ... </div>
```

### ✅ GOOD: Accessible modal behavior
```javascript
function openModal() {
  // trap focus, restore on close, Esc to close
}
```

### ❌ BAD: Direct DOM updates inside tight loops
```javascript
items.forEach(item => container.appendChild(renderItem(item)));
```

### ✅ GOOD: Use document fragments
```javascript
const fragment = document.createDocumentFragment();
items.forEach(item => fragment.appendChild(renderItem(item)));
container.innerHTML = '';
container.appendChild(fragment);
```

## When You Think You Need Exceptions
### Small lists (<5 items)
Direct appends are acceptable; keep code simple but readable.

## Specific Project Patterns
```javascript
// ✅ GOOD: Keep rendering pure and separate from event wiring
function renderNewsSection(topic, items) { /* ... */ }
```

## Alternative Solutions
### 1. Minimal templating with tagged templates for readability
### 2. Small helper to manage event delegation on result lists

## Tool Configuration (Optional)
```json
{
  "ui": {
    "enableFocusTrap": true
  }
}
```

## Checklist for the Assistant
- [ ] Implement accessible modal interactions (Esc, focus trap)
- [ ] Manage and persist `selectedTopics` in `localStorage`
- [ ] Batch DOM updates to avoid jank
- [ ] Provide clear empty/error states


