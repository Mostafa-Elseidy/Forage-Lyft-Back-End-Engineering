import pytest
from datetime import date
from utils.add_years_to_date import add_years_to_date


def test_add_years_to_date():
    original_date = date(2020, 1, 1)
    years_to_add = 5

    result = add_years_to_date(original_date, years_to_add)

    assert result == date(2025, 1, 1)
