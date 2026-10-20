---
name: eng-system-design
description: "Design end-to-end systems with workloads, capacity estimates, data flows, consistency, scaling, and failure handling. Use for new system designs or bottleneck analysis across components, rather than internal changes to a single function."
---

# Engineering System Design

Start with user journeys, invariants, workloads, latency and availability targets, budget, and operational capabilities. Separate supplied figures from design assumptions. Do not choose technology before the needs that distinguish the options are clear.

## Estimate relevant capacity

Show units and distinguish averages, peaks, and concurrency limits:

- Average requests/s = daily requests / 86,400; a peak factor needs its own assumption.
- In-flight requests ≈ throughput/s × latency in seconds under stable conditions.
- Storage ≈ writes/s × record size × retention in seconds; identify omitted index and replica overhead.
- Video delivery ≈ concurrent viewers × bitrate. 10,000 × 4 Mb/s = 40 Gb/s, or roughly 5 GB/s before overhead; this is not automatically API or origin bandwidth.

Concurrent users are not QPS without an action and request model. Separate CDN, API, worker, and database load. Request-based and byte-based cache hit rates are not necessarily equal.

## Trace the design

Describe main read and write paths, data-owning components, API and event contracts, access boundaries, and user-visible states. Define consistency requirements per operation; delayed search results differ from stock or booking confirmation.

For asynchronous flows, explain relevant delivery semantics, ordering scope, consumer idempotency, backlog and backpressure, poison messages, and replay. Do not promise exactly-once effects merely because a broker supports transactions.

For synchronous dependencies, define deadline budgets, safe retries, concurrency limits, and degraded behavior. A circuit breaker does not replace timeouts or capacity planning.

Start with a baseline that meets current requirements. Connect caches, replicas, partitioning, or service extraction to a specific bottleneck and a way to measure it. Show simpler alternatives and the operational cost of the selected option.

## Recovery and evolution

Connect SLIs and SLOs to the main journey. Distinguish high availability, backups, and regional disaster recovery. Label RTO and RPO as targets until failover or restore has been tested.

Deliver assumptions, decision-relevant calculations, necessary flows or diagrams, core contracts and data, trade-offs, failure handling, and the next vertical slice or validation experiment. Do not claim implementation or benchmarks for a hypothetical design.

Example: `$eng-system-design Design a notification platform with traffic bursts and safely repeatable delivery.`
