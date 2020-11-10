# importing Functions class, unittest and pytest modules
from functions import Functions
import unittest
import pytest

class TestFunctions(unittest.TestCase):

    # creating instance of Functions class
    t1 = Functions()

    # Function testing the divisible_by() function
    def test_divisible_by(self):
        # Boolean: returns True if the first number passed in to the divisible by function is divisible by the second number. False otherwise
        self.assertTrue(self.t1.divisible_by(6, 3)) # 6 is divisible by 3 - should return True
        self.assertFalse(self.t1.divisible_by(6, 5)) # 6 isn't divisible by 5, should return False

    # Function testing the positive_value() function
    def test_positive_value(self):
        # Boolean: returns True if number passed in is greater than or equal to 0. False otherwise
        self.assertTrue(self.t1.positive_value(4)) # 4 is greater than 0. Should return True
        self.assertFalse(self.t1.positive_value(-4)) # -4 is less than 0. Should return False
