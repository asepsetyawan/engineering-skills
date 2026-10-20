---
name: eng-frontend
description: "Implement or fix interfaces, components, state, forms, rendering, and API integration. Use for frontend user journeys that need responsive, accessible behavior verified across real states."
---

# Engineering Frontend

Start with user journeys and the actual codebase: framework versions, component system, styling, routing, API client, and tests. Preserve the project's language and design system; use specialized visual design guidance when available and relevant to the task.

## Ownership and state

Define user actions, data sources, visible outcomes, and completion conditions. Implement relevant loading, empty, error, success, pending submission, and retry states.

Separate local UI state, shareable URL state, fetched or cached server state, and form state. Do not duplicate sources of truth across stores. Asynchronous search needs stale-response protection; debouncing alone does not prevent response races.

Use existing backend contracts. Client validation improves the experience, but the server remains responsible for validation and authorization. Do not put secrets in client bundles or silently change APIs to fit mocks.

For optimistic updates, explain rollback or reconciliation, conflicts, and duplicate submissions. Avoid automatic retries for operations that are unsafe to repeat. Choose SSR, SSG, or CSR based on SEO, freshness, and runtime needs; a static application does not automatically need server rendering.

## Make the interface usable

Use semantic elements, input labels, keyboard navigation, and appropriate focus management. Loading and error states that affect interaction should be understandable to assistive technology users. Check long text and relevant screen sizes, rather than only the default desktop happy path.

Preserve user data such as drafts, notes, bookmarks, and localStorage during refactoring. Changes to storage keys or schemas need intentional compatibility or migration.

For optimization, measure the reported repeated requests, bundle size, images, rendering, or interaction delays. Global memoization without profiling is not evidence of improvement.

## Verification and result

Exercise user journeys, including relevant error and empty states, and run project build, type, and lint checks. Screenshots demonstrate appearance, rather than interaction. Choose component or end-to-end tests for important regressions; manual flow verification can be sufficient for small changes according to their risk.

Report UI outcomes, actual integrations versus mocks, viewports and interactions checked, and checks that could not be performed.

Example: `$eng-frontend Build a checkout form with validation, pending submission, server errors, and keyboard navigation.`
