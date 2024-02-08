# build python

## enviroment

```
# cat /etc/os-release
NAME="Amazon Linux"
VERSION="2023"
ID="amzn"
ID_LIKE="fedora"
VERSION_ID="2023"
PLATFORM_ID="platform:al2023"
PRETTY_NAME="Amazon Linux 2023"
ANSI_COLOR="0;33"
CPE_NAME="cpe:2.3:o:amazon:amazon_linux:2023"
HOME_URL="https://aws.amazon.com/linux/"
BUG_REPORT_URL="https://github.com/amazonlinux/amazon-linux-2023"
SUPPORT_END="2028-03-15"
VARIANT_ID="202401231141-2023.120.0"
```

## Install build package

ソースコードダウンロードと解凍

```
dnf install -y tar xz wget gzip

dnf install -y zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel tk-devel libffi-devel xz-devel libuuid-devel libdb-devel gdbm-devel

dnf gcc make
```

```
./configure --disable-test-modules --prefix=$HOME/.python-runtime/

make -j 4

make install
```
