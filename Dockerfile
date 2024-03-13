FROM python:3.9

WORKDIR /app

COPY . /app

# PYTHONPATHに/appを追加
# Pythonファイルでのモジュール検索が容易になる
ENV PYTHONPATH "${PYTHONPATH}:/app"

# ホストマシンのポート8000を、docker内のポート8000に接続する
# このコマンドを実行することで、ホストマシンからdocker内のポート8000にアクセスできるようになる
# EXPOSE 8000


RUN pip install -r requirements.txt

