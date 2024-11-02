def get_diff(data_1: dict | str | bool | None, data_2: dict = {}) -> dict:
    """Return data that describes difference between two dictionaries"""
    if not isinstance(data_1, dict):
        return data_1
    if not data_2:
        data_2 = data_1.copy()

    keys = data_1.keys() | data_2.keys()
    result = {}
    for key in sorted(keys):
        if key not in data_1:
            result[key] = {
                'status': 'added',
                'value': get_diff(data_2[key])
            }
        elif key not in data_2:
            result[key] = {
                'status': 'removed',
                'value': get_diff(data_1[key])
            }
        elif isinstance(data_1[key], dict) and isinstance(data_2[key], dict):
            result[key] = {
                'status': 'inserted',
                'value': get_diff(data_1[key], data_2[key])
            }
        elif data_1[key] != data_2[key]:
            result[key] = {
                'status': 'updated',
                'old value': get_diff(data_1[key]),
                'new value': get_diff(data_2[key])
            }
        else:
            result[key] = {
                'status': 'no change',
                'value': data_1[key]
            }
    return result
