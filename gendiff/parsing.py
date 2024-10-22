import json
import yaml


DICT_TO_JSON = {
    'None': 'null',
    'True': 'true',
    'False': 'false',
}


def parse(file_path: str) -> dict:
    """Return a dictionary with contents of given JSON or YML file"""
    _, f = file_path.split('.')
    if f == 'json':
        return json.load(open(file_path))
    else:
        return yaml.safe_load(open(file_path))


def to_json(string: str) -> str:
    """Convert text into JSON-style text"""
    for key, value in DICT_TO_JSON.items():
        string = string.replace(key, value)
    return string
