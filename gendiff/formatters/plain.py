import json
from typing import Any


def stringify(value: Any) -> str:
    """Check type of value to apply certain style for plain text"""
    if isinstance(value, dict):
        return "[complex value]"

    elif isinstance(value, int | bool | None):
        return json.dumps(value)

    return f"'{value}'"


def make_plain(diff: dict, parent_key: str = '') -> str:
    """
    Converts diff dictionary into plain text.

    Args:
        diff: Diff dictionary.
        parent_key: String that keeps names of parent keys in dictionary.

    Returns:
        Plain text that describes difference between two files.
    """
    result = []
    for key, value in diff.items():
        new_key = f"{parent_key}.{key}" if parent_key else key
        status = value.get('status')
        pattern = f"Property '{new_key}' was {status}"
        if status == 'added':
            result.append(
                f"{pattern} with value: {stringify(value.get('value'))}"
            )
        elif status == 'removed':
            result.append(f"{pattern}")

        elif status == 'updated':
            old_value = stringify(value.get('old value'))
            new_value = stringify(value.get('new value'))
            result.append(f"{pattern}. From {old_value} to {new_value}")

        elif status == 'inserted':
            result.append(make_plain(value.get('value'), new_key))

    return '\n'.join(result)
