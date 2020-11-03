from typing import Any, Dict

from snippy.core.commands import BaseCommand
from snippy.loaders.commands import get_app_commands
from snippy.loaders.commands import get_app_command
from snippy.loaders.settings import get_app_settings
from snippy.tools import get_project_name
from snippy.tools import objname


class HelpCommand(BaseCommand):
    name = 'help'
    description = 'display application help'
    parameters = {
        ('command'): {
            'help': 'display help text for specific command(s)',
            'nargs': '*', 'default': 'all'
        }
    }

    def execute(self, argv):
        if argv.command == 'all':
            self.print_all()
        else:
            for cmd in argv.command:
                self.print_one(cmd)
        quit()

    def print_one(self, command):
        app_info = get_app_settings('PROGRAM')
        command = get_app_command(command)
        cmd_obj = command()

        params = list()
        max_buffer = 1

        for param in cmd_obj.parameters:
            param_ = self._format_param(param)
            help_ = self._format_help(cmd_obj.parameters[param])
            params.append([param_, help_])

            max_buffer = max(max_buffer, len(param_))

        print('\n| %s | %s' % (app_info, cmd_obj.name))
        print('| %s:\n|' % cmd_obj.description)
        for param in params:
            self._print_param(param[0], param[1], max_buffer)
        print()

    def print_all(self):
        commands = get_app_commands()
        app_info = get_app_settings(('PROGRAM', 'DESCRIPTION', 'HELP'))

        commands_ = list()
        max_buffer = 1

        for c in commands:
            cmd_obj = commands[c]()
            command_ = self._format_param(cmd_obj.name)
            description = cmd_obj.description
            commands_.append([command_, description])

            max_buffer = max(max_buffer, len(command_))

        print('\n| %s | %s' % (app_info['PROGRAM'], app_info['DESCRIPTION']))
        print('| %s:\n|' % app_info['HELP'])
        for command in commands_:
            self._print_param(command[0], command[1], max_buffer)

        print('|\n| use %s help [command] for more info\n' % get_project_name())

    def _format_param(self, param: str or tuple):
        strfparam = '[%s]'
        if isinstance(param, str):
            return strfparam % param
        return strfparam % '  '.join([p for p in param])

    def _format_help(self, param_vars: Dict[str, str]):
        strfhelp = self._check_nargs('%s', param_vars.get('nargs'))
        strfhelp = self._check_type(strfhelp, param_vars.get('type'))
        return strfhelp % param_vars.get('help')

    def _print_param(self, param: str, description: str, max_buffer: int):
        buffer = (max_buffer - len(param)) + 1
        print('|   %s%s%s' % (param, ' ' * buffer, description))

    def _check_nargs(self, base_strf: str, nargs: str or int):
        narg_vars = {
            None: '', '?': '(0-1) ', '+': '(1+) ', '*': '(*) ',
        }
        if nargs in narg_vars:
            return narg_vars[nargs] + base_strf
        return ('(%s) ' % nargs) + base_strf

    def _check_type(self, base_strf: str, type_: Any):
        if type_ == None:
            return base_strf
        return ('%s ' % objname(type_)) + base_strf
