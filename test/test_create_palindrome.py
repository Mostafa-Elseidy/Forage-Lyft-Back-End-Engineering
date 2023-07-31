import pytest
from datetime import date
from car_factory import CarFactory
from car import Car
from batteries.spindler_battery import SpindlerBattery
from engines.sternman_engine import SternmanEngine


def test_create_palindrome():
    current_date = date.today()
    last_service_date = date.today()
    warning_light_is_on = True

    car = CarFactory.create_palindrome(
        current_date, last_service_date, warning_light_is_on)

    assert isinstance(car, Car)
    assert isinstance(car.engine, SternmanEngine)
    assert isinstance(car.battery, SpindlerBattery)
