class APIError(Exception):
    """Base exception for API errors."""

    def __init__(self, message: str, status_code: int | None = None):
        self.message = message
        self.status_code = status_code
        super().__init__(self.message)


class APINetworkError(APIError):
    """Network-related API error."""

    pass


class APITimeoutError(APIError):
    """API request timeout error."""

    pass


class APIValidationError(APIError):
    """API response validation error."""

    pass
