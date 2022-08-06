
import re
from typing import Type


ALPHA: re.Pattern = re.compile(r'[a-zA-Z]')
BIT: re.Pattern = re.compile(r'[0-1]')
CHAR: re.Pattern = re.compile(r'[\u0000-\u007F]')
CR: re.Pattern = re.compile(r'\x0D')
CTL: re.Pattern = re.compile(r'[\x00-\x1F]|\x7F')
DIGIT: re.Pattern = re.compile(r'[0-9]')
DQUOTE: re.Pattern = re.compile(r'\x22')
HEXDIG: re.Pattern = re.compile(r'[0-9A-Fa-f]')
HTAB: re.Pattern = re.compile(r'\x09')
LF: re.Pattern = re.compile(r'\x0A')
CRLF: re.Pattern = re.compile(rf'{CR.pattern}{LF.pattern}')
OCTET: re.Pattern = re.compile(r'[\x00-\xFF]')
SP: re.Pattern = re.compile(r'\x20')
VCHAR: re.Pattern = re.compile(r'[\u0021-\u007E]')
WSP: re.Pattern = re.compile(rf'[{SP.pattern}{HTAB.pattern}]')
LWSP: re.Pattern = re.compile(rf'(?:(?:{CRLF.pattern})?{WSP.pattern})*')


hex_digit: re.Pattern = re.compile(r'[0-9a-fA-F]')
pct_encoded: re.Pattern = re.compile(rf'%{hex_digit.pattern}{{2}}')

gen_delims: re.Pattern = re.compile(r'[:/?#\[\]@]')
sub_delims: re.Pattern = re.compile(r'[!$&\'()*+,;=]')
reserved: re.Pattern = re.compile(rf'{gen_delims}|{sub_delims}')
unreserved: re.Pattern = re.compile(rf'[a-zA-Z0-9-._~]')

pchar: re.Pattern = re.compile(rf'{unreserved}|{pct_encoded}|{sub_delims}|[:@]')
reg_name: re.Pattern = re.compile(rf'({unreserved}|{pct_encoded}|{sub_delims})*')

ipv4_address: re.Pattern = re.compile(r'(?P<ipv4>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})')


if __name__ == '__main__':
    print('\u00A1')


