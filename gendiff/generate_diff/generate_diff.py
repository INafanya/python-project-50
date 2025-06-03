from gendiff.parsing.parsing_file import get_parsed_file


def generate_diff(file_path1, file_path2):
    file1_data = get_parsed_file(file_path1)
    file2_data = get_parsed_file(file_path2)

    diff_result = '{\n'

    all_data = sorted(set(file1_data.keys()) | set(file2_data.keys()))
    for key in all_data:
        if key not in file1_data:
            diff_result += f'  + {key}: {file2_data[key]}\n'
        elif key not in file2_data:
            diff_result += f'  - {key}: {file1_data[key]}\n'
        else:
            if file1_data[key] == file2_data[key]:
                diff_result += f'    {key}: {file1_data[key]}\n'
            else:
                diff_result += f'  - {key}: {file1_data[key]}\n'
                diff_result += f'  + {key}: {file2_data[key]}\n'
    diff_result += '}'
    diff_result = diff_result.lower()

    print(diff_result)
    return diff_result
