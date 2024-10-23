import json


def make_json(dictionary: dict) -> str:
    return json.dumps(dictionary, indent=4)
