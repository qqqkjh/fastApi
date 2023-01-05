from enum import Enum, unique
from typing import Any


class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __str__(self):
        return self.name


@unique
class Color(StrEnum):
    """
    FastApi 에서 Enum 을 사용 할 경우 URL파라매터 기준 Enum 의  value 기준 으로 Checking
    """
    RED = "red"
    YELLOW = "yellow"
    GREEN = "green"
    NULL = None

    @classmethod
    def _missing_(cls, value: object) -> Any:
        """
        기준에 맞지 않는 value 값이 들어 왔을 경우 lower 시켜서 한번더 비교
        """
        if type(value) is str:
            for member in cls:
                if member.value == value.lower():
                    return member
        return None
