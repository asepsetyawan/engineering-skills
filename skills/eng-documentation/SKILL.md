---
name: eng-documentation
description: "Write or update READMEs, API guides, onboarding, decision notes, and technical handoffs from project evidence. Use when documentation is the requested deliverable or must reflect implementation changes."
---

# Engineering Documentation

Identify the reader, the task they need to complete, and the project's documentation format and location. Inspect implementation, configuration, contracts, tests, and actual commands; old documentation is a lead to verify.

## Write for the reader's task

Lead with outcomes and the minimum required steps: prerequisites, commands with working directories, configuration to supply, expected results, and relevant troubleshooting. Distinguish local development, tests, staging, and production.

Do not include secrets, personal data, internal hosts or accounts, or experience claims not supplied for publication. Use clearly nonsecret examples. Do not invent deployments, benchmarks, supported versions, or team approval.

Update existing sources of truth instead of creating conflicting guides. When an API specification or generator is authoritative, follow that workflow. Link to details maintained elsewhere; do not copy vendor manuals or hardcode versions without a need.

## Match the deliverable

- **README or onboarding:** minimum setup, run commands, tests, and environment limits.
- **API guide:** contracts, authorization scope, schema-consistent request, response, and error examples, and compatibility.
- **Decision note or handoff:** context, decisions, consequences, implementation status, verification, and remaining work.
- **Operational guide:** use existing project procedures or runbooks; distinguish read-only commands from mutations.

Small documents do not need every section. Preserve domain terminology and the reader's language. Explain rationale only when it helps a decision or prevents a real mistake.

## Verify

Check local paths and links, and ensure examples match code and contracts. Run safe local commands when needed and available; do not deploy or perform destructive operations merely to verify documentation. Label commands or runtime steps not tested.

Report changed documents, their main content, and verification limits. Remove placeholders from completed sections; state open questions as questions, rather than invented facts.

Example: `$eng-documentation Update the setup guide so a new engineer can run the API and tests locally.`
