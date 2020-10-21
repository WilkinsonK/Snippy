

def annotation(obj: object) -> None:
    '''
    Return an objects annotations (if any)
    '''
    if '__annotations__' in dir(obj):
        return obj.__annotations__
    return dict()
