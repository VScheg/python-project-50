from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.formatters.json import make_json


def apply_formatter(dictionary: dict, format_name: str) -> str:
    """Converts dictionary to formatted string.

    Args:
        dictionary: Dictionary.
        format_name: Name of format of output.

    Returns:
        Formatted string.

    """
    match format_name:
        case 'stylish':
            return make_stylish(dictionary)
        case 'plain':
            return make_plain(dictionary)
        case 'json':
            return make_json(dictionary)
        case _:
            raise ValueError(
                'Wrong format. Format should be strylish, plain or json'
            )
