import pytest
from datetime import date
from batteries.spindler_battery import SpindlerBattery


def test_needs_service_true():
    current_date = date.fromisoformat("2020-05-15")
    last_service_date = date.fromisoformat("2018-01-25")
    battery = SpindlerBattery(current_date, last_service_date)
    assert battery.needs_service() == True


def test_needs_service_false():
    current_date = date.fromisoformat("2020-05-15")
    last_service_date = date.fromisoformat("2019-01-10")
    battery = SpindlerBattery(current_date, last_service_date)
    assert battery.needs_service() == False
