import argparse

# from gendiff.parsing.parsing_file import get_parsed_file
from gendiff.generate_diff.generate_diff import generate_diff


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


if __name__ == '__main__':
    main()
