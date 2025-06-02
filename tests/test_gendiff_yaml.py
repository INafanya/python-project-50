from pathlib import Path

from gendiff.scripts.gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_text_file(filename):
    return get_test_data_path(filename).read_text()

    
def test_gendiff_yaml():
    file1_yaml = get_test_data_path('file1.yaml')
    file2_yaml = get_test_data_path('file2.yaml')
    expected_similar = read_text_file('similar_result.txt')
    expected_different = read_text_file('different_result.txt')
    
    # Сравнение одинкаовых json
    assert generate_diff(file1_yaml, file1_yaml) == expected_similar
    
    # Сравнение разных json
    assert generate_diff(file1_yaml, file2_yaml) == expected_different
    
    # Сравнение некорректных json