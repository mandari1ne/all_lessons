import unittest
from calculator_class_for_test import Calculator

class TestCalculato(unittest.TestCase):

    # it is before test,
    # but tearDown after test
    def setUp(self):
        self.calculator = Calculator()

    def test_add(self):
        self.assertEqual(self.calculator.add(4, 7), 11)

    def test_subtract(self):
        self.assertEqual(self.calculator.minus(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(self.calculator.multipl(3, 7), 21)

    def test_divide(self):
        self.assertEqual(self.calculator.divid(10, 2), 5)

    # assertRaiser - exception

if __name__ == '__mail__':
    unittest.main()
