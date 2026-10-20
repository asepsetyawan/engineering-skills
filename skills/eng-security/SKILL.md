---
name: eng-security
description: "Review or fix security at a specific trust boundary: authentication, authorization, tenant isolation, input and output, secrets, or supply chain. Use for explicit security tasks or changes to sensitive boundaries, rather than automatic full audits."
---

# Engineering Security

Limit the review to surfaces and threats relevant to the task. Inspect actor identities, assets, entry points, trust boundaries, and abuse impact. Do not expand an assessment into a platform-wide checklist without a need.

## Trace boundaries

- Follow identity and permissions from ingress to data operations and resources. Authentication does not prove access to every resource. Check tenant scope from verified identity, rather than client parameters alone.
- Validate inputs against contracts and use parameterized queries. Output encoding depends on HTML, URL, or script context; sanitizing in one place does not automatically make every context safe.
- Evaluate cookies and sessions, CSRF, CORS, token storage, redirects, and uploads according to how the application actually works. Do not add irrelevant controls merely because a category name exists.
- For URLs, webhooks, and integrations, check relevant SSRF, redirects, and network access, and bind signed identities to payloads and replay windows when used.
- Keep secrets within appropriate server or secret-store boundaries. Protect tokens and sensitive data in logs and traces. Do not include secret values in reports; if a real leak is found, identify the location, type, and rotation action without copying the value.
- For pipelines and dependencies, evaluate identities, permissions, artifact provenance, and updates or scans according to project facilities. A pinned version is not automatically free of vulnerabilities.

## Prove and fix

Use local tests and fixtures for relevant unauthorized access, cross-tenant access, malformed input, replay, or privilege escalation scenarios. Do not test external targets or live accounts outside the authorized scope.

Explain exploitation prerequisites, data or code paths, impact, and the narrowest mitigation that closes the issue. Distinguish demonstrated weaknesses from suspicions requiring more configuration or runtime evidence. For current vulnerabilities or dependencies, verify official advisories and actual versions before making claims.

When fixing an issue, preserve safe contracts, add appropriate regression evidence, and check affected callers. Do not weaken authorization or firewalls merely to make a test or demo work.

## Result

Report actionable findings with locations, triggering conditions, impact, fixes, and performed validation. State scope limitations; do not declare a system secure merely because a limited surface produced no findings.

Example: `$eng-security Review tenant isolation in the export endpoint and add relevant regression tests.`
