from gendiff.parsing import to_json


NONSTRINGS = [True, False, None, '[complex value]']


def make_plain(dictionary):
    return to_json(plainify(flatten_dict(dictionary)))


def need_quote(value):
    return f"{value}" if value in NONSTRINGS else f"'{value}'"


def plainify(dictionary):
    for value in dictionary.values():
        for key in value.keys():
            if 'value' in key and isinstance(value[key], dict):
                value[key] = '[complex value]'
    result = []
    for key, val in dictionary.items():
        pattern = f"Property '{key}' was {val['status']}"
        if val['status'] == 'added':
            value = need_quote(val['value'])
            result.append(f"{pattern} with value: {value}")
        elif val['status'] == 'removed':
            result.append(f"{pattern}")
        elif val['status'] == 'updated':
            old_val = need_quote(val['old value'])
            new_val = need_quote(val['new value'])
            result.append(f"{pattern}. From {old_val} to {new_val}")
    return '\n'.join(result)


def flatten_dict(dictionary, parent_key='', sep='.'):
    flattened = {}
    for key, value in dictionary.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict) and 'status' not in value:
            flattened.update(flatten_dict(value, new_key, sep=sep))
        else:
            flattened[new_key] = value
    return flattened
