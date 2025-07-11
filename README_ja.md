# OS情報収集ツール

システム情報（OS、ネットワーク、ユーザー）を収集するPythonツールです。

## 機能

- システム情報の収集
  - OS名
  - バージョン
  - ビルド番号
  - アーキテクチャ
  - インストール日時
  - 最終起動時刻

- ネットワーク情報の収集
  - ホスト名
  - ネットワークインターフェース
    - インターフェース名
    - IPアドレス
    - MACアドレス

- ユーザー情報の収集
  - 現在のユーザー
  - システムユーザー一覧

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

## インストール方法

### 前提条件
- Python 3.7以上

### セットアップ手順

1. リポジトリをクローン：
   ```bash
   git clone https://github.com/veltrea/os-info.git
   cd os-info
   ```

2. 必要なパッケージをインストール：
   ```bash
   pip install -r requirements.txt
   ```
   または
   ```bash
   pip install psutil>=5.9.0 PyYAML>=6.0
   ```

### Windowsユーザー向け

`setup.bat`を実行することで、必要なパッケージが自動的にインストールされます：
```cmd
.\setup.bat
```

## ライセンス

MIT