# python

## Windows

### Subsystem for LINUX 2

https://docs.microsoft.com/ja-jp/windows/wsl/install-win10

dism.exe /online /enable-feature /featurename:Microsoft-Windows-Subsystem-Linux /all /norestart

x64 システムの場合:バージョン 1903 以降、ビルド 18362 以上

dism.exe /online /enable-feature /featurename:VirtualMachinePlatform /all /norestart

https://wslstorestorage.blob.core.windows.net/wslblob/wsl_update_x64.msi

## Mac
https://qiita.com/crankcube/items/15f06b32ec56736fc43a

### Homebrew

https://brew.sh/index_ja.html

/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

brew update

brew install pyenv

pyenv install --list

pyenv install 3.8.5

pyenv global 3.8.5

pyenv versions

