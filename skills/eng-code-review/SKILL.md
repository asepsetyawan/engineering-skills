---
name: eng-code-review
description: "Review diffs or code changes for bugs, regressions, compatibility, data loss, and verification gaps. Use when a user requests change review, rather than unsolicited refactoring or a full audit."
---

# Engineering Code Review

Identify the requested revision, diff, and scope, then read project instructions, related files, callers, contracts, and tests needed to assess the change. Do not assume a small diff requires reviewing the entire codebase.

## Find explainable failures

Prioritize correctness, data loss, authorization, concurrency, backward compatibility, and error or failure behavior. Trace inputs and states that trigger an issue; style preferences are not bugs unless they violate a contract or applicable project instructions.

Check changes to public APIs or schemas, ordering and transactions, cancellation and retries, UI state, configuration defaults, and release sequencing as appropriate to the diff. Trace generated files to sources or generators when they affect behavior.

Use focused checks or reproductions when needed to assess a claim. Do not fix code during a review-only task. When review and fixes are both requested, perform both while preserving initial evidence and results after the change.

## Filter findings

Each finding needs a precise location, triggering conditions, plausible impact, and an explanation of how the change introduces or worsens it. Explain required assumptions and verify callers when available before concluding that a contract is wrong.

Do not present hypothetical risks without a code path as proven bugs. Separate pre-existing issues when needed for context; do not incorrectly attribute them to the diff.

Prioritize by impact and likelihood, rather than finding count. If the project does not define priorities, use critical, high, medium, or low, clarifying their meaning briefly when ambiguous.

## Result

Order actionable findings by impact, with locations and suggested fixes. Include questions or assumptions that determine conclusions and summarize checks actually performed. If no findings exist, say so and state material verification gaps; do not pad the report with praise or nitpicks.

Example: `$eng-code-review Review this checkout change for duplicate payments and API compatibility.`
