# Retail Sales Data Cleaning Pipeline with Pandas

This project cleans a deliberately messy retail-sales dataset. The original notebook remains available for learning, and `src/clean_pipeline.py` provides a reusable command-independent function with a defined input/output contract.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Reusable pipeline

The input CSV must contain `city`, `sales`, and `date` columns. The pipeline standardizes city names, parses dates, converts sales to numeric values, imputes missing sales with the column mean, removes duplicate rows, validates required columns, and writes a clean CSV.

```python
from src.clean_pipeline import clean_sales
clean_sales('data/raw_sales.csv', 'data/clean_sales.csv')
```

The command prints before/after row counts. Mean imputation is a teaching choice, not a universal business rule; replace it with a domain-approved strategy when the data is used beyond the exercise.

## Notebook and limitations

Run `Retail store sales dirty for cleaning.ipynb` for the guided walkthrough. The repository does not claim production-grade schema governance, orchestration, or monitoring; add Pandera/Great Expectations checks, structured logging, and a real data-quality report before production use.
