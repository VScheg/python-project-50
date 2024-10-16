import os
from gendiff import generate_diff, parse


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def get_dict(string):
    return parse(get_fixture_path(string))


def test_stylish_flat():
    expected = read(get_fixture_path('result1.txt'))
    assert generate_diff(get_dict('flat1.json'), get_dict('flat2.json')) == expected
    assert generate_diff(get_dict('flat1.yaml'), get_dict('flat2.yml')) == expected

    expected = read(get_fixture_path('result2.txt'))
    assert generate_diff(get_dict('flat1.json'), get_dict('flat3.json')) == expected


def test_stilysh_nested():    
    expected = read(get_fixture_path('result3.txt'))
    assert generate_diff(get_dict('nested1.json'), get_dict('nested2.json')) == expected
    assert generate_diff(get_dict('nested1.yml'), get_dict('nested2.yml')) == expected
    assert generate_diff(get_dict('nested1.yml'), get_dict('nested2.json')) == expected
