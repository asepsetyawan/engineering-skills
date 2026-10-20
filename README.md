# Engineering Skills

A collection of 14 custom skills for end-to-end software engineering. Each skill is stack-agnostic: it checks the current project's requirements, runtime, contracts, and conventions before choosing an approach.

## Choose a skill

| Skill | When to use it |
|---|---|
| `$eng-workflow` | Features spanning disciplines, from requirements through verification |
| `$eng-requirements` | Scope, business rules, acceptance criteria, and vertical slices |
| `$eng-architecture` | Module and service boundaries, ownership, dependencies, and ADRs |
| `$eng-design-patterns` | Justified pattern selection and refactoring |
| `$eng-system-design` | Capacity, data flows, scaling, consistency, and failure handling |
| `$eng-backend` | REST and gRPC APIs, business logic, workers, and integrations |
| `$eng-frontend` | Interfaces, forms and state, API integration, and accessibility |
| `$eng-database` | Schemas, transactions, SQL, indexes, caching, and migrations |
| `$eng-testing` | Behavioral evidence, regressions, integration and concurrency tests |
| `$eng-security` | Trust boundaries, authorization, tenant isolation, and secrets |
| `$eng-delivery` | Builds, containers, CI/CD, infrastructure as code, and releases |
| `$eng-reliability` | Incident and performance diagnosis, SLOs, recovery, and runbooks |
| `$eng-code-review` | Bugs and regression risks in diffs |
| `$eng-documentation` | Setup, API guides, onboarding, and handoffs |

Use one skill for a focused task. `eng-workflow` selects the stages needed for work spanning disciplines; it does not need to run the whole collection or create additional agents. Each specialist works independently without depending on other skills.

## Usage examples

```text
$eng-workflow Build a booking feature with an API, database, UI, and local verification.
$eng-architecture Evaluate the order and payment module boundaries in this repository.
$eng-design-patterns Separate logistics vendor contracts from shipping rules.
$eng-system-design Design a notification service with traffic bursts and safe retries.
$eng-backend Implement an idempotent order endpoint following project contracts.
$eng-frontend Fix stale search responses and verify loading and error states.
$eng-database Analyze a slow query using the available query plan.
$eng-code-review Review this diff for concurrency bugs and compatibility.
```

Include project or file paths, the goal, constraints, and acceptance criteria when known. All collection content is written in English. Use English by default unless the user explicitly requests another language. Scope, external authorization, and verification claims follow the actual task; creating configuration does not automatically mean live deployment.

## Structure

```text
skills/
  eng-*/
    SKILL.md               Workflow, triggers, and responsibility boundaries
    agents/openai.yaml     Display names and example prompts
    assets/                Output templates, only where needed
scripts/
  validate.py              Validate manifests, metadata, and local links
  install.py               Install local symlinks without overwriting entries
tests/
  test_install.py          Check conflicts, dry runs, and idempotency
```

## Validation

Run from the project root with Python 3.10+ and PyYAML:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/validate.py
python3 -m unittest discover -s tests -v
```

The validator checks package format and integrity, rather than the quality of an agent's decisions. Behavioral quality needs evaluation on real tasks. Package checks do not require cloud accounts or external services.

## Local installation

Review the plan first:

```bash
python3 scripts/install.py --all --dry-run
python3 scripts/install.py --all
```

Or select individual skills:

```bash
python3 scripts/install.py --name eng-backend --name eng-database
```

The default destination is `CODEX_HOME/skills`, or `~/.codex/skills` when the variable is unset. Use `--destination /absolute/path` for another destination.

The installer creates symlinks to this project's sources. Source changes immediately affect the installation; do not move the project without updating the symlinks. Files, directories, and symlinks belonging to other installations are not overwritten. Repeating installation against the same symlinks is safe. The installer stops before creating links if the initial plan contains conflicts, and rolls back links created during that run if link creation fails.

To uninstall, remove only the symlinks created by the installer in the destination folder; project sources remain available. The project contains the collection's sources and management tools, while each `skills/eng-*` directory is an independent skill package.

## Customize the collection

Edit `skills/<name>/SKILL.md` and its `agents/openai.yaml` metadata. Keep instructions that change decisions; avoid generic tutorials, assumed stacks, or new approval rules. Output templates belong in `assets/` and are read only when a deliverable needs the artifact.

Add a skill as `skills/<name>/` with a lowercase hyphenated name and matching metadata. The installer discovers skills through these folders. Run validation and installer tests after structural or tooling changes; instruction-only changes need package validation and relevant usage evaluation.
