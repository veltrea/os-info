#!/usr/bin/env python3

import argparse
import sys
from os_info.collector import collect_all
from os_info.formatter import format_output

def main():
    parser = argparse.ArgumentParser(description='システム情報収集ツール')
    parser.add_argument('--format', choices=['json', 'csv', 'yaml'], default='json',
                        help='出力形式を指定（デフォルト: json）')
    parser.add_argument('--output', type=str, help='出力ファイルを指定（デフォルト: 標準出力）')
    parser.add_argument('--pretty', action='store_true', help='整形された出力（JSON/YAML形式の場合）')
    parser.add_argument('--minimal', action='store_true', help='最小限の情報のみ出力')
    parser.add_argument('--no-timestamps', action='store_true', help='タイムスタンプを含めない')
    parser.add_argument('--utf8', action='store_true', help='UTF-8エンコーディングを強制')
    parser.add_argument('--quiet', action='store_true', help='警告メッセージを抑制')

    args = parser.parse_args()

    try:
        data = collect_all(minimal=args.minimal, no_timestamps=args.no_timestamps)
        output = format_output(data, args.format, pretty=args.pretty)

        if args.output:
            encoding = 'utf-8' if args.utf8 else None
            with open(args.output, 'w', encoding=encoding) as f:
                f.write(output)
        else:
            if args.utf8:
                sys.stdout.reconfigure(encoding='utf-8')
            print(output)

    except Exception as e:
        if not args.quiet:
            print(f'エラー: {str(e)}', file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()