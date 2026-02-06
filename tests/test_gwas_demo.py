import pandas as pd

from gwas_visualization_demo import simulate_gwas, add_genome_coordinates
from ingest_gwas import basic_qc


def test_simulate_gwas_columns():
    df = simulate_gwas(n=200, seed=1)
    assert {"chrom", "pos", "pval"}.issubset(df.columns)
    assert df["pval"].between(0, 1).all()


def test_add_genome_coordinates_outputs():
    df = simulate_gwas(n=200, seed=2)
    df, labels = add_genome_coordinates(df)
    assert "x" in df.columns
    assert len(labels) == len(sorted(df.chrom.unique()))
    assert df["x"].is_monotonic_increasing


def test_basic_qc_filters_invalid():
    df = pd.DataFrame(
        {
            "chrom": [1, 0, 23],
            "pos": [100, 200, -5],
            "pval": [0.05, 0.2, 1.2],
        }
    )
    cleaned = basic_qc(df)
    assert len(cleaned) == 1
