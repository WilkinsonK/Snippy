import sys

from snippy.controllers.controller import AppController
from snippy.loaders.commands import get_app_command


def main(argv=sys.argv):
    program = AppController('settings')
    try:
        program.start_application(argv)
        x = get_app_command('queenvictoria')
        x().execute()
    except:
        program.raise_runtime()


if __name__ == '__main__':
    main()
