def get_formatted_value(value):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, dict):
        return '[complex value]'
    if isinstance(value, str):
        return f"'{value}'"
    return str(value)


def get_diff_formatted_plain(diff, parents=None, lines=None):
    if lines is None:
        lines = []

    for item in diff:
        key_name = item['key']
        value_old = get_formatted_value(item.get("value_old"))
        value_new = get_formatted_value(item.get("value_new"))
        current_value = get_formatted_value(item.get("value"))
        status = item["status"]

        parent = f"{parents}.{key_name}" if parents else key_name 

        if status == "added":
            lines.append(f"Property '{parent}' was added with value: {current_value}")
        elif status == "deleted":
            lines.append(f"Property '{parent}' was removed")
        elif status == "changed":
            lines.append(f"Property '{parent}' was updated. From {value_old} to {value_new}")
        elif status == 'nested':
            get_diff_formatted_plain(
                item.get("children"), parent, lines)

    return "\n".join(lines)