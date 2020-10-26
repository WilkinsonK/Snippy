from logging import StreamHandler

PROGRAM = 'Snippy Core'
DESCRIPTION = 'CLI framework'
HELP = 'Seamlessly build command line interfaces'

EXTENSIONS = ()

COMMANDS = (
    'core.command_init',
    'core.command_add',
    'core.command_test'
)

LOGGING = ({
    'NAME': 'main',
    'HANDLERS': ({
        'TYPE': StreamHandler,
        'FORMAT': "[%(name)s] [%(levelname)s] %(message)s",
        'LEVEL': 'debug'
    },)
})
