import json
import yaml


def get_data(data: str, text_format: str) -> dict:
    """Return a dictionary with contents of given JSON or YML file"""
    try:
        if text_format == 'json':
            return json.load(data)
        else:
            return yaml.safe_load(data)
    except ValueError:
        raise ValueError("Wrong format. Files should be JSON or YML.")
