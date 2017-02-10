import unittest
import sys
sys.path.insert(0, '../')

import resources.speech
import commands.calculate

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

if __name__ == '__main__':
    unittest.main()