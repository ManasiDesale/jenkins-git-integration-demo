"""
test_calc_func.py contains pytest tests for math functions.
pytest discovers tests named "test_*".
Each function in this module is a test case.
"""

import pytest
from com.automationpanda.example.calc_func import *

NUMBER_1 = 3.0
NUMBER_2 = 2.0


def test_add():
    value = add(NUMBER_1, NUMBER_2)
    assert value == 5.0