
class ConfigValueError(BaseException):
    def __init__(self, message='Value Error in logger config'):
        self.message = message

    def __repr__(self):
        return self.message


class ConfigPathError(BaseException):
    def __init__(self, message='Path Error in logger config'):
        self.message = message

    def __repr__(self):
        return self.message


class ConfigAttrError(BaseException):
    def __init__(self, message='Attribute Error in logger config'):
        self.message = message

    def __repr__(self):
        return self.message
