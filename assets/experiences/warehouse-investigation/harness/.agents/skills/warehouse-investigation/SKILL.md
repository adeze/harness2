---
name: warehouse-investigation
description: Investigate repeated discussion and moderation patterns using warehouse evidence, scoped reply paths, matched comparisons and an explicit aggregate cost ceiling.
---

Use the owning repository's established query, archive and Jev contracts. This skill
is a proposed lesson from an external case, not an evaluated classifier or authority
to acquire new data, spend money, publish or train. Inspect the synthetic development
contrasts in `scripts/development_contrasts.json` before adapting the workflow.

## Evidence acquisition and identity

1. Start from warehouse metadata and retained evidence; live-platform retrieval fills
   named gaps. Record collection coverage, snapshot cutoff, schema and source receipts.
2. A current mirror can lag append-only observations. Project only required columns,
   prune observation partitions and deduplicate deterministically. Keep publication,
   observation, transport capture and reconciliation timestamps distinct. Do not treat
   `observed_at` as capture time when the pipeline copied publication time into it.
3. Reconstruct parent, reply and return paths through to all captured descendants.
   Join exact governed comment + parent-post + physical-source tenant identities;
   use the owning resolver for normalization and reject collisions or mismatched
   parents. Physical tenant provenance is not invented global analytical authority.
   Calculate path depth from links when stored depth resets. Disclose missing parents,
   truncated bodies and reported-versus-captured thread counts.

## Semantic and moderation judgments

- Preserve original transport fields and the ingestion-derived status separately.
  Body `[deleted]`, body `[removed]`, author `[deleted]` and `[unavailable]` differ.
  A derived `removed_by_mod` enum does not identify a named human moderator; evidence
  may instead concern AutoModerator, Reddit admin, another tool or an unresolved actor.
  Preserve authenticated/anonymous transport and account-specific visibility limits.
- Public distinguished moderator comments, stated reasons, rule versions and state
  transitions are auditable observations even if private action/report logs are absent.
  Separate observed action, stated justification, report receipt, review acknowledgement
  and later outcome. Missing logs do not prove either no moderation or deliberate inaction.
- Classify rhetoric with full source/target/quotation context. A lexical hit is a
  retrieval candidate, not a harassment label. Sarcastic counterspeech, substantive
  criticism, personal abuse and unsupported payment allegations can coexist.
- Apply affiliation tests symmetrically. A documented advocacy-group award is source
  context, not proof of membership, payment, editorial control or false reporting.
  Neither Jewish identity nor pro-Palestinian advocacy establishes paid propaganda.
  Retain a user's stated mirroring rationale and chronological antecedent separately
  from whether the later reply itself satisfies the same civility standard.
- If Jev is available, use registered context-gated questions, versions and retained
  request/response receipts. Separate model proposal, independent cross-check and user
  review. These development contrasts are not human-approved labels or protected tests.

## Comparisons, cost and reporting

- Match both arms to identical thread/date support and state denominators. Threads
  containing the focus account are not necessarily threads with a captured reply to
  that account. Account for wording, nesting, timing and incomplete attribution.
- Scores are reception snapshots, not vote counts or moderator approval. Repeated
  participants are not proof of coordination. A cohort selected for negative scores
  cannot independently validate negative reception; keep exposure and outcome separate.
- Dry-run every query; enforce hard per-job byte caps and a persistent cumulative
  ledger under the task-approved ceiling. Reserve unresolved jobs, settle failures,
  retain all job IDs and costs, and do not auto-retry. A prior case's 200 GiB ceiling
  grants no budget to a new task. Use local cached artifacts for repeat analysis.
- Retain immutable source snapshots with hashes and separate private evidence from
  public derivatives. Report observed facts, interpretations, alternatives and gaps.
  Phrase a governance-audit recommendation as a recommendation, not as a claim that
  a government has access or a legal entitlement without current primary evidence.

## Monitoring feedback into existing policy

1. Inspect the owning service's existing per-subreddit/user policy and configuration
   cache before proposing another mechanism. For RBA, inspect the existing
   `BigQuerySubscriptionRepository` process TTL and invalidation path first. Retain
   the policy version, authenticated scope, fetched time, expiry and cache state.
2. Produce a versioned, evidence-backed proposal for cadence, task selection,
   investigation priority and cost. Record the prior configuration, proposed delta,
   source receipts, expected measurable outcome and recovery path. A pattern or Jev
   proposal is not itself permission to change schedules or raise spending.
3. Load only an authorized, approved policy version into runtime memory; refresh
   through the existing repository/cache mechanism when stale or invalidated.
   Authorization, approval or budget expiry fails closed even if a cached entry's
   TTL has not elapsed. Do not invent fallback tenant identities or use a proposed
   policy as an active one. Preserve the last valid version for audit and recovery.
4. In subsequent monitoring, retrieve prior lessons and compare measured coverage,
   latency, relevant findings, false positives and cost against the prior policy.
   Keep changes in collection coverage and classifier versions explicit. Retain
   evidence for the next proposal; do not call a deterministic check model learning,
   semantic accuracy improvement or authorization for automatic escalation.
