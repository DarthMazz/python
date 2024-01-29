# python

## Windows

### Subsystem for LINUX 2

https://docs.microsoft.com/ja-jp/windows/wsl/install-win10

1.  Linux 用 Windows サブシステムを有効

```
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
```

2. WSL 2 に更新する条件確認

x64 システムの場合:バージョン 1903 以降、ビルド 18362 以上

3. 仮想マシンの機能を有効

```
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
```

4. Linux カーネル更新プログラム パッケージをダウンロード

https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

5. WSL 2 を既定のバージョンとして設定

```
wsl --set-default-version 2
```

## Azure に ASP.NET Core Web アプリを作成する

https://docs.microsoft.com/ja-jp/azure/app-service/quickstart-dotnetcore?pivots=platform-linux

## ハードウェア構成の変更後に Windows 10 のライセンス認証をもう一度行う

https://office-hack.com/windows/windows10-license-authentication/#section1_2

## カスタム コンテナーを使用して Linux で関数を作成

https://docs.microsoft.com/ja-jp/azure/azure-functions/functions-create-function-linux-custom-image?tabs=bash%2Cportal&pivots=programming-language-csharp

## MacOS と Homebrew と pyenv で快適 python 環境を

https://qiita.com/crankcube/items/15f06b32ec56736fc43a

### Mac GitHub SSH 接続設定

https://qiita.com/ucan-lab/items/e02f2d3a35f266631f24

### Homebrew

https://brew.sh/index_ja.html

```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

brew update

brew install pyenv

pyenv install --list

pyenv install 3.8.5

pyenv global 3.8.5

pyenv versions
```

### PYTHONPATH

テストフォルダからメイン処理を参照するために、環境変数にパッケージのパスを通す

```
export PYTHONPATH=./coverage
```

### pylint -> flake8

https://qiita.com/psychoroid/items/2c2acc06c900d2c0c8cb

### pytest

https://pypi.org/project/pytest-flake8/

```
pytest --flake8
```

### Coverage

https://qiita.com/kg1/items/e2fc65e4189faf50bfe6

```
pytest -v --cov=CODE_DIRECTORY
```
## Ubuntu

### Install pyenv

```
curl https://pyenv.run | bash
```

### Setup pyenv

PATH 設定を .bashrc に設定
```
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```
```
source .bashrc
pyenv --version
pyenv 2.3.35
```

python をインストールするために必要なパッケージをインストール

```
sudo apt update; sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev curl \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```



# reference

## 構文

http://www.tohoho-web.com/python/index.html

## Docstring

https://qiita.com/simonritchie/items/49e0813508cad4876b5a

## コマンドライン

https://qiita.com/stkdev/items/e262dada7b68ea91aa0c

## Markdown

https://gist.github.com/mignonstyle/083c9e1651d7734f84c99b8cf49d57fa

## Nested Virtualization

https://blog.amedama.jp/entry/virtualbox-nested-virtualization

## Google Drive API, SpreadSheet

https://qiita.com/akabei/items/0eac37cb852ad476c6b9

## pyenv

[automatic installer](https://github.com/pyenv/pyenv#automatic-installer)

[build environment](https://github.com/pyenv/pyenv/wiki)