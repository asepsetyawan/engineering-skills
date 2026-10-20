---
name: eng-delivery
description: "Build or fix reproducible builds, containers, CI/CD, infrastructure as code, and releases. Use for delivery automation, environment configuration, promotion, or deployment preparation; this does not automatically authorize live deployment."
---

# Engineering Delivery

Inspect existing pipelines, runtimes, artifacts, environments, identities, tools, and versions. Follow the project's delivery approach; do not introduce Kubernetes or a new CI platform for a simpler need.

## Delivery contract

Define what is built, its source revision, checks that prove behavior, configuration per environment, and the identity authorized to perform each step. Promoted artifacts must be traceable to revisions and verification results; distinguish build artifacts from runtime configuration.

Separate tests, builds, and scans from deployment actions. Use project credential scopes and identity mechanisms; avoid secrets in images, sources, logs, or example configurations. Do not change permission or protection gates without a request that covers them.

## Infrastructure and environments

Identify the target provider, account, region, root, and state before plans or mutations. Separate state does not automatically isolate IAM. Choose provider locks, backend encryption and locking, and module versioning according to team and project usage.

Distinguish formatting or static validation, mock plans, plans against real accounts, applies, and runtime verification. Create plans for the appropriate environment and revision; do not copy saved plans or state to promote between environments.

A request to create configuration or fix a workflow does not authorize paid cloud resources. Follow existing scope and authorization; prepare changes and review results before external actions that require an additional decision.

## Release behavior

Check schema and API compatibility during rolling deployments, readiness, graceful draining, and relevant cutover strategies. Liveness checks that depend on every downstream service can cause cascading restarts.

Explain smoke checks, failure signals, and rollback or roll-forward appropriate to contracts and data. Reverting an application does not roll back data; destructive migrations need separate recovery. Previewed or rendered configuration does not prove a working cluster runtime.

## Verification and result

Run available local checks, rendering, linting, configuration validation, or pipeline tests appropriate to the change. State evidence limits when credentials or runtimes are unavailable.

Report changed artifacts or configuration, intended target environments, check evidence, release and recovery plans, and live actions actually performed when requested and authorized.

Example: `$eng-delivery Build a test and build pipeline with image promotion traceable to a commit.`
