---
name: eng-reliability
description: "Diagnose errors, latency, saturation, and incidents; design SLIs, SLOs, observability, recovery, or reliability experiments. Use for runtime and operational issues needing evidence, rather than choosing an initial architecture."
---

# Engineering Reliability

Start with user impact, the time window, environment, recent changes, and available evidence. Determine whether the task calls for diagnosis only, code fixes, or live mitigation that has actually been authorized.

## Diagnose with hypotheses

Connect symptoms to request paths and dependencies. Compare latency, errors, traffic, and saturation before and after changes when data is available. Separate queue time, service time, and dependency time when assessing p95 or p99; averages can hide tail latency.

Form hypotheses that logs, metrics, traces, query plans, or focused experiments can distinguish. Correlation with a deployment does not prove root cause. Separate causes, contributing factors, and unknowns.

During incidents, prioritize recovery within the authorized scope while preserving evidence. Every action needs an expected signal and an evaluation time limit; stop repeating mitigations that do not help or increase risk.

## Reliability by journey

SLIs and SLOs must define good and bad events, denominators, windows, and justified exclusions. Do not combine availability, latency, and business success without definitions. Alerts should identify impact and an operator action; avoid high-cardinality metric labels.

Choose timeouts, retries with backoff and jitter, concurrency limits, bounded queues, and load shedding based on failure modes. Retries without a budget can worsen overload. Prove relevant degraded behavior under dependency failures.

Distinguish high availability, backups, and regional recovery. RTO and RPO remain targets until restore or failover is measured; read replicas do not replace backups. Do not run chaos or failure injection against live services without appropriate scope and authorization.

## Runbooks and results

Use the [runbook template](assets/runbook.md) when the task needs a saved operational procedure. Fill in service-specific signals, actions, and recovery; do not invent production commands or on-call contacts.

Report impact, evidence, actions actually performed, signal changes, proven root causes or remaining hypotheses, and next fixes. Do not declare an incident resolved from one successful request while the affected journey remains impaired.

Example: `$eng-reliability Investigate an API p99 increase after deployment and choose the quickest experiment to distinguish likely causes.`
