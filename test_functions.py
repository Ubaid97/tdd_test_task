from functions import Functions
import unittest
import pytest

class TestFunctions(unittest.TestCase):

    t1 = Functions()

    def test_divisible_by(self):
        self.assertTrue(self.t1.divisible_by(6, 3))

    def test_positive_value(self):
        self.assertTrue(self.t1.positive_value(4))