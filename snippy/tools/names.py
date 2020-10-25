import sys
from os.path import dirname, isdir, abspath


def classname(obj: object) -> str:
    '''
    Return an object's class name
    '''
    return obj.__class__.__name__


def objname(obj: object) -> str:
    '''
    Returns an object's name
    '''
    return obj.__name__


def get_project_name() -> str:
    '''
    Returns the name of the project from execution path
    '''
    path = sys.argv[0]
    path = path.replace('\\', '/')
    if not isdir(path):
        return dirname(path).split('/')[-1]
    return abspath(path).split('/')[-1]
