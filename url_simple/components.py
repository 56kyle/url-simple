
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
    suffix: str = ':'
    value_regex: re.Pattern = re.compile(r'[a-zA-Z][a-zA-Z\d+.-]+')
    validation_regex: re.Pattern = re.compile(rf'^{value_regex.pattern}$')
    find_regex: re.Pattern = re.compile(rf'^(?P<scheme>{value_regex}):.+$')
    validation_error = InvalidSchemeError


class UserInfo(URIComponent):
    suffix: str = '@'
    username_regex: re.Pattern = re.compile(r'[a-zA-Z\d+.-]+')
    password_regex: re.Pattern = re.compile(r':[a-zA-Z\d+.-]*')
    value_regex: re.Pattern = re.compile(rf'{username_regex.pattern}(?:{password_regex.pattern})?')
    validation_regex: re.Pattern = re.compile(rf'^{value_regex.pattern}@$')
    find_regex: re.Pattern = re.compile(rf'^(?P<user_info>{value_regex.pattern})@.*$')
    validation_error = InvalidUserInfoError


class Host(URIComponent):
    label_regex: re.Pattern = re.compile(r'[a-zA-Z\d-]{1,63}')
    label_with_joining_dot_regex: re.Pattern = re.compile(rf'\.{label_regex.pattern}')
    hostname_regex: re.Pattern = re.compile(rf'{label_regex.pattern}(?:{label_with_joining_dot_regex.pattern}){{0,3}}')

    ipv4_regex: re.Pattern = re.compile(r'(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')

    hex_regex: re.Pattern = re.compile(r'[0-9a-fA-F]')
    ipv6_regex: re.Pattern = re.compile(rf'(?:\[{hex_regex.pattern}{{1,4}}(?::{hex_regex.pattern}{{1,4}}){7})\])')

    value_regex: re.Pattern = re.compile(rf'(?:(?:{hostname_regex.pattern})|(?:{ipv4_regex.pattern})|(?:{ipv6_regex.pattern}))')
    validation_regex: re.Pattern = re.compile(rf'^{value_regex.pattern}$')
    find_regex: re.Pattern = re.compile(rf'(?:.*@)?(?P<host>{value_regex.pattern})(?::\d+)?')
    validation_error = InvalidHostError


class Port(URIComponent):
    prefix = ':'
    value_regex: re.Pattern = re.compile(r'\d{1,5}')
    validation_regex: re.Pattern = re.compile(rf'{value_regex.pattern}$')
    find_regex: re.Pattern = re.compile(rf'.*{prefix}(?P<port>{value_regex.pattern})')
    validation_error = InvalidPortError


class Authority(URIComponent):
    value_regex: re.Pattern = re.compile(r'')
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

