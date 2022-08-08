
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


def test_uri_component_init():
    uri_component = URIComponent('')
    assert uri_component.value == ''


def test_scheme_init():
    scheme = Scheme('http')
    assert scheme.value == 'http'

