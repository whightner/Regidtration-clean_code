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


def get_valid_name() -> str:
	"""Prompt the user until a valid name is provided.

	Uses `NameChecker.validate` which returns a normalized name.
	"""
	while True:
		raw = prompt_loop("Enter your name: ")
		try:
			return NameChecker.validate(raw)
		except (NameValidationError, TypeError) as exc:
			print(f"Invalid name: {exc}")


def get_valid_dob() -> date:
	"""Prompt the user until a valid date of birth is provided.

	Returns a `datetime.date` object for the parsed DOB. The function
	enforces the age bounds defined in `AgeChecker`.
	"""
	while True:
		raw = prompt_loop("Enter your date of birth (YYYY-MM-DD or DD/MM/YYYY): ")
		try:
			dob = AgeChecker.parse_dob(raw)
			# compute age and check bounds explicitly to provide friendly messages
			age = AgeChecker.age_from_dob(dob)
			if age < AgeChecker.MIN_AGE or age > AgeChecker.MAX_AGE:
				raise AgeValidationError(f"age must be between {AgeChecker.MIN_AGE} and {AgeChecker.MAX_AGE} years; computed {age}")
			return dob
		except (AgeValidationError, TypeError) as exc:
			print(f"Invalid date of birth: {exc}")


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

	Return exit code 0 on success, non-zero on user cancellation.
	"""
	try:
		name = get_valid_name()
		dob = get_valid_dob()
	except SystemExit:
		return 1

	display_summary(name, dob)
	return 0


if __name__ == "__main__":
	raise SystemExit(main())
