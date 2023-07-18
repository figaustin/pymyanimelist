from dacite import Config, from_dict
from enum import Enum
from typing import Type, TypeVar

T= TypeVar("T")

config = Config(
    cast=[Enum],
)


def as_dataclass(data_class: Type[T], data: dict) -> T:
    return from_dict(data_class, data, config=config)