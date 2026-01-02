"""Name validation utilities.

This module provides a small, well-documented `NameChecker` class
that validates and normalizes user-provided names according to the
project README rules (non-empty, letters only).
"""
from __future__ import annotations

from typing import Tuple
import re


class NameValidationError(ValueError):
    """Raised when a name does not meet validation rules."""


class NameChecker:
    """Validate and normalize a user's name.

    Validation rules (from README):
    - must be a non-empty string
    - may contain letters, spaces, hyphens and apostrophes
      (letters-only requirement interpreted as allowing common
      name punctuation but no digits or symbols)

    Use `validate` to obtain a normalized, title-cased name or
    raise `NameValidationError` on invalid input. Use `is_valid`
    when you prefer a boolean result.
    """

    # Pattern to split name parts (space, hyphen, apostrophe)
    _SEPARATORS = re.compile(r"[\s'-]+")

    @classmethod
    def validate(cls, name: str) -> str:
        """Validate and normalize a name.

        :param name: Raw user input
        :return: Normalized name (title-cased, single spaces)
        :raises NameValidationError: If the name is invalid
        :raises TypeError: If `name` is not a string
        """
        if not isinstance(name, str):
            raise TypeError("name must be a string")

        stripped = name.strip()
        if not stripped:
            raise NameValidationError("name must not be empty")

        # Ensure all characters are letters or accepted punctuation
        for ch in stripped:
            if ch.isalpha() or ch in (" ", "-", "'"):
                continue
            raise NameValidationError(f"invalid character in name: '{ch}'")

        # Collapse multiple whitespace into single spaces
        collapsed = re.sub(r"\s+", " ", stripped)

        # Title-case alphabetic runs while preserving hyphens and apostrophes
        def _title_preserve(token: str) -> str:
            return re.sub(r"[A-Za-zÀ-ÖØ-öø-ÿ]+", lambda m: m.group(0).title(), token)

        parts = [p for p in collapsed.split(" ") if p]
        if not parts:
            raise NameValidationError("name must contain letters")

        normalized = " ".join(_title_preserve(p) for p in parts)
        return normalized

    @classmethod
    def is_valid(cls, name: str) -> Tuple[bool, str]:
        """Check validity without raising.

        :param name: Raw user input
        :return: Tuple (is_valid, message). Message is empty on success.
        """
        try:
            cls.validate(name)
            return True, ""
        except Exception as exc:  # explicitly convert to message
            return False, str(exc)