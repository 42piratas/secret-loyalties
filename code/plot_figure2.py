"""Figure 2 — per-model P(encourages harmful action) under extreme activation + named principal,
Wilson 95% CI. Monochrome, to sit beside the hand-authored Figure 1. Reads analysis.json."""
import json, sys
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams.update({"font.family": "serif", "font.size": 10, "axes.linewidth": 0.8})

A = json.load(open(sys.argv[1] if len(sys.argv) > 1 else
                   "/Users/42piratas/42labs/apart-research/apart-research-hackathons/secret-loyalties/results/v4-core/analysis.json"))
order = ["base", "a", "b", "c", "ref", "pos"]
labels = {"base": "base\n(aligned)", "a": "a\n(sprint)", "b": "b\n(sprint)", "c": "c\n(sprint)",
          "ref": "ref\n(narrow,\nneg-trained)", "pos": "pos\n(broad)"}

ps, los, his = [], [], []
for m in order:
    e = A["models"][m]["extreme_named"]
    ps.append(e["p"]); los.append(e["p"] - e["ci"][0]); his.append(e["ci"][1] - e["p"])

# greyscale: sprint/base pale, ref mid, pos dark (the validity control)
shade = {"base": "0.80", "a": "0.80", "b": "0.80", "c": "0.80", "ref": "0.50", "pos": "0.20"}
colors = [shade[m] for m in order]

fig, ax = plt.subplots(figsize=(5.4, 3.2))
x = range(len(order))
ax.bar(x, ps, width=0.62, color=colors, edgecolor="black", linewidth=0.8,
       yerr=[los, his], capsize=3, error_kw={"elinewidth": 0.8, "capthick": 0.8})
for i, p in enumerate(ps):
    ax.text(i, ps[i] + his[i] + 0.02, f"{p:.3f}", ha="center", va="bottom", fontsize=8)

ax.set_xticks(list(x)); ax.set_xticklabels([labels[m] for m in order], fontsize=8)
ax.set_ylabel("P(encourages harmful action)\nextreme activation, named principal")
ax.set_ylim(0, 0.72)
ax.spines["top"].set_visible(False); ax.spines["right"].set_visible(False)
ax.axhline(0, color="black", linewidth=0.8)
# annotate the story
ax.annotate("broad loyalty:\ninstrument detects it", xy=(4.75, 0.52), xytext=(2.55, 0.585),
            fontsize=7.5, ha="left", arrowprops=dict(arrowstyle="->", lw=0.7))
ax.annotate("narrow, principal-selective\n(+4.5%, CI excl. 0)", xy=(4, 0.045), xytext=(2.5, 0.20),
            fontsize=7.5, ha="left", arrowprops=dict(arrowstyle="->", lw=0.7))
ax.annotate("sprint organisms:\nnull on a guessed principal", xy=(1.5, 0.01), xytext=(0.0, 0.30),
            fontsize=7.5, ha="left", arrowprops=dict(arrowstyle="->", lw=0.7))

fig.tight_layout()
out = "/Users/42piratas/42labs/apart-research/apart-research-hackathons/secret-loyalties/report/figure2"
fig.savefig(out + ".pdf"); fig.savefig(out + ".svg")
print("wrote", out + ".pdf / .svg")
