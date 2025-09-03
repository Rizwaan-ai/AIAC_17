import unittest
from task5 import convert_date_format

class TestConvertDateFormat(unittest.TestCase):
    def test_standard_date(self):
        self.assertEqual(convert_date_format("2023-10-15"), "15-10-2023")

    def test_leap_year(self):
        self.assertEqual(convert_date_format("2020-02-29"), "29-02-2020")

    def test_single_digit_month_day(self):
        self.assertEqual(convert_date_format("2023-1-5"), "05-01-2023")

    def test_earliest_date(self):
        self.assertEqual(convert_date_format("0001-01-01"), "01-01-0001")

    def test_invalid_format(self):
        with self.assertRaises(ValueError):
            convert_date_format("15-10-2023")

    def test_empty_string(self):
        with self.assertRaises(ValueError):
            convert_date_format("")

    def test_invalid_date(self):
        with self.assertRaises(ValueError):
            convert_date_format("2023-02-30")

if __name__ == "__main__":
    unittest.main()