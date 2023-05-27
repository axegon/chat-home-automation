from unittest.mock import patch

from chat_home_automation.commands import Commands
from chat_home_automation.validator import Validator


def test_init():
    commands = Commands(Validator)
    assert commands._validator is Validator


@patch("chat_home_automation.commands.yaml.load")
def test_execute_command_invalid_command(yaml_load_mock, mocker):
    yaml_load_mock.return_value = {"commands": {}}
    commands = Commands(Validator)
    result = commands.execute_command("invalid_command")
    assert result == "invalid_command not in available commands. Available commands: "


@patch("chat_home_automation.commands.yaml.load")
def test_generate_help_command(yaml_load_mock, mocker):
    yaml_load_mock.return_value = {
        "commands": {
            "device": {
                "param1": {"type": "str", "enum": ["a", "b"]},
                "param2": {"type": "int", "min": 1, "max": 10},
            }
        }
    }
    commands = Commands(Validator)
    result = commands.generate_help_command("device")
    assert (
        result
        == "Here are the possible options:\n'param1':\n\t: string. Possible values are a, b.\n'param2':\n\t: integer. Possible values range from 1 to 10.\n"
    )
