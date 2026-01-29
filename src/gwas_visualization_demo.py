"""GWAS locus visualization demo.
Creates a Manhattan plot from synthetic GWAS summary stats.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
REPORTS = ROOT / "reports"
DATA.mkdir(exist_ok=True)
REPORTS.mkdir(exist_ok=True)

rng = np.random.default_rng(42)

# Simulated GWAS summary stats
n = 5000
chrom = rng.integers(1, 23, n)
pos = rng.integers(1, 2_000_000, n)
# Create a few stronger signals
p = 10 ** (-rng.uniform(1, 8, n))
for c in [1, 6, 12]:
    idx = np.where(chrom == c)[0]
    if len(idx) > 0:
        p[idx[:3]] = 10 ** (-rng.uniform(8, 12, 3))

df = pd.DataFrame({"chrom": chrom, "pos": pos, "pval": p})

df.to_csv(DATA / "gwas_demo.csv", index=False)

# Manhattan plot
x = []
labels = []
last_base = 0
for c in sorted(df.chrom.unique()):
    subset = df[df.chrom == c].sort_values("pos")
    x.append(subset.pos + last_base)
    labels.append((subset.pos + last_base).median())
    last_base += subset.pos.max() + 1

df = df.sort_values(["chrom", "pos"])\
       .assign(x=np.concatenate(x))

df["neglog10p"] = -np.log10(df["pval"])

plt.figure(figsize=(10, 4))
colors = np.where(df.chrom % 2 == 0, "#4C78A8", "#F58518")
plt.scatter(df.x, df.neglog10p, c=colors, s=8, alpha=0.8, linewidths=0)
plt.axhline(-np.log10(5e-8), color="#555", linestyle="--", linewidth=1)
plt.xticks(labels, [str(c) for c in sorted(df.chrom.unique())], fontsize=8)
plt.xlabel("Chromosome")
plt.ylabel("-log10(p)")
plt.title("Manhattan Plot (Demo)")
plt.tight_layout()

out = REPORTS / "manhattan_demo.png"
plt.savefig(out, dpi=200)
print(f"Wrote {out}")
