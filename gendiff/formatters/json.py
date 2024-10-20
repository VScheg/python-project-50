import json
from .stylish import make_dict


def make_json(file1, file2):
    return json.dumps(make_dict(file1, file2), indent=4)
