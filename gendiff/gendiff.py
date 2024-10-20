from .formatters import make_stylish, make_plain


def generate_diff(file1, file2, format_name='stylish'):
    if format_name == 'stylish':
        return make_stylish(file1, file2)
    else:
        return make_plain(file1, file2)
