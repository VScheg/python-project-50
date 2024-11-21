def get_diff(data_1: dict, data_2: dict) -> dict:
    """
    Generates difference between two dictionaries.

    Args:
        data_1: First dictionary.
        data_2: Second dictionary.

    Returns:
        Data that describes difference between two dictionaries.
    """
    sorted_keys = sorted(data_1.keys() | data_2.keys())
    result = {}
    for key in sorted_keys:
        if key not in data_1:
            result[key] = {
                'status': 'added',
                'value': data_2.get(key)
            }
        elif key not in data_2:
            result[key] = {
                'status': 'removed',
                'value': data_1.get(key)
            }
        elif (
            isinstance(data_1.get(key), dict)
            and isinstance(data_2.get(key), dict)
        ):
            result[key] = {
                'status': 'inserted',
                'value': get_diff(data_1.get(key), data_2.get(key))
            }
        elif data_1.get(key) == data_2.get(key):
            result[key] = {
                'status': 'no change',
                'value': data_1.get(key)
            }
        else:
            result[key] = {
                'status': 'updated',
                'old value': data_1.get(key),
                'new value': data_2.get(key)
            }
    return result
