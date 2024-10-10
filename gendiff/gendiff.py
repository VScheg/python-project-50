import itertools
import json


def generate_diff(file_path1, file_path2):
    dict1 = json.load(open(file_path1))
    dict2 = json.load(open(file_path2))
    sorted_dict1 = dict(sorted(dict1.items()))
    sorted_dict2 = dict(sorted(dict2.items()))
    lines = []
    for k1, v1 in sorted_dict1.items():
        if k1 in sorted_dict2 and sorted_dict2[k1] == v1:
            lines.append(' ' * 4 + f'{k1}: {v1}')
        elif k1 not in sorted_dict2.keys():
            lines.append(' ' * 2 + f'- {k1}: {v1}')
        else:
            lines.append(' ' * 2 + f'- {k1}: {v1}')
            lines.append(' ' * 2 + f'+ {k1}: {sorted_dict2[k1]}')
    for k2, v2 in sorted_dict2.items():
        if k2 not in sorted_dict1.keys():
            lines.append(' ' * 2 + f'+ {k2}: {v2}')

    result = itertools.chain('{', lines, '}')
    return '\n'.join(result).lower()
