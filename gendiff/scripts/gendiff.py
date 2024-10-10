#!/usr/bin/env python3
import argparse
import json


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference.")
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    first = json.load(open(f'gendiff/fixtures/{args.first_file}'))
    second = json.load(open(f'gendiff/fixtures/{args.second_file}'))


if __name__ == "__main__":
    main()
