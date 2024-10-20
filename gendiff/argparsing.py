import argparse
from .parsing import parse


def get_arguments():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    arguments = [parse(args.first_file), parse(args.second_file)]
    if args.format:
        arguments.append(args.format)

    return arguments
