"""Age validation and utility functions.

Provides `AgeChecker` that validates user-provided ages according
to project README rules (integer between 0 and 70 inclusive) and
can compute an estimated birth year given the current year.
"""
from __future__ import annotations

from typing import Tuple
import datetime


class AgeValidationError(ValueError):
    """Raised when an age does not meet validation rules."""


class AgeChecker:
    """Validate ages and compute birth years.

    Usage:
        AgeChecker.validate("25") -> 25
        AgeChecker.birth_year(25) -> 2000  # if current year is 2025
    """

    MIN_AGE = 16
    MAX_AGE = 70

    @classmethod
    def validate(cls, age_value) -> int:
        """Validate and convert an age input to an integer.

        Accepts strings or numbers. Raises `AgeValidationError` for
        invalid values and `TypeError` when the input type is
        unsupported.

        :param age_value: value to validate
        :return: integer age between MIN_AGE and MAX_AGE inclusive
        """
        if isinstance(age_value, bool):
            # bool is subclass of int, but not valid age input
            raise TypeError("age must be an integer between 0 and 70")

        # Convert from string if necessary
        if isinstance(age_value, str):
            age_value = age_value.strip()
            if not age_value:
                raise AgeValidationError("age must not be empty")
            if not age_value.lstrip("+-").isdigit():
                raise AgeValidationError("age must be an integer")
            try:
                age = int(age_value)
            except ValueError:
                raise AgeValidationError("age must be an integer")
        elif isinstance(age_value, int):
            age = age_value
        else:
            # allow numeric types convertible to int (e.g., float with .0)
            if isinstance(age_value, float) and age_value.is_integer():
                age = int(age_value)
            else:
                raise TypeError("age must be an integer or string representing an integer")

        if age < cls.MIN_AGE or age > cls.MAX_AGE:
            raise AgeValidationError(f"age must be between {cls.MIN_AGE} and {cls.MAX_AGE} inclusive")

        return age

    @classmethod
    def is_valid(cls, age_value) -> Tuple[bool, str]:
        """Return (True, '') if valid, else (False, message)."""
        try:
            cls.validate(age_value)
            return True, ""
        except Exception as exc:
            return False, str(exc)

    @staticmethod
    def birth_year(age: int, current_year: int | None = None) -> int:
        """Compute an estimated birth year from age.

        :param age: validated integer age
        :param current_year: if None, uses the current calendar year
        :return: estimated birth year
        """
        if current_year is None:
            current_year = datetime.date.today().year
        return current_year - age
