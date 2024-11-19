import itertools
import json
from typing import Any


DIFF_SYMBOLS = {
    'added': '+ ',
    'removed': '- ',
    'no change': '  ',
}
REPLACER = ' '
SPACES_COUNT = 2


def convert_to_json(data: Any) -> str:
    """Replace Boolean and NoneType values with JSON equivalent."""
    if isinstance(data, bool | None):
        return json.dumps(data)
    return str(data)


def get_indent(depth: int) -> tuple[int, str]:
    """Returns size of deep indentation and deep indentation."""
    deep_indent_size = depth + SPACES_COUNT * 2
    deep_indent = REPLACER * deep_indent_size
    return deep_indent_size, deep_indent


def make_stylish(diff: dict) -> str:
    """
    Converts diff dictionary into stylish text.

    Args:
        diff: Diff dictionary.

    Returns:
        Stylish text that describes difference between two files.
    """
    return iter_diff(diff, -SPACES_COUNT)


def iter_diff(diff: dict, depth: int) -> str:
    """Converts diff dictionary into stylish string with diff symbols."""
    deep_indent_size, deep_indent = get_indent(depth)

    lines = []
    for key, value in diff.items():
        status = value.get('status')
        if status in DIFF_SYMBOLS:
            lines.append(f"{deep_indent}{DIFF_SYMBOLS.get(status)}{key}: {iter_value(value.get('value'), deep_indent_size)}")
        elif status == 'updated':
            lines.append(f"{deep_indent}{DIFF_SYMBOLS.get('removed')}{key}: {iter_value(value.get('old value'), deep_indent_size)}")
            lines.append(f"{deep_indent}{DIFF_SYMBOLS.get('added')}{key}: {iter_value(value.get('new value'), deep_indent_size)}")
        elif status == 'inserted':
            lines.append(f"{deep_indent}  {key}: {iter_diff(value.get('value'), deep_indent_size)}")

    current_indent = REPLACER * (depth + SPACES_COUNT)
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)


def iter_value(value: Any, depth: int) -> str:
    """Converts values of diff dictionary into stylish string."""
    if not isinstance(value, dict):
        return convert_to_json(value)

    deep_indent_size, deep_indent = get_indent(depth)

    lines = []
    for key, value in value.items():
        lines.append(f"{deep_indent}  {key}: {iter_value(value, deep_indent_size)}")

    current_indent = REPLACER * (depth + SPACES_COUNT)
    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)
