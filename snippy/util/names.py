

def classname(obj: object) -> str:
    '''
    Return an object's class name
    '''
    return obj.__class__.__qualname__


def objname(obj: object) -> str:
    '''
    Returns an object's name
    '''
    return obj.__name__
