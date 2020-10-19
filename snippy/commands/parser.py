from snippy.commands.base import BaseCommand


class Parser:

    def __init__(self, command_obj: BaseCommand, argv):
        self.command_obj = command_obj(argv)
        self.argv = argv
        self.get_command_required_args()
        self.get_command_optional_args()

    def get_command_required_args(self):
        self.required_args = self.command_obj._arguments

    def get_command_optional_args(self):
        self.optional_args = self.command_obj._optionals

    def parse_args(self, argv):
        pass

    def parse_required_args(self, argv):
        pass

    def parse_optional_args(self, argv):
        pass
