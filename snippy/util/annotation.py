

def annotation(obj: object) -> None:
    '''
    Return an objects annotations (if any)
    '''
    if '__annotations__' in obj.__dir__():
        return obj.__annotations__
    return dict()
