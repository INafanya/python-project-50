import json
from pathlib import Path

import yaml


def read_json(file_path):
    with open(f'{file_path}', 'r') as file:
        data = json.load(file)
    return data


def read_yaml(file_path):
    with open(f'{file_path}') as file:
        data = yaml.safe_load(file)
    return data


def get_parsed_file(file_path):
    ext = Path(file_path).suffix
    if ext == '.json':
        return read_json(file_path)
    elif ext in ('.yml', '.yaml'):
        return read_yaml(file_path)
    else:
        return 'not json or yaml file'
