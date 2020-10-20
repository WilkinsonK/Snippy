import sys

from snippy.controllers.controller import AppController


def main(argv=sys.argv):
    program = AppController('settings')
    try:
        program.start_application(argv)
    except:
        program.raise_runtime()


if __name__ == '__main__':
    main()
