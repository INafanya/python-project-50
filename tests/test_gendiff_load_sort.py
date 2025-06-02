import json
from pathlib import Path

import yaml

from gendiff.parsing.parsing_file import read_and_sort_json, read_and_sort_yaml


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_text_file(filename):
    return get_test_data_path(filename).read_text()


def read_json_file(filename):
    with open(get_test_data_path(filename), 'r') as file:
        return json.load(file)


def read_yaml_file(filename):
    with open(get_test_data_path(filename), 'r') as file:
        return yaml.safe_load(file)


def test_gendiff_load_and_sort_json():
    file1_json = get_test_data_path('file1.json')
    expected = read_json_file('file1_sorting.json')
    
    # Сравнение сортировки json
    assert read_and_sort_json(file1_json) == expected
    
    
def test_gendiff_load_and_sort_yaml():
    file1_json = get_test_data_path('file1.yaml')
    expected = read_yaml_file('file1_sorting.yaml')
    
    # Сравнение сортировки json
    assert read_and_sort_yaml(file1_json) == expected
    
    
read_yaml_file('file1.yaml')