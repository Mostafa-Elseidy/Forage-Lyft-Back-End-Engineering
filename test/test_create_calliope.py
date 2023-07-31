import pytest
from datetime import date
from car_factory import CarFactory
from car import Car
from batteries.spindler_battery import SpindlerBattery
from engines.capulet_engine import CapuletEngine


def test_create_calliope():
    current_date = date.today()
    last_service_date = date.today()
    current_mileage = 1000
    last_service_mileage = 500

    car = CarFactory.create_calliope(
        current_date, last_service_date, current_mileage, last_service_mileage)

    assert isinstance(car, Car)
    assert isinstance(car.engine, CapuletEngine)
    assert isinstance(car.battery, SpindlerBattery)
