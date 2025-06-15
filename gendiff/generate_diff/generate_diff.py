from gendiff.build_diff.build_diff import build_diff
from gendiff.formatters.stylish import get_diff_formatted_stylish
from gendiff.parsing.parsing_file import get_parsed_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1_data = get_parsed_file(file_path1)
    file2_data = get_parsed_file(file_path2) 
    diff_data = build_diff(file1_data, file2_data)
    
    if format_name == 'stylish':
        return get_diff_formatted_stylish(diff_data)
    else:
        return 'other format'
