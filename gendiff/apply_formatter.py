from gendiff.formatters import make_stylish, make_plain, make_json


DICT_TO_JSON = {
    'None': 'null',
    'True': 'true',
    'False': 'false',
}


def to_json(string: str) -> str:
    """Convert text into JSON-style text"""
    for key, val in DICT_TO_JSON.items():
        string = string.replace(key, val)
    return string


def apply_formatter(dictionary: dict, format_name: str) -> str:
    """Apply formatter to dictionary"""
    match format_name:
        case 'stylish':
            return to_json(make_stylish(dictionary))
        case 'plain':
            return to_json(make_plain(dictionary))
        case 'json':
            return make_json(dictionary)
