import json
import yaml


def parse(data: str, text_format: str) -> dict:
    """Return a dictionary with contents of given JSON or YML file"""
    if text_format == 'json':
        return json.load(data)
    else:
        return yaml.safe_load(data)


def get_text_format(file_path: str) -> str:
    _, f = file_path.split('.')
    return f
