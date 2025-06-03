import json
from pathlib import Path

import yaml

from gendiff.parsing.parsing_file import read_json, read_yaml, get_parsed_file


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


def test_parsing_json():
    file1_json = get_test_data_path('file1.json')
    expected = read_json_file('file1.json')

    assert read_json(file1_json) == expected
    
    
def test_parsing_yaml():
    file1_yaml = get_test_data_path('file1.yaml')
    expected = read_yaml_file('file1.yaml')

    assert read_yaml(file1_yaml) == expected


def test_parsing():
    file1_json = get_test_data_path('file1.json')
    file1_yaml = get_test_data_path('file1.yaml')
    expected_json = read_json_file('file1.json')
    expected_yaml = read_yaml_file('file1.yaml')
    
    assert get_parsed_file(file1_json) == expected_json
    assert get_parsed_file(file1_yaml) == expected_yaml
    

def test_parsing_other_files():
    incorrect_file = get_test_data_path('file.csv')
    
    assert get_parsed_file(incorrect_file) == 'not json or yaml file'
    
    
# Написать тест для проверки json и yaml на корректность