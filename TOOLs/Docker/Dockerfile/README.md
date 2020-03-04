# Dockerfile

- [Basic commands](#basic-commands)

## Basic commands

|説明|コマンド|使用例|
|---|---|---|
|元となるイメージ|FROM|`FROM name/web:ver1.0`|
|作成者|MAINTAINER|`MAINTAINER name`|
|環境変数|ENV|`ENV KEY=VALUE`|
|指定のコマンドの実行|RUN|`RUN yum -y install httpd`|
|イメージにファイル追加|ADD|`ADD index.html /var/www/html/index.html`|
|ポート番号を指定|EXPOSE|`EXPOSE 3306`|
|コンテナ起動時に実行するコマンド|CMD|`CMD ["service","httpd","start"]`|
|カレントディレクトリを指定|WORKDIR|`WORKDIR /var/www/html`|
|ボリューム指定|VOLUME|`VOLUME /var/log/httpd`|