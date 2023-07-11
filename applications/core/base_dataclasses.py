from typing import Any
from dataclasses import dataclass, asdict
from abc import ABC, abstractmethod


class DefaultSchema:
    def to_dict(self):
        return {k: v for k, v in asdict(self).items()}

    def choices(self):
        return [(v, k) for k, v in asdict(self).items()]

    def in_choices(self, value) -> bool:
        for item in self.choices():
            if value == item[0]:
                return True
        return False


@dataclass(frozen=True)
class DefaultChoiceInterfaceSchema:
    display: str
    value: Any


@dataclass(frozen=True)
class DefaultChoiceSchema(DefaultSchema):
    data: list[DefaultChoiceInterfaceSchema]

    def choices(self):
        return [(item["value"], item["display"]) for item in self.data]


class AbstractChoices(ABC):
    @classmethod
    @abstractmethod
    def get_data(cls) -> dict:
        pass

    @classmethod
    def choices(cls) -> list:
        data: dict = cls.get_data()
        default_choice = DefaultChoiceSchema(data=data)
        cls.default_choice = default_choice
        return default_choice.choices()

    @classmethod
    def in_choices(cls, value) -> bool:
        cls.choices()
        return cls.default_choice.in_choices(value)
