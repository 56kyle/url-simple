
import re
import url_simple.components as components
import url_simple.exceptions as exceptions
import url_simple.mixins as mixins

from abc import ABC, abstractmethod
from typing import List, NamedTuple


class URI(mixins.ValueStringValidatable):
    scheme: components.Scheme
    authority: components.Authority
    path: components.Path
    query: components.Query
    fragment: components.Fragment

    def __init__(self, value: str):
        self.scheme = components.Scheme(value)
        self.authority = components.Authority(value)
        self.path = components.Path(value)
        self.query = components.Query(value)
        self.fragment = components.Fragment(value)
        self.components = [
            self.scheme,
            self.authority,
            self.path,
            self.query,
            self.fragment,
        ]
