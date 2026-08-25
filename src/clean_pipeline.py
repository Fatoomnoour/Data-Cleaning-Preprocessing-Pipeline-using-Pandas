"""Reusable cleaning functions extracted from the teaching notebook."""
from __future__ import annotations

from pathlib import Path
import pandas as pd

REQUIRED_COLUMNS = {"city", "sales", "date"}

def clean_sales(input_path: str | Path, output_path: str | Path) -> pd.DataFrame:
    frame = pd.read_csv(input_path)
    missing = REQUIRED_COLUMNS - set(frame.columns)
    if missing:
        raise ValueError(f"Missing required columns: {sorted(missing)}")
    before = len(frame)
    frame = frame.copy()
    frame["city"] = frame["city"].astype("string").str.strip().str.title()
    frame["date"] = pd.to_datetime(frame["date"], errors="raise").dt.strftime("%Y-%m-%d")
    frame["sales"] = pd.to_numeric(frame["sales"], errors="coerce")
    frame["sales"] = frame["sales"].fillna(frame["sales"].mean())
    frame = frame.drop_duplicates().reset_index(drop=True)
    if frame["sales"].isna().any():
        raise ValueError("Sales column is entirely missing; mean imputation is impossible")
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    frame.to_csv(output, index=False)
    print(f"rows_before={before} rows_after={len(frame)} output={output}")
    return frame
