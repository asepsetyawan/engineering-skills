---
name: eng-database
description: "Design or change schemas, SQL, transactions, indexes, migrations, and caches based on queries and business invariants. Use for data correctness, slow queries, concurrency, or persistence evolution."
---

# Engineering Database

Inspect the database engine and version, schema, migration tools, data access, known volume and distribution, and actual queries. Use the project's dialect. Choose SQL or NoSQL based on transactions and access patterns, rather than JSON-shaped data.

## Model and invariants

Define ownership and tenants, keys, relationships, lifecycles, and business constraints. Connect indexes to actual predicates, joins, and ordering, and explain write and storage costs. Choose money and timestamp types according to the domain; do not use floating point for money requiring exact precision.

Read-check-write can fail under concurrency. Evaluate atomic conditional updates, constraints, locking, or isolation based on the engine. Locking one row does not automatically prevent races involving rows that do not yet exist.

For inventory, a conditional update using `stock >= requested` and a check of the affected row count can form part of a correct transaction. For bookings, the mechanism depends on discrete slots versus time intervals; a unique slot key does not solve arbitrary interval overlap.

Explain deadlock or serialization retries when needed. Redis locks do not replace database invariants; lease expiry and stale owners may require fencing at the protected resource. Read replicas can lag and are not backups.

## Queries and migrations

Use query plans and representative data to distinguish estimates from evidence. `EXPLAIN ANALYZE` executes the query; check context and authorization, especially for writes or expensive queries. Do not index every column without a hypothesis and supporting plan.

For schema changes in running applications, consider expand → incremental backfill → switch → contract. Check null or duplicate data, locks and rewrites, backfill resumability, and compatibility during staggered deployments. A down migration that drops columns is not data recovery.

## Caching and recovery

Define key namespaces and tenant scope, TTLs, invalidation, misses and stampedes, and the source of truth. Invalidation after commit can still allow stale refills; choose versioning or reconciliation when correctness requires it. Do not make a cache authoritative for confirmations with strong invariants without an adequate mechanism.

Backups and PITR need retention and restore tests. Do not claim RPO or RTO from configuration alone. A design or local migration request does not authorize writes to a live database.

## Evidence

Provide the requested schemas, queries, or migrations, the rationale for indexes and transactions, compatibility risks, and actual verification. Claims of preventing double booking need concurrent tests against the relevant engine, rather than mocks or sequential tests alone.

Example: `$eng-database Prevent double booking for discrete slots using constraints and verified transactions.`
