# ベースは Python 3.11 の slim 版
FROM python:3.11-slim

# 必要なパッケージをインストール(今回は何もなし)
RUN apt-get update && apt-get install -y git

# Python のパッケージインストール
RUN pip install sqlfluff
