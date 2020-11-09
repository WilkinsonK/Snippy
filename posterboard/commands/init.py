from os.path import dirname
from os import path, listdir
from datetime import datetime

from posterboard import get_version
from posterboard.core.commands import BaseCommand
from posterboard.tools import get_file_contents
from posterboard.tools import parse_template_files
from posterboard.tools import make_proj_directory


class InitCommand(BaseCommand):
    name = 'init'
    description = 'create a new posterboard project'
    parameters = {
        ('proj_name'): {'help': 'provide project name', 'type':str},
        ('-s', '--skip-subdir'): {
            'action': 'store_true', 
            'help': 'skip initiation of commands sub-directory'
        }
    }

    template_dir = path.join(dirname(__file__), 'templates')

    def execute(self, argv):
        self.argv = argv
        self.argv.description = input('description: ')
        self.argv.help_text = input('help text: ')
        self.argv.initdate = datetime.now().strftime('%Y-%m-%d')
        self.argv.PBversion = get_version()

        self.files = parse_template_files({
            c:get_file_contents(
                self.template_dir, c
            ) for c in listdir(self.template_dir)
        })
        make_proj_directory(self.argv, self.files)
