


import pytest
import re

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
    VCHAR,
    WSP,
)


def test_alpha_with_lower_case_letter():
    assert ALPHA.fullmatch('a')

def test_alpha_with_upper_case_letter():
    assert ALPHA.fullmatch('A')

def test_alpha_with_digit():
    assert ALPHA.fullmatch('0') is None

def test_alpha_with_punctuation():
    assert ALPHA.fullmatch('.') is None

def test_alpha_with_space():
    assert ALPHA.fullmatch(' ') is None

def test_bit_with_0():
    assert BIT.fullmatch('0')

def test_bit_with_1():
    assert BIT.fullmatch('1')

def test_bit_with_2():
    assert BIT.fullmatch('2') is None

def test_bit_with_character():
    assert BIT.fullmatch('a') is None

def test_bit_with_space():
    assert BIT.fullmatch(' ') is None

def test_char_with_digit():
    assert CHAR.fullmatch('0')

def test_char_with_character():
    assert CHAR.fullmatch('a')

def test_char_with_space():
    assert CHAR.fullmatch(' ')

def test_char_with_punctuation():
    assert CHAR.fullmatch('.')

def test_char_with_control():
    assert CHAR.fullmatch('\x00')

def test_char_with_upside_down_question_mark():
    assert CHAR.fullmatch('\u00A1') is None

def test_cr_with_carriage_return():
    assert CR.fullmatch('\x0D')

def test_cr_with_non_carriage_return():
    assert CR.fullmatch('a') is None

def test_crlf_with_carriage_return_line_feed():
    assert CRLF.fullmatch('\x0D\x0A')

def test_crlf_with_non_carriage_return_line_feed():
    assert CRLF.fullmatch('a') is None

def test_ctl_with_control():
    assert CTL.fullmatch('\x00')

def test_ctl_with_non_control():
    assert CTL.fullmatch('a') is None

def test_digit_with_0():
    assert DIGIT.fullmatch('0')

def test_digit_with_character():
    assert DIGIT.fullmatch('a') is None

def test_digit_with_space():
    assert DIGIT.fullmatch(' ') is None

def test_dquote_with_double_quote():
    assert DQUOTE.fullmatch('\x22')

def test_dquote_with_non_double_quote():
    assert DQUOTE.fullmatch('a') is None

def test_hexdig_with_digit_min():
    assert HEXDIG.fullmatch('0')

def test_hexdig_with_digit_max():
    assert HEXDIG.fullmatch('9')

def test_hexdig_with_character_min():
    assert HEXDIG.fullmatch('a')

def test_hexdig_with_character_max():
    assert HEXDIG.fullmatch('f')

def test_hexdig_with_character_over_max():
    assert HEXDIG.fullmatch('g') is None

def test_htab_with_horizontal_tab():
    assert HTAB.fullmatch('\x09')

def test_htab_with_non_horizontal_tab():
    assert HTAB.fullmatch('a') is None

def test_lf_with_line_feed():
    assert LF.fullmatch('\x0A')

def test_lf_with_non_line_feed():
    assert LF.fullmatch('a') is None

def test_lwsp_with_space():
    assert LWSP.fullmatch(' ')

def test_lwsp_with_horizontal_tab():
    assert LWSP.fullmatch('\x09')

def test_lwsp_with_carriage_return_line_feed_and_space():
    assert LWSP.fullmatch('\x0D\x0A ')

def test_lwsp_with_non_carriage_return_line_feed_and_space():
    assert LWSP.fullmatch('a ') is None

def test_lwsp_with_carriage_return_line_feed():
    assert LWSP.fullmatch('\x0D\x0A') is None

def test_lwsp_with_carriage_return_line_feed_and_non_space():
    assert LWSP.fullmatch('\x0D\x0Aa') is None

def test_octet_with_value_min():
    assert OCTET.fullmatch('\x00')

def test_octet_with_value_max():
    assert OCTET.fullmatch('\xFF')

def test_octet_with_value_over_max():
    assert OCTET.fullmatch(str(0x100)) is None

def test_sp_with_space():
    assert SP.fullmatch(' ')

def test_sp_with_non_space():
    assert SP.fullmatch('a') is None

def test_vchar_with_value_min():
    assert VCHAR.fullmatch('\x21')

def test_vchar_with_value_under_min():
    assert VCHAR.fullmatch('\x20') is None

def test_vchar_with_value_max():
    assert VCHAR.fullmatch('\x7E')

def test_vchar_with_value_over_max():
    assert VCHAR.fullmatch('\x7F') is None

def test_wsp_with_space():
    assert WSP.fullmatch(' ')

def test_wsp_with_horizontal_tab():
    assert WSP.fullmatch('\x09')

def test_wsp_with_non_space():
    assert WSP.fullmatch('a') is None



