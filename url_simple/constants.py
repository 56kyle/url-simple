
import re
from typing import Type

class Bases:
    b: Type[bin] = bin
    d: Type[float] = float
    x: Type[hex] = hex


ALPHA: re.Pattern = re.compile(r'[a-zA-Z]')
BIT: re.Pattern = re.compile(r'')
CHAR: re.Pattern = re.compile(r'[\u0000-\u007F]')
CR: re.Pattern = re.compile(r'\x0D')
CRLF: re.Pattern = re.compile(r'\x0D\x0A')
CTL: re.Pattern = re.compile(r'')
DIGIT: re.Pattern = re.compile(r'')
DQUOTE: re.Pattern = re.compile(r'')
HEXDIG: re.Pattern = re.compile(r'')
HTAB: re.Pattern = re.compile(r'')
LF: re.Pattern = re.compile(r'\x0A')
LWSP: re.Pattern = re.compile(r'')
OCTET: re.Pattern = re.compile(r'[\x00-\xFF]')
SP: re.Pattern = re.compile(r'\x20')


CR = '0x0D' # carriage return

CRLF = 'R LF' # Internet standard newline

CTL = '0x00-1F / 0x7F' # controls

DIGIT = '0x30-39' # 0-9

DQUOTE = '0x22' # " (Double Quote)

HEXDIG = 'IGIT / "A" / "B" / "C" / "D" / "E" / "F"'

HTAB = '0x09' # horizontal tab

LF = '0x0A' # linefeed

LWSP = '*(WSP / CRLF WSP)' # linear white space (past newline)

OCTET = '0x00-FF' # 8 bits of data
SP = '0x20'

hex_digit: re.Pattern = re.compile(r'[0-9a-fA-F]')
percent_encoded_char: re.Pattern = re.compile(rf'%{hex_digit.pattern}{{2}}')

ipv4: re.Pattern = re.compile(r'(?P<ipv4>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')
ipv6: re.Pattern = re.compile(rf'(?P<ipv6>\[{hex_digit.pattern}{{1,4}}(?::{hex_digit.pattern}{{1,4}}){7}])')

gen_delims: re.Pattern = re.compile(r'[:/?#\[\]@]')
sub_delims: re.Pattern = re.compile(r'[!$&\'()*+,;=]')
reserved: re.Pattern = re.compile(rf'{gen_delims.pattern}|{sub_delims.pattern}')
unreserved: re.Pattern = re.compile(rf'[a-zA-Z0-9\-._~]')

pchar: re.Pattern = re.compile(rf'{unreserved.pattern}')


if __name__ == '__main__':
    print('\u00A1')


