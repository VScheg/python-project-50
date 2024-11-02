from gendiff.formatters import make_stylish, make_plain, make_json


def apply_formatter(dictionary: dict, format_name: str) -> str:
    """Apply formatter to dictionary"""
    match format_name:
        case 'stylish':
            return make_stylish(dictionary)
        case 'plain':
            return make_plain(dictionary)
        case 'json':
            return make_json(dictionary)
        case _:
            return 'Wrong format'
