# Private Registory を利用する

## 参考

- https://docs.docker.com/registry/deploying/
- https://qiita.com/Gin/items/c58c4485caae1c139e8f
- https://blog.nishi.network/2020/06/17/hosting-docker-private-registry/

## localhost に private registry を作成する

- Registry コンテナを起動

  ```shell
  $ docker run -d \
  -p 5018:5000 \
  --restart=always \
  --name registry \
  -v "$(pwd)"/registry:/var/lib/registry \
  registry:2
  ```

- Registry コンテナを起動（イメージを削除可能にする場合）

  ```shell
  $ docker run -e REGISTRY_STORAGE_DELETE_ENABLED=true -d \
  -p 5018:5000 \
  --restart=always \
  --name registry \
  -v "$(pwd)"/registry:/var/lib/registry \
  registry:2
  ```

- イメージのタグを変更する

  ```shell
  $ docker tag ubuntu localhost:5018/ubuntu
  ```

- イメージを push する
  ```shell
  $ docker push localhost:5018/ubuntu
  ```

## Local Registry の操作

- リポジトリを取得

  ```shell
  $ curl http://localhost:5018/v2/_catalog
  {"repositories":["my-ubuntu","ubuntu"]}
  ```

- タグを取得

  ```shell
  $ curl http://localhost:5018/v2/my-ubuntu/tags/list
  {"name":"my-ubuntu","tags":["latest"]}
  ```

- マニフェストを取得する

  ```shell
  $ curl http://localhost:5018/v2/my-ubuntu/manifests/latest
  ```

- Digest を取得する
  ```shell
  $ curl -i -H "Accept: application/vnd.docker.distribution.manifest.v2+json" localhost:5018/v2/my-ubuntu/manifests/latest
  HTTP/1.1 200 OK
  Content-Length: 1150
  Content-Type: application/vnd.docker.distribution.manifest.v2+json
  Docker-Content-Digest: sha256:f4c51ba054967fd4b06715f1b67078efbe9ca152e8be98d8f3c1f4d08c6042f8
  Docker-Distribution-Api-Version: registry/2.0
  Etag: "sha256:f4c51ba054967fd4b06715f1b67078efbe9ca152e8be98d8f3c1f4d08c6042f8"
  X-Content-Type-Options: nosniff
  Date: Thu, 29 Dec 2022 12:43:26 GMT
   :
  ```
- イメージを削除する
  - 削除したいイメージの Docker-Content-Digest を指定して削除する
  ```shell
  $ curl -X DELETE localhost:5018/v2/my-ubuntu/manifests/sha256:f4c51ba054967fd4b06715f1b67078efbe9ca152e8be98d8f3c1f4d08c6042f8
  ```

## 簡易的な Web Dashboard

- Dashboard を起動
  ```shell
  $ docker run -d -e ENV_DOCKER_REGISTRY_HOST=192.168.11.50 -e ENV_DOCKER_REGISTRY_PORT=5018 -p 8080:80 konradkleine/docker-registry-frontend:v2
  ```
