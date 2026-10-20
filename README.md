# Engineering Skills

A collection of 14 custom skills for end-to-end software engineering, with local installation instructions for Codex, Claude Code, and Cursor. Each skill checks the current project's requirements, runtime, contracts, and conventions before choosing an approach.

## Choose a skill

| Skill name | When to use it |
|---|---|
| `eng-workflow` | Features spanning disciplines, from requirements through verification |
| `eng-requirements` | Scope, business rules, acceptance criteria, and vertical slices |
| `eng-architecture` | Module and service boundaries, ownership, dependencies, and ADRs |
| `eng-design-patterns` | Justified pattern selection and refactoring |
| `eng-system-design` | Capacity, data flows, scaling, consistency, and failure handling |
| `eng-backend` | REST and gRPC APIs, business logic, workers, and integrations |
| `eng-frontend` | Interfaces, forms and state, API integration, and accessibility |
| `eng-database` | Schemas, transactions, SQL, indexes, caching, and migrations |
| `eng-testing` | Behavioral evidence, regressions, integration and concurrency tests |
| `eng-security` | Trust boundaries, authorization, tenant isolation, and secrets |
| `eng-delivery` | Builds, containers, CI/CD, infrastructure as code, and releases |
| `eng-reliability` | Incident and performance diagnosis, SLOs, recovery, and runbooks |
| `eng-code-review` | Bugs and regression risks in diffs |
| `eng-documentation` | Setup, API guides, onboarding, and handoffs |

Use one skill for a focused task. `eng-workflow` selects the stages needed for work spanning disciplines; it does not need to run the whole collection or create additional agents. Each specialist works independently without depending on other skills.

## Chat syntax: `$` versus `/`

The skill name is `eng-database`. The prefix is the application's chat invocation syntax; it is not part of the folder name or the `name` field in `SKILL.md`.

