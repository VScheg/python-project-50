from .stylish import make_stylish


def generate_diff(file1, file2, format_name='stylish'):
    if format_name == 'stylish':
        return make_stylish(file1, file2)
