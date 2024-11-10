import itertools
import json


DIFF_SYMBOLS = {
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
    return str(data)


def get_indent(depth):
    deep_indent_size = depth + SPACES_COUNT * 2
    deep_indent = REPLACER * deep_indent_size
    return deep_indent_size, deep_indent


def make_stylish(value: dict) -> str:
    """Convert diff dictionary into stylish text"""

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return convert_to_json(current_value)

        def iter_dict(current_value, depth):
            deep_indent_size, deep_indent = get_indent(depth)
            return f"{deep_indent}  {key}: {iter_(current_value, deep_indent_size)}"

        deep_indent_size, deep_indent = get_indent(depth)
        lines = []
        for key, val in current_value.items():

            if isinstance(val, dict) and 'status' in val.keys():
                status = val.get('status')
                if status in DIFF_SYMBOLS:
                    lines.append(f"{deep_indent}{DIFF_SYMBOLS[status]}{key}: {iter_(val['value'], deep_indent_size)}")
                elif status == 'updated':
                    lines.append(f"{deep_indent}{DIFF_SYMBOLS['removed']}{key}: {iter_(val['old value'], deep_indent_size)}")
                    lines.append(f"{deep_indent}{DIFF_SYMBOLS['added']}{key}: {iter_(val['new value'], deep_indent_size)}")
            else:
                lines.append(iter_dict(val, depth))

        current_indent = REPLACER * (depth + SPACES_COUNT)
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, -2)
