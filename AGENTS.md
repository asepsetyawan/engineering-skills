# Maintaining Engineering Skills

This repository contains reusable engineering skills, not application code.

- Keep skills independent, stack-agnostic, and scoped to recognizable user goals.
- Keep repository instructions, descriptions, examples, prompts, and templates in English. Use English by default unless the user explicitly requests another language.
- Keep names, examples, metadata, templates, and paths generic. Do not embed employer/client identities, personal records, private workspace paths, or credentials.
- The source of truth is `skills/<name>/`. Installed symlinks should point here; do not maintain divergent global copies.
- Read only relevant skill bodies when evaluating a workflow. `eng-workflow` routes work without requiring every specialist or delegating to subagents.
- Keep ordinary engineering requests focused on the requested work rather than unsolicited quizzes.
- Add references/scripts/templates only when they improve an actual recurring workflow.
- Run `python3 scripts/validate.py` after skill edits. Run `python3 -m unittest discover -s tests -v` when installer/validator behavior changes.
- Package validation does not prove behavioral quality. Report checks accurately and avoid claims of runtime or production verification without evidence.
