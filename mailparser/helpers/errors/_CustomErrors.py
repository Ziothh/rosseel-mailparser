class __CustomError(Exception):
    action = None

    @property
    def class_name(self):
        return self.__class__.__name__

    @property
    def class_type(self):
        return self.__class__

    def __eq__(self, other: Exception) -> bool:
        return type(self) is type(other)

    def __ne__(self, other: Exception) -> bool:
        return type(self) is not type(other)


class LaunchArgumentsError(__CustomError):
    pass


class EmptyMailboxError(__CustomError):
    pass


class ParsingError(__CustomError):
    pass


class KeyNotFoundError(__CustomError):
    pass


class TableNotFoundError(__CustomError):
    pass


class NotTruthyError(__CustomError):
    pass


class FormSourceNotFoundError(__CustomError):
    """Requires a company to be added"""
    pass
