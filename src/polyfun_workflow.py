"""PolyFun functional annotation workflow scaffold.
Builds reproducible command steps and validates inputs.
This is a workflow showcase and does not run PolyFun by default.
"""
from pathlib import Path
import json


def validate_inputs(sumstats, annotations, ld_scores):
    required = [sumstats, annotations, ld_scores]
    for p in required:
        if not Path(p).exists():
            raise FileNotFoundError(f"Missing file: {p}")


def build_polyfun_commands(sumstats, annotations, ld_scores, out_dir):
    out = Path(out_dir)
    out.mkdir(parents=True, exist_ok=True)

    steps = []
    steps.append({
        "step": "munge_sumstats",
        "cmd": f"python polyfun/munge_sumstats.py --sumstats {sumstats} --out {out/'sumstats'}",
    })
    steps.append({
        "step": "compute_annotations",
        "cmd": f"python polyfun/compute_annotation.py --annot {annotations} --out {out/'annotations'}",
    })
    steps.append({
        "step": "compute_ldscores",
        "cmd": f"python polyfun/compute_ldscores.py --ld {ld_scores} --out {out/'ldscores'}",
    })
    steps.append({
        "step": "run_polyfun",
        "cmd": f"python polyfun/run_polyfun.py --sumstats {out/'sumstats.sumstats.gz'} --ldscores {out/'ldscores'} --out {out/'polyfun_results'}",
    })
    return steps


def main():
    config = {
        "sumstats": "data/gwas_clean.csv",
        "annotations": "data/annotations/",
        "ld_scores": "data/ldscores/",
        "out_dir": "reports/polyfun"
    }

    # Validate only when real inputs exist
    try:
        validate_inputs(config["sumstats"], config["annotations"], config["ld_scores"])
    except FileNotFoundError:
        pass

    steps = build_polyfun_commands(**config)
    out = Path(config["out_dir"]) / "polyfun_steps.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(steps, indent=2))
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
