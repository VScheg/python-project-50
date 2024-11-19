from gendiff.reading import get_text, get_text_format
from gendiff.parsing import get_data
from gendiff.formatters.apply_formatter import apply_formatter
from gendiff.diff import get_diff


def generate_diff(file_1: str, file_2: str, format_name: str = 'stylish') -> str:
    """
    Generates difference between two files.

    Args:
        file_1: File path of first file.
        file_2: File path of second file.
        format_name: Name of format of output.

    Returns:
        Text that describes difference between two files in chosen format - stylish, plain or json.
    """
    data_1 = get_data(get_text(file_1), get_text_format(file_1))
    data_2 = get_data(get_text(file_2), get_text_format(file_2))
    return apply_formatter(get_diff(data_1, data_2), format_name)
