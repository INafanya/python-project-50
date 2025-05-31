from pathlib import Path

from gendiff.scripts.gendiff import generate_diff


def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename


def read_text_file(filename):
    return get_test_data_path(filename).read_text()

    
def test_gendiff_json():
    file1_json = get_test_data_path('file1.json')
    file2_json = get_test_data_path('file2.json')
    expected_similar = read_text_file('gendiff_json_similar_result.txt')
    expected_different = read_text_file('gendiff_json_different_result.txt')
    
    # Сравнение одинкаовых json
    assert generate_diff(file1_json, file1_json) == expected_similar
    
    # Сравнение разных json
    assert generate_diff(file1_json, file2_json) == expected_different
    
    # Сравнение некорректных json