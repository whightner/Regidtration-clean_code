#!/usr/bin/env python3
"""Test entrypoint: run the project's test suite.

This script attempts to run `pytest`. If `pytest` is not
installed, it prints a short instruction to install it and exits
with a non-zero status.

Usage: `python3 tests/test.py`
"""
import sys


def main() -> int:
    try:
        import pytest
    except Exception:
        print(
            "pytest is not installed. Install it with:\n  python3 -m pip install --user pytest",
            file=sys.stderr,
        )
        return 2

    # Run pytest quietly and return its exit code
    return pytest.main(["-q"])


if __name__ == "__main__":
    raise SystemExit(main())
