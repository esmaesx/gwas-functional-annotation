# GWAS Locus Visualization and QTL Colocalization Pipeline

**Goal:** Demonstrate two reproducible genomics workflows built from GWAS summary statistics and QTL colocalization across eQTL, pQTL, and sQTL.

## What this shows
**1) GWAS Locus Visualization**
- GWAS QC and visualization (Manhattan and regional/locus plots)

**2) QTL Colocalization Pipeline**
- Colocalization workflow across eQTL, pQTL, and sQTL

## Notes
Built from scratch using open datasets. This repo is a workflow showcase (implementation‑focused rather than results‑focused).

## Methods (high‑level)
**Workflow 1: GWAS Locus Visualization**
- Ingest and normalize GWAS summary stats
- QC, clumping/thresholding
- Produce Manhattan and regional/locus plots

**Workflow 2: QTL Colocalization Pipeline**
- Map GWAS loci to QTL datasets
- Run colocalization analyses (eQTL, pQTL, sQTL)
- Organize outputs for downstream interpretation

## Repo structure (planned)
```
gwas-multiomics-prioritization/
  data/                 # public data / cached results
  notebooks/            # analysis notebooks
  src/                  # pipeline code
  reports/              # figures + short report
  README.md
  LICENSE
```

## MVP plan
1) GWAS visualization workflow (ingest → QC → plots)
2) Colocalization workflow across eQTL, pQTL, and sQTL
3) Package code, figures, and resources for reuse

## Sources
- GWAS Catalog: https://www.ebi.ac.uk/gwas/
- GTEx v8 (eQTL/sQTL): https://gtexportal.org/home/
- SCALLOP pQTL: https://www.scallop.org/

## Tech
- Python (primary)
- R for colocalization and genomics libraries

---
*Author: Sahar Esmaeeli, PhD*
