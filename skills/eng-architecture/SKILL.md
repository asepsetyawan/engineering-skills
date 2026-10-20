---
name: eng-architecture
description: "Design or review module and service boundaries, data ownership, dependency direction, and architecture decisions. Use for application structure, clean or hexagonal architecture, bounded contexts, service extraction, or ADRs; detailed capacity planning belongs to system design."
---

# Engineering Architecture

Start with business invariants, changes the design must support, team and data ownership, transaction boundaries, and project constraints. Inspect the actual implementation before asserting component relationships or dependencies.

## Choose boundaries

For each changed boundary, show who owns business rules and data, exposed contracts, dependency direction, and one use case including failures. Use a simple diagram when it clarifies relationships; a single function does not need a system diagram.

- **Modular monolith:** separate module ownership and dependencies without requiring separate deployments. Evaluate actual coupling, rather than folder size alone.
- **Microservices:** require a reason such as independent releases or scaling, isolation, or ownership. Include the costs of network failures, contract evolution, observability, and cross-service consistency.
- **Clean or hexagonal architecture:** use ports at boundaries that need substitution or isolation; do not automatically create interfaces and mapping layers for every class.
- **DDD:** bounded contexts follow domain language and invariants. Aggregate boundaries follow consistency needs, rather than every entity relationship.

Compare relevant options against requirements and the team's operational capabilities. Do not impose a favorite architecture on simple CRUD or assume high traffic automatically requires microservices.

## Plan the change

Map affected callers and contracts. When extracting a module or service, explain temporary ownership, data migration, cutover, compatibility, and recovery. Avoid dual writes without explicit consistency and reconciliation mechanisms.

Use an implementation sketch or vertical slice to test the boundary before a broad refactor. Do not modify code when only analysis was requested.

## Decisions and evidence

For decisions across teams or changes that are difficult to reverse, use the [ADR template](assets/adr.md) when a saved artifact helps. Mark proposed or accepted according to the actual decision; do not invent approval.

At minimum, provide context, the choice and rationale, consequences, affected files or components, and a way to validate the boundaries. State what would trigger reconsideration.

Example: `$eng-architecture Evaluate whether the payment module should become an independent service.`
