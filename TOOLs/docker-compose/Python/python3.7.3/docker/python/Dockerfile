FROM python:3.7.3

USER root

# ソースを置くディレクトリを変数として格納
ARG project_dir=/setup/

# 必要なファイルをローカルからコンテナにコピー
ADD requirements.txt $project_dir

# requirements.txtに記載されたパッケージをインストール
WORKDIR $project_dir
RUN rm /bin/sh && ln -s /bin/bash /bin/sh
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
