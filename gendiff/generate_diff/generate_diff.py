from gendiff.parsing.parsing_file import get_parsed_file


def generate_diff(file_path1, file_path2):
    diff_result = '{\n'
    
    file1_data = get_parsed_file(file_path1)
    file2_data = get_parsed_file(file_path2)
    
    for key_1 in file1_data:
        if key_1 in file2_data:
            for key_2 in file2_data:
                if key_2 in file1_data:
                    if key_1 == key_2:
                        if file1_data[key_1] == file2_data[key_2]:
                            diff_result += f'    {key_1}: {file1_data[key_1]}\n'
                        else:
                            diff_result += f'  - {key_1}: {file1_data[key_1]}\
\n  + {key_2}: {file2_data[key_2]}\n'
                else:
                    diff_result += f'  + {key_2}: {file2_data[key_2]}\n'
        else:
            diff_result += f'  - {key_1}: {file1_data[key_1]}\n'
    diff_result += '}'
    print(diff_result)
    return diff_result
