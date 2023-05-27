from typing import Any, Dict


class Validator:
    def __init__(self, data: Dict[str, Any], device_template):
        self._data = data
        self._template = device_template

    def validate(self):
        for k, v in self._data.items():
            type_ = self._template.get(k, {}).get("type")
            if type_ == "int":
                v = int(v)
            value_type = type(v).__name__
            if type_ is None:
                raise ValueError(f"No validator for {k}")
            if value_type != type_:
                raise TypeError(
                    f"{k} is {value_type}, expected %s", k, value_type, type_
                )
            if (
                value_type == "str"
                and isinstance(self._template[k].get("enum"), list)
                and v not in self._template[k].get("enum")
            ):
                raise ValueError(
                    f"{k} has invalid value {v}; possible options {', '.join(self._template[k].get('enum'))}"
                )
            if (
                value_type == "int"
                and isinstance(self._template[k].get("min"), int)
                and int(v) < self._template[k].get("min")
            ):
                raise ValueError(
                    f"{k} has value lower than {self._template[k].get('min')}",
                )
            if (
                value_type == "int"
                and isinstance(self._template[k].get("max"), int)
                and int(v) > self._template[k].get("max")
            ):
                raise ValueError(
                    f"{k} has value lower than {self._template[k].get('max')}"
                )
        return True
