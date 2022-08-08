
import re
import url_simple.exceptions as exceptions

from abc import ABC, abstractmethod
from typing import Generic, TypeVar, Type


T = TypeVar('T')


class ValueDependent(Generic[T]):

    def __init__(self, value: T):
        self.value: T = value


class StringDependent(ValueDependent[str]):
    regex: re.Pattern = re.compile(r'')

    def __init__(self, value: str):
        super().__init__(value=value)

    def __str__(self) -> str:
        return self.value

    def __eq__(self, other):
        return str(self) == str(other)


class ValueValidatable(ABC, ValueDependent):
    validation_error: Type[exceptions.ValidationError] = exceptions.ValidationError

    @classmethod
    @abstractmethod
    def validate(cls, *args, **kwargs):
        pass


class StringValidatable(ValueValidatable, StringDependent):
    validation_error = exceptions.ValidationError

    @classmethod
    def validate(cls, value: str) -> None:
        if cls._get_fullmatch(value) is None:
            raise cls.validation_error(f'Invalid value for {cls.__name__}: {value}')

    @classmethod
    def _get_fullmatch(cls, value: str) -> re.Match | None:
        return cls.regex.fullmatch(value)




