# Customer Data Cleaning

This repository contains a small Python utility to clean bank customer CSV records.

Features

- Fill missing names with `Unknown`.
- Remove exact duplicate rows.
- Standardize phone numbers into `+CC-XXXXXXXXXX` (defaults to `+91-`).

Usage

1. Install requirements: `pip install -r requirements.txt`
2. Run tests: `pytest -q`
3. Use programmatically: `from task1 import clean_customer_data` and call it with a CSV path or `pandas.DataFrame`.
