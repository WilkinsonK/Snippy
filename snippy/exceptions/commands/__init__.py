
class CommandValueError(BaseException):
    def __init__(self, message='Value Error in command config'):
        self.message = message

    def __repr__(self):
        return self.message


class CommandAttrError(BaseException):
    def __init__(self, message='Attribute Error in command config'):
        self.message = message

    def __repr__(self):
        return self.message
