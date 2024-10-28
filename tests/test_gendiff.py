import os
from gendiff import generate_diff


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_stylish_flat():
    expected = read(get_fixture_path('stylish_flat_result1.txt'))
    assert generate_diff(get_fixture_path('flat1.json'), get_fixture_path('flat2.json')) == expected
    assert generate_diff(get_fixture_path('flat1.yaml'), get_fixture_path('flat2.yml')) == expected

    expected = read(get_fixture_path('stylish_flat_result2.txt'))
    assert generate_diff(get_fixture_path('flat1.json'), get_fixture_path('flat3.json'), 'stylish') == expected


def test_stylish_nested():
    expected = read(get_fixture_path('stylish_nested_result1.txt'))
    assert generate_diff(get_fixture_path('nested1.json'), get_fixture_path('nested2.json')) == expected
    assert generate_diff(get_fixture_path('nested1.yml'), get_fixture_path('nested2.yml')) == expected
    assert generate_diff(get_fixture_path('nested1.yml'), get_fixture_path('nested2.json')) == expected

    expected = read(get_fixture_path('stylish_nested_result2.txt'))
    assert generate_diff(get_fixture_path('nested1.json'), get_fixture_path('nested3.json')) == expected


def test_plain_flat():
    expected = read(get_fixture_path('plain_flat_result.txt'))
    assert generate_diff(get_fixture_path('flat1.json'), get_fixture_path('flat2.json'), 'plain') == expected
    assert generate_diff(get_fixture_path('flat1.yaml'), get_fixture_path('flat2.yml'), 'plain') == expected


def test_plain_nested():
    expected = read(get_fixture_path('plain_nested_result.txt'))
    assert generate_diff(get_fixture_path('nested1.json'), get_fixture_path('nested2.json'), 'plain') == expected
    assert generate_diff(get_fixture_path('nested1.yml'), get_fixture_path('nested2.yml'), 'plain') == expected
    assert generate_diff(get_fixture_path('nested1.yml'), get_fixture_path('nested2.json'), 'plain') == expected


def test_json_nested():
    expected = read(get_fixture_path('json_nested_result.txt'))
    assert generate_diff(get_fixture_path('nested1.json'), get_fixture_path('nested2.json'), 'json') == expected
    assert generate_diff(get_fixture_path('nested1.yml'), get_fixture_path('nested2.yml'), 'json') == expected
    assert generate_diff(get_fixture_path('nested1.yml'), get_fixture_path('nested2.json'), 'json') == expected
