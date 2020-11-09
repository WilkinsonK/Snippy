from functools import wraps

from posterboard import get_app_logger
from posterboard.tools import objname
from posterboard.tools import get_project_name


def _get_logger():
    project_name = get_project_name()
    return get_app_logger(project_name)


def _format_message(func, variables: dict):
    message = f"executing '{objname(func)}':"
    for v in variables:
        if v in ('debugger_logger', 'func'):
            continue
        if v == 'args':
            message += f'\n\t{v}:\n\t  '
            message += '\n\t  '.join(
                [str(a) for a in variables[v]]
            )
            continue
        if v == 'kwargs' and variables['kwargs'] != {}:
            message += f'\n\t{v}:\n\t  '
            message += '\n\t  '.join([
                f"{k}: {variables[v][k]}" for k in variables[v]]
            )
            continue
        message += f"\n\t{v}: {variables[v]}"
    return message


def debugger(func):
    '''
    Logs debugging messages on a function call
    '''

    @wraps(func)
    def __inner_debugger(*args, **kwargs):
        debugger_logger = _get_logger()
        message = _format_message(func, locals())
        try:
            debugger_logger.debug(message)
            result = func(*args, **kwargs)
        except Exception as error:
            debugger_logger.error(str(error))
            raise RuntimeError
        else:
            debugger_logger.debug(f"{objname(func)} result:\n\t{result}")
            return result
    return __inner_debugger
