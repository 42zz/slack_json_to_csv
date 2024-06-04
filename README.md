# Slack JSON to CSV Converter

このプロジェクトは、Slackのエクスポートデータ（JSON形式）をチャンネルごとにまとめてCSVファイルに変換するPythonスクリプトです。Dockerを使用して仮想環境内でスクリプトを実行します。

## 依存関係

このプロジェクトは以下のPythonライブラリに依存しています：

- pandas

これらの依存関係は、`requirements.txt`にリストされています。

## 使用方法

1. Dockerイメージをビルドします。
```sh
docker build -t slack-to-csv .
```
2. コンテナを実行します。
```sh
docker run --rm -v $(pwd):/app -v $(pwd)/slack_export:/app/slack_export -v $(pwd)/csv_output:/app/csv_output slack-to-csv
```
3. 生成されたCSVファイルはcsv_outputディレクトリに保存されます。
