#!/usr/bin/env python3
"""Validate this collection's skill manifests, UI metadata, and package links."""

import argparse
from pathlib import Path
import re
import sys

try:
    import yaml
except ImportError:
    raise SystemExit('Install development dependencies: python3 -m pip install -r requirements-dev.txt')


PROJECT_ROOT = Path(__file__).resolve().parents[1]
NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')


def validate_skill(folder):
    errors = []
    path = folder / 'SKILL.md'
    if not path.is_file():
        return [f'{folder.name}: SKILL.md missing']
    source = path.read_text(encoding='utf-8')
    match = re.match(r'\A---\n(.*?)\n---(?:\n|$)', source, re.S)
    if not match:
        return [f'{folder.name}: invalid YAML frontmatter delimiters']
    try:
        manifest = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return [f'{folder.name}: invalid manifest YAML: {exc}']
    if not isinstance(manifest, dict):
        return [f'{folder.name}: manifest must be a mapping']
    name = manifest.get('name')
    if not isinstance(name, str) or not NAME.fullmatch(name) or len(name) > 64 or name != folder.name:
        errors.append(f'{folder.name}: name must match folder and use lowercase hyphens, max 64 chars')
    description = manifest.get('description')
    if not isinstance(description, str) or not description.strip() or len(description) > 1024:
        errors.append(f'{folder.name}: nonempty description required, max 1024 chars')
    allowed = {'name', 'description', 'metadata', 'license', 'allowed-tools'}
    if set(manifest) - allowed:
        errors.append(f'{folder.name}: unexpected frontmatter fields')
    if not source[match.end():].strip():
        errors.append(f'{folder.name}: instructions missing')
    try:
        metadata = yaml.safe_load((folder / 'agents/openai.yaml').read_text(encoding='utf-8'))
        interface = metadata['interface']
        display = interface['display_name']
        short = interface['short_description']
        prompt = interface['default_prompt']
        if not isinstance(display, str) or not display.strip():
            errors.append(f'{folder.name}: display_name required')
        if not isinstance(short, str) or not 25 <= len(short) <= 64:
            errors.append(f'{folder.name}: short_description must be 25–64 chars')
        if not isinstance(prompt, str) or f'${folder.name}' not in prompt:
            errors.append(f'{folder.name}: default_prompt must invoke its skill')
    except (OSError, yaml.YAMLError, KeyError, TypeError) as exc:
        errors.append(f'{folder.name}: invalid UI metadata: {exc}')
    for document in folder.rglob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', document.read_text(encoding='utf-8')):
            if '://' in target or target.startswith('#'):
                continue
            linked = (document.parent / target.split('#', 1)[0]).resolve()
            if not linked.is_relative_to(folder.resolve()) or not linked.is_file():
                errors.append(f'{folder.name}: missing or nonportable local link: {target}')
    return errors


def validate_collection(root):
    skills = sorted(p for p in (root / 'skills').iterdir() if p.is_dir()) if (root / 'skills').is_dir() else []
    errors = [] if skills else ['No skill directories found']
    for folder in skills:
        errors.extend(validate_skill(folder))
    return skills, errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=PROJECT_ROOT)
    args = parser.parse_args()
    skills, errors = validate_collection(args.root.resolve())
    if errors:
        print('\n'.join(errors), file=sys.stderr)
        return 1
    print(f'Valid: {len(skills)} skills; manifests, UI metadata, and local links checked.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
