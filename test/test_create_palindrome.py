import pytest
from datetime import date
from car_factory import CarFactory
from car import Car
from batteries.spindler_battery import SpindlerBattery
from engines.sternman_engine import SternmanEngine
from tires.octoprime_tire import OctoprimeTires


def test_create_palindrome():
    current_date = date.today()
    last_service_date = date.today()
    warning_light_is_on = True
    tire_wear = [0.8, 0.8, 0.8, 0.7]

    car = CarFactory.create_palindrome(
        current_date, last_service_date, warning_light_is_on, tire_wear)

    assert isinstance(car, Car)
    assert isinstance(car.engine, SternmanEngine)
    assert isinstance(car.battery, SpindlerBattery)
    assert isinstance(car.tire, OctoprimeTires)
