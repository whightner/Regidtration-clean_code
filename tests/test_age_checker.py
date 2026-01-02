import pytest
from datetime import date

from features.age_checker import AgeChecker, AgeValidationError


def test_parse_supported_formats():
    assert AgeChecker.parse_dob("2000-05-20") == date(2000, 5, 20)
    assert AgeChecker.parse_dob("20/05/2000") == date(2000, 5, 20)
    assert AgeChecker.parse_dob("20-05-2000") == date(2000, 5, 20)


def test_parse_invalid_and_type():
    with pytest.raises(AgeValidationError):
        AgeChecker.parse_dob("")
    with pytest.raises(AgeValidationError):
        AgeChecker.parse_dob("not-a-date")
    with pytest.raises(TypeError):
        AgeChecker.parse_dob(123)


def test_age_from_dob_on_date():
    dob = date(2006, 1, 2)
    # before birthday in the reference year
    assert AgeChecker.age_from_dob(dob, on_date=date(2026, 1, 1)) == 19
    # on birthday
    assert AgeChecker.age_from_dob(dob, on_date=date(2026, 1, 2)) == 20


def test_validate_dob_bounds(monkeypatch):
    # Make validation deterministic by fixing the reference date
    fixed_today = date(2026, 1, 2)
    original_age_from = AgeChecker.age_from_dob

    monkeypatch.setattr(
        AgeChecker,
        "age_from_dob",
        lambda dob, on_date=None: original_age_from(dob, fixed_today),
    )

    # exactly 16 years old on fixed_today
    assert AgeChecker.validate_dob("2010-01-02") == 16

    # too young
    with pytest.raises(AgeValidationError):
        AgeChecker.validate_dob("2012-01-01")

    # too old
    with pytest.raises(AgeValidationError):
        AgeChecker.validate_dob("1940-01-01")


def test_is_valid_returns_tuple(monkeypatch):
    fixed_today = date(2026, 1, 2)
    original_age_from = AgeChecker.age_from_dob
    monkeypatch.setattr(
        AgeChecker,
        "age_from_dob",
        lambda dob, on_date=None: original_age_from(dob, fixed_today),
    )

    ok, msg = AgeChecker.is_valid("2010-01-02")
    assert ok and msg == ""
    ok, msg = AgeChecker.is_valid("not-a-date")
    assert not ok and msg


def test_birth_year_from_dob():
    dob = date(1990, 6, 15)
    assert AgeChecker.birth_year_from_dob(dob) == 1990
