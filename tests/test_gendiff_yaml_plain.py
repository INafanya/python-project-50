from pathlib import Path

from gendiff.generate_diff.generate_diff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_text_file(filename):
    return get_test_data_path(filename).read_text()


def test_gendiff_tree_yaml():
    file3 = get_test_data_path('file3.yaml')
    file4 = get_test_data_path('file4.yaml')
    expected = read_text_file('different_plain_result.txt')

    # Сравнение разных yaml
    assert generate_diff(file3, file4, format_name='plain') == expected
