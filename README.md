# python

## Windows

### Subsystem for LINUX 2

https://docs.microsoft.com/ja-jp/windows/wsl/install-win10

1. Linux 用 Windows サブシステムを有効
~~~
dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart
~~~

2. WSL 2 に更新する条件確認

x64 システムの場合:バージョン 1903 以降、ビルド 18362 以上

3. 仮想マシンの機能を有効
~~~
dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart
~~~

https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

## Azure に ASP.NET Core Web アプリを作成する
https://docs.microsoft.com/ja-jp/azure/app-service/quickstart-dotnetcore?pivots=platform-linux

## ハードウェア構成の変更後に Windows 10 のライセンス認証をもう一度行う
https://office-hack.com/windows/windows10-license-authentication/#section1_2

## Mac
https://qiita.com/crankcube/items/15f06b32ec56736fc43a

### Homebrew

https://brew.sh/index_ja.html

~~~
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

brew update

brew install pyenv

pyenv install --list

pyenv install 3.8.5

pyenv global 3.8.5

pyenv versions
~~~

### pytest
https://pypi.org/project/pytest-flake8/

~~~
pytest --flake8
~~~

### reference
#### 構文
http://www.tohoho-web.com/python/index.html

#### Docstring
https://qiita.com/simonritchie/items/49e0813508cad4876b5a

#### Markdown
https://gist.github.com/mignonstyle/083c9e1651d7734f84c99b8cf49d57fa
