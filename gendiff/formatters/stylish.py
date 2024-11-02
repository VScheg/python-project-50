import itertools
import json


MARKERS = {
    'added': '+ ',
    'removed': '- ',
    'no change': '  ',
    'inserted': '  '
}
REPLACER = ' '
SPACES_COUNT = 2


def convert_to_json(data: dict) -> dict:
    """Replace Boolean and NoneType values with JSON equivalent"""
    if isinstance(data, bool | None):
        return json.dumps(data)
    elif isinstance(data, dict):
        for key, val in data.items():
            data[key] = convert_to_json(val)
        return data
    else:
        return data


def make_stylish(value: dict, replacer: str = REPLACER, spaces_count: int = SPACES_COUNT) -> str:
    """Convert diff dictionary into stylish text"""
    value = convert_to_json(value)

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        if depth == 0:
            deep_indent_size = depth + spaces_count
            current_indent = ''
        else:
            deep_indent_size = depth + (spaces_count * 2)
            current_indent = replacer * (depth + spaces_count)
        deep_indent = replacer * deep_indent_size

        lines = []
        for key, val in current_value.items():

            def make_line(status, value):
                return f"{deep_indent}{MARKERS[status]}{key}: {iter_(value, deep_indent_size)}"

            status = val['status']
            if status in MARKERS:
                lines.append(make_line(status, val['value']))
            elif status == 'updated':
                lines.append(make_line('removed', val['old value']))
                lines.append(make_line('added', val['new value']))

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)
