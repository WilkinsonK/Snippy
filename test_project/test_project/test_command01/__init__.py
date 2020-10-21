from snippy import BaseCommand


class TestCommand01(BaseCommand):
    name = 'queenvictoria'

    def execute(self):
        print("Off with their heads!!")

    def parse_arguments(self, argv: list):
        pass

    def add_parameters(self, parser):
        pass
