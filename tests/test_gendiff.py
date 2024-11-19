import pytest
import os
from gendiff import generate_diff
from gendiff.reading import get_text


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


@pytest.mark.parametrize(
    "file_name_1,file_name_2,format,expected", [
        (get_fixture_path('flat1.json'), get_fixture_path('flat2.json'), 'stylish', get_text(get_fixture_path('stylish_flat_result1'))),
        (get_fixture_path('flat1.yaml'), get_fixture_path('flat2.yml'), 'stylish', get_text(get_fixture_path('stylish_flat_result1'))),
        (get_fixture_path('flat1.json'), get_fixture_path('flat3.json'), 'stylish', get_text(get_fixture_path('stylish_flat_result2'))),
        (get_fixture_path('nested1.json'), get_fixture_path('nested2.json'), 'stylish', get_text(get_fixture_path('stylish_nested_result1'))),
        (get_fixture_path('nested1.yml'), get_fixture_path('nested2.yml'), 'stylish', get_text(get_fixture_path('stylish_nested_result1'))),
        (get_fixture_path('nested1.yml'), get_fixture_path('nested2.json'), 'stylish', get_text(get_fixture_path('stylish_nested_result1'))),
        (get_fixture_path('nested1.json'), get_fixture_path('nested3.json'), 'stylish', get_text(get_fixture_path('stylish_nested_result2'))),
        (get_fixture_path('flat1.json'), get_fixture_path('flat2.json'), 'plain', get_text(get_fixture_path('plain_flat_result'))),
        (get_fixture_path('flat1.yaml'), get_fixture_path('flat2.yml'), 'plain', get_text(get_fixture_path('plain_flat_result'))),
        (get_fixture_path('nested1.json'), get_fixture_path('nested2.json'), 'plain', get_text(get_fixture_path('plain_nested_result'))),
        (get_fixture_path('nested1.yml'), get_fixture_path('nested2.yml'), 'plain', get_text(get_fixture_path('plain_nested_result'))),
        (get_fixture_path('nested1.yml'), get_fixture_path('nested2.json'), 'plain', get_text(get_fixture_path('plain_nested_result'))),
        (get_fixture_path('nested1.json'), get_fixture_path('nested2.json'), 'json', get_text(get_fixture_path('json_nested_result.json'))),
        (get_fixture_path('nested1.yml'), get_fixture_path('nested2.yml'), 'json', get_text(get_fixture_path('json_nested_result.json'))),
        (get_fixture_path('nested1.yml'), get_fixture_path('nested2.json'), 'json', get_text(get_fixture_path('json_nested_result.json')))
    ],
)
def test_generate_diff(file_name_1, file_name_2, format, expected):
    assert generate_diff(file_name_1, file_name_2, format) == expected
