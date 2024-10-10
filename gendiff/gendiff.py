import itertools
import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    keys = data1.keys() | data2.keys()
    result = {}
    for key in keys:
        if key not in data1:
            result[f'+ {key}'] = data2[key]
        elif key not in data2:
            result[f'- {key}'] = data1[key]
        elif data1[key] == data2[key]:
            result[f'  {key}'] = data1[key]
        else:
            result[f'- {key}'] = data1[key]
            result[f'+ {key}'] = data2[key]
    result = dict(sorted(result.items(), key=lambda x: x[0][2:]))
    lines = []
    for k, v in result.items():
        lines.append(f'  {k}: {v}')
    result = itertools.chain('{', lines, '}')
    return '\n'.join(result).lower()
