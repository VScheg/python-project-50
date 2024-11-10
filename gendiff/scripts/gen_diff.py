#!/usr/bin/env python3
from gendiff.argparsing import get_arguments
from gendiff import generate_diff


def main():
    """Print difference between two files"""
    args = get_arguments()
    print(generate_diff(args.first_file, args.second_file, args.format))


if __name__ == "__main__":
    main()
