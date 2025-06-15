def build_diff(data1, data2):
    diff_result = []
    all_data = sorted(set(data1.keys()) | set(data2.keys()))
    for key in all_data:
        if key not in data2:
            diff_result.append(
                {
                    'key': key,
                    'status': 'deleted',
                    'value': data1[key],
                }
            )
        elif key not in data1:
            diff_result.append(
                {
                    'key': key,
                    'status': 'added',
                    'value': data2[key],
                }
            )
        elif isinstance(data1[key], dict) and isinstance(data2[key], dict):
            nested_diff = build_diff(data1[key], data2[key])
            if nested_diff:
                diff_result.append(
                {
                    'key': key,
                    'status': 'nested',
                    'children': nested_diff,
                }
            )
        elif data1[key] == data2[key]:
            diff_result.append(
                {
                    'key': key,
                    'status': 'unchanged',
                    'value': data1[key],
                }
            )
        else:
            diff_result.append(
                {
                    'key': key,
                    'status': 'changed',
                    'value_old': data1[key],
                    'value_new': data2[key]
                }
            )
    return diff_result

