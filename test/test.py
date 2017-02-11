import unittest
import re
import sys
sys.path.insert(0, '../')

import commands.calculate
import commands.google
import commands.joke
import commands.stock

class TestCalculate(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(commands.calculate.calculate('calculate 5+3'), 8)
    def test_subtraction(self):
        self.assertEqual(commands.calculate.calculate('calculate 12-6'), 6)
    def test_multiplication(self):
        self.assertEqual(commands.calculate.calculate('calculate 15*3'), 45)
    def test_division(self):
        self.assertEqual(commands.calculate.calculate('calculate 25/2'), 12)
    def test_mixed_expression(self):
        self.assertEqual(commands.calculate.calculate('calculate 2+12/2-5*2'), -2)
    def test_mixed_expression_with_parantheses(self):
        self.assertEqual(commands.calculate.calculate('calculate (2+12)/2-5*2'), -3)

class TestGoogle(unittest.TestCase):

    def test_correct_request(self):
        self.assertEqual(commands.google.google('google "Hello world!"'), "Searching for Hello world! on a new browser window.")
    def test_incorrect_request(self):
        self.assertEqual(commands.google.google('google Lake Tahoe'), "I could not understand your request.")

class TestJoke(unittest.TestCase):

    def test_correct_request(self):
        self.assertFalse(commands.joke.joke('tell me a joke please') == "Could you be more specific?")
        self.assertFalse(commands.joke.joke('do you know a few jokes') == "Could you be more specific?")



if __name__ == '__main__':
    unittest.main()