from logging import StreamHandler

PROGRAM = 'test_project'
DESCRIPTION = 'testing Console App'
HELP = "Test the Console App project for all that it's got"

EXTENTIONS = ()

COMMANDS = (
    'test_project.test_command01',
    'test_project.test_command02'
)

LOGGING = ({
    'NAME': 'main',
    'HANDLERS': ({
        'TYPE': StreamHandler,
        'FORMAT': "[%(name)s] [%(levelname)s] %(message)s",
        'LEVEL': 'info'
    },)
})
