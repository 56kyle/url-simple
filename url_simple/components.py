
import re

from dataclasses import dataclass, field
from typing import Dict, List

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
    InvalidHostError,
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
        self.parse(self.value)

    @classmethod
    def parse(cls, value: str):
        cls.validate(value)
        cls._get_components(value)

    @classmethod
    def _get_components(cls, value: str) -> Dict[str, StringValidatable]:
        pass


class Scheme(URIComponent):
    suffix: str = ':'
    regex: re.Pattern = re.compile(r'(?P<scheme>[a-zA-Z][a-zA-Z\d+.-]+)')
    validation_error = InvalidSchemeError


class UserInfo(URIComponent):
    regex: re.Pattern = re.compile(rf'(?P<user_info>(?:{unreserved}|{pct_encoded}|{sub_delims}|:)*)')
    validation_error = InvalidUserInfoError


class Host(URIComponent):
    hostname = re.compile(rf'({unreserved}|{pct_encoded}|{sub_delims}){1,254}')
    ipv4 = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')#, re.DEBUG)
    ipv6 = re.compile(r'[0-9a-fA-F]{1,4}(?::[0-9a-fA-F]{1,4}){7}')
    regex: re.Pattern = re.compile(rf'(?P<host>{hostname}|{ipv4}|{ipv6})')
    validation_error = InvalidHostError


class Port(URIComponent):
    prefix: str = ':'
    regex: re.Pattern = re.compile(r'(?P<port>\d{1,5})')
    validation_error = InvalidPortError


class Authority(URIComponent):
    prefix: str = '//'
    regex = re.compile(rf'(?P<authority>(?:{UserInfo.regex.pattern}@)?{Host.regex.pattern}(?::{Port.regex.pattern})?)')
    validation_error = InvalidAuthorityError

    @classmethod
    def _get_components(cls, value: str) -> Dict[str, StringValidatable]:
        match = cls.regex.fullmatch(value)
        user_info: UserInfo | None = UserInfo(value=match.group('user_info')) if match.group('user_info') else None
        host: Host | None = Host(value=match.group('host')) if match.group('host') else None
        port: Port | None = Port(value=match.group('port')) if match.group('port') else None
        return {
            'user_info': user_info,
            'host': host,
            'port': port,
        }


class Path(URIComponent):
    regex: re.Pattern = re.compile(rf'[^?#]*')
    validation_error = InvalidPathError


class Query(URIComponent):
    regex: re.Pattern = re.compile(r'^(?P<query>.)')
    validation_error = InvalidQueryError


class Fragment(URIComponent):
    regex: re.Pattern = re.compile(r'^(?P<fragment>.)')
    validation_error = InvalidFragmentError


if __name__ == '__main__':
    print(Host.value_regex.pattern)
