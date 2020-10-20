

class NameObject(str, object):

    def __new__(cls, obj: object):
        return obj.__class__.__name__


def classname(obj: object) -> str:
    '''
    Return an object's class name
    '''
    return NameObject(obj)
