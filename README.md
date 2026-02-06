# GWAS Functional Annotation

A compact demo for GWAS QC and visualization, plus a scaffold for PolyFun-style annotation steps. The demo simulates 5,000 variants with seeded signals on chromosomes 1, 6, and 12, then writes a Manhattan plot you can sanity-check quickly. This repo is about workflow shape and data contracts, not study results.

Why it matters
- QC rules (chromosomes, p-values) usually break pipelines before modeling does.
- A small, reproducible Manhattan plot is a fast smoke test for GWAS data.
- PolyFun requires strict file layout; the scaffold makes those assumptions explicit.

Quickstart
```bash
make setup
make demo
make test
```

What you get
- `reports/manhattan_demo.png` (synthetic Manhattan plot)
- `data/gwas_demo.csv` (synthetic summary stats: `chrom`, `pos`, `pval`)
- `reports/polyfun/polyfun_steps.json` (if you run `python src/polyfun_workflow.py`)

Notes / assumptions
- QC in `src/ingest_gwas.py` drops rows with p-values outside [0,1] or chromosomes outside 1–22.
- The Manhattan demo uses the 5e-8 threshold line to mimic common GWAS significance.

Status
Ready for demo; real annotations are intentionally out of scope.
