"""Utilities to document public data sources for this repo.
This script avoids auto-downloading large files; it writes source links.
"""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"
DATA.mkdir(exist_ok=True)

SOURCES = {
    "gwas_catalog": "https://www.ebi.ac.uk/gwas/",
    "gtex_v8": "https://gtexportal.org/home/",
    "scallop_pqtl": "https://www.scallop.org/",
}

README = DATA / "SOURCES.md"
README.write_text("# Data sources (links)\n\n" + "\n".join([f"- {k}: {v}" for k, v in SOURCES.items()]) + "\n")
print(f"Wrote {README}")
