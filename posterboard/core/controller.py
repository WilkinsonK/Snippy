from traceback import format_exc

from posterboard.tools import get_project_name
from posterboard.tools.debugging import debugger
from posterboard.loaders.loggers import get_app_logger
from posterboard.loaders.loader import AppLoader
from posterboard.core.parsers import AppParser


project_name = get_project_name()


class AppController:
    '''
    Central control for posterboard. Handles starting of the application,
    parsing arguments, logging exceptions, etc.
    '''

    def __init__(self, module: str):
        self.module = module

    def start_application(self, argv):
        settings = '.'.join([project_name, self.module])
        AppLoader.load_settings(settings)
        AppLoader.load_application()

        self.logger = get_app_logger(project_name)
        self.logger.debug(f"Starting {project_name}")

        self.parse_and_execute(argv)

    def parse_and_execute(self, argv):
        app_parser = AppParser(argv)
        app_parser.execute_commands()

    def raise_runtime(self):
        error = format_exc().strip()
        error = f"{project_name} encountered an error at runtime:\n\n{error}"
        try:
            self.logger.critical(error)
        except AttributeError:
            print(error)
        quit()