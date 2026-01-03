"""Console entry point for the Clean Code practice application.

This script prompts the user for their name and date of birth,
validates the inputs using `features.name_checker.NameChecker` and
`features.age_checker.AgeChecker`, computes the age, and prints a
clean, formatted summary.

The script performs robust error handling and keeps user prompts
simple for clarity and testing.
"""
from __future__ import annotations

from datetime import date
import sys

from features.name_checker import NameChecker, NameValidationError
from features.age_checker import AgeChecker, AgeValidationError


def prompt_loop(prompt: str) -> str:
    """Prompt repeatedly until receiving a non-empty response.

    Returns the raw input string (not validated).
    """
    while True:
        try:
            value = input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            print("\nInput cancelled. Exiting.")
            raise SystemExit(1)

        if value:
            return value
        print("Input must not be empty. Please try again.")


def prompt_continue_or_quit() -> bool:
    """Ask user whether to continue. Return True to continue, False to quit."""
    while True:
        try:
            choice = input("Press Enter to continue or type 'q' to quit: ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nInput cancelled. Exiting.")
            raise SystemExit(1)

        if choice == "" or choice in ("y", "yes"):
            return True
        if choice in ("q", "quit", "n", "no"):
            return False
        print("Please press Enter to continue or type 'q' to quit.")


def get_valid_name(max_attempts: int = 3) -> str:
    """Prompt the user until a valid name is provided or attempts exhausted.

    Uses `NameChecker.validate` which returns a normalized name.
    Exits the program with code 1 if attempts are exhausted.
    """
    for attempt in range(1, max_attempts + 1):
        raw = prompt_loop("Enter your name: ")
        try:
            return NameChecker.validate(raw)
        except (NameValidationError, TypeError) as exc:
            remaining = max_attempts - attempt
            if remaining:
                print(f"Invalid name: {exc} ({remaining} attempt{'s' if remaining>1 else ''} left)")
            else:
                print(f"Invalid name: {exc} (no attempts left). Exiting.")
                raise SystemExit(1)


def get_valid_dob(max_attempts: int = 3) -> date:
    """Prompt the user until a valid date of birth is provided or attempts exhausted.

    Returns a `datetime.date` object for the parsed DOB. The function
    enforces the age bounds defined in `AgeChecker`.
    Exits the program with code 1 if attempts are exhausted.
    """
    for attempt in range(1, max_attempts + 1):
        raw = prompt_loop("Enter your date of birth (YYYY-MM-DD or DD/MM/YYYY): ")
        try:
            dob = AgeChecker.parse_dob(raw)
            age = AgeChecker.age_from_dob(dob)
            if age < AgeChecker.MIN_AGE or age > AgeChecker.MAX_AGE:
                raise AgeValidationError(f"age must be between {AgeChecker.MIN_AGE} and {AgeChecker.MAX_AGE} years; computed {age}")
            return dob
        except (AgeValidationError, TypeError) as exc:
            remaining = max_attempts - attempt
            if remaining:
                print(f"Invalid date of birth: {exc} ({remaining} attempt{'s' if remaining>1 else ''} left)")
            else:
                print(f"Invalid date of birth: {exc} (no attempts left). Exiting.")
                raise SystemExit(1)


def display_summary(name: str, dob: date) -> None:
    """Print a concise summary with name, age and birth year."""
    age = AgeChecker.age_from_dob(dob)
    birth_year = AgeChecker.birth_year_from_dob(dob)
    print()
    print(f"Name: {name}")
    print(f"Age: {age} years")
    print(f"Birth year: {birth_year}")


def main() -> int:
    """Run the interactive prompt sequence and display results.

    Return exit code 0 on success, non-zero on user cancellation or failure.
    """
    try:
        while True:
            name = get_valid_name()
            dob = get_valid_dob()
            display_summary(name, dob)

            if prompt_continue_or_quit():
                # continue the outer loop to ask again
                continue
            return 0
    except SystemExit:
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
