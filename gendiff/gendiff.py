from gendiff.parsing import parse
from gendiff.apply_formatter import apply_formatter
from gendiff.diff_dict import generate_diff_dict


def generate_diff(file_path1: str, file_path2: str, format_name: str = 'stylish') -> str:
    """
    Return text that describes difference between two given files
    using 3 formatters - stylish, plain or json.
    """
    file1, file2 = parse(file_path1), parse(file_path2)
    return apply_formatter(generate_diff_dict(file1, file2), format_name)
