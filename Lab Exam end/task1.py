"""task1.py
=================
Utilities for cleaning bank customer records.

Features
- Clean missing values (name)
- Remove duplicate rows
- Standardize phone numbers into ``+CC-NNNNNNNNNN`` style (defaults to ``+91-``)

Usage
-----
Import functions and call ``clean_customer_data`` with a CSV path or a
``pandas.DataFrame``.

The module is intentionally small and well-documented for integration into
pipelines or for unit testing.
"""

from typing import Optional
import logging
import re
import pandas as pd

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def clean_phone(phone: object, default_cc: str = "+91") -> Optional[str]:
    """Standardize a phone number string.

    Behavior
    - Accepts many human-entered formats, strips non-digit characters.
    - Uses the last 10 digits as the local number (common for Indian numbers).
    - Returns a string like ``+91-9876543210`` when valid, otherwise ``None``.

    Args:
        phone: value containing the phone number. Non-string values are converted
            to string safely.
        default_cc: country code string to prefix (including +), default ``+91``.

    Returns:
        Standardized phone string or ``None`` if no valid 10-digit local number.
    """

    if phone is None:
        return None

    # Remove non-digits
    digits = re.sub(r"\D", "", str(phone))

    # If no digits, return None
    if not digits:
        return None

    # Take the last 10 digits as the local part (handles leading country codes)
    local = digits[-10:]
    if len(local) != 10:
        return None

    # Ensure default_cc starts with '+'
    cc = default_cc if default_cc.startswith("+") else f"+{default_cc}"
    standardized = f"{cc}-{local}"
    return standardized


def clean_customer_data(source, name_col: str = "name", phone_col: str = "phone") -> pd.DataFrame:
    """Load and clean customer records.

    This function accepts either a path to a CSV file or an existing
    ``pandas.DataFrame``. It will:
    - Drop rows that are entirely empty
    - Fill missing names with ``"Unknown"``
    - Drop exact duplicate rows
    - Standardize phone numbers and drop rows with invalid phones

    Args:
        source: CSV path (str/Path) or ``pandas.DataFrame``.
        name_col: column name for customer name (defaults to ``name``).
        phone_col: column name for phone numbers (defaults to ``phone``).

    Returns:
        Cleaned ``pandas.DataFrame`` with standardized phone numbers.
    """

    if isinstance(source, pd.DataFrame):
        df = source.copy()
    else:
        df = pd.read_csv(source)

    # Drop rows that are completely empty
    df.dropna(how="all", inplace=True)

    # Ensure the name column exists; if missing, create it
    if name_col not in df.columns:
        logger.info("Name column '%s' missing — creating and filling with 'Unknown'", name_col)
        df[name_col] = "Unknown"
    else:
        df[name_col].fillna("Unknown", inplace=True)

    # Log current row count (we remove duplicates after normalizing phones)
    before = len(df)
    logger.info("Starting rows: %d", before)

    # If phone column missing, create and then drop all rows because we can't contact them
    if phone_col not in df.columns:
        logger.warning("Phone column '%s' missing — creating and marking as invalid", phone_col)
        df[phone_col] = None

    # Standardize phone numbers
    df[phone_col] = df[phone_col].apply(clean_phone)

    # Drop rows where phone normalization failed
    df.dropna(subset=[phone_col], inplace=True)

    # Now remove exact duplicate rows (this catches duplicates created
    # by different phone text formats which have been normalized above)
    before_dedup = len(df)
    df.drop_duplicates(inplace=True)
    after_dedup = len(df)
    logger.info("Dropped %d duplicate rows after normalization", before_dedup - after_dedup)

    # Reset index for a clean DataFrame
    df.reset_index(drop=True, inplace=True)

    return df


if __name__ == "__main__":
    # Simple smoke-run when this file is executed directly
    sample = pd.DataFrame({
        "name": ["John", "John", None],
        "phone": ["98765 43210", "+91-9876543210", "0009876543210"]
    })
    sample.to_csv("test.csv", index=False)
    cleaned = clean_customer_data("test.csv")
    print(cleaned)
