---
name: eng-design-patterns
description: "Choose, explain, or refactor design patterns for concrete code problems. Use for Strategy, Adapter, Factory, Repository, domain events, outbox, Saga, CQRS, and coupling reduction; do not impose a pattern catalog on an application."
---

# Engineering Design Patterns

Explain the problem before naming a pattern. Inspect behavioral variation, coupling, recurring changes, and existing tests. Also consider a simple function or branch that may be sufficient.

## Decision map

| Problem | Candidate | Decision boundary |
|---|---|---|
| Multiple discount or shipping policies | Strategy | Actual behavioral variants, rather than one implementation that has not changed |
| Different vendor contracts | Adapter | Normalize inputs, outputs, and errors at the boundary |
| Variable collaborator construction | Factory or composition root | Do not hide simple construction without a benefit |
| Domain tied to persistence details | Repository or port | Direct ORM use can be clearer for simple CRUD |
| State and events must be recorded atomically | Transactional outbox | Commit state and outbox together; the relay may still duplicate messages |
| A business process spans services | Saga | Compensation is not a database rollback and can fail |
| Reads and writes have different needs | CQRS | Separate models only when the benefit exceeds synchronization costs |

Dependency injection wires collaborators; it is not a reason to add a container or framework. An in-process observer has different semantics from a durable broker. CQRS does not require event sourcing.

## Demonstrate the refactor

Show a caller example and behavior before and after the change. Preserve public contracts and error semantics unless their change is requested. Separate structural refactoring from business behavior changes so regressions can be identified.

Put abstractions at boundaries with demonstrated variation. Avoid base classes, service locators, or interfaces for every function merely to apply a pattern. For distributed patterns, explain relevant durability, ordering scope, retries, deduplication, and failure paths.

Verify the behavior that must remain intact and one example of variation that becomes easier to support. Do not write tests that merely assert class names or pattern structure.

## Result

Provide the problem, the simplest sufficient choice, rationale, consequences, an application example, and behavioral evidence. For a conceptual question, use one concrete example and explain when the pattern is unnecessary.

Example: `$eng-design-patterns Refactor two payment provider integrations so vendor contracts do not leak into business logic.`
