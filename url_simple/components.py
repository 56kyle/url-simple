
import re

from dataclasses import dataclass, field
from typing import List, AnyStr

from url_simple.constants import (
    hex_digit,
    pct_encoded,
    gen_delims,
    sub_delims,
    reserved,
    unreserved,
    pchar,
    reg_name,
)
from url_simple.exceptions import (
    ValidationError,
    InvalidURIError,
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
    StringValidatable,
)


class URIComponent(StringValidatable):
    prefix: str = ''
    suffix: str = ''

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.parse()

    @classmethod
    def as_pattern(cls) -> str:
        return rf'{cls.prefix}{cls.value_regex.pattern}{cls.suffix}'

    def parse(self):
        match: re.Match = self._get_fullmatch(self.value)
        self._validate_against_match(self.value, match)
        self._get_components(match)

    def _get_components(self, match: re.Match):
        pass


class Scheme(URIComponent):
    suffix: str = ':'
    value_regex: re.Pattern = re.compile(r'(?P<scheme>[a-zA-Z][a-zA-Z\d+.-]+)')
    validation_error = InvalidSchemeError


class UserInfo(URIComponent):
    suffix: str = '@'
    value_regex: re.Pattern = re.compile(rf'(?P<user_info>(?:{unreserved}|{pct_encoded}|{sub_delims}|:)*)')
    validation_error = InvalidUserInfoError


class Host(URIComponent):
    hostname = re.compile(rf'({unreserved}|{pct_encoded}|{sub_delims}){1,254}')
    ipv4 = re.compile(r'(?:\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')#, re.DEBUG)
    ipv6 = re.compile(r'(?:[0-9a-fA-F]{1,4}(?::[0-9a-fA-F]{1,4}){7})')
    value_regex: re.Pattern = re.compile(rf'(?P<host>{hostname}|{ipv4}|{ipv6})')
    validation_error = InvalidHostError


class Port(URIComponent):
    prefix: str = ':'
    value_regex: re.Pattern = re.compile(r'(?P<port>\d{1,5})')
    validation_error = InvalidPortError


class Authority(URIComponent):
    prefix: str = '//'
    value_regex = re.compile(rf'(?P<authority>(?:{UserInfo.as_pattern()})?(?:{Host.as_pattern()})(?:{Port.as_pattern()})?)')
    validation_error = InvalidAuthorityError

    def _get_components(self, match: re.Match):
        self.user_info: UserInfo | None = UserInfo(value=match.group('user_info'))
        self.host: Host | None = Host(value=match.group('host'))
        self.port: Port | None = Port(value=match.group('port'))


class Path(URIComponent):
    value_regex: re.Pattern = re.compile(rf'[^?#]*')
    validation_error = InvalidPathError


class Query(URIComponent):
    value_regex: re.Pattern = re.compile(r'^(?P<query>.)')
    validation_error = InvalidQueryError


class Fragment(URIComponent):
    value_regex: re.Pattern = re.compile(r'^(?P<fragment>.)')
    validation_error = InvalidFragmentError


if __name__ == '__main__':
    print(Host.value_regex.pattern)
