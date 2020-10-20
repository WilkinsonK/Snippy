

class AnnotationObject(str, object):

    def __new__(cls, obj: object):
        if '__annotations__' in obj.__dir__():
            return obj.__annotations__
        return dict()


def annotation(obj: object) -> None:
    '''
    Return an objects annotations (if any)
    '''
    return AnnotationObject(obj)
