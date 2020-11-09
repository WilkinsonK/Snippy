from posterboard.tools.names import classname
from posterboard.tools.names import objname
from posterboard.tools.names import get_project_name
from posterboard.tools.dictionary import annotation
from posterboard.tools.dictionary import dictionary
from posterboard.tools.debugging import debugger
from posterboard.tools.filehandling import get_file_contents
from posterboard.tools.filehandling import parse_template_files
from posterboard.tools.filehandling import is_block_start
from posterboard.tools.filehandling import has_suffix
from posterboard.tools.filehandling import make_proj_directory
from posterboard.tools.filehandling import make_cmd_directory
from posterboard.tools.filehandling import write_proj_file


__all__ = (
    'classname', 'objname', 'get_project_name', 
    'annotation', 'dictionary', 'debugger', 'get_file_contents',
    'parse_template_files', 'is_block_start', 'has_suffix',
    'make_proj_directory', 'make_cmd_directory', 'write_proj_file'
)

__doc__ = '''
Basic tools for posterboard applictations
'''
