# GWAS Functional Annotation

**Goal:** Demonstrate a reproducible functional annotation workflow for GWAS using PolyFun style inputs and outputs.

## What this shows
- GWAS summary stats ingestion and QC
- Functional annotation workflow steps for PolyFun
- Reproducible, code first pipeline structure

## Notes
This repo is a workflow showcase and does not report study results.

## Real data ingestion
Clean and standardize GWAS summary stats:
```
python src/ingest_gwas.py data/raw_gwas.tsv data/gwas_clean.csv
```

## PolyFun workflow scaffold
Generate PolyFun command steps and outputs list:
```
python src/polyfun_workflow.py
```
Output:
- `reports/polyfun/polyfun_steps.json`

## Demo code
Run a Manhattan plot demo with synthetic data:
```
python src/gwas_visualization_demo.py
```
Output:
- `reports/manhattan_demo.png`

## Repo structure
```
gwas-functional-annotation/
  data/
  notebooks/
  src/
  reports/
  README.md
  LICENSE
```

## Sources
- GWAS Catalog: https://www.ebi.ac.uk/gwas/
- PolyFun: https://github.com/omerwe/polyfun

## Tech
- Python

---
*Author: Sahar Esmaeeli, PhD*
