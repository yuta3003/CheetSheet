# Docker

- [Basic commands](#basic-commands)
- [Create DockerImage from Dockerfile](#create-dockerimage-from-dockerfile)
- [Push DockerImage to DockerHub](#push-dockerimage-to-dockerhub)
- [Application on Docker](#application-on-docker)
    - [DVWA on Docker](#dvwa)
    - [OWASP juice shop on Docker](#owasp-juice-shop)


## Basic commands
```sh
docker images   # Dockerイメージの一覧表示
docker ps -a    # Dockerコンテナ一覧表示
docker rm CONTEINNER_ID     # コンテナの削除
docker rmi IMAGE_ID         # イメージの削除
docker image inspect IMAGE_ID   # イメージの詳細表示
docker run CONTEINNER_ID        # コンテナ起動

docker save {image} > {tar_file}    # Dockeriamgeをtarファイルへ変換
docker load < {tar_file}    # tarファイルをDockerimageへ変換

docker inspect <コンテナID> # Dockerコンテナの情報を表示
```

## Create DockerImage from Dockerfile.
```sh
docker build [ -t ｛イメージ名｝ [ :｛タグ名｝ ] ] .
```

## Push DockerImage to DockerHub
```sh
docker commit <コンテナID> <イメージ名>     # コンテナをイメージ化
docker tag イメージID DockerHubのユーザ名/任意の名前    #タグ付加
docker push <イメージ名>    #イメージをpush
```

## Application on Docker

### DVWA
```sh
docker pull vulnerables/web-dvwa
docker run --rm -it -p 80:80 vulnerables/web-dvwa
```

### OWASP juice shop
```sh
docker pull bkimminich/juice-shop
docker run --rm -p 3000:3000 bkimminich/juice-shop
```