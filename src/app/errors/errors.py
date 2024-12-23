class HHAPIError(Exception):
    """Custom exception for HH API errors."""
    def __init__(self, message: str, status_code: int = None):
        super().__init__(message)
        self.status_code = status_code