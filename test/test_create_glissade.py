import pytest
from datetime import date
from car_factory import CarFactory
from car import Car
from batteries.spindler_battery import SpindlerBattery
from engines.willoughby_engine import WilloughbyEngine
from tires.carrigan_tire import CarriganTires


def test_create_glissade():
    current_date = date.today()
    last_service_date = date.today()
    current_mileage = 1000
    last_service_mileage = 500
    tire_wear = [0.1, 0.3, 0.2, 0.9]

    car = CarFactory.create_glissade(
        current_date, last_service_date, current_mileage, last_service_mileage, tire_wear)

    assert isinstance(car, Car)
    assert isinstance(car.engine, WilloughbyEngine)
    assert isinstance(car.battery, SpindlerBattery)
    assert isinstance(car.tire, CarriganTires)
