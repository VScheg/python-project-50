import json


def apply_type(value: str | bool | None) -> str:
    """Check type of value to apply certain style for plain text"""
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, int | bool | None):
        return f"{json.dumps(value)}"
    else:
        return f"'{value}'"


def make_plain(dictionary: dict, parent_key: str = '') -> str:
    """Convert diff dictionary into plain text"""
    result = []
    for key, val in dictionary.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        pattern = f"Property '{new_key}' was {val['status']}"
        if val['status'] == 'added':
            value = apply_type(val['value'])
            result.append(f"{pattern} with value: {value}")
        elif val['status'] == 'removed':
            result.append(f"{pattern}")
        elif val['status'] == 'updated':
            old_val = apply_type(val['old value'])
            new_val = apply_type(val['new value'])
            result.append(f"{pattern}. From {old_val} to {new_val}")
        elif val['status'] == 'inserted':
            result.append(make_plain(val['value'], new_key))

    return '\n'.join(result)
