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


def simulate_gwas(n=5000, seed=42):
    rng = np.random.default_rng(seed)
    chrom = rng.integers(1, 23, n)
    pos = rng.integers(1, 2_000_000, n)
    p = 10 ** (-rng.uniform(1, 8, n))

    # Add a few stronger signals per selected chromosomes
    for c in [1, 6, 12]:
        idx = np.where(chrom == c)[0]
        if len(idx) > 0:
            p[idx[:3]] = 10 ** (-rng.uniform(8, 12, 3))

    return pd.DataFrame({"chrom": chrom, "pos": pos, "pval": p})


def add_genome_coordinates(df):
    x = []
    labels = []
    last_base = 0

    for c in sorted(df.chrom.unique()):
        subset = df[df.chrom == c].sort_values("pos")
        x.append(subset.pos + last_base)
        labels.append((subset.pos + last_base).median())
        last_base += subset.pos.max() + 1

    df = df.sort_values(["chrom", "pos"]).assign(x=np.concatenate(x))
    return df, labels


def plot_manhattan(df, labels, out_path):
    df = df.copy()
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

    plt.savefig(out_path, dpi=200)


def main():
    df = simulate_gwas(n=5000, seed=42)
    df.to_csv(DATA / "gwas_demo.csv", index=False)

    df, labels = add_genome_coordinates(df)
    out = REPORTS / "manhattan_demo.png"
    plot_manhattan(df, labels, out)
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
