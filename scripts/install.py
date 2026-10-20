#!/usr/bin/env python3
"""Install selected skills as local symlinks without overwriting existing entries."""

import argparse
import os
from pathlib import Path
import sys

from validate import PROJECT_ROOT, validate_collection


def install(root, destination, names=None, dry_run=False):
    folders, errors = validate_collection(root)
    if errors:
        raise ValueError('\n'.join(errors))
    available = {folder.name: folder.resolve() for folder in folders}
    selected = sorted(set(names)) if names is not None else sorted(available)
    unknown = set(selected) - set(available)
    if unknown:
        raise ValueError(f'Unknown skills: {", ".join(sorted(unknown))}')
    if not selected:
        raise ValueError('Select at least one skill')
    destination = destination.expanduser().absolute()
    if destination.exists() and not destination.is_dir():
        raise ValueError(f'Destination is not a directory: {destination}')
    plan = []
    conflicts = []
    for name in selected:
        source = available[name]
        target = destination / name
        if target.is_symlink() and target.resolve() == source:
            plan.append(('unchanged', target, source))
        elif target.exists() or target.is_symlink():
            conflicts.append(str(target))
        else:
            plan.append(('link', target, source))
    if conflicts:
        raise ValueError('Refusing to overwrite existing entries:\n' + '\n'.join(conflicts))
    if dry_run:
        return plan
    destination.mkdir(parents=True, exist_ok=True)
    created = []
    try:
        for action, target, source in plan:
            if action == 'link':
                target.symlink_to(source, target_is_directory=True)
                created.append((target, source))
    except OSError:
        for target, source in reversed(created):
            if target.is_symlink() and target.resolve() == source:
                target.unlink()
        raise
    return plan


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    selection = parser.add_mutually_exclusive_group(required=True)
    selection.add_argument('--all', action='store_true', help='Install the entire collection')
    selection.add_argument('--name', action='append', help='Select a skill; repeat for several skills')
    default_home = Path(os.environ.get('CODEX_HOME') or Path.home() / '.codex')
    parser.add_argument('--destination', type=Path, default=default_home / 'skills')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()
    try:
        plan = install(PROJECT_ROOT, args.destination, None if args.all else args.name, args.dry_run)
    except (ValueError, OSError) as exc:
        print(str(exc), file=sys.stderr)
        return 1
    for action, target, source in plan:
        print(f'{"plan " if args.dry_run else ""}{action}: {target} -> {source}')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
