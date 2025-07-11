# OS情報収集ツール

システム情報（OS、ネットワーク、ユーザー）を収集するPythonツールです。

## 機能

- システム情報の収集（OS名、バージョン、ビルド番号など）
- ネットワーク情報の収集（ホスト名、インターフェース、IPアドレスなど）
- ユーザー情報の収集（現在のユーザー、システムユーザー一覧）
- 複数の出力形式対応（JSON、CSV、YAML）

## 使用方法

```bash
# 基本的な使用方法（JSON形式で出力）
python os-info.py

# CSV形式で出力
python os-info.py --format csv

# YAML形式でファイルに出力
python os-info.py --format yaml --output info.yaml

# 整形されたJSON形式で出力
python os-info.py --pretty

# 最小限の情報のみ出力
python os-info.py --minimal
```

## オプション

- `--format {json,csv,yaml}` : 出力形式を指定（デフォルト: json）
- `--output FILE` : 出力ファイルを指定（デフォルト: 標準出力）
- `--pretty` : 整形された出力（JSON/YAML形式の場合）
- `--minimal` : 最小限の情報のみ出力
- `--no-timestamps` : タイムスタンプを含めない
- `--utf8` : UTF-8エンコーディングを強制
- `--quiet` : 警告メッセージを抑制

## インストール

1. Python 3.7以上をインストール
2. 必要なパッケージをインストール：
   ```bash
   pip install -r requirements.txt
   ```
   または
   ```bash
   pip install psutil>=5.9.0 PyYAML>=6.0
   ```

## ライセンス

MIT