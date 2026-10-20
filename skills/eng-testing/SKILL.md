---
name: eng-testing
description: "Plan and run behavioral verification for features, bug fixes, contracts, or regressions. Use for focused test strategies, integration and concurrency tests, failing tests, or evidence gaps, rather than coverage without a purpose."
---

# Engineering Testing

Start with the behavior to prove, change risks, and the project's commands and frameworks. Tests should fail when a contract or invariant is violated, rather than merely when internal implementation details change.

## Choose the level of evidence

| Risk | Usually the most direct evidence |
|---|---|
| Pure domain rules | Unit tests with inputs and boundaries that distinguish outcomes |
| SQL, constraints, and transactions | Integration tests against the relevant database engine |
| Service interfaces | Contract and compatibility tests, plus transport integration |
| Races or duplicate effects | Concurrent operations with relevant interleavings |
| Important user journeys | Component or end-to-end tests of actions and outcomes |
| Throughput or latency | Load experiments with datasets, warmup, and documented conditions |

Select a subset appropriate to the task. Wording edits or small reversible changes do not automatically require new tests. Coverage helps identify untouched areas; it does not prove correctness.

## Build distinguishing cases

For bug fixes, reproduce the failure before the change when possible, then prove the same condition works afterward. Distinguish product failures from an unavailable environment or test harness.

Use controlled clocks, seeds, or fixtures when they affect determinism. Mock collaborators at appropriate boundaries; do not mock the component whose semantics are under test. Avoid fixed sleeps for concurrency coordination when signals, barriers, or bounded polling are available.

Define observable acceptance: final state, response, side effects, duration or deadline, or an invariant. For asynchronous work, await completion with a clear timeout. Do not hide flaky behavior with blind retries or increase timeouts without finding the cause.

## Run and interpret

Start with checks appropriate to the change, then run required project checks. Broaden testing when failures or unverified boundaries warrant it. Do not rerun the same suite without a change or new question.

Distinguish static checks, unit or mock tests, local integration, staging, and production runtime. If facilities are unavailable, report commands that failed or were not run, and how that limits the conclusion. Do not report passed tests from a plan or old output.

Report verified behavior, actual commands, results, and material gaps. Avoid unmeasured percentages or benchmarks.

Example: `$eng-testing Prove that retrying an order request does not create two transactions.`
