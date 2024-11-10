#!/usr/bin/env python3
from gendiff.argparsing import get_arguments
from gendiff import generate_diff


def main():
    """Print difference between two files"""
    args = get_arguments()
    print(generate_diff(args.file_1, args.file_2, args.format_name))


if __name__ == "__main__":
    main()
