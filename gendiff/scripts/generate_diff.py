from ..formatters.json import get_diff_formatted_json
from ..formatters.plain import get_diff_formatted_plain
from ..formatters.stylish import get_diff_formatted_stylish
from .build_diff import build_diff
from .parsing_file import get_parsed_file


def generate_diff(file_path1, file_path2, format_name='stylish'):
    file1_data = get_parsed_file(file_path1)
    file2_data = get_parsed_file(file_path2) 
    diff_data = build_diff(file1_data, file2_data)
    
    if format_name == 'stylish':
        return get_diff_formatted_stylish(diff_data)
    elif format_name == 'plain':
        return get_diff_formatted_plain(diff_data)
    elif format_name == 'json':
        return get_diff_formatted_json(diff_data)
    else:
        raise ValueError(f"Unsupported formatter: {format_name}")
