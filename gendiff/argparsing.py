import argparse
from typing import Optional


def get_arguments() -> tuple[str, str, Optional[str]]:
    """
    Get arguments for gendiff program from command line and form documentation.
    """
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument("-f", "--format", help="set format of output")
    args = parser.parse_args()
    if args.format:
        return args.first_file, args.second_file, args.format
    else:
        return args.first_file, args.second_file, None
