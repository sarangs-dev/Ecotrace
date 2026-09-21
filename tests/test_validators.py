"""Unit tests for src/validators.py."""

import pytest
from src.validators import validate_menu_choice, validate_non_negative_float


def test_validate_non_negative_float_valid():
    assert validate_non_negative_float("100") == 100.0
    assert validate_non_negative_float("0.5") == 0.5
    assert validate_non_negative_float("0") == 0.0
    assert validate_non_negative_float("  42.7  ") == 42.7


def test_validate_non_negative_float_invalid():
    with pytest.raises(ValueError, match="cannot be empty"):
        validate_non_negative_float("")

    with pytest.raises(ValueError, match="cannot be empty"):
        validate_non_negative_float("   ")

    with pytest.raises(ValueError, match="must be a valid number"):
        validate_non_negative_float("abc")

    with pytest.raises(ValueError, match="cannot be negative"):
        validate_non_negative_float("-15")


def test_validate_menu_choice_valid():
    choices = ["1", "2", "3", "4"]
    assert validate_menu_choice("1", choices) == "1"
    assert validate_menu_choice(" 3 ", choices) == "3"

    diet_choices = ["meat_heavy", "balanced", "vegetarian", "vegan"]
    assert validate_menu_choice("VEGAN", diet_choices) == "vegan"


def test_validate_menu_choice_invalid():
    choices = ["1", "2", "3", "4"]
    with pytest.raises(ValueError, match="cannot be empty"):
        validate_menu_choice("", choices)

    with pytest.raises(ValueError, match="Invalid option"):
        validate_menu_choice("5", choices)
