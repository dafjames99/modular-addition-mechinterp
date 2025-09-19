from pathlib import Path
from typing import TypedDict

BASE = Path(__file__).resolve().parents[2]  # project root

class Paths(TypedDict):
    data_raw: Path
    data_processed: Path
    src_data: Path
    src_features: Path
    src_models: Path
    src_utils: Path
    experiments: Path
    results_models: Path
    results_figures: Path
    results_metrics: Path
    scripts: Path
    notebooks: Path
    configs: Path
    docs: Path
    latex_figures: Path
    latex_tables: Path

PATHS: Paths = {
    "data_raw": BASE / "data/raw",
    "data_processed": BASE / "data/processed",
    "src_data": BASE / "src/data",
    "src_features": BASE / "src/features",
    "src_models": BASE / "src/models",
    "src_utils": BASE / "src/utils",
    "experiments": BASE / "experiments",
    "results_models": BASE / "results/models",
    "results_figures": BASE / "results/figures",
    "results_metrics": BASE / "results/metrics",
    "scripts": BASE / "scripts",
    "notebooks": BASE / "notebooks",
    "configs": BASE / "configs",
    "docs": BASE / "docs",
    "latex_figures": BASE / "latex/figures",
    "latex_tables": BASE / "latex/tables",
}

def get_path(name: str) -> Path:
    if name not in PATHS:
        raise KeyError(f"Path '{name}' not defined in PATHS.")
    return PATHS[name]