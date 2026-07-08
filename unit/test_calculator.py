import pytest

from utils.calculator import Calculator


@pytest.mark.unit
class TestCalculator:

    def test_addition(self):

        calculator = Calculator()

        result = calculator.add(2, 3)

        assert result == 5


    def test_subtraction(self):

        calculator = Calculator()

        result = calculator.subtract(5, 3)

        assert result == 2