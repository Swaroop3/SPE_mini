"""Unit tests for the scientific calculator operations."""

from __future__ import annotations

import math

import pytest

from spe_calculator import calculator


def test_square_root_returns_expected_value() -> None:
    assert calculator.square_root(25) == 5


def test_square_root_rejects_negative_input() -> None:
    with pytest.raises(ValueError):
        calculator.square_root(-1)


def test_factorial_accepts_integer_like_float() -> None:
    assert calculator.factorial(5.0) == math.factorial(5)


def test_factorial_rejects_negative_values() -> None:
    with pytest.raises(ValueError):
        calculator.factorial(-3)


def test_factorial_rejects_non_integer() -> None:
    with pytest.raises(ValueError):
        calculator.factorial(3.5)


def test_natural_log_returns_expected_value() -> None:
    assert calculator.natural_log(math.e) == pytest.approx(1.0)


def test_natural_log_rejects_non_positive_values() -> None:
    for value in (0, -1):
        with pytest.raises(ValueError):
            calculator.natural_log(value)


def test_power_operation() -> None:
    assert calculator.power(2, 3) == 8
