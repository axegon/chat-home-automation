import logging

import requests
import yaml

from chat_home_automation.validator import Validator

logger = logging.getLogger(__name__)


class Commands:
    _validator = Validator
    _valid_methods = ["get", "post", "put", "patch", "delete"]
    _valid_payloads = ["params", "data", "json"]

    def __init__(self, validator=None):
        if validator is not None:
            self._validator = Validator

    @property
    def _commands(self):
        return yaml.load(
            open("/etc/chat-home-automation.yaml").read(), Loader=yaml.Loader
        )

    def execute_command(self, command):
        logger.debug(command)
        command = list(map(lambda l: l.strip(), command.split()))
        commands = self._commands
        if command[0] not in self._commands["commands"]:
            available_commands = ", ".join(list(commands["commands"].keys()))
            return f"{command[0]} not in available commands. Available commands: {available_commands}"
        if len(command) == 2 and command[1] == "help":
            return True, self.generate_help_command(command[0])
        request = command[1:]
        command_request = {
            request[i]: request[i + 1] for i in range(0, len(request), 2)
        }
        logger.debug(command_request)
        new_validator = self._validator(
            command_request, commands["commands"][command[0]]
        )
        try:
            new_validator.validate()
        except Exception as e:
            return False, str(e)
        return self.eval_command(command[0], command_request)

    def eval_command(self, target, command_request):
        cmd_template = self._commands["commands"][target]
        meta = cmd_template.get("meta", {})
        if meta.get("type") == "rest":
            if meta.get("server") is None:
                return False, "No server set in meta.server"
            if meta.get("method") not in self._valid_methods:
                return False, f"Unsupported method {meta.get('method')}"
            if meta.get("payload") not in self._valid_payloads:
                return False, f"Unsupported method {meta.get('method')}"
            kwargs = {
                meta["payload"]: command_request,
                "timeout": meta.get("timeout", 6),
            }
            try:
                resp = getattr(requests, meta["method"])(meta["server"], **kwargs)
                if resp.status_code == 200:
                    success = True
                if meta.get("on_success") is not None and resp.text != meta.get(
                    "on_success"
                ):
                    success = False
                return success, resp.text
            except Exception as e:
                return False, str(e)

    def generate_help_command(self, device_template_name):
        help_message = "Here are the possible options:\n"

        for key, value in self._commands["commands"][device_template_name].items():
            if key == "meta":
                continue
            help_message += f"'{key}':\n"

            if value["type"] == "str" and "enum" in value:
                options = ", ".join(value["enum"])
                help_message += f"\t: string. Possible values are {options}.\n"
            elif value["type"] == "int" and "min" in value or "max" in value:
                min_val = value["min"]
                max_val = value["max"]
                help_message += (
                    f"\t: integer. Possible values range from {min_val} to {max_val}.\n"
                )
            else:
                help_message += f"\t- Should be of type {value['type']}.\n"

        return help_message
