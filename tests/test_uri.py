
import pytest

from url_simple import URI


def test_uri_init():
    uri = URI('https://example.com')
    assert uri.value == 'https://example.com'

def test_uri_str():
    uri = URI('https://example.com')
    assert str(uri) == 'https://example.com'

def test_uri_repr():
    uri = URI('https://example.com')
    assert repr(uri) == 'URI(https://example.com)'


