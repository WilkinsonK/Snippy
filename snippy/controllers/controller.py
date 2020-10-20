from traceback import format_exc

from snippy.util import get_project_name
from snippy.loaders.loggers import get_app_logger
from snippy.loaders.loader import load_app_settings
from snippy.loaders.loader import load_application


project_name = get_project_name()


class AppController:

    def __init__(self, module: str):
        settings_module = '.'.join([project_name, module])
        load_app_settings(settings_module)

    def start_application(self, argv):
        load_application()
        self.logger = get_app_logger(project_name)
        self.logger.debug(f"Starting {project_name}")

    def raise_runtime(self):
        error = format_exc().strip()
        self.logger.critical(
            f"{project_name} encountered an error at runtime:\n\t{error}"
        )
        quit()
