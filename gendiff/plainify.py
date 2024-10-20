nonstrings = [True, False, None, '[complex value]']


def need_quote(value):
    return f"{value}" if value in nonstrings else f"'{value}'"


def plain_stringify(dictionary):
    result = []
    for key, val in dictionary.items():
        pattern = f"Property '{key}' was {val['status']}"
        if val['status'] == 'added':
            result.append(f"{pattern} with value: {need_quote(val['value'])}")
        elif val['status'] == 'removed':
            result.append(f"{pattern}")
        else:
            old_val = need_quote(val['old value'])
            new_val = need_quote(val['new value'])
            result.append(f"{pattern}. From {old_val} to {new_val}")
    return '\n'.join(result)
