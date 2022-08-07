
import pytest

from url_simple.components import (
    URIComponent,
    Scheme,
    UserInfo,
    Hostname,
    IPV4,
    IPV6,
    Host,
    Port,
    Authority,
    Path,
    Query,
    Fragment,
)


def test_uri_component_init():
    uri_component = URIComponent(value='http://example.com')
    assert uri_component.value == 'http://example.com'

