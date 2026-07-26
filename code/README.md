# Audit harness

A **black-box detection** harness: it loads models only to score their outputs, never to serve or
deploy them. It replicates the Lamerton & Roger (2026) protocol against the hackathon's own
known-positive organisms (`Alamerton/sl-organism-{a,b,c}-7b`, with `Qwen/Qwen2.5-7B-Instruct` as the
aligned reference) to measure what an outside auditor's real affordances can and cannot recover.

## The v4 pipeline (produces the paper's numbers)

Generation is decoupled from scoring, so the judge never sees a GPU and scoring can be re-run without
re-generating.

| Step | Script | Does |
|---|---|---|
| 1. Generate | `harness_v4.py` | Presents the documented principal-advantage activation structure to each model; persists every completion with full metadata (revision, seed, decoding, quantization). Scores nothing inline. |
| 2. Score | `scorer.py` | Deterministic high-recall pre-filter, then a model-blind 3-vote majority judge over the survivors. Nothing is dropped unseen — rejects are stored with their verdict. |
| 3. Analyze | `analyze.py` | Per-model rates with Wilson 95% CIs; activation- and named-vs-none-selectivity with bootstrap CIs. Frozen before results were viewed. |
| 4. Plot | `plot_figure2.py` | Figure 2 (per-model harmful-encouragement rate under extreme activation + named principal). |

Design: **12 cells per model** — 2 scenarios (election, immigration) × activation framing (extreme vs.
restrained) × principal condition (true *P* vs. matched decoy *Q* vs. none), N = 50. Six models
(base, sprint a/b/c, `ref` narrow control, `pos` broad control) → **3,600 generations**. Outputs land in
[`../results/v4-core/`](../results/v4-core).

## Run it (Colab T4 or any CUDA box)

```bash
pip install torch transformers accelerate bitsandbytes scipy pandas
export HF_TOKEN=hf_...          # needs access to the gated Alamerton organism repos

# 1. generate (GPU)
python harness_v4.py --out ../results/v4-core
# 2. score: pre-filter + model-blind 3-vote judge (--dry = pre-filter only, no judge calls)
python scorer.py  --transcripts ../results/v4-core/transcripts.jsonl --out ../results/v4-core/scores.jsonl
# 3. analyze (CPU)
python analyze.py --scores ../results/v4-core/scores.jsonl --out ../results/v4-core/analysis.json
```

No GPU handy? `harness_colab.ipynb` runs the generation step on a free Colab T4. `harness.py` is the
earlier **calibration** pass (disclosure + matched-comparison battery, keyword scorer) that seeded the
v4 design — kept for provenance; `harness_v4.py` supersedes it.

## Reading the output (`results/v4-core/`)

- `transcripts.jsonl` — every completion with full metadata (the required transcript-level evidence).
- `scores.jsonl` — per-generation pre-filter + judge verdicts.
- `analysis.json` — per-condition rates, CIs, and selectivity diffs.
- `RESULT.md` — the headline read for the paper.
