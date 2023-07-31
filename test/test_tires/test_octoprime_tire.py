import pytest
from tires.octoprime_tire import OctoprimeTires


def test_needs_service_true():
    tire_wear = [0.8, 0.8, 0.8, 0.7]
    tires = OctoprimeTires(tire_wear)
    assert tires.needs_service() == True


def test_needs_service_false():
    tire_wear = [0.1, 0.2, 0.4, 0.2]
    tires = OctoprimeTires(tire_wear)
    assert tires.needs_service() == False
