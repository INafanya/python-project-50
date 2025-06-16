import json
from pathlib import Path

import yaml

from gendiff.scripts.generate_diff import generate_diff
from gendiff.scripts.parsing_file import get_parsed_file, read_json, read_yaml


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
    expected_falt_json = read_json_file('file1.json')
    expected_flat_yaml = read_yaml_file('file1.yaml')
    file3_json = get_test_data_path('file3.json')
    file3_yaml = get_test_data_path('file3.yaml')
    expected_tree_json = read_json_file('file3.json')
    expected__tree_yaml = read_yaml_file('file3.yaml')

    assert get_parsed_file(file1_json) == expected_falt_json
    assert get_parsed_file(file1_yaml) == expected_flat_yaml
    assert get_parsed_file(file3_json) == expected_tree_json
    assert get_parsed_file(file3_yaml) == expected__tree_yaml


def test_generate_diff_stylish():
    json1 = get_test_data_path('file1.json')
    json2 = get_test_data_path('file2.json')
    json3 = get_test_data_path('file3.json')
    json4 = get_test_data_path('file4.json')
    yaml1 = get_test_data_path('file1.yaml')
    yaml2 = get_test_data_path('file2.yaml')
    yaml3 = get_test_data_path('file3.yaml')
    yaml4 = get_test_data_path('file4.yaml')

    expected_flat_similar = read_text_file('similar_result.txt')
    expected_flat_different = read_text_file('different_result.txt')
    expected_tree_similar = read_text_file('similar_tree_result.txt')
    expected_tree_different = read_text_file('different_tree_result.txt')
    # Сравнение одинкаовых плоских json
    assert generate_diff(json1, json1) == expected_flat_similar
    # Сравнение разных плоских json
    assert generate_diff(json1, json2) == expected_flat_different
    # Сравнение одинкаовых json
    assert generate_diff(json3, json3) == expected_tree_similar
    # Сравнение разных json
    assert generate_diff(json3, json4) == expected_tree_different
    # Сравнение одинкаовых плоских yaml
    assert generate_diff(yaml1, yaml1) == expected_flat_similar
    # Сравнение разных плоских yaml
    assert generate_diff(yaml1, yaml2) == expected_flat_different
    # Сравнение одинкаовых yaml
    assert generate_diff(yaml3, yaml3) == expected_tree_similar
    # Сравнение разных yaml
    assert generate_diff(yaml3, yaml4) == expected_tree_different


def test_generate_diff_plain():
    formatter = 'plain'
    json3 = get_test_data_path('file3.json')
    json4 = get_test_data_path('file4.json')
    yaml3 = get_test_data_path('file3.yaml')
    yaml4 = get_test_data_path('file4.yaml')

    expected_plain = read_text_file('different_plain_result.txt')
    # Сравнение разных json
    assert generate_diff(json3, json4, formatter) == expected_plain
    # Сравнение разных yaml
    assert generate_diff(yaml3, yaml4, formatter) == expected_plain


def test_generate_diff_json():
    file3 = get_test_data_path('file3.json')
    file4 = get_test_data_path('file4.json')
    expected = read_text_file('different_json_format.txt')
    # Сравнение разных json
    assert generate_diff(file3, file4, format_name='json') == expected
