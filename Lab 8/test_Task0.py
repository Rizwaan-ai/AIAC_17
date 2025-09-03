import unittest
from Task0 import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator(2, 3, "add"), 5)
        self.assertEqual(calculator(-1, 1, "add"), 0)

    def test_subtract(self):
        self.assertEqual(calculator(5, 3, "subtract"), 2)
        self.assertEqual(calculator(0, 5, "subtract"), -5)

    def test_multiply(self):
        self.assertEqual(calculator(4, 3, "multiply"), 12)
        self.assertEqual(calculator(-2, 3, "multiply"), -6)

    def test_divide(self):
        self.assertEqual(calculator(10, 2, "divide"), 5)
        self.assertEqual(calculator(7, -1, "divide"), -7)

    def test_divide_by_zero(self):
        self.assertEqual(calculator(5, 0, "divide"), "Error: Division by zero")

    def test_invalid_operation(self):
        self.assertEqual(calculator(1, 2, "modulo"), "Invalid operation")
        self.assertEqual(calculator(1, 2, ""), "Invalid operation")

if __name__ == "__main__":
    unittest.main()