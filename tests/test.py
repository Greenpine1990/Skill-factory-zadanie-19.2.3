import pytest
from app.calculator import Calculator

class TestCalc:
    def setup_method(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 4) == 8

    def test_division_calculate_correctly(self):
        assert  self.calc.division(self, 6, 3) == 2

    def test_subtraction_calculate_correctly(self):
        assert  self.calc.subtraction(self, 5, 1) == 4

    def test_adding_calculate_correctly(self):
        assert  self.calc.adding(self, 4, 3) == 7

    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,8,0)