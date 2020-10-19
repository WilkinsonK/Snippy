from logging import StreamHandler
from consoleapp.logger.levels import DEBUG

PROGRAM = 'test_project'
DESCRIPTION = 'testing Console App'
HELP = "Test the Console App project for all that it's got"

EXTENTIONS = ()

COMMANDS = (
    'test_project.test_command01',
    'test_project.test_command02'
)

LOGGING = ({
    'NAME': 'test_project',
    'HANDLERS': ({
        'TYPE': StreamHandler,
        'FORMAT': "[%(name)s] [%(levelname)s] %(message)s",
        'LEVEL': DEBUG
    },)
})
