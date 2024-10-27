def generate_diff_dict(data_1: dict, data_2: dict) -> dict:
    """Return data that describes difference between two dictionaries"""
    keys = data_1.keys() | data_2.keys()
    result = {}
    for key in keys:
        if key not in data_1:
            result[key] = {
                'status': 'added',
                'value': data_2[key]
            }
        elif key not in data_2:
            result[key] = {
                'status': 'removed',
                'value': data_1[key]
            }
        elif isinstance(data_1[key], dict) and isinstance(data_2[key], dict):
            result[key] = generate_diff_dict(data_1[key], data_2[key])
        elif data_1[key] != data_2[key]:
            result[key] = {
                'status': 'updated',
                'old value': data_1[key],
                'new value': data_2[key]
            }
        else:
            result[key] = {
                'status': 'no change',
                'value': data_1[key]
            }

    return dict(sorted(result.items(), key=lambda x: x[0]))
