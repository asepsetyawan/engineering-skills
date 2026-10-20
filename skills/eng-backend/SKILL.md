---
name: eng-backend
description: "Implement or fix REST and gRPC APIs, business logic, workers, and service integrations. Use for concrete backend changes involving contracts, error handling, concurrency, and behavioral verification."
---

# Engineering Backend

Inspect runtime versions, frameworks, callers, contracts, domain structure, and project tests. Follow existing conventions; do not migrate the stack to solve a focused task.

## Define contracts and invariants

Determine caller-visible inputs, outputs, and errors. Use existing OpenAPI, Protobuf, or schemas as the source of truth. Change generated code through the project's generator workflow, rather than treating generated files as primary sources; state when the generator is unavailable.

Place business rules and invariants at the appropriate boundary. Handler validation does not replace database constraints under concurrency. Separate transport parsing, domain logic, and SDKs where the boundary helps, without imposing excessive layers.

## Get behavior right

- Authentication establishes identity; authorization checks resources and tenants along the actual access path. A client-supplied tenant ID is not evidence of permission.
- For write retries, define semantic idempotency: key scope, payload conflicts, concurrent duplicates, response replay, and retention when needed.
- Propagate cancellation and deadlines to dependencies; all calls must fit the request budget. Bound queues and concurrency, and define overload responses when relevant.
- Pagination needs stable ordering and a tie-breaker. Cursors are not mandatory for every endpoint.
- External side effects do not participate in a database rollback. Choose outbox, compensation, or reconciliation based on invariants and provider contracts.
- Workers need acknowledgment or commit points, duplicate handling, poison message behavior, and replay appropriate to their business effects.

When changing contracts, check caller compatibility and staggered deployments. Do not expose internal errors, secrets, or cross-tenant details in responses or logs.

## Implement and verify

Complete the requested vertical slice, including required configuration, migrations, and wiring. Mock routes or stub persistence are not a completed implementation when the task requires real integration.

Choose domain unit tests, transport or database integration tests, contract tests, or concurrency tests based on risk. For timeout or retry changes, test dependency failures and cancellation; happy-path mocks alone are insufficient. Use actual project commands and distinguish unit or static checks from runtime integration not yet run.

Report changed behavior, key contracts and files, verification evidence, and material limitations.

Example: `$eng-backend Implement an idempotent order endpoint with consistent error mapping.`
