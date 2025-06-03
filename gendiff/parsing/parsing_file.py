import json

import yaml


def read_json(file_path):
    with open(f'{file_path}', 'r') as file:
        data = json.load(file)
    # sorted_data = dict(sorted(data.items()))
    return data


def read_yaml(file_path):
    with open(f'{file_path}') as file:
        data = yaml.safe_load(file)
    # sorted_data = dict(sorted(data.items()))
    return data


def get_parsed_file(file_path):
    str_file_path = str(file_path)
    if str_file_path.endswith('.json'):
        return read_json(file_path)
    elif str_file_path.endswith('.yml') or str_file_path.endswith('yaml'):
        return read_yaml(file_path)
    else:
        print('not json or yaml file')
        return 'not json or yaml file'

