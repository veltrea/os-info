@echo off
rem OS情報収集ツールのセットアップスクリプト

rem Pythonが利用可能か確認
python --version > nul 2>&1
if errorlevel 1 (
    echo Python が見つかりません。Python 3.7以上をインストールしてください。
    exit /b 1
)

rem 必要なパッケージをインストール
echo 必要なパッケージをインストールしています...
pip install psutil>=5.9.0 PyYAML>=6.0
if errorlevel 1 (
    echo パッケージのインストールに失敗しました。
    exit /b 1
)

echo セットアップが完了しました。
echo os-info.py を実行してツールを使用できます。