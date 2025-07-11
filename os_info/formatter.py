#!/usr/bin/env python3

import json
import csv
import yaml
from io import StringIO

def to_json(data, pretty=False):
    if pretty:
        return json.dumps(data, indent=2, ensure_ascii=False)
    return json.dumps(data)

def to_csv(data):
    output = StringIO()
    writer = csv.writer(output)
    
    def flatten_dict(d, prefix=''):
        items = []
        for k, v in d.items():
            new_key = f'{prefix}{k}' if prefix else k
            if isinstance(v, dict):
                items.extend(flatten_dict(v, f'{new_key}.'))
            elif isinstance(v, list):
                for i, item in enumerate(v):
                    if isinstance(item, dict):
                        items.extend(flatten_dict(item, f'{new_key}[{i}].'))
                    else:
                        items.append((f'{new_key}[{i}]', str(item)))
            else:
                items.append((new_key, str(v)))
        return items
    
    flattened = flatten_dict(data)
    writer.writerow(['Key', 'Value'])
    writer.writerows(flattened)
    
    return output.getvalue()

def to_yaml(data):
    return yaml.dump(data, allow_unicode=True)

def format_output(data, format_type, pretty=False):
    formats = {
        'json': lambda: to_json(data, pretty),
        'csv': lambda: to_csv(data),
        'yaml': lambda: to_yaml(data)
    }
    
    if format_type not in formats:
        raise ValueError(f'未対応の出力形式: {format_type}')
    
    return formats[format_type]()