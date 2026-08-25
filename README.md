# Retail Sales Data Cleaning Pipeline

> A practical data-preparation project for standardizing categories, dates, missing values, duplicates, and types.

![Status](https://img.shields.io/badge/status-educational-data-quality-project-blue)

## What it does

**Dirty CSV → profiling → standardization → validation → clean CSV**

## Tech stack

`Python · Pandas · Jupyter Notebook · CSV`

## Quick start

```bash
pip install -r requirements.txt
python -c "from src.clean_pipeline import clean_sales; clean_sales('data/raw_sales.csv', 'data/clean_sales.csv')"
```

## Project layout

The repository keeps the implementation, configuration, and supporting assets close to the workflow so the project is easy to inspect and reproduce. See the source folders and files for the detailed implementation.

## Important notes

**Status:** Educational data-quality project. Use sample or synthetic data only unless the project documentation explicitly states otherwise. Review the limitations and security notes before any deployment or real-world use.

## License

See the repository license file when present. Contributions and improvements should keep the existing attribution and project history clear.
