class OCPIError(Exception):
    """
    Generic Error
    """


class AuthorizationOCPIError(OCPIError):
    def __str__(self):
        return 'Your authorization token is invalid.'
