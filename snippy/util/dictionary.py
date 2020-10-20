

class DictionaryObject(str, object):

    def __new__(cls, obj: object):
        if '__dict__' in obj.__dir__():
            return obj.__dict__
        return dict()


def dictionary(obj: object) -> str:
    '''
    Return an object's dictionary (if exists)
    '''
    return DictionaryObject(obj)
