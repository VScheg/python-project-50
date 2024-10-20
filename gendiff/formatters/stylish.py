from ..parsing import to_json
from ..stringify import stringify


def make_stylish(file1, file2):
    return to_json(stringify(make_dict(file1, file2)))


def make_dict(file1, file2):

    def inner(data1, data2):
        if not isinstance(data1, dict):
            return data1
        keys = data1.keys() | data2.keys()
        result = {}
        for key in keys:
            if key not in data1:
                result[f'+ {key}'] = inner(data2[key], data2[key])
            elif key not in data2:
                result[f'- {key}'] = inner(data1[key], data1[key])
            elif data1[key] == data2[key] or isinstance(data2[key], dict):
                result[f'  {key}'] = inner(data1[key], data2[key])
            else:
                result[f'- {key}'] = inner(data1[key], data1[key])
                result[f'+ {key}'] = inner(data2[key], data2[key])

        return dict(sorted(result.items(), key=lambda x: x[0][2:]))

    return inner(file1, file2)
