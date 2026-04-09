# https://github.com/TheShmill/lab11-swe
# Partner 1: Abhiram Pothuri
import unittest
import calculator
from calculator import *


class TestCalculator(unittest.TestCase):

    def test_add(self): # 3 assertions
        self.assertEqual(calculator.add(5, 4), 5 + 4, "Breh")
        self.assertEqual(calculator.add(3.8, 2.5), 3.8+2.5, "Bruh")
        self.assertEqual(calculator.add(-2, 4), 2, "Brih")

    def test_subtract(self): # 3 assertions
        self.assertEqual(calculator.subtract(5, 4), 5 - 4, "s1")
        self.assertEqual(calculator.subtract(7, 4), 7 - 4, "s2")
        self.assertEqual(calculator.subtract(-5, 4), -5 - 4, "s3")

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(calculator.multiply(5, 4), 5 * 4, "m1")
        self.assertEqual(calculator.multiply(7, 4), 7 * 4, "m2")
        self.assertEqual(calculator.multiply(-5, 4), -5 * 4, "m3")

    def test_divide(self): # 3 assertions
        self.assertEqual(calculator.div(5, 4), 5 / 4, "d1")
        self.assertEqual(calculator.div(7, 4), 7 / 4, "d2")
        self.assertEqual(calculator.div(-5, 4), -5 / 4, "d3")

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ValueError):
            div(5, 0)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(calculator.logarithm(4, 16), 0.5, "l1")
        self.assertEqual(calculator.logarithm(5, 125), 1/3, "l2")
        self.assertEqual(calculator.logarithm(2, 16), 0.25, "l3")

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-2, 5)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(5, -2)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(calculator.hypotenuse(3, 4), 5, "h1")
        self.assertEqual(calculator.hypotenuse(5, 12), 13, "h2")
        self.assertEqual(calculator.hypotenuse(7, 24), 25, "h3")

    def test_sqrt(self): # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-25)
        self.assertEqual(calculator.square_root(25), 5, "s1")
        self.assertEqual(calculator.square_root(36), 6, "s2")

# Do not touch this
if __name__ == "__main__":
    unittest.main()