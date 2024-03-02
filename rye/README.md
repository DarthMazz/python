# Python Package Manger Rye

## Setup

### Install Rye

```bash
curl -sSf https://rye-up.com/get | bash
```

```bash
echo 'source "$HOME/.rye/env"' >> ~/.zshrc
```

```bash
$ rye --version
rye 0.27.0
commit: 0.27.0 (43ee4fce0 2024-02-26)
platform: linux (aarch64)
self-python: cpython@3.12
symlink support: true
uv enabled: false
```


## Setup Project

```bash
rye init my_project
```

```bash
cd my_project
```

```bash
rye sync
```

## Change python version

```bash
rye pin 3.11.6
```

```bash
rye sync
```

## Add python module

```bash
rye add boto3
```

```bash
rye sync
```

## Add python development module

```bash
rye add --dev pytest
```

```bash
rye sync
```

## Delete python module

```bash
rye remove boto3
```

## Delete python development module

```bash
rye remove --dev pytest
```

```bash
rye sync
```


# Reference

- [【Pythonのパッケージ管理に悩む方へ】パッケージ管理ツールRyeを使ってみた](https://dev.classmethod.jp/articles/get-start-rye-python/)

 - [Installaiton](https://rye-up.com/guide/installation/)