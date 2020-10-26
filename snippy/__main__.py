import sys
from snippy.core.controller import AppController


def main(argv=sys.argv):
    program = AppController('core_settings')
    try:
        program.start_application(argv)
    except Exception:
        program.raise_runtime()


if __name__ == '__main__':
    main()