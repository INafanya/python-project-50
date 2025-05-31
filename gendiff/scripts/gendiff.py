import argparse
import json


def main():
    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration \
                        files and shows a difference.'
                    )
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    
    file1 = args.first_file
    file2 = args.second_file
    
    generate_diff(file1, file2)


def read_and_sort_json(json_file):
    with open(f'{json_file}', 'r') as file:
        data = json.load(file)
    sorted_data = dict(sorted(data.items()))
    return sorted_data


def generate_diff(file_path1, file_path2):
    diff_result = '{\n'
    
    file1_data = read_and_sort_json(file_path1)
    file2_data = read_and_sort_json(file_path2)
    
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
    return diff_result


if __name__ == '__main__':
    main()