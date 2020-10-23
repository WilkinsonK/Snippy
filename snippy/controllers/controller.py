from traceback import format_exc

from snippy.util import get_project_name
from snippy.loaders.loggers import get_app_logger
from snippy.loaders.loader import AppLoader
from snippy.parser.parsers import AppParser


project_name = get_project_name()


class AppController:

    def __init__(self, module: str):
        self.module = module

    def start_application(self, argv):
        settings = '.'.join([project_name, self.module])
        AppLoader.load_settings(settings)
        AppLoader.load_application()

        self.logger = get_app_logger(project_name)
        self.logger.debug(f"Starting {project_name}")
        self.parse_arguments(argv)

    def parse_arguments(self, argv):
        parser = AppParser(argv)

    def raise_runtime(self):
        error = format_exc().strip()
        error = f"{project_name} encountered an error at runtime:\n\n{error}"
        try:
            self.logger.critical(error)
        except AttributeError:
            print(error)
        quit()
