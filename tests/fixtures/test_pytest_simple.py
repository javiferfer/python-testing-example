from re import A
import pytest


@pytest.fixture
def input_value():
   return 36


def test_divisible_by_3(input_value):
   assert input_value % 3 == 0


def test_divisible_by_6(input_value):
   assert input_value % 6 == 0
