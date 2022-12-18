# Private Registory を利用する

- Dockerfile よりコンテナイメージを作成する
  - デバッグ用とプロダクション用でイメージを分ける
  ```shell
  docker image build --tag lambda-python:3.9  .
  ```
