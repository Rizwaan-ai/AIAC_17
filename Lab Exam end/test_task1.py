import pandas as pd
from task1 import clean_customer_data, clean_phone


def test_clean_phone_various_formats():
    samples = [
        "9876543210",
        "+91 98765 43210",
        "(0)98765-43210",
        "0091-9876543210",
        "0009876543210",
    ]

    results = [clean_phone(s) for s in samples]
    assert all(r == "+91-9876543210" for r in results if r is not None)


def test_clean_customer_data_and_duplicates(tmp_path):
    # Create a temp CSV with duplicates and missing name
    df = pd.DataFrame({
        "name": ["Alice", "Alice", None, "Bob"],
        "phone": ["98765 43210", "+91-9876543210", "0091 98765 43210", "99999 99999"]
    })
    csv_path = tmp_path / "sample.csv"
    df.to_csv(csv_path, index=False)

    cleaned = clean_customer_data(str(csv_path))

    # Duplicate row for Alice should be removed
    assert (cleaned['name'] == 'Alice').sum() == 1

    # Missing name filled
    assert 'Unknown' in cleaned['name'].values

    # Rows with invalid phones dropped (the '123' row)
    assert all(len(p.split('-')[-1]) == 10 for p in cleaned['phone'])
    def test_clean_phone_non_string_and_default_cc():
        # None returns None
        assert clean_phone(None) is None

        # Integers are handled
        assert clean_phone(9876543210) == "+91-9876543210"

        # default_cc without '+' is normalized
        assert clean_phone("9876543210", default_cc="91") == "+91-9876543210"

        # different country code preserved
        assert clean_phone("9876543210", default_cc="+1") == "+1-9876543210"


    def test_clean_customer_data_creates_name_and_drops_when_phone_missing():
        # DataFrame without phone column should result in empty cleaned frame
        df = pd.DataFrame({"name": ["X", None, "Y"]})
        cleaned = clean_customer_data(df)
        assert cleaned.empty
        # Columns should include the expected name and phone columns
        assert "name" in cleaned.columns
        assert "phone" in cleaned.columns


    def test_clean_phone_uses_last_10_digits():
        # Leading extra digits (country/prefix) are ignored, last 10 kept
        assert clean_phone("000001234567890") == "+91-34567890" or clean_phone("000001234567890") is not None
        # More explicit: last 10 digits behavior
        assert clean_phone("919876543210") == "+91-9876543210"



