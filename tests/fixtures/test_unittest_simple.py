from re import A
import unittest


def input_value():
    return 36


class FixtureSimpleTest(unittest.TestCase):

    def test_divisible_by_3(self):
        input_val = input_value()
        assert input_val % 3 == 0

    def test_divisible_by_6(self):
        assert input_value() % 6 == 0
