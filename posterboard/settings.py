
PROGRAM = 'Posterboard Core'
DESCRIPTION = 'CLI framework'
HELP = 'seamlessly build command line interfaces'

COMMANDS = (
    'posterboard.commands.help',
    'posterboard.commands.init'
)

LOGGING = ({
    'NAME': 'main',
    'HANDLERS': ({
        'TYPE': 'stream',
        'FORMAT': "[%(name)s] [%(levelname)s] %(message)s",
        'LEVEL': 'debug'
    },)
})
