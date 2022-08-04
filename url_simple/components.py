
import re

from dataclasses import dataclass, field
from typing import List, AnyStr

from url_simple.constants import (
    hex_digit,
    percent_encoded_char,
    gen_delims,
    sub_delims,
    reserved,
    unreserved,
)
from url_simple.exceptions import (
    ValidationError,
    InvalidSchemeError,
    InvalidAuthorityError,
    InvalidUserInfoError,
    InvalidUsernameError,
    InvalidPasswordError,
    InvalidHostError,
    InvalidHostnameError,
    InvalidIPV4Error,
    InvalidIPV6Error,
    InvalidPortError,
    InvalidPathError,
    InvalidQueryError,
    InvalidFragmentError,
)
from url_simple.mixins import (
    ValueStringValidatable,
)


class URIComponent(ValueStringValidatable):
    prefix: str = ''
    suffix: str = ''
    value_regex: re.Pattern = None
    validation_regex: re.Pattern = None
    validation_error: ValidationError = ValidationError

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parse()

    @classmethod
    def as_pattern(cls) -> str:
        return f'{cls.prefix}{cls.value_regex.pattern}{cls.suffix}'

    def parse(self):
        match: re.Match | None = self._get_fullmatch()
        self._get_components(match)
        self._validate(match)

    def _get_components(self, match: re.Match):
        pass


class Scheme(URIComponent):
    suffix: str = ':'
    value_regex: re.Pattern = re.compile(r'(?P<scheme>[a-zA-Z][a-zA-Z\d+.-]+)')
    validation_regex: re.Pattern = re.compile(rf'^{value_regex.pattern}$')
    validation_error = InvalidSchemeError

class Username(URIComponent):
    value_regex: re.Pattern = re.compile(r'[a-zA-Z\d+.-]+')
    validation_regex: re.Pattern = re.compile(rf'^{value_regex.pattern}$')
    validation_error = InvalidUsernameError

class Password(URIComponent):
    prefix: str = ':'
    value_regex: re.Pattern = re.compile(r'(?P<password>[a-zA-Z\d+.-]+)')
    validation_error = InvalidPasswordError

class UserInfo(URIComponent):
    suffix: str = '@'
    value_regex: re.Pattern = re.compile(rf'(?P<user_info>{Username.as_pattern()}{Password.as_pattern()}?)')
    validation_error = InvalidUserInfoError

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = None
        self.password = None

    def _get_components(self, match: re.Match):
        match = self.value_regex.fullmatch(self.value)
        self.username = Username(value=match.group('username'))
        self.password = Password(value=match.group('password'))


class Hostname(URIComponent):
    label_regex: re.Pattern = re.compile(r'[a-zA-Z\d-]{1,63}')
    label_with_joining_dot_regex: re.Pattern = re.compile(rf'\.{label_regex.pattern}')
    value_regex: re.Pattern = re.compile(
        rf'(?P<hostname>{label_regex.pattern}(?:{label_with_joining_dot_regex.pattern}){{0,3}})'
    )
    validation_error = InvalidHostnameError

class IPV4(URIComponent):
    value_regex: re.Pattern = re.compile(r'(?P<ipv4>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
    validation_error = InvalidIPV4Error

class IPV6(URIComponent):
    prefix = '['
    suffix = ']'
    value_regex: re.Pattern = re.compile(rf'(?P<ipv6>{hex_digit.pattern}{{1,4}}(?::{hex_digit.pattern}{{1,4}}){7})')
    validation_error = InvalidIPV6Error

class Host(URIComponent):
    value_regex: re.Pattern = re.compile(rf'(?P<host>{Hostname.as_pattern()}|{IPV4.as_pattern()}|{IPV6.as_pattern()}')
    validation_error = InvalidHostError

    def _get_components(self, match: re.Match):
        self.hostname: Hostname | None = Hostname(value=match.group('hostname'))
        self.ipv4: IPV4 | None = IPV4(value=match.group('ipv4'))
        self.ipv6: IPV6 | None = IPV6(value=match.group('ipv6'))

class Port(URIComponent):
    prefix = ':'
    value_regex: re.Pattern = re.compile(r'(?P<port>\d{1,5})')
    validation_error = InvalidPortError

class Authority(URIComponent):
    value_regex = re.compile(r'^//{}{}{}')
    validation_error = InvalidAuthorityError

    def __init__(self, value: str):
        super().__init__(value)

    def _get_components(self, match: re.Match):
        self.user_info: UserInfo | None = UserInfo(value=match.group('user_info'))
        self.host: Host | None = Host(value=match.group('host'))
        self.port: Port | None = Port(value=match.group('port'))


class Path(URIComponent):
    value_regex: re.Pattern = re.compile(r'^(?P<path>.)')
    validation_error = InvalidPathError


class Query(URIComponent):
    value_regex: re.Pattern = re.compile(r'^(?P<query>.)')
    validation_error = InvalidQueryError

class Fragment(URIComponent):
    value_regex: re.Pattern = re.compile(r'^(?P<fragment>.)')
    validation_error = InvalidFragmentError

