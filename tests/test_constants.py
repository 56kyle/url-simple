


import pytest

from url_simple.constants import (
    ALPHA,
    BIT,
    CHAR,
    CR,
    CRLF,
    CTL,
    DIGIT,
    DQUOTE,
    HEXDIG,
    HTAB,
    LF,
    LWSP,
    OCTET,
    SP,
)


def test_alpha_lower_case_letter():
    assert ALPHA.match('a')

def test_alpha_upper_case_letter():
    assert ALPHA.match('A')

def test_alpha_digit():
    assert ALPHA.match('0') is None

def test_alpha_punctuation():
    assert ALPHA.match('.') is None

def test_alpha_space():
    assert ALPHA.match(' ') is None

def test_bit_0():
    assert BIT.match('0')

def test_bit_1():
    assert BIT.match('1')

def test_bit_2():
    assert BIT.match('2') is None

def test_bit_character():
    assert BIT.match('a') is None

def test_bit_space():
    assert BIT.match(' ') is None

def test_char_digit():
    assert CHAR.match('0')

def test_char_character():
    assert CHAR.match('a')

def test_char_space():
    assert CHAR.match(' ')

def test_char_punctuation():
    assert CHAR.match('.')

def test_char_control():
    assert CHAR.match('\x00')

def test_char_upside_down_question_mark():
    assert CHAR.match('\u00A1') is None




