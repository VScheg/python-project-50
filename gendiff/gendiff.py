from .formatters import make_stylish, make_plain
import json


def generate_diff(file1, file2, format_name='stylish'):

    def inner(data1, data2=None):

        if not isinstance(data1, dict) and isinstance(data2, dict):
            return data1, data2
        elif isinstance(data1, dict) and not isinstance(data2, dict):
            return data1, data2
        elif not isinstance(data1, dict) and not isinstance(data2, dict):
            return data1, data2

        keys = data1.keys() | data2.keys()
        result = {}
        for key in keys:
            if key not in data1:
                result[key] = {
                    'status': 'added',
                    'value': inner(data2[key])[0]
                }
            elif key not in data2:
                result[key] = {
                    'status': 'removed',
                    'value': inner(data1[key])[0]
                }
            elif isinstance(data2[key], dict):
                result[key] = inner(data1[key], data2[key])
            elif data1[key] != data2[key]:
                result[key] = {
                    'status': 'updated',
                    'old value': inner(data1[key], data2[key])[0],
                    'new value': inner(data1[key], data2[key])[1]
                }
            else:
                result[key] = {
                    'status': 'no change',
                    'value': data1[key]
                }

        return dict(sorted(result.items(), key=lambda x: x[0]))

    match format_name:
        case 'stylish':
            return make_stylish(inner(file1, file2))
        case 'plain':
            return make_plain(inner(file1, file2))
        case 'json':
            return json.dumps(inner(file1, file2), indent=4)
