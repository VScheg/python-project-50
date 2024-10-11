import os
from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_generate_diff():
    expected = read(get_fixture_path('result1.txt'))
    assert generate_diff(get_fixture_path('file1.json'), get_fixture_path('file2.json')) == expected
    assert generate_diff(get_fixture_path('file1.yaml'), get_fixture_path('file2.yml')) == expected

    expected = read(get_fixture_path('result2.txt'))
    assert generate_diff(get_fixture_path('file1.json'), get_fixture_path('file3.json')) == expected