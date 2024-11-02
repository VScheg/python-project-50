#!/usr/bin/env python3
from gendiff.argparsing import get_arguments
from gendiff import generate_diff


def main():
    file_1, file_2, format_name = get_arguments()
    if not format_name:
        print(generate_diff(file_1, file_2))
    else:
        print(generate_diff(file_1, file_2, format_name))


if __name__ == "__main__":
    main()
