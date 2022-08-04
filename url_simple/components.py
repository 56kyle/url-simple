
import re

import url_simple.mixins as mixins

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, AnyStr


from exceptions import (
    ValidationError,
    InvalidSchemeError,
    InvalidAuthorityError,
    InvalidUserInfoError,
    InvalidHostError,
    InvalidPortError,
    InvalidPathError,
    InvalidQueryError,
    InvalidFragmentError,
)


class URIComponent(mixins.ValueStringValidatable, mixins.ValueStringFindable):
    prefix: str = ''
    suffix: str = ''
    value_regex: re.Pattern = None
    validation_regex: re.Pattern = None
    validation_error: ValidationError = ValidationError
    find_regex: re.Pattern = None


class Scheme(URIComponent):
    prefix: str = ':'
    value_regex: re.Pattern = re.compile(r'[a-zA-Z][a-zA-Z\d+.-]')
    validation_regex: re.Pattern = re.compile(rf'^{value_regex.pattern}*$')
    validation_error = InvalidSchemeError
    find_regex: re.Pattern = re.compile(rf'^(?P<scheme>{value_regex}*):.+$')

class UserInfo(URIComponent):
    validation_regex: re.Pattern = re.compile(r'^')
    validation_error = InvalidUserInfoError
    find_regex: re.Pattern = re.compile(r'^(?P<userinfo>.+?)@.+$')

class Host(URIComponent):
    allowed_characters_regex_portion: str = r'[a-zA-Z\d\-.]'
    validation_regex: re.Pattern = re.compile(rf'^{allowed_characters_regex_portion}{{1,253}}$')
    validation_error = InvalidHostError
    find_regex: re.Pattern = re.compile(rf'^(?:.+@)?(?P<host>{allowed_characters_regex_portion}{{1,253}})(?::.+)?$')

class Port(URIComponent):
    validation_regex: re.Pattern = re.compile(r'')
    validation_error = InvalidPortError
    find_regex: re.Pattern = re.compile(r'^.+:(?P<port>\d+)$')

class Authority(URIComponent):
    validation_regex: re.Pattern = re.compile(r'')
    validation_error = InvalidAuthorityError

    def __init__(self, value: str):
        super().__init__(value)
        self.user_info: UserInfo | None = UserInfo.find(value)
        self.host: Host | None = Host.find(value)
        self.port: Port | None = Port.find(value)


class Path(URIComponent):
    authority_regex_portion = r'(?://.*/)'
    validation_regex: re.Pattern = re.compile(r'')
    validation_error = InvalidPathError
    find_regex: re.Pattern = re.compile(rf'^.*:{authority_regex_portion}?(?P<path>.+)$')


class Query(URIComponent):
    validation_regex: re.Pattern = re.compile(r'')
    validation_error = InvalidQueryError

    _param_regex = re.compile(r'')


class Fragment(URIComponent):
    validation_regex: re.Pattern = re.compile(r'')
    validation_error = InvalidFragmentError

