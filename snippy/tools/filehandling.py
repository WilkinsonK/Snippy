import sys
from os import path, mkdir
from os.path import dirname
from typing import Dict
from re import match


exe_dir = dirname(sys.argv[0])
root_dir = path.curdir


def is_block_start(line: str):
    return match(r'\[(.+)\]', line)


def has_suffix(dir_item: str):
    return match(r'(.+)\.[a-z]+', dir_item)


def make_proj_directory(argv, files: Dict[str, dict]):
    proj_name = argv.proj_name
    proj_template = files['directory.txt'].get('[project dir]')

    for d in proj_template:
        d = d.replace('\n', '')
        d = d.replace('\\', '/')
        if 'projname' in d:
            d = d % {'projname': proj_name}
        if len(d) == 0:
            continue
        if len(d.split('/')) > 1 and argv.skip_subdir and not has_suffix(d):
            continue
        if not has_suffix(d):
            mkdir(path.join(root_dir, d))
        else:
            write_proj_file(argv, d, files)


def make_cmd_directory(argv, files: Dict[str, dict]):
    command_name = argv.command_name
    command_dir = argv.command_dir
    cmd_template = files['directory.txt'].get('[command dir]')

    for d in cmd_template:
        d = d.replace('\n', '').replace('\\', '/')
        if 'commandname' in d:
            d = d % {'commandname': command_name}
        if len(d) == 0:
            continue
        if not has_suffix(d):
            mkdir(path.join(exe_dir, command_dir, command_name))
        else:
            write_command_file(argv, d, files)


def write_proj_file(argv, file_name: str, files: Dict[str, dict]):
    file_args = {
        'projname': argv.proj_name,
        'description': argv.description,
        'help': argv.help_text,
        'initdate': argv.initdate,
        'snippyversion': argv.snippyversion,
        'name': '%(name)s',
        'levelname': '%(levelname)s',
        'message': '%(message)s'
    }

    temp_key = '[%s]' % file_name.split('/')[-1]
    file_template = files['files.txt'].get(temp_key)
    contents = ''.join(file_template) % file_args

    with open(path.join(root_dir, file_name), 'w') as file:
        file.write(contents)


def write_command_file(argv, file_name: str, files: Dict[str, dict]):
    file_args = {
        'command': argv.command,
        'commandname': argv.command_name,
        'description': argv.description
    }

    file_template = files['files.txt'].get('[command]')
    contents = ''.join(file_template) % file_args

    with open(path.join(exe_dir, argv.command_dir, file_name), 'w') as file:
        file.write(contents)


def get_file_contents(template_dir, file_name: str):
    with open(path.join(template_dir, file_name), 'r') as file:
        contents = file.readlines()
    return contents


def parse_template_files(contents: Dict[str, list]):
    for file_ in contents:
        markers = list()
        blocks = dict()

        for i in contents[file_]:
            if is_block_start(i):
                markers.append(contents[file_].index(i))

        for i in range(len(markers)):
            block_id = contents[file_][markers[i]].replace('\n', '')
            try:
                blocks[block_id] = contents[file_][
                    markers[i]+1:markers[i+1]
                ]
            except IndexError:
                blocks[block_id] = contents[file_][markers[i]+1:]

        contents[file_] = blocks

    return contents
