from typing import Union


NONSTRINGS = [True, False, None, '[complex value]']


def make_plain(dictionary: dict) -> str:
    """Apply plain formatter to diff dictionary"""
    return plainify(flatten_dict(dictionary))


def need_quote(value: Union[str, bool, None]) -> str:
    """Check if value is a string and needs quotes for plain text"""
    return f"{value}" if value in NONSTRINGS else f"'{value}'"


def convert_dict_value(dictionary: dict) -> dict:
    """Shorten dict value in diff dictionary to '[complex value]'"""
    for key in dictionary.keys():
        if 'value' in key and isinstance(dictionary[key], dict):
            dictionary[key] = '[complex value]'
    return dictionary


def plainify(dictionary: dict) -> str:
    """Convert diff dictionary into plain text"""
    for diff in dictionary.values():
        convert_dict_value(diff)
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


def flatten_dict(dictionary: dict, parent_key: str = '') -> dict:
    """
    Flatten nested dictionary so that
    it may only contain dictionaries describing difference
    """
    flattened = {}
    for key, value in dictionary.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        if isinstance(value, dict) and 'status' not in value:
            flattened.update(flatten_dict(value, new_key))
        else:
            flattened[new_key] = value
    return flattened
