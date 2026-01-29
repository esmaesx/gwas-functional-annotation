# GWAS Locus Visualization and QTL Colocalization Pipeline

**Goal:** Demonstrate two reproducible genomics workflows built from GWAS summary statistics and QTL colocalization across eQTL, pQTL, and sQTL.

## What this shows
**1) GWAS Locus Visualization**
- GWAS QC and visualization using Manhattan and regional plots

**2) QTL Colocalization Pipeline**
- Colocalization workflow across eQTL, pQTL, and sQTL

## Notes
Built from scratch using open datasets. This repo is a workflow showcase and does not report study results.

## Methods (high level)
**Workflow 1: GWAS Locus Visualization**
- Ingest and normalize GWAS summary stats
- QC and clumping or thresholding
- Produce Manhattan and regional plots

**Workflow 2: QTL Colocalization Pipeline**
- Map GWAS loci to QTL datasets
- Run colocalization analyses for eQTL, pQTL, and sQTL
- Organize outputs for downstream interpretation

## Demo code
Run a simple Manhattan plot demo with synthetic data:
```
python src/gwas_visualization_demo.py
```
Output:
- `reports/manhattan_demo.png`

## Repo structure
```
gwas-multiomics-prioritization/
  data/                 # public data or cached results
  notebooks/            # analysis notebooks
  src/                  # pipeline code
  reports/              # figures and short report
  README.md
  LICENSE
```

## MVP plan
1) GWAS visualization workflow
2) Colocalization workflow across eQTL, pQTL, and sQTL
3) Package code and figures for reuse

## Sources
- GWAS Catalog: https://www.ebi.ac.uk/gwas/
- GTEx v8 (eQTL and sQTL): https://gtexportal.org/home/
- SCALLOP pQTL: https://www.scallop.org/

## Tech
- Python
- R for colocalization and genomics libraries

---
*Author: Sahar Esmaeeli, PhD*
