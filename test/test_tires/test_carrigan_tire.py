import pytest
from tires.carrigan_tire import CarriganTires


def test_needs_service_true():
    tire_wear = [0.1, 0.3, 0.2, 0.9]
    tires = CarriganTires(tire_wear)
    assert tires.needs_service() == True


def test_needs_service_false():
    tire_wear = [0.1, 0.2, 0.4, 0.2]
    tires = CarriganTires(tire_wear)
    assert tires.needs_service() == False
