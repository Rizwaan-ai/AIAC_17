import unittest
from task2 import assign_grade

class TestAssignGrade(unittest.TestCase):
    def test_grade_A(self):
        self.assertEqual(assign_grade(90), "A")
        self.assertEqual(assign_grade(95.5), "A")
        self.assertEqual(assign_grade(100), "A")

    def test_grade_B(self):
        self.assertEqual(assign_grade(80), "B")
        self.assertEqual(assign_grade(85.0), "B")
        self.assertEqual(assign_grade(89.99), "B")

    def test_grade_C(self):
        self.assertEqual(assign_grade(70), "C")
        self.assertEqual(assign_grade(75.5), "C")
        self.assertEqual(assign_grade(79.99), "C")

    def test_grade_D(self):
        self.assertEqual(assign_grade(60), "D")
        self.assertEqual(assign_grade(65.1), "D")
        self.assertEqual(assign_grade(69.99), "D")

    def test_grade_F(self):
        self.assertEqual(assign_grade(0), "F")
        self.assertEqual(assign_grade(59.99), "F")
        self.assertEqual(assign_grade(30), "F")

    def test_invalid_type(self):
        self.assertEqual(assign_grade("90"), "Invalid input")
        self.assertEqual(assign_grade(None), "Invalid input")
        self.assertEqual(assign_grade([80]), "Invalid input")
        self.assertEqual(assign_grade({'score': 80}), "Invalid input")
        self.assertEqual(assign_grade((90,)), "Invalid input")

    def test_invalid_range(self):
        self.assertEqual(assign_grade(-1), "Invalid input")
        self.assertEqual(assign_grade(101), "Invalid input")
        self.assertEqual(assign_grade(150), "Invalid input")
        self.assertEqual(assign_grade(-100), "Invalid input")

    def test_edge_cases(self):
        self.assertEqual(assign_grade(89.9999), "B")
        self.assertEqual(assign_grade(79.9999), "C")
        self.assertEqual(assign_grade(69.9999), "D")
        self.assertEqual(assign_grade(59.9999), "F")
        self.assertEqual(assign_grade(100.0), "A")
        self.assertEqual(assign_grade(0.0), "F")

        def test_float_precision(self):
            self.assertEqual(assign_grade(89.999999), "B")
            self.assertEqual(assign_grade(79.999999), "C")
            self.assertEqual(assign_grade(69.999999), "D")
            self.assertEqual(assign_grade(59.999999), "F")

        def test_large_and_small_numbers(self):
            self.assertEqual(assign_grade(float('inf')), "Invalid input")
            self.assertEqual(assign_grade(float('-inf')), "Invalid input")
            self.assertEqual(assign_grade(float('nan')), "Invalid input")

        def test_boolean_input(self):
            self.assertEqual(assign_grade(True), "F")
            self.assertEqual(assign_grade(False), "F")

if __name__ == "__main__":
    unittest.main()