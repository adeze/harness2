# Warehouse investigation experience

This opt-in Codex harness preserves a process lesson from the 6 November 2026
OpenAussie investigation through the existing `Library` and `ContextTree`
mechanisms. It contains an on-demand skill, synthetic development contrasts and
source-file hashes. It does not copy source comment bodies into improvement
context, claim model training, promote human labels or establish Jev accuracy.

Import the retained evidence once, from the repository checkout:

```sh
uv run --python 3.12 --no-project python -m scripts.learn_warehouse_investigation \
  --evidence-dir "/path/to/retained/initial-capture" \
  --output local_experience/openaussie-2026-11-06
```

The import refuses an existing entry and requires all five named source files
before writing anything. Local provenance includes the supplied private source
directory; do not publish that generated library. The checked-in synthetic
fixture contains no Reddit usernames, real comment IDs or raw user text.

The current strategy imports as `openaussie-2026-11-06-policy-v2`. Its separate
entry preserves the original `openaussie-2026-11-06` tree and source provenance.
Version 2 adds an operator-requested feedback loop: inspect existing policy/cache,
retain evidence-backed changes to cadence/tasks/priority/cost as proposals, enforce
approval/budget/authorization expiry, refresh only approved runtime policy through
the existing repository, and compare subsequent outcomes against the prior policy.
It does not migrate a live cache or activate monitoring. The existing RBA process
TTL must be inspected before adding any cache mechanism.

For a subsequent operator-owned investigation, retrieve the full domain library
with `Library(output, "warehouse-investigations", CODEX_SURFACE).context_dir()`
and pass it as `library_dir` to `harness2.core.context.build`. Its index, full
harness, source hashes, experience note and contrasts then reach the improver via
the established context route. The runtime Codex harness names the skill in
`AGENTS.md`, so it remains discoverable on demand when materialised normally.

This local external experience is isolated from benchmark sweeps. Their
per-run/per-mode libraries deliberately retain only prior tasks from the same
stream; do not inject this external lesson into a benchmark and compare its
results against an unseeded baseline. No benchmark defaults, model bindings or
automatic paid runs change. A future contrastive probe must record both complete
trajectories and distinguish a deterministic integration check from semantic
quality evaluation.

Offline validation:

```sh
uv run --python 3.12 --no-project python -m unittest discover \
  -s tests -p test_warehouse_experience.py
```
