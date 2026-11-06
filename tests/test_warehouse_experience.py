"""Offline checks for the opt-in external experience's real library/context route."""

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

from harness2.core import context, tree
from harness2.core.library import Library
from harness2.demo import DemoAdapter
from harness2.substrate.codex import CODEX_SURFACE

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "learn_warehouse_investigation", ROOT / "scripts/learn_warehouse_investigation.py"
)
lesson = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lesson)


class WarehouseExperienceTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.source = self.root / "evidence"
        self.source.mkdir()
        for name in lesson.EVIDENCE_FILES:
            (self.source / name).write_text('{"private_body":"must not travel"}\n')

    def test_import_reaches_full_context_without_raw_source(self):
        entry = lesson.import_experience(self.root / "library", self.source)
        library = Library(self.root / "library", lesson.DOMAIN, CODEX_SURFACE)
        self.assertEqual(library.entries(), [lesson.CASE_ID])
        harness = library.tree_of(lesson.CASE_ID)
        self.assertEqual(tree.validate(CODEX_SURFACE, harness)["skills"], 1)
        adapter = DemoAdapter(self.root / "demo")
        result = context.build(
            self.root / "context", adapter, "ledger-1", library_dir=library.context_dir()
        )
        self.assertTrue(result.library)
        copied = self.root / "context/library/harnesses" / lesson.CASE_ID
        self.assertTrue((copied / "EXPERIENCE.md").exists())
        self.assertTrue(
            (copied / "harness/.agents/skills/warehouse-investigation/scripts/development_contrasts.json").exists()
        )
        text = "\n".join(p.read_text() for p in copied.rglob("*") if p.is_file())
        self.assertNotIn("must not travel", text)
        self.assertIn("not an adopted model-backed candidate", (entry / "EXPERIENCE.md").read_text())
        provenance = json.loads(
            (entry / "harness/.agents/skills/warehouse-investigation/scripts/source_provenance.json").read_text()
        )
        self.assertEqual(set(provenance["source_hashes"]), set(lesson.EVIDENCE_FILES))
        self.assertEqual(provenance["strategy_version"], 2)

    def test_existing_or_incomplete_evidence_never_overwrites(self):
        output = self.root / "library"
        entry = lesson.import_experience(output, self.source)
        before = {str(p.relative_to(entry)): p.read_bytes() for p in entry.rglob("*") if p.is_file()}
        with self.assertRaises(FileExistsError):
            lesson.import_experience(output, self.source)
        after = {str(p.relative_to(entry)): p.read_bytes() for p in entry.rglob("*") if p.is_file()}
        self.assertEqual(before, after)
        (self.source / lesson.EVIDENCE_FILES[0]).unlink()
        with self.assertRaises(FileNotFoundError):
            lesson.import_experience(self.root / "incomplete", self.source)
        self.assertFalse((self.root / "incomplete").exists())

    def test_untriggered_skill_is_rejected_and_contrasts_are_development_only(self):
        harness = tree.read_tree(CODEX_SURFACE, lesson.ASSET / "harness")
        harness["AGENTS.md"] = "Investigate carefully.\n"
        with self.assertRaisesRegex(ValueError, "never named"):
            tree.validate(CODEX_SURFACE, harness)
        fixture = json.loads(
            (lesson.ASSET / "harness/.agents/skills/warehouse-investigation/scripts/development_contrasts.json").read_text()
        )
        self.assertIn("not_human_gold", fixture["status"])
        policy = next(case for case in fixture["cases"] if case["id"] == "policy_memory_refresh_and_feedback")
        self.assertTrue(policy["authorization"]["expired"])
        self.assertFalse(policy["cache"]["ttl_elapsed"])
        self.assertEqual(policy["proposed_policy"]["state"], "proposal")


if __name__ == "__main__":
    unittest.main()
