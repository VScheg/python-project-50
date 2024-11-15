import json
import yaml


def get_data(text: str, text_format: str) -> dict:
    """Return a dictionary with contents of given JSON or YML file"""
    match text_format:
        case 'json':
            return json.loads(text)
        case 'yml' | 'yaml':
            return yaml.safe_load(text)

    raise ValueError("Wrong format. Files should be JSON or YML.")
