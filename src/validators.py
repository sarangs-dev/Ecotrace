"""Validation helper functions for CLI input boundary checks."""

from typing import Sequence


def validate_non_negative_float(value_str: str, field_name: str = "Input") -> float:
    """Validate and convert an input string to a non-negative float.

    Args:
        value_str: The user input string.
        field_name: The descriptive field name for error messages.

    Returns:
        float: Verified non-negative float value.

    Raises:
        ValueError: If value is empty, non-numeric, or negative.
    """
    if value_str is None:
        raise ValueError(f"{field_name} cannot be empty.")

    cleaned = str(value_str).strip()
    if not cleaned:
        raise ValueError(f"{field_name} cannot be empty.")

    try:
        val = float(cleaned)
    except ValueError as err:
        raise ValueError(f"{field_name} must be a valid number (e.g., 50 or 12.5).") from err

    if val < 0:
        raise ValueError(f"{field_name} cannot be negative. Please enter a number >= 0.")

    return val


def validate_menu_choice(value_str: str, valid_choices: Sequence[str]) -> str:
    """Validate that a menu choice is among valid options.

    Args:
        value_str: User input choice.
        valid_choices: Sequence of allowed choices (case-insensitive string checks).

    Returns:
        str: Cleaned matching valid choice.

    Raises:
        ValueError: If choice is invalid or empty.
    """
    if value_str is None:
        raise ValueError("Menu selection cannot be empty.")

    cleaned = str(value_str).strip()
    if not cleaned:
        raise ValueError("Menu selection cannot be empty.")

    # Match case-insensitively or exactly
    options_lower = [c.lower() for c in valid_choices]
    if cleaned.lower() in options_lower:
        idx = options_lower.index(cleaned.lower())
        return list(valid_choices)[idx]

    valid_fmt = ", ".join(map(str, valid_choices))
    raise ValueError(f"Invalid option '{cleaned}'. Please choose from: {valid_fmt}")
