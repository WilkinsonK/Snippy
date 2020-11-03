
PROGRAM = 'Snippy Core'
DESCRIPTION = 'CLI framework'
HELP = 'seamlessly build command line interfaces'

COMMANDS = (
    'snippy.commands',
    'snippy.commands.init'
)

LOGGING = ({
    'NAME': 'main',
    'HANDLERS': ({
        'TYPE': 'stream',
        'FORMAT': "[%(name)s] [%(levelname)s] %(message)s",
        'LEVEL': 'info'
    },)
})
