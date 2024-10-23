import json
import yaml


def parse(file_path: str) -> dict:
    """Return a dictionary with contents of given JSON or YML file"""
    _, f = file_path.split('.')
    if f == 'json':
        return json.load(open(file_path))
    else:
        return yaml.safe_load(open(file_path))
