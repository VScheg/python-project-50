from gendiff.formatters.stylish import make_stylish
from gendiff.formatters.plain import make_plain
from gendiff.formatters.json import make_json


def apply_formatter(diff: dict, format_name: str) -> str:
    """Converts diff dictionary to formatted string.

    Args:
        diff: diff dictionary.
        format_name: Name of format of output.

    Returns:
        Formatted string.

    """
    match format_name:
        case 'stylish':
            return make_stylish(diff)
        case 'plain':
            return make_plain(diff)
        case 'json':
            return make_json(diff)
        case _:
            raise ValueError(
                'Wrong format. Format should be strylish, plain or json'
            )
