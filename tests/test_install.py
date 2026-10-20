"""Exercise installation side effects and failure boundaries in temporary directories."""

from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from install import install


class InstallTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.base = Path(self.temporary.name)
        self.root = self.base / 'project'
        self.destination = self.base / 'installed'
        for name in ('eng-alpha', 'eng-beta'):
            folder = self.root / 'skills' / name
            (folder / 'agents').mkdir(parents=True)
            (folder / 'SKILL.md').write_text(
                f'---\nname: {name}\ndescription: "A focused engineering task."\n---\n\nPerform the requested task.\n'
            )
            (folder / 'agents/openai.yaml').write_text(
                'interface:\n  display_name: "Engineering test"\n'
                '  short_description: "Focused engineering workflow for tests"\n'
                f'  default_prompt: "Use ${name} for this task."\n'
            )

    def test_dry_run_has_no_filesystem_side_effect(self):
        plan = install(self.root, self.destination, dry_run=True)
        self.assertEqual(len(plan), 2)
        self.assertFalse(self.destination.exists())

    def test_install_is_selective_and_idempotent(self):
        install(self.root, self.destination, ['eng-alpha'])
        target = self.destination / 'eng-alpha'
        self.assertTrue(target.is_symlink())
        self.assertEqual(target.resolve(), (self.root / 'skills/eng-alpha').resolve())
        self.assertFalse((self.destination / 'eng-beta').exists())
        self.assertEqual(install(self.root, self.destination, ['eng-alpha'])[0][0], 'unchanged')

    def test_conflict_prevents_partial_install(self):
        occupied = self.destination / 'eng-beta'
        occupied.mkdir(parents=True)
        marker = occupied / 'user.txt'
        marker.write_text('preserve me')
        with self.assertRaises(ValueError):
            install(self.root, self.destination)
        self.assertFalse((self.destination / 'eng-alpha').exists())
        self.assertEqual(marker.read_text(), 'preserve me')

    def test_dangling_symlink_is_not_overwritten(self):
        self.destination.mkdir()
        target = self.destination / 'eng-alpha'
        target.symlink_to(self.base / 'missing')
        with self.assertRaises(ValueError):
            install(self.root, self.destination)
        self.assertTrue(target.is_symlink())

    def test_invalid_package_and_unknown_selection_do_not_install(self):
        with self.assertRaises(ValueError):
            install(self.root, self.destination, ['../outside'])
        (self.root / 'skills/eng-beta/agents/openai.yaml').unlink()
        with self.assertRaises(ValueError):
            install(self.root, self.destination)
        self.assertFalse(self.destination.exists())

    def test_link_failure_rolls_back_only_new_links(self):
        install(self.root, self.destination, ['eng-alpha'])
        original = Path.symlink_to

        def fail_beta(target, *args, **kwargs):
            if target.name == 'eng-beta':
                raise OSError('simulated link failure')
            return original(target, *args, **kwargs)

        with patch.object(Path, 'symlink_to', fail_beta):
            with self.assertRaises(OSError):
                install(self.root, self.destination)
        self.assertTrue((self.destination / 'eng-alpha').is_symlink())
        self.assertFalse((self.destination / 'eng-beta').exists())
        fresh_destination = self.base / 'fresh'
        with patch.object(Path, 'symlink_to', fail_beta):
            with self.assertRaises(OSError):
                install(self.root, fresh_destination)
        self.assertEqual(list(fresh_destination.iterdir()), [])


if __name__ == '__main__':
    unittest.main()
