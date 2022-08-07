
import pytest
import re

from url_simple.exceptions import ValidationError
from url_simple.mixins import (
    ValueDependent,
    ValueStringDependent,
    ValueValidatable,
    ValueStringValidatable,
)


def test_value_dependent_init_with_int_value():
    assert ValueDependent(42).value == 42
def test_value_dependent_init_with_str_value():
    assert ValueDependent('foo').value == 'foo'

def test_value_dependent_init_with_none_value():
    assert ValueDependent(None).value is None

def test_string_value_dependent_init_with_str_value():
    assert ValueStringDependent('foo').value == 'foo'

def test_string_value_dependent_str():
    assert str(ValueStringDependent('foo')) == 'foo'

def test_string_value_dependent_eq_with_same_obj_value():
    value_string_dependent = ValueStringDependent('foo')
    assert value_string_dependent == value_string_dependent

def test_string_value_dependent_eq_with_same_str_value():
    assert ValueStringDependent('foo') == 'foo'

def test_string_value_dependent_ne_with_diff_str_value():
    assert ValueStringDependent('foo') != 'bar'

def test_value_validatable_validate_through_dummy():
    class Dummy(ValueValidatable):
        @classmethod
        def validate(cls):
            ValueValidatable.validate()
    dummy = Dummy(42)
    assert dummy.validate() is None

def test_value_string_validatable_validate_with_valid_value():
    class DummyValueStringValidatable(ValueStringValidatable):
        value_regex = re.compile('^foo$')

    DummyValueStringValidatable.validate('foo')

def test_value_string_validatable_validate_with_invalid_value():
    with pytest.raises(ValidationError):
        ValueStringValidatable.validate('foo')


