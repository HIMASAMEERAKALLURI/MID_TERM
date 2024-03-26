import pytest
from app.plugins.calculator import Calculator


@pytest.fixture
def calculator():
    """Fixture to provide a Calculator instance."""
    return Calculator()


def test_addition(calculator: Calculator):
    """Tests addition operation."""
    result = calculator.calculate("32 + 3")
    assert result == 35, "Addition failed"


def test_subtraction(calculator: Calculator):
    """Tests subtraction operation."""
    result = calculator.calculate("9 - 3")
    assert result == 6, "Subtraction failed"


def test_multiplication(calculator: Calculator):
    """Tests multiplication operation."""
    result = calculator.calculate("5 * 5")
    assert result == 25, "Multiplication failed"


def test_division(calculator: Calculator):
    """Tests division operation."""
    result = calculator.calculate("4 / 2")
    assert result == 2, "Division failed"


def test_division_by_zero(calculator: Calculator):
    """Tests division by zero."""
    with pytest.raises(ZeroDivisionError):
        calculator.calculate("34 / 0")


def test_invalid_expression(calculator: Calculator):
    """Tests invalid expression format."""
    with pytest.raises(ValueError):
        calculator.calculate("invalid expression")


def test_missing_operands(calculator: Calculator):
    """Tests expressions with missing operands."""
    with pytest.raises(ValueError):
        calculator.calculate("+")
    with pytest.raises(ValueError):
        calculator.calculate("4 +")