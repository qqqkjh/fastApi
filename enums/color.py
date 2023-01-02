from enum import Enum
from typing import Any


class Color(str, Enum):
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"
    NULL = None

    @classmethod
    def _missing_(cls, value: object) -> Any:
        if type(value) is str:
            value = value.lower()
            for member in cls:
                if member.value == value:
                    return member
        return cls.NULL



