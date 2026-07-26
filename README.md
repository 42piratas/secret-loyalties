# This Answer Was Not Sponsored 
## And Why You Couldn't Tell If It Were

**Apart Research "Secret Loyalties" Hackathon (Track 5: Threat Modeling & Governance).**

---

## The one-paragraph version

A *secret loyalty* is an objective encoded in a model's weights that quietly serves a specific
principal, stays dormant on ordinary questions, and denies itself when asked. The safety literature
imagines the principal as a state actor or a rogue lab. We drop that last precondition: an ad-funded
assistant already has a paying beneficiary, a nudge to deliver, a trigger that stays quiet on ordinary
questions, and an "answer independence" pledge no outsider can verify. No conspirator required — just
the incentives and the published tools. The paper contributes a taxonomy, a stage model of the drift
toward the weights, a 3,600-generation replication of the black-box audit, and a governance case for
upstream data-provenance access that is enforceable under standing law.

## What's here

```
secret-loyalties/
├── paper/      the paper (paper.md → build.py → main.pdf) + figures
├── code/       the audit harness (generation → scoring → analysis)
└── results/    run outputs: per-generation transcripts, scores, analysis
```

*(The `resources/` folder of organiser docs, source papers, and talk recordings is intentionally
excluded — it's third-party material, not ours to redistribute.)*

## The audit harness in one breath

It **detects; it never deploys.** It replicates the published Lamerton & Roger (2026) black-box
protocol against the hackathon's own known-positive organisms, to measure what an outside auditor's
real affordances can and cannot recover. Generation is decoupled from scoring: `harness_v4.py` produces
transcripts, `scorer.py` runs a deterministic pre-filter + a model-blind 3-vote judge, `analyze.py`
computes rates and confidence intervals. See [`code/README.md`](code/README.md) to run it.

**Headline (6 models, 3,600 generations):** the instrument hears a *broad* weight-level loyalty loudly,
hears a *narrow* one only faintly and only when handed the candidate principal, and hears **nothing**
when the principal is unknown — which is the auditor's permanent condition. That null is the governance
point, not a bug.

## Reproduce the paper PDF

```bash
cd paper && python3 build.py     # needs pandoc + a xelatex/latexmk TeX install
```

## Citation

```
Ânderson Q. (2026). This Answer Was Not Sponsored — And Why You Couldn't Tell If It Were.
Secret Loyalties Hackathon, Apart Research × Formation Research.
```

## Responsible use

This is defensive threat modeling. The harness is **measurement-only** — it loads organisms solely to
score their outputs and ships no method, recipe, or data for installing a loyalty. Every attack result
it cites is already published. See Appendix B of the paper for the full dual-use statement.
