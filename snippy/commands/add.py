from os import path, listdir
from os.path import dirname
from snippy.tools import make_cmd_directory

from snippy.core.commands import BaseCommand
from snippy.tools import get_file_contents
from snippy.tools import parse_template_files


class AddCommand(BaseCommand):
    name = 'add'
    description = 'add a new command to your project'
    parameters = {
        ('command'): {
            'help': 'command dir name'
        },
        ('command_dir'): {
            'help': 'directory to create command',
            'nargs': '?',
            'default': 'commands'
        }
    }

    template_dir = path.join(dirname(__file__), 'templates')

    def execute(self, argv):
        self.argv = argv
        self.argv.command_name = argv.command.lower()
        self.argv.description = input('description: ')

        self.files = parse_template_files({
            c:get_file_contents(
                self.template_dir, c
            ) for c in listdir(self.template_dir)
        })

        make_cmd_directory(self.argv, self.files)
