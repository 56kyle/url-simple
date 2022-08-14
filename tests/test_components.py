
import pytest

from url_simple.components import (
    URIComponent,
    Scheme,
    UserInfo,
    Host,
    Port,
    Authority,
    Path,
    Query,
    Fragment,
)
from url_simple.exceptions import (
    ValidationError,
    InvalidURIError,
    InvalidURLError,
    InvalidURNError,
    InvalidSchemeError,
    InvalidAuthorityError,
    InvalidUserInfoError,
    InvalidHostError,
    InvalidPortError,
    InvalidPathError,
    InvalidQueryError,
    InvalidFragmentError,
)


def test_uri_component_init():
    uri_component = URIComponent('')
    assert uri_component.value == ''


def test_scheme_validate_with_valid_scheme():
    Scheme.validate('http')


def test_scheme_validate_with_invalid_scheme():
    with pytest.raises(InvalidSchemeError):
        Scheme.validate('%93333333')


def test_scheme_get_components_returns_none():
    assert Scheme._get_components('http') is None


def test_authority_validate_with_valid_authority():
    Authority.validate('user:password@host:port')


def test_authority_validate_with_invalid_authority():
    with pytest.raises(InvalidAuthorityError):
        Authority.validate('user:password@host:port:')


def test_authority_get_components_with_all_valid():
    components = Authority._get_components('user:password@host:port')
    assert components['user_info'].value == 'user:password'
    assert components['host'].value == 'host'
    assert components['port'].value == 'port'


