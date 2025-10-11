"""Core scientific calculator operations."""

from __future__ import annotations

import math
from typing import Union

Number = Union[int, float]


def square_root(value: Number) -> float:
    """Return the square root of a non-negative value."""
    if value < 0:
        raise ValueError("Square root is undefined for negative numbers.")
    return math.sqrt(value)


def factorial(value: Number) -> int:
    """Return the factorial of a non-negative integer value."""
    if isinstance(value, float) and not value.is_integer():
        raise ValueError("Factorial is only defined for whole numbers.")
    integer_value = int(value)
    if integer_value < 0:
        raise ValueError("Factorial is undefined for negative numbers.")
    return math.factorial(integer_value)


def natural_log(value: Number) -> float:
    """Return the natural logarithm (base e) of a positive value."""
    if value <= 0:
        raise ValueError("Natural log is only defined for positive numbers.")
    return math.log(value)


def power(base: Number, exponent: Number) -> float:
    """Return the value of base raised to the given exponent."""
    return math.pow(base, exponent)


__all__ = ["square_root", "factorial", "natural_log", "power"]
