from snippy import BaseCommand


class TestCommand01(BaseCommand):
    parameters = {
        ('integer1'): {'action': 'store', 'help': 'first integer argument'},
        ('integer2'): {'action': 'store', 'help': 'second integer argument'},
    }
    description = 'A test command object for ensuring quality'

    def execute(self, args):
        print(args)
