
import re
import url_simple.exceptions as exceptions

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type


T = TypeVar('T')


class ValueDependent(Generic[T]):
    def __init__(self, value: Generic[T]):
        self.value: T = value


class ValueStringDependent(ValueDependent[str]):
    def __str__(self) -> str:
        return self.value

    def __eq__(self, other):
        return self.value == str(other)


class ValueValidatable(ABC, ValueDependent):
    validation_error: Type[exceptions.ValidationError]

    @abstractmethod
    def validate(self):
        pass


class ValueStringValidatable(ValueValidatable, ValueStringDependent):
    validation_regex: re.Pattern

    def validate(self):
        if not self.validation_regex.fullmatch(self.value):
            raise self.validation_error()


class ValueStringFindable(ABC, ValueStringDependent):
    find_regex: re.Pattern

    @classmethod
    def find(cls, value: str) -> ValueStringDependent | None:
        found_value = cls._find_value(value)
        return cls(found_value) if found_value else None

    @classmethod
    def _find_value(cls, search_string: str) -> str | None:
        return cls.find_regex.search(search_string)



