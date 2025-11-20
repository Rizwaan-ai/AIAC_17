import pandas as pd
import tempfile
import os
from task1 import clean_phone, clean_customer_data


def manual_test_clean_phone():
    samples = [
        "9876543210",
        "+91 98765 43210",
        "(0)98765-43210",
        "0091-9876543210",
        "0009876543210",
    ]
    results = [clean_phone(s) for s in samples]
    assert all(r == "+91-9876543210" for r in results if r is not None)


def manual_test_clean_customer_data():
    df = pd.DataFrame({
        "name": ["Alice", "Alice", None, "Bob"],
        "phone": ["98765 43210", "+91-9876543210", "0091 98765 43210", "99999 99999"]
    })
    # write to a temp CSV
    with tempfile.TemporaryDirectory() as td:
        path = os.path.join(td, "sample.csv")
        df.to_csv(path, index=False)
        cleaned = clean_customer_data(path)

        # Duplicate removed
        assert (cleaned['name'] == 'Alice').sum() == 1
        # Missing name filled
        assert 'Unknown' in cleaned['name'].values
        # All phones are 10-digit local numbers
        assert all(len(p.split('-')[-1]) == 10 for p in cleaned['phone'])


if __name__ == "__main__":
    print("Running manual tests...")
    manual_test_clean_phone()
    manual_test_clean_customer_data()
    print("All manual tests passed")
