from gendiff.parsing import to_json
from gendiff.plainify import plain_stringify


def make_plain(file1, file2):

    def inner(data1, data2=None):

        if not isinstance(data1, dict) and isinstance(data2, dict):
            return data1, '[complex value]'
        elif isinstance(data1, dict) and not isinstance(data2, dict):
            return '[complex value]', data2
        elif not isinstance(data1, dict) and not isinstance(data2, dict):
            return data1, data2

        keys = data1.keys() | data2.keys()
        result = {}
        for key in keys:
            if key not in data1:
                result[key] = {'status': 'added', 'value': inner(data2[key])[0]}
            elif key not in data2:
                result[key] = {'status': 'removed'}
            elif isinstance(data2[key], dict):
                result[key] = inner(data1[key], data2[key])
            elif data1[key] != data2[key]:
                result[key] = {
                    'status': 'updated',
                    'old value': inner(data1[key], data2[key])[0],
                    'new value': inner(data1[key], data2[key])[1]
                }
        return dict(sorted(result.items(), key=lambda x: x[0]))

    return to_json(plain_stringify(flatten_dict(inner(file1, file2))))


def flatten_dict(dictionary, parent_key='', sep='.'):
    flattened = {}
    for key, value in dictionary.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict) and 'status' not in value:
            flattened.update(flatten_dict(value, new_key, sep=sep))
        else:
            flattened[new_key] = value
    return flattened
