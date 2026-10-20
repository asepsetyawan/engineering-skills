---
name: eng-workflow
description: "Deliver software features or changes across requirements, implementation, and verification. Use for end-to-end requests, rather than conceptual questions or clearly scoped tasks within a single discipline."
---

# Engineering Workflow

Turn requests that span engineering disciplines into working results with traceable decisions and verification evidence. Run only the stages the task needs; small tasks do not require the entire lifecycle.

## Establish scope and context

Check workspace instructions, the target repository or folder, unfinished user changes, the stack and versions, contracts, tests, and project run commands. Use English by default unless the user explicitly requests another language. Follow project conventions. Distinguish examples, assumptions, and measurements.

Identify the user outcome, acceptance criteria, and business invariants before designing a solution. Ask only for information that affects a decision and is not already available. When part of the request is unclear, continue independent work and state safe assumptions.

## Select relevant stages

The following skills are optional specialists, not required dependencies. When available, read relevant `SKILL.md` files from sibling folders or the skill catalog; do not load the entire collection. If a specialist is unavailable, handle that stage directly using project context. Using a specialist does not automatically mean spawning a subagent.

| Need | Skill |
|---|---|
| Requirements and acceptance criteria | `$eng-requirements` |
| Boundaries, ownership, and ADRs | `$eng-architecture` |
| Patterns and code refactoring | `$eng-design-patterns` |
| Capacity and distributed behavior | `$eng-system-design` |
| Service, API, or worker implementation | `$eng-backend` |
| UI implementation and integration | `$eng-frontend` |
| Schemas, transactions, SQL, and caching | `$eng-database` |
| Behavioral evidence and regression checks | `$eng-testing` |
| Security assessment or sensitive boundaries | `$eng-security` |
| Builds, CI/CD, IaC, and releases | `$eng-delivery` |
| Incidents, performance, SLOs, and recovery | `$eng-reliability` |
| Change review | `$eng-code-review` |
| Documentation of the work | `$eng-documentation` |

## Execution and handoff

For longer work, keep concise notes on scope, decisions, dependencies between changes, acceptance criteria, and check results. Use available task tracking; do not automatically create a document for every task.

Build a verifiable vertical slice before expanding other parts. Contract and schema changes must remain compatible with callers and the planned deployment order. Do not add frameworks, layers, services, or processes without a benefit that matches the need.

Carry the required context across boundaries: current contracts, invariants, completed changes, test evidence, and remaining work. Keep a single source of truth for data and decisions; do not introduce conflicting assumptions across disciplines.

Close acceptance criteria with suitable checks and identify checks not run. An end-to-end request does not automatically grant production access, publishing authorization, or permission to send messages. Follow existing authorization without asking again; prepare a reviewable result before external actions that require a user decision.

## Final result

Report completed behavior, key files, material decisions, actual verification, and remaining gaps. Do not claim production readiness from mocks or static validation, or mark the entire task complete while the main user journey remains unverified.

Example: `$eng-workflow Build a booking feature across the API, database, and UI, then verify it locally.`
