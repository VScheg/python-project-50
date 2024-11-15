import json


def make_json(diff: dict) -> str:
    """Converts diff dictionary into json text."""
    return json.dumps(diff, indent=4)
