import argparse


def get_arguments() -> tuple[str, str, str]:
    """
    Get arguments for gendiff program from command line and form documentation.
    """
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument(
        "-f", "--format",
        help="set format of output - stylish, plain or json",
        default="stylish"
    )
    return parser.parse_args()
