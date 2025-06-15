import json


def get_diff_formatted_json(diff):
    return json.dumps(diff, indent=4)
