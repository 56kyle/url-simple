

class ValidationError(ValueError):
    pass

class InvalidURIError(ValidationError):
    pass

class InvalidURLError(InvalidURIError):
    pass

class InvalidURNError(InvalidURIError):
    pass


class InvalidSchemeError(ValidationError):
    pass


class InvalidAuthorityError(ValidationError):
    pass


class InvalidUserInfoError(InvalidAuthorityError):
    pass

class InvalidHostError(InvalidAuthorityError):
    pass

class InvalidPortError(InvalidAuthorityError):
    pass


class InvalidPathError(ValidationError):
    pass


class InvalidQueryError(ValidationError):
    pass


class InvalidFragmentError(ValidationError):
    pass



