import pytest
from engines.capulet_engine import CapuletEngine


def test_needs_service_true():
    current_mileage = 30001
    last_service_mileage = 0
    engine = CapuletEngine(current_mileage, last_service_mileage)
    assert engine.needs_service() == True


def test_needs_service_false():
    current_mileage = 30000
    last_service_mileage = 0
    engine = CapuletEngine(current_mileage, last_service_mileage)
    assert engine.needs_service() == False
