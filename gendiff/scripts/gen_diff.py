#!/usr/bin/env python3
from ..argparsing import get_arguments
from gendiff import generate_diff


def main():
    args = get_arguments()
    print(generate_diff(*args))


if __name__ == "__main__":
    main()
