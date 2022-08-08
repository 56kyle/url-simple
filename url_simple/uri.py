
import re
import url_simple.components as components
import url_simple.exceptions as exceptions
import url_simple.mixins as mixins

from abc import ABC, abstractmethod
from typing import List, NamedTuple


class URI(components.URIComponent):
    regex: re.Pattern = re.compile(rf'^((?P<scheme>[^:/?#]+):)?(//([^/?#]*))?([^?#]*)(?P<query>\?([^#]*))?(?P<fragment>#(.*))?', re.DEBUG)
    validation_error = exceptions.InvalidURIError

    def _get_components(self, match: re.Match):
        scheme_match = match.group('scheme')
        authority_match = match.group('authority')
        path_match = match.group('path')
        query_match = match.group('query')
        fragment_match = match.group('fragment')

        self.scheme = components.Scheme(scheme_match) if scheme_match else None
        self.authority = components.Authority(authority_match) if authority_match else None
        self.path = components.Path(path_match) if path_match else None
        self.query = components.Query(query_match) if query_match else None
        self.fragment = components.Fragment(fragment_match) if fragment_match else None

