import itertools


def make_stylish(value: dict, replacer: str = ' ', spaces_count: int = 2) -> str:
    """Convert diff dictionary into stylish text"""

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        if depth == 0:
            deep_indent_size = depth + spaces_count
            current_indent = ''
        else:
            deep_indent_size = depth + 4
            current_indent = replacer * (depth + 2)

        deep_indent = replacer * deep_indent_size
        lines = []
        for key, val in current_value.items():
            if isinstance(val, dict) and 'status' in val.keys():
                status = val.pop('status')
                if status == 'added':
                    value = val['value']
                    lines.append(f'{deep_indent}+ {key}: {iter_(value, deep_indent_size)}')
                elif status == 'removed':
                    value = val['value']
                    lines.append(f'{deep_indent}- {key}: {iter_(value, deep_indent_size)}')
                elif status == 'no change':
                    value = val['value']
                    lines.append(f'{deep_indent}  {key}: {iter_(value, deep_indent_size)}')
                elif status == 'updated':
                    old_val = val['old value']
                    new_val = val['new value']
                    lines.append(f'{deep_indent}- {key}: {iter_(old_val, deep_indent_size)}')
                    lines.append(f'{deep_indent}+ {key}: {iter_(new_val, deep_indent_size)}')
            else:
                lines.append(f'{deep_indent}  {key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)
