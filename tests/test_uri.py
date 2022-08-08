import pytest

from url_simple import URI


def test_uri_init_gets_components():
    uri = URI('http://user:pass@host:8080/path?query=value#fragment')
    uri._get_components(uri.value_regex.match(uri.value))
    assert uri.scheme == 'http'
    assert uri.authority == 'user:pass@host:8080'
    assert uri.path == '/path'
    assert uri.query == 'query=value'
    assert uri.fragment == 'fragment'

