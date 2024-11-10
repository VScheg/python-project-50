from gendiff.reading import read, get_text_format
from gendiff.parsing import get_data
from gendiff.formatters.apply_formatter import apply_formatter
from gendiff.diff import get_diff


def generate_diff(file_1: str, file_2: str, format_name: str = 'stylish') -> str:
    """
    Return text that describes difference between two given files
    using 3 formatters - stylish, plain or json.
    """
    dict_1 = get_data(read(file_1), get_text_format(file_1))
    dict_2 = get_data(read(file_2), get_text_format(file_2))
    return apply_formatter(get_diff(dict_1, dict_2), format_name)
