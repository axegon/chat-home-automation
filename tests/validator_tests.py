import pytest

from chat_home_automation.validator import Validator


def setup():
    data = {"state": "on", "temp": 20, "mode": "cool", "fanspeed": 3}
    device_template = {
        "state": {"type": "str", "enum": ["on", "off"]},
        "temp": {"type": "int", "min": 17, "max": 30},
        "mode": {"type": "str", "enum": ["cool", "dry", "heat", "auto"]},
        "fanspeed": {"type": "int", "min": 1, "max": 3},
    }
    return data, device_template


def test_validate():
    data, device_template = setup()
    validator = Validator(data, device_template)
    assert validator.validate() is True


def test_invalid_data():
    data, device_template = setup()
    invalid_data = {"state": "on", "temp": 20, "mode": "cooler", "fanspeed": "max"}
    validator = Validator(invalid_data, device_template)
    with pytest.raises(ValueError):
        validator.validate()


def test_invalid_type():
    data, device_template = setup()
    invalid_data = {"state": "on", "temp": "hot", "mode": "cool", "fanspeed": "high"}
    validator = Validator(invalid_data, device_template)
    with pytest.raises(ValueError):
        validator.validate()


def test_out_of_range():
    data, device_template = setup()
    invalid_data = {"state": "on", "temp": 40, "mode": "cool", "fanspeed": "high"}
    validator = Validator(invalid_data, device_template)
    with pytest.raises(ValueError):
        validator.validate()
