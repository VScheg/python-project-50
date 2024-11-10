import pytest
import os
from gendiff import generate_diff
from gendiff.reading import read


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


@pytest.mark.parametrize(
        "file_name_1,file_name_2,format,expected",
        [
            (get_fixture_path('flat1.json'), get_fixture_path('flat2.json'), 'stylish', read(get_fixture_path('stylish_flat_result1.txt'))),
            (get_fixture_path('flat1.yaml'), get_fixture_path('flat2.yml'), 'stylish', read(get_fixture_path('stylish_flat_result1.txt'))),
            (get_fixture_path('flat1.json'), get_fixture_path('flat3.json'), 'stylish', read(get_fixture_path('stylish_flat_result2.txt')))
    ],
)
def test_stylish_flat(file_name_1, file_name_2, format, expected):
    assert generate_diff(file_name_1, file_name_2, format) == expected


@pytest.mark.parametrize(
        "file_name_1,file_name_2,expected",
        [
            (get_fixture_path('nested1.json'), get_fixture_path('nested2.json'), read(get_fixture_path('stylish_nested_result1.txt'))),
            (get_fixture_path('nested1.yml'), get_fixture_path('nested2.yml'), read(get_fixture_path('stylish_nested_result1.txt'))),
            (get_fixture_path('nested1.yml'), get_fixture_path('nested2.json'), read(get_fixture_path('stylish_nested_result1.txt'))),
            (get_fixture_path('nested1.json'), get_fixture_path('nested3.json'), read(get_fixture_path('stylish_nested_result2.txt')))
    ],
)
def test_stylish_nested(file_name_1, file_name_2, expected):
    assert generate_diff(file_name_1, file_name_2) == expected


@pytest.mark.parametrize(
        "file_name_1,file_name_2,format,expected",
        [
            (get_fixture_path('flat1.json'), get_fixture_path('flat2.json'), 'plain', read(get_fixture_path('plain_flat_result.txt'))),
            (get_fixture_path('flat1.yaml'), get_fixture_path('flat2.yml'), 'plain', read(get_fixture_path('plain_flat_result.txt'))),
    ],
)
def test_plain_flat(file_name_1, file_name_2, format, expected):
    assert generate_diff(file_name_1, file_name_2, format) == expected


@pytest.mark.parametrize(
        "file_name_1,file_name_2,format,expected",
        [
            (get_fixture_path('nested1.json'), get_fixture_path('nested2.json'), 'plain', read(get_fixture_path('plain_nested_result.txt'))),
            (get_fixture_path('nested1.yml'), get_fixture_path('nested2.yml'), 'plain', read(get_fixture_path('plain_nested_result.txt'))),
            (get_fixture_path('nested1.yml'), get_fixture_path('nested2.json'), 'plain', read(get_fixture_path('plain_nested_result.txt'))),
    ],
)
def test_plain_nested(file_name_1, file_name_2, format, expected):
    assert generate_diff(file_name_1, file_name_2, format) == expected


@pytest.mark.parametrize(
        "file_name_1,file_name_2,format,expected",
        [
            (get_fixture_path('nested1.json'), get_fixture_path('nested2.json'), 'json', read(get_fixture_path('json_nested_result.txt'))),
            (get_fixture_path('nested1.yml'), get_fixture_path('nested2.yml'), 'json', read(get_fixture_path('json_nested_result.txt'))),
            (get_fixture_path('nested1.yml'), get_fixture_path('nested2.json'), 'json', read(get_fixture_path('json_nested_result.txt'))),
    ],
)
def test_json_nested(file_name_1, file_name_2, format, expected):
    assert generate_diff(file_name_1, file_name_2, format) == expected
