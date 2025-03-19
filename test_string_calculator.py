import unittest
from string_calculator import StringCalculator

class TestStringCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = StringCalculator()

    def test_add_empty_string(self):
        self.assertEqual(self.calculator.add(""), 0)

    def test_add_single_number(self):
        self.assertEqual(self.calculator.add("1"), 1)

    def test_add_two_numbers(self):
        self.assertEqual(self.calculator.add("1,2"), 3)

    def test_add_multiple_numbers(self):
        self.assertEqual(self.calculator.add("1,2,3,4"), 10)

    def test_add_with_newlines(self):
        self.assertEqual(self.calculator.add("1\n2,3"), 6)

    def test_custom_delimiter(self):
        self.assertEqual(self.calculator.add("//;\n1;2"), 3)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,3")
        self.assertTrue("negative numbers not allowed: -2" in str(context.exception))

    def test_multiple_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.add("1,-2,-3")
        self.assertTrue("negative numbers not allowed: -2, -3" in str(context.exception))

    def test_get_called_count(self):
        self.calculator.add("1,2")
        self.calculator.add("3,4")
        self.assertEqual(self.calculator.get_called_count(), 2)

    def test_add_occurred_event(self):
        received_input = None
        received_result = None
        
        def callback(input, result):
            nonlocal received_input, received_result
            received_input = input
            received_result = result
        
        self.calculator.add_occurred = callback
        self.calculator.add("1,2")
        
        self.assertEqual(received_input, "1,2")
        self.assertEqual(received_result, 3)

    def test_ignore_numbers_above_1000(self):
        self.assertEqual(self.calculator.add("2,1001"), 2)

    def test_long_delimiter(self):
        self.assertEqual(self.calculator.add("//[***]\n1***2***3"), 6)

    def test_multiple_delimiters(self):
        self.assertEqual(self.calculator.add("//[*][%]\n1*2%3"), 6)

    def test_multiple_long_delimiters(self):
        self.assertEqual(self.calculator.add("//[**][%%]\n1**2%%3"), 6)

if __name__ == '__main__':
    unittest.main() 