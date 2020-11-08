from snippy.tools.names import classname
from snippy.tools.names import objname
from snippy.tools.names import get_project_name
from snippy.tools.dictionary import annotation
from snippy.tools.dictionary import dictionary
from snippy.tools.debugging import debugger
from snippy.tools.filehandling import get_file_contents
from snippy.tools.filehandling import parse_template_files
from snippy.tools.filehandling import is_block_start
from snippy.tools.filehandling import has_suffix
from snippy.tools.filehandling import make_proj_directory
from snippy.tools.filehandling import make_cmd_directory
from snippy.tools.filehandling import write_proj_file


__all__ = (
    'classname', 'objname', 'get_project_name', 
    'annotation', 'dictionary', 'debugger', 'get_file_contents',
    'parse_template_files', 'is_block_start', 'has_suffix',
    'make_proj_directory', 'make_cmd_directory', 'write_proj_file'
)

__doc__ = '''
Basic tools for Snippy applictations
'''
