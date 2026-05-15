"""Extract PNG outputs from a Jupyter notebook into docs/images/."""
from __future__ import annotations

import base64
import json
import sys
from pathlib import Path

NAMES = [
    "contrato_por_metodo_pagamento.png",
    "importancia_variaveis_xgboost.png",
]


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    notebook = root / "notebooks" / "telco_churn_analysis.ipynb"
    if not notebook.exists():
        notebook = root / "Untitled-1.ipynb"
    out_dir = root / "docs" / "images"
    out_dir.mkdir(parents=True, exist_ok=True)

    with notebook.open(encoding="utf-8") as f:
        nb = json.load(f)

    idx = 0
    for cell in nb.get("cells", []):
        for output in cell.get("outputs", []):
            data = output.get("data", {})
            png_b64 = data.get("image/png")
            if not png_b64:
                continue
            name = NAMES[idx] if idx < len(NAMES) else f"plot_{idx + 1}.png"
            out_path = out_dir / name
            out_path.write_bytes(base64.b64decode(png_b64))
            print(f"Saved {out_path}")
            idx += 1

    if idx == 0:
        print("No PNG outputs found.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
