import argparse
import json

path_to_files = './gendiff/files'
def main():
    parser = argparse.ArgumentParser(
                    prog='gendiff',
                    description='Compares two configuration files and shows a difference.')
    parser.add_argument('-f', '--format', type=str, help='set format of output')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    args = parser.parse_args()
    
    file1 = args.first_file
    file2 = args.second_file
    
    # file1 = json.load(open(f'{path_to_files}/{first_file}'))
    # file2 = json.load(open(f'{path_to_files}/{file2}'))
    
    with open(f'{path_to_files}/{file1}', 'r') as file:
        file1_data = json.load(file)
        
    with open(f'{path_to_files}/{file2}', 'r') as file:
        file2_data = json.load(file)

    print('\nfile1 data:')
    for data in file1_data:
        print(f'{data} = {file1_data[data]}')
    
    print('\nfile2 data:')
    for data in file2_data:
        print(f'{data} = {file2_data[data]}')


if __name__ == '__main__':
    main()