

def dictionary(obj: object) -> str:
    '''
    Return an object's dictionary (if exists)
    '''
    if '__dict__' in dir(obj):
        return obj.__dict__
    return dict()


def annotation(obj: object) -> None:
    '''
    Return an objects annotations (if any)
    '''
    if '__annotations__' in dir(obj):
        return obj.__annotations__
    return dict()
