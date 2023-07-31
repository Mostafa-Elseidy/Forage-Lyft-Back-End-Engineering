import pytest
from engines.willoughby_engine import WilloughbyEngine


def test_needs_service_true():
    current_mileage = 60001
    last_service_mileage = 0
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    assert engine.needs_service() == True


def test_needs_service_false():
    current_mileage = 60000
    last_service_mileage = 0
    engine = WilloughbyEngine(current_mileage, last_service_mileage)
    assert engine.needs_service() == False
