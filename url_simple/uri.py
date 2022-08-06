
import re
import url_simple.components as components
import url_simple.exceptions as exceptions
import url_simple.mixins as mixins

from abc import ABC, abstractmethod
from typing import List, NamedTuple


class URI(components.URIComponent):
    value_regex: re.Pattern = re.compile(rf'{components.Scheme.as_pattern()}')
    validation_error = exceptions.InvalidURIError

    def _get_components(self, match: re.Match):
        self.scheme = components.Scheme(match.group('scheme'))
        self.authority = components.Authority(match.group('authority'))
        self.path = components.Path(match.group('path'))
        self.query = components.Query(match.group('query'))
        self.fragment = components.Fragment(match.group('fragment'))

