from gendiff.formatters import make_stylish, make_plain, make_json
from gendiff.parsing import parse


DICT_TO_JSON = {
    'None': 'null',
    'True': 'true',
    'False': 'false',
}


def to_json(string: str) -> str:
    """Convert text into JSON-style text"""
    for key, value in DICT_TO_JSON.items():
        string = string.replace(key, value)
    return string


def generate_diff(file_path1: str, file_path2: str, format_name: str = 'stylish') -> str:
    """
    Return text that describes difference between two given files
    using 3 formatters - stylish, plain or json.
    """
    file1, file2 = parse(file_path1), parse(file_path2)

    def inner(data1, data2):

        keys = data1.keys() | data2.keys()
        result = {}
        for key in keys:
            if key not in data1:
                result[key] = {
                    'status': 'added',
                    'value': data2[key]
                }
            elif key not in data2:
                result[key] = {
                    'status': 'removed',
                    'value': data1[key]
                }
            elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
                result[key] = inner(data1[key], data2[key])
            elif data1[key] != data2[key]:
                result[key] = {
                    'status': 'updated',
                    'old value': data1[key],
                    'new value': data2[key]
                }
            else:
                result[key] = {
                    'status': 'no change',
                    'value': data1[key]
                }

        return dict(sorted(result.items(), key=lambda x: x[0]))

    match format_name:
        case 'stylish':
            return to_json(make_stylish(inner(file1, file2)))
        case 'plain':
            return to_json(make_plain(inner(file1, file2)))
        case 'json':
            return make_json(inner(file1, file2))
