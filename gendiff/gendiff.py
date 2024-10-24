from gendiff.parsing import parse
from gendiff.apply_formatter import apply_formatter


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

    return apply_formatter(inner(file1, file2), format_name)
