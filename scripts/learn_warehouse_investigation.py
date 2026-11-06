"""Import an external investigation lesson into an isolated local Harness² library."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from harness2.core import tree
from harness2.core.library import Library
from harness2.substrate.codex import CODEX_SURFACE

CASE_ID = "openaussie-2026-11-06-policy-v2"
DOMAIN = "warehouse-investigations"
ASSET = Path(__file__).resolve().parents[1] / "assets/experiences/warehouse-investigation"
EVIDENCE_FILES = (
    "ledger.json",
    "thread.json",
    "monthly_frozen.json",
    "reception_frozen.json",
    "comparison_frozen.json",
)


def import_experience(output: Path, evidence_dir: Path) -> Path:
    """Keep the learned tree and source hashes; never copy public account text into it."""
    library = Library(output, DOMAIN, CODEX_SURFACE)
    if library.entry_dir(CASE_ID).exists():
        raise FileExistsError(f"experience already exists: {library.entry_dir(CASE_ID)}")
    provenance = {
        "source_case": "openaussie-2026-11-06",
        "strategy_version": 2,
        "source_directory": str(evidence_dir.resolve()),
        "review_state": "machine_proposed_external_experience",
        "model_evaluation": "not_run",
        "source_hashes": {
            name: hashlib.sha256((evidence_dir / name).read_bytes()).hexdigest()
            for name in EVIDENCE_FILES
        },
    }
    harness = tree.read_tree(CODEX_SURFACE, ASSET / "harness")
    harness[".agents/skills/warehouse-investigation/scripts/source_provenance.json"] = (
        json.dumps(provenance, indent=2) + "\n"
    )
    tree.validate(CODEX_SURFACE, harness)
    experience = json.loads((ASSET / "experience.json").read_text())
    result = library.add(
        CASE_ID,
        harness,
        label="external-unprobed",
        why=(
            "Operator requested retaining this external case as a proposed strategy. "
            "This is not an adopted model-backed candidate, human-approved finding, "
            "benchmark result or model training. The source hash manifest is retained "
            "inside the skill; the development contrasts are synthetic."
        ),
        experience=experience,
    )
    assert result is not None
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--evidence-dir", type=Path, required=True)
    args = parser.parse_args()
    print(import_experience(args.output, args.evidence_dir))


if __name__ == "__main__":
    main()
