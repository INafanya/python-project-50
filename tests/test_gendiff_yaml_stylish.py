from pathlib import Path

from gendiff.generate_diff.generate_diff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_text_file(filename):
    return get_test_data_path(filename).read_text()


format_name = 'stylish'

    
def test_gendiff_flat_yaml():
    file1 = get_test_data_path('file1.yaml')
    file2 = get_test_data_path('file2.yaml')
    expected_similar = read_text_file('similar_result.txt')
    expected_different = read_text_file('different_result.txt')
    # Сравнение одинкаовых плоских yaml
    assert generate_diff(file1, file1, format_name) == expected_similar
    # Сравнение разных плоских yaml
    assert generate_diff(file1, file2, format_name) == expected_different
    
    
def test_gendiff_tree_yaml():
    file3 = get_test_data_path('file3.yaml')
    file4 = get_test_data_path('file4.yaml')
    expected_similar = read_text_file('similar_tree_result.txt')
    expected_different = read_text_file('different_tree_result.txt')
    # Сравнение одинкаовых yaml
    assert generate_diff(file3, file3, format_name) == expected_similar
    # Сравнение разных yaml
    assert generate_diff(file3, file4, format_name) == expected_different
