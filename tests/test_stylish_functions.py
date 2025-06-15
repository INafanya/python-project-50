from gendiff.formatters.stylish import (
    get_diff_formatted_stylish,
    get_formatted_value,
    get_indent,
)


def test_indent():
    expected_indent = '      '
    assert get_indent(depth=2) == expected_indent
    

def test_get_formatted_value():
    expected_none = 'null'
    expected_bool = 'true'
    expected_str = 'Value 1'
    dict_to_format = {"gro": {
                "baz": "bas",
            }}
    expected_dict = '{\n        gro: {\n            baz: bas\n        }\n    }'
    assert get_formatted_value(None, depth=1) == expected_none
    assert get_formatted_value(True) == expected_bool
    assert get_formatted_value('Value 1') == expected_str
    assert get_formatted_value(dict_to_format) == expected_dict
    
    
def test_get_diff_formatted_stylish():
    unchanged = [{'key': 'setting1',
                  'status': 'unchanged',
                  'value': 'Value 1'}]
    changed = [{'key': 'wow',
                'status': 'changed',
                'value_old': '',
                'value_new': 'so much'}]
    deleted = [{'key': 'setting2',
                'status': 'deleted',
                'value': 200}]
    added = [{'key': 'follow',
              'status': 'added',
              'value': False}]
    nested = [{'key': 'doge',
               'status': 'nested',
               'children': [
                   {'key': 'one',
                    'status': 'unchanged',
                             'value': '1'},
                    {'key': 'two',
                     'status': 'unchanged',
                     'value': '2'}
                    ]
               }
              ]
    
    expected_unchanged = '{\n    setting1: Value 1\n}'
    expected_changed = '{\n  - wow: \n  + wow: so much\n}'
    expected_deleted = '{\n  - setting2: 200\n}'
    expected_added = '{\n  + follow: false\n}'
    expected_nested = '{\n    doge: {\n        one: 1\n        two: 2\n    }\n}'
    
    assert get_diff_formatted_stylish(unchanged) == expected_unchanged
    assert get_diff_formatted_stylish(changed) == expected_changed
    assert get_diff_formatted_stylish(deleted) == expected_deleted
    assert get_diff_formatted_stylish(added) == expected_added
    assert get_diff_formatted_stylish(nested) == expected_nested
