"""Age validation and utilities based on date of birth.

The application requests a date of birth (DOB) from the user and
derives the age. Validation enforces a minimum age of 16 and a
maximum age of 70 (inclusive). This module provides parsing,
age calculation and clear error types.
"""
from __future__ import annotations

from typing import Tuple
import datetime


class AgeValidationError(ValueError):
    """Raised when a date of birth does not meet validation rules."""


class AgeChecker:
    """Validate date of birth and compute age and birth year.

    Public methods:
    - `parse_dob(value)` -> datetime.date: parse and validate input format
    - `age_from_dob(dob)` -> int: compute age in years
    - `validate_dob(value)` -> int: parse and return age, raising on invalid
    - `is_valid(value)` -> (bool, message)
    """

    MIN_AGE = 16
    MAX_AGE = 70

    _FORMATS = (
        "%Y-%m-%d",  # 2020-01-31 (ISO)
        "%d/%m/%Y",  # 31/01/2020
        "%d-%m-%Y",  # 31-01-2020
    )

    @classmethod
    def parse_dob(cls, value) -> datetime.date:
        """Parse a date-of-birth value into a `datetime.date`.

        Accepts a `datetime.date` or a string in one of the supported
        formats. Raises `AgeValidationError` or `TypeError` on bad input.
        """
        if isinstance(value, datetime.date) and not isinstance(value, datetime.datetime):
            return value

        if not isinstance(value, str):
            raise TypeError("date of birth must be a string or date")

        text = value.strip()
        if not text:
            raise AgeValidationError("date of birth must not be empty")

        for fmt in cls._FORMATS:
            try:
                return datetime.datetime.strptime(text, fmt).date()
            except ValueError:
                continue

        raise AgeValidationError("date of birth must be in YYYY-MM-DD or DD/MM/YYYY format")

    @staticmethod
    def age_from_dob(dob: datetime.date, on_date: datetime.date | None = None) -> int:
        """Compute the age in years given a birth date.

        Accounts for whether the birthday has occurred yet in the
        reference year.
        """
        if on_date is None:
            on_date = datetime.date.today()
        years = on_date.year - dob.year
        if (on_date.month, on_date.day) < (dob.month, dob.day):
            years -= 1
        return years

    @classmethod
    def validate_dob(cls, value) -> int:
        """Parse `value` as DOB and return computed age.

        Raises `AgeValidationError` when the resulting age is outside
        allowed bounds.
        """
        dob = cls.parse_dob(value)
        age = cls.age_from_dob(dob)
        if age < cls.MIN_AGE or age > cls.MAX_AGE:
            raise AgeValidationError(f"age must be between {cls.MIN_AGE} and {cls.MAX_AGE} years")
        return age

    @classmethod
    def is_valid(cls, value) -> Tuple[bool, str]:
        """Return (True, '') if DOB is valid and age within bounds.

        Otherwise returns (False, message).
        """
        try:
            cls.validate_dob(value)
            return True, ""
        except Exception as exc:
            return False, str(exc)

    @staticmethod
    def birth_year_from_dob(dob: datetime.date) -> int:
        """Return the birth year extracted from the date of birth."""
        return dob.year
