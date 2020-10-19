import sys
import traceback
sys.path.append('/Users/wilkinsonk/Documents/Development/Snippy')

from snippy import load_application
from snippy import load_app_settings
from snippy import get_app_logger


def main(args):
    try:
        load_app_settings('test_project.settings')
        load_application()

        logger = get_app_logger('test_project')
        logger.info("Starting test_project")
    except:
        trace = traceback.format_exc().strip()
        raise RuntimeError(
            f"Error occured during application runtime:\n{trace}"
        )


if __name__ == '__main__':
    main(sys.argv)