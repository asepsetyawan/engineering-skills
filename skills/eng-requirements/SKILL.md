---
name: eng-requirements
description: "Turn product needs into scope, business rules, acceptance criteria, and testable delivery slices. Use when requirements are ambiguous, a feature needs decomposition, or a team needs a specification before implementation."
---

# Engineering Requirements

Produce a specification sufficient to make decisions and verify behavior, without turning it into a complete technical design before one is needed.

## Discover the actual requirements

Inspect user flows, available issues or specifications, contracts, and current project behavior. Separate explicit needs, evidence of existing behavior, and assumptions. Do not turn an example into a universal requirement or invent stakeholder approval.

Identify users or actors, goals, triggers, prerequisites, observable outcomes, and access or tenant boundaries. Find invariants that must hold: for example, a slot cannot be confirmed twice, or a refund cannot exceed the payment.

Ask only about ambiguities that change scope or correctness. Label unspecified latency, traffic, budget, SLA, and retention figures as proposed targets or assumptions, rather than facts.

## Specify verifiable behavior

- Express acceptance examples as input or conditions → action → outcome. Use Given/When/Then when it helps communication, rather than as a mandatory format.
- Include failure paths, authorization, retries or duplicates, and concurrency when they affect the domain. A simple wording change does not need the entire list.
- Define user-visible states and lifecycles, and who owns decisions at each transition.
- Separate current scope, agreed exclusions, and open questions. Do not add an unsolicited feature backlog.

## Break down delivery

Choose vertical slices that deliver an outcome, rather than isolated database, backend, and frontend layers without integration. Identify contract and data dependencies, migration needs, and relevant acceptance checks for each slice.

Use the [specification template](assets/specification.md) only when the user requests a specification document or coordination requires a saved artifact. Complete or remove irrelevant sections; do not leave placeholders.

## Result

Provide scope, rules and invariants, acceptance criteria, material assumptions, and the next implementation step. When the task is already clear, summarize briefly and continue the requested work.

Example: `$eng-requirements Turn this expense approval idea into an MVP scope and acceptance criteria.`
