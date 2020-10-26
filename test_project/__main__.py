import sys

from snippy.controller import AppController


def main(argv=sys.argv):
    program = AppController('settings')
    try:
        program.start_application(argv)
    except Exception:
        program.raise_runtime()


if __name__ == '__main__':
    main()
