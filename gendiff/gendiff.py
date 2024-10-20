from .formatters import make_stylish, make_plain, make_json


def generate_diff(file1, file2, format_name='stylish'):
    match format_name:
        case 'stylish':
            return make_stylish(file1, file2)
        case 'plain':
            return make_plain(file1, file2)
        case 'json':
            return make_json(file1, file2)
