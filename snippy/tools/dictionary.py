

def dictionary(obj: object) -> str:
    '''
    Return an object's dictionary (if exists)
    '''
    if '__dict__' in dir(obj):
        return obj.__dict__
    return dict()
