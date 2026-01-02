#!/usr/bin/env python3
"""Test entrypoint: run the project's test suite.

This script attempts to run `pytest`. If `pytest` is not
installed, it prints a short instruction to install it and exits
with a non-zero status.

Usage: `python3 tests/test.py`
"""
import sys
from pathlib import Path

# Ensure project root is on sys.path so `features` imports work when
# running this script directly (not needed when pytest is run via CLI).
project_root = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(project_root))


def main() -> int:
    try:
        import pytest
    except Exception:
        # Provide helpful guidance and fall back to unittest discovery
        print(
            "pytest is not installed. Falling back to unittest discovery (may not support pytest-only features).",
            file=sys.stderr,
        )
        print("To run the full test suite with pytest, install it:\n  python3 -m pip install --user pytest", file=sys.stderr)

        import unittest

        loader = unittest.TestLoader()
        suite = loader.discover("tests")
        runner = unittest.TextTestRunner(verbosity=2)
        result = runner.run(suite)
        return 0 if result.wasSuccessful() else 1

    # Run pytest quietly and return its exit code
    return pytest.main(["-q"]) 


if __name__ == "__main__":
    raise SystemExit(main())
