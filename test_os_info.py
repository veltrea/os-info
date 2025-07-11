#!/usr/bin/env python3

import os
import json
import csv
import yaml
import subprocess
import tempfile

def run_os_info(args):
    cmd = ['python', 'os-info.py'] + args
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout, result.stderr, result.returncode

def validate_json(output):
    try:
        data = json.loads(output)
        assert isinstance(data, dict)
        assert 'system' in data
        assert 'network' in data
        assert 'users' in data
        return True
    except:
        return False

def validate_csv(output):
    try:
        reader = csv.reader(output.splitlines())
        headers = next(reader)
        assert headers == ['Key', 'Value']
        assert sum(1 for _ in reader) > 0
        return True
    except:
        return False

def validate_yaml(output):
    try:
        data = yaml.safe_load(output)
        assert isinstance(data, dict)
        assert 'system' in data
        assert 'network' in data
        assert 'users' in data
        return True
    except:
        return False

def test_default_output():
    output, error, code = run_os_info([])
    assert code == 0
    assert validate_json(output)

def test_format_options():
    # JSON形式
    output, _, code = run_os_info(['--format', 'json'])
    assert code == 0
    assert validate_json(output)

    # CSV形式
    output, _, code = run_os_info(['--format', 'csv'])
    assert code == 0
    assert validate_csv(output)

    # YAML形式
    output, _, code = run_os_info(['--format', 'yaml'])
    assert code == 0
    assert validate_yaml(output)

def test_output_file():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        output, _, code = run_os_info(['--output', tmp.name])
        assert code == 0
        with open(tmp.name) as f:
            content = f.read()
        assert validate_json(content)
        os.unlink(tmp.name)

def test_pretty_option():
    output, _, code = run_os_info(['--pretty'])
    assert code == 0
    assert validate_json(output)
    assert '\n' in output

def test_minimal_option():
    output, _, code = run_os_info(['--minimal'])
    assert code == 0
    data = json.loads(output)
    assert len(data['system'].keys()) == 2
    assert len(data['network'].keys()) == 1
    assert len(data['users'].keys()) == 1

def test_no_timestamps():
    output, _, code = run_os_info(['--no-timestamps'])
    assert code == 0
    data = json.loads(output)
    assert 'install_date' not in data['system']
    assert 'last_boot_time' not in data['system']

def test_utf8_option():
    output, _, code = run_os_info(['--utf8'])
    assert code == 0
    assert validate_json(output)

def test_quiet_option():
    # 正常系
    output, error, code = run_os_info(['--quiet'])
    assert code == 0
    assert not error

    # エラー系（存在しない出力ファイル）
    output, error, code = run_os_info(['--quiet', '--output', '/path/to/nonexistent/dir/file'])
    assert code == 1
    assert not error  # エラーメッセージが抑制されていることを確認