# Docker を利用して Remote Debug する

## 参照

- [Dockerひとつでリモートデバッグ可能な開発・本番環境を作る方法](https://qiita.com/sebastianrettig/items/f68b23c150dde419bb96)

## 動作環境

```shell
$ cat /etc/os-release 
NAME="Ubuntu"
VERSION="20.04 LTS (Focal Fossa)"
ID=ubuntu
ID_LIKE=debian
PRETTY_NAME="Ubuntu 20.04 LTS"
VERSION_ID="20.04"
HOME_URL="https://www.ubuntu.com/"
SUPPORT_URL="https://help.ubuntu.com/"
BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"
PRIVACY_POLICY_URL="https://www.ubuntu.com/legal/terms-and-policies/privacy-policy"
VERSION_CODENAME=focal
UBUNTU_CODENAME=focal
```

```shell
$ cat /proc/version 
Linux version 5.10.16.3-microsoft-standard-WSL2 (oe-user@oe-host) (x86_64-msft-linux-gcc (GCC) 9.3.0, GNU ld (GNU Binutils) 2.34.0.20200220) #1 SMP Fri Apr 2 22:23:49 UTC 2021
```

```shell
$ docker --version
Docker version 20.10.21, build baeda1f
```


## 手順

- デバッグしたいアプリを作成する
  - app.py
    ```python
    if __name__ == '__main__':
    print('aha')
    ```

- デバッグ環境の Dockerfile を作成する
  - Dockerfile
    ```docker
    FROM python:3.8 AS base

    WORKDIR /app

    # COPY requirements.txt requirements.txt
    # RUN pip install --no-cache-dir -r requirements.txt

    # ENV FLASK_ENV="docker"
    # ENV FLASK_APP=app.py
    # EXPOSE 5000

    # Development Stage
    FROM base AS develop
    RUN pip install debugpy
    # Keeps Python from generating .pyc files in the container
    ENV PYTHONDONTWRITEBYTECODE 1
    # Turns off buffering for easier container logging
    ENV PYTHONUNBUFFERED 1

    # Production Stage
    FROM base AS production
    RUN pip install --no-cache-dir gunicorn
    COPY . .
    # CMD ["gunicorn", "--reload", "--bind", "0.0.0.0:5000", "app:app"]
    ```

- Dockerfile よりコンテナイメージを作成する
  - デバッグ用とプロダクション用でイメージを分ける
  ```shell
  docker image build --tag remote-debug-debugpy:test --target develop .
  ```

- docker-compose.yml でデバッグ用のアプリを起動するように設定する
  ```yml
  version: "3.9"

  services:
    flask-app:
      image: remote-debug-debugpy:test
      container_name: remote-debug-debugpy
      build:
        context: .
        target: develop
      ports:
        - 5678:5678
      volumes:
        - .:/app
      environment:
        - FLASK_DEBUG=1
      entrypoint:
        [
          "python",
          "-m",
          "debugpy",
          "--listen",
          "0.0.0.0:5678",
          "--wait-for-client",
          "-m",
          "app"
        ]
      networks:
        - remote-debug-debugpy

  networks:
    remote-debug-debugpy:
      name: remote-debug-debugpy
  ```

- docker-compose によりアプリを起動する
  ```shell
  docker-compose up
  ```

- vscode のデバッグでリモートの python にアタッチするように設定する
  - .vscode/launch.json
    ```json
      {
        // IntelliSense を使用して利用可能な属性を学べます。
        // 既存の属性の説明をホバーして表示します。
        // 詳細情報は次を確認してください: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Remote Attach",
                "type": "python",
                "request": "attach",
                "connect": {
                    "host": "localhost",
                    "port": 5678
                },
                "pathMappings": [
                    {
                        "localRoot": "${workspaceFolder}",
                        "remoteRoot": "."
                    }
                ]
            }
        ]
    }
    ```

- vscode からデバッグで起動する