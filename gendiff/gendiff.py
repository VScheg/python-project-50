from gendiff.parsing import parse, get_text_format
from gendiff.formatters import apply_formatter
from gendiff.diff import get_diff


ERROR_MESSAGE = """
Files are not found.
Check paths and names of the files.
Files should be JSON or YML.
"""


def generate_diff(file_1: str, file_2: str, format_name: str = 'stylish') -> str:
    """
    Return text that describes difference between two given files
    using 3 formatters - stylish, plain or json.
    """
    try:
        data_1, data_2 = open(file_1), open(file_2)
    except FileNotFoundError:
        return ERROR_MESSAGE
    text_format_1, text_format_2 = get_text_format(file_1), get_text_format(file_2)
    dict_1, dict_2 = parse(data_1, text_format_1), parse(data_2, text_format_2)
    data_1.close()
    data_2.close()
    return apply_formatter(get_diff(dict_1, dict_2), format_name)
