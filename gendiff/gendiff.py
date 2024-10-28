from gendiff.parsing import parse, get_text_format
from gendiff.formatters import apply_formatter
from gendiff.diff_dict import generate_diff_dict


def generate_diff(file_1: str, file_2: str, format_name: str = 'stylish') -> str:
    """
    Return text that describes difference between two given files
    using 3 formatters - stylish, plain or json.
    """
    data_1, data_2 = open(file_1), open(file_2)
    text_format_1, text_format_2 = get_text_format(file_1), get_text_format(file_2)
    dict_1, dict_2 = parse(data_1, text_format_1), parse(data_2, text_format_2)
    return apply_formatter(generate_diff_dict(dict_1, dict_2), format_name)
