import pytest

from features.name_checker import NameChecker, NameValidationError


def test_validate_simple_name():
    assert NameChecker.validate("Alex") == "Alex"


def test_validate_hyphen_and_apostrophe():
    assert NameChecker.validate(" jean-luc  ") == "Jean-Luc"
    assert NameChecker.validate("O'connor") == "O'Connor"


def test_validate_accented():
    assert NameChecker.validate("élodie") == "Élodie"


def test_invalid_empty_name():
    with pytest.raises(NameValidationError):
        NameChecker.validate("   ")


def test_invalid_characters():
    with pytest.raises(NameValidationError):
        NameChecker.validate("Bob123")
    with pytest.raises(NameValidationError):
        NameChecker.validate("Name!")


def test_type_error_on_non_string():
    with pytest.raises(TypeError):
        NameChecker.validate(123)


def test_is_valid_returns_tuple():
    ok, msg = NameChecker.is_valid("Marie")
    assert ok and msg == ""
    ok, msg = NameChecker.is_valid("123")
    assert not ok and msg
