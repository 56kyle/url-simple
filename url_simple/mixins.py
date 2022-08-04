
import re
import url_simple.exceptions as exceptions

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type


T = TypeVar('T')


class ValueDependent(Generic[T]):

    def __init__(self, value: T):
        self.value: T = value


class ValueStringDependent(ValueDependent[str]):
    def __init__(self, value: str):
        super().__init__(value=value)

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other):
        return str(self) == str(other)


class ValueValidatable(ABC, ValueDependent):
    validation_error: Type[exceptions.ValidationError] = exceptions.ValidationError

    @abstractmethod
    def _validate(self, *args, **kwargs):
        pass


class ValueStringValidatable(ValueValidatable, ValueStringDependent):
    value_regex: re.Pattern = re.compile('')

    def _validate(self, match: re.Match = None) -> None:
        if match is None:
            raise self.validation_error()

    def _get_fullmatch(self) -> re.Match | None:
        return self.value_regex.fullmatch(self.value)