| Application | Enter in the application's agent chat | Reference |
|---|---|---|
| Codex | `$eng-database` | [Codex skills](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code | `/eng-database` | [Claude Code skills](https://code.claude.com/docs/en/skills) |
| Cursor | `/eng-database` | [Cursor skills](https://cursor.com/help/customization/skills) |

Chat examples below are prompts, not terminal commands. Skill files and Codex UI prompts in this collection use `$eng-...` examples; select or invoke the same skill with `/eng-...` in Claude Code and Cursor.

## Get the collection

The terminal commands below target macOS and Linux. Use Python 3.10+ with virtual environment support; `python3` must resolve to a compatible version.

```bash
git clone https://github.com/asepsetyawan/engineering-skills.git
cd engineering-skills
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-dev.txt
```

If you already cloned the repository, open its root folder and run only the environment setup commands you still need. Keep running the installer from this collection's root, even when installing skills for another project.

## Use with Claude Code

Install all skills for your local Claude Code projects:

```bash
.venv/bin/python scripts/install.py --all --destination "$HOME/.claude/skills"
```

To install only selected skills instead:

```bash
.venv/bin/python scripts/install.py --name eng-backend --name eng-database --destination "$HOME/.claude/skills"
```

Personal skills load from `~/.claude/skills/`; repository skills belong in `.claude/skills/`. Start a Claude Code session in the project you want to work on, then enter a prompt such as:

```text
/eng-database Review this project's schema, transactions, and indexes.
/eng-backend Implement an idempotent order endpoint following project contracts.
/eng-workflow Build a booking feature with an API, database, UI, and local verification.
```

Type `/` to find the skill in the command menu. Claude Code can also select relevant skills automatically. These paths and invocation behavior follow the [official Claude Code skill guide](https://code.claude.com/docs/en/skills).

## Use with Cursor

Install all skills for your local Cursor projects:

```bash
.venv/bin/python scripts/install.py --all --destination "$HOME/.cursor/skills"
```

To install only the database skill instead:

```bash
.venv/bin/python scripts/install.py --name eng-database --destination "$HOME/.cursor/skills"
```

Open your application project in Cursor. Start a new Agent chat, type `/`, and search for a skill name. If newly installed skills do not appear, restart Cursor and check **Customize → Skills**. Then select the skill and add your request:

```text
/eng-frontend Fix stale search responses and verify loading and error states.
/eng-architecture Evaluate the order and payment module boundaries in this repository.
/eng-code-review Review this diff for concurrency bugs and compatibility.
/eng-workflow Build a booking feature with an API, database, UI, and tests.
```

Personal skills load from `~/.cursor/skills/`; repository skills can live in `.cursor/skills/` or `.agents/skills/`. Cursor also reads compatible Claude and Codex skill directories, so avoid installing duplicate copies when a skill already appears. See the [official Cursor skill guide](https://cursor.com/help/customization/skills).

## Use with Codex

Install using this repository's default destination:

```bash
.venv/bin/python scripts/install.py --all --dry-run
.venv/bin/python scripts/install.py --all
```

The default is `CODEX_HOME/skills`, or `~/.codex/skills` when the variable is unset. Use `--destination /absolute/path` to select another location. In Codex chat, use:

```text
$eng-design-patterns Separate logistics vendor contracts from shipping rules.
$eng-system-design Design a notification service with traffic bursts and safe retries.
$eng-workflow Build a booking feature with an API, database, UI, and local verification.
```

Include project or file paths, the goal, constraints, and acceptance criteria when known. All collection content is written in English. Use English by default unless the user explicitly requests another language. Scope, external authorization, and verification claims follow the actual task; creating configuration does not automatically mean live deployment.

## Project scope, updates, and removal

To limit installation to one project, use `--destination` with that project's absolute skills directory:

| Application | Destination within the target project |
|---|---|
| Claude Code | `.claude/skills/` |
| Cursor | `.cursor/skills/` |
| Codex | `.agents/skills/` |

For example, replace `/path/to/your-project` with your application project's absolute path:

```bash
.venv/bin/python scripts/install.py --name eng-database --destination /path/to/your-project/.cursor/skills
```

The installer creates symlinks to this collection's sources and refuses to overwrite existing entries. Repeating installation against the same links is safe. It checks conflicts before creating links and rolls back links created during that run if link creation fails. Add `--dry-run` to any install command to preview it.

Keep this collection at a stable location. Source edits and `git pull --ff-only` from this repository's root update linked installations. For team-shared repository skills, copy complete skill folders into the application repository and commit actual files; local absolute symlinks will not work on teammates' machines. Copied skills need their own updates.

To uninstall, remove only the symlinks created by the installer from the selected destination. The project sources remain available. The expected layout is `<destination>/eng-database/SKILL.md`, with its supporting files alongside it, rather than a lone `SKILL.md` directly inside the destination.

## Structure

```text
skills/
  eng-*/
    SKILL.md               Workflow, triggers, and responsibility boundaries
    agents/openai.yaml     Codex display names and example prompts
    assets/                Output templates, only where needed
scripts/
  validate.py              Validate manifests, metadata, and local links
  install.py               Install local symlinks without overwriting entries
tests/
  test_install.py          Check conflicts, dry runs, and idempotency
```

## Validation

After the environment setup above, run from the collection's root:

```bash
.venv/bin/python scripts/validate.py
.venv/bin/python -m unittest discover -s tests -v
```

The validator checks package format and integrity, rather than the quality of an agent's decisions. Behavioral quality needs evaluation on real tasks. Package checks do not require cloud accounts or external services. Local installer checks do not establish that a particular editor version has discovered or invoked the skills; confirm that in the application's chat.

## Customize the collection

Edit `skills/<name>/SKILL.md` and its `agents/openai.yaml` metadata. Keep instructions that change decisions; avoid generic tutorials, assumed stacks, or new approval rules. Output templates belong in `assets/` and are read only when a deliverable needs the artifact.

Add a skill as `skills/<name>/` with a lowercase hyphenated name and matching metadata. The installer discovers skills through these folders. Run validation and installer tests after structural or tooling changes; instruction-only changes need package validation and relevant usage evaluation.
