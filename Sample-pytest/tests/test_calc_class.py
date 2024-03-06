"""
test_calc_class.py contains pytest tests for the Calculator class.
pytest discovers tests named "test_*".
pytest can run test classes, but functions are a better way.
Each test function uses a fixture for setup.
Compare this example to test_calc.py in example-py-unittest.
"""

import pytest
from com.automationpanda.example.calc_class import Calculator

# "Constants"

NUMBER_1 = 3.0
NUMBER_2 = 2.0


# Fixtures

@pytest.fixture
def calculator():
    return Calculator()


# Helpers

def verify_answer(expected, answer, last_answer):
    assert expected == answer
    assert expected == last_answer


# Test Cases

def test_last_answer_init(calculator):
    assert calculator.last_answer == 0.0


def test_add(calculator):
    answer = calculator.add(NUMBER_1, NUMBER_2)
    verify_answer(5.0, answer, calculator.last_answer)