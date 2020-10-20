

def dictionary(obj: object) -> str:
    '''
    Return an object's dictionary (if exists)
    '''
    if '__dict__' in obj.__dir__():
        return obj.__dict__
    return dict()
