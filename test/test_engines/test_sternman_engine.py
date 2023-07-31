import pytest
from engines.sternman_engine import SternmanEngine


def test_needs_service_true():
    warning_light_is_on = True
    engine = SternmanEngine(warning_light_is_on)
    assert engine.needs_service() == True


def test_needs_service_false():
    warning_light_is_on = False
    engine = SternmanEngine(warning_light_is_on)
    assert engine.needs_service() == False
