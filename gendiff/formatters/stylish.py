def get_indent(depth, replacer=' '):
    return replacer * (depth * 4 - 2)


def get_formatted_value(value, depth=1):
    if value is None:
        return "null"
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        indent = get_indent(depth + 1)
        lines = []
        for key, val in value.items():
            formatted_value = get_formatted_value(val, depth + 1)
            lines.append(f"{indent}  {key}: {formatted_value}")
        return "{{\n{}\n{}}}".format("\n".join(lines), indent[:-2])
    return f"{value}"


def get_diff_formatted_stylish(diff, depth=1):
    indent = get_indent(depth)
    lines = []
    for item in diff:
        key_name = item['key']
        value_old = get_formatted_value(item.get("value_old"), depth)
        value_new = get_formatted_value(item.get("value_new"), depth)
        current_value = get_formatted_value(item.get("value"), depth)
        status = item["status"]
        if status == "unchanged":
            lines.append(f"{indent}  {key_name}: {current_value}")
        elif status == "changed":
            lines.append(f"{indent}- {key_name}: {value_old}")
            lines.append(f"{indent}+ {key_name}: {value_new}")
        elif status == "deleted":
            lines.append(f"{indent}- {key_name}: {current_value}")
        elif status == "added":
            lines.append(f"{indent}+ {key_name}: {current_value}")
        elif status == 'nested':
            children = get_diff_formatted_stylish(
                item.get("children"), depth + 1
            )
            lines.append(f"{indent}  {key_name}: {children}")
    return "{{\n{}\n{}}}".format("\n".join(lines), indent[:-2])
