import sys


def get_project_name():
    '''
    Returns the name of the project from execution path
    '''
    if not isinstance((path := sys.argv[0].split('/')), list):
        path = sys.argv[0].split('\\')
    return path[-2]
