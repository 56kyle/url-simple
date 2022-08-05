
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
CRLF: re.Pattern = re.compile(rf'{CR}{LF}')
OCTET: re.Pattern = re.compile(r'[\x00-\xFF]')
SP: re.Pattern = re.compile(r'\x20')
VCHAR: re.Pattern = re.compile(r'[\u0021-\u007E]')
WSP: re.Pattern = re.compile(rf'{SP}|{HTAB}')
LWSP: re.Pattern = re.compile(rf'(?:{CRLF}?{WSP})*')


''''''
    URI           = re.compile(rf'{scheme}:{hier-part}(?:?{query})?(?:#{fragment})?')

    hier-part     = re.compile(rf'//{authority}(?:path-abempty | path-absolute | path-rootless | path-empty)')

    URI-reference = re.compile(rf'{URI}|{relative-ref}')

    absolute-URI  = re.compile(rf'{scheme}:{hier-part}(?:?{query})?')

    relative-ref  = re.compile(rf'{relative-part}(?:?{query})?(?:#{fragment})?')

    relative-part = re.compile(rf'//{authority}(?:{path-abempty}|{path-absolute}|{path-noscheme}|{path-empty})')

    scheme        = re.compile(rf'{ALPHA}(?:{ALPHA}|{DIGIT}|[+-.])*')

    authority     = re.compile(rf'(?:{userinfo}@)?{host}(?::{port})?')
    userinfo      = re.compile(rf'(?:{unreserved}|{pct-encoded}|{sub-delims}|:)*')
    host          = re.compile(rf'{IP-literal}|{IPv4address}|{reg-name}')
    port          = re.compile(rf'{DIGIT}*')

    IP-literal    = "[" ( IPv6address / IPvFuture  ) "]"

    IPvFuture     = "v" 1*HEXDIG "." 1*( unreserved / sub-delims / ":" )

    IPv6address   =                            6( h16 ":" ) ls32
                 /                       "::" 5( h16 ":" ) ls32
                 / [               h16 ] "::" 4( h16 ":" ) ls32
                 / [ *1( h16 ":" ) h16 ] "::" 3( h16 ":" ) ls32
                 / [ *2( h16 ":" ) h16 ] "::" 2( h16 ":" ) ls32
                 / [ *3( h16 ":" ) h16 ] "::"    h16 ":"   ls32
                 / [ *4( h16 ":" ) h16 ] "::"              ls32
                 / [ *5( h16 ":" ) h16 ] "::"              h16
                 / [ *6( h16 ":" ) h16 ] "::"

    h16           = 1*4HEXDIG
    ls32          = ( h16 ":" h16 ) / IPv4address
    IPv4address   = dec-octet "." dec-octet "." dec-octet "." dec-octet
    dec-octet     = DIGIT                 ; 0-9
                 / %x31-39 DIGIT         ; 10-99
                 / "1" 2DIGIT            ; 100-199
                 / "2" %x30-34 DIGIT     ; 200-249
                 / "25" %x30-35          ; 250-255

    reg-name      = *( unreserved / pct-encoded / sub-delims )

    path          = path-abempty    ; begins with "/" or is empty
                 / path-absolute   ; begins with "/" but not "//"
                 / path-noscheme   ; begins with a non-colon segment
                 / path-rootless   ; begins with a segment
                 / path-empty      ; zero characters

    path-abempty  = *( "/" segment )
    path-absolute = "/" [ segment-nz *( "/" segment ) ]
    path-noscheme = segment-nz-nc *( "/" segment )
    path-rootless = segment-nz *( "/" segment )
    path-empty    = 0<pchar>

    segment       = *pchar
    segment-nz    = 1*pchar
    segment-nz-nc = 1*( unreserved / pct-encoded / sub-delims / "@" )
                 ; non-zero-length segment without any colon ":"

    pchar         = unreserved / pct-encoded / sub-delims / ":" / "@"

    query         = *( pchar / "/" / "?" )

    fragment      = *( pchar / "/" / "?" )

    pct-encoded   = "%" HEXDIG HEXDIG

    unreserved    = ALPHA / DIGIT / "-" / "." / "_" / "~"
    reserved      = gen-delims / sub-delims
    gen-delims    = ":" / "/" / "?" / "#" / "[" / "]" / "@"
    sub-delims    = "!" / "$" / "&" / "'" / "(" / ")"
                 / "*" / "+" / "," / ";" / "="
''''''

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


