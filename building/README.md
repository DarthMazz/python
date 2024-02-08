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

## lambda python311 information

```
# ll /var/lang/bin/
total 104
drwxr-xr-x 3 root root  4096 Feb  7 15:45 ./
drwxr-xr-x 1 root root  4096 Feb  7 18:34 ../
-rwxr-xr-x 1 root root  1703 Dec  4 13:39 jp.py*
lrwxrwxrwx 1 root root     4 Feb  7 18:34 pip -> pip3*
-rwxr-xr-x 1 root root   229 Dec  4 13:39 pip3*
-rwxr-xr-x 1 root root   229 Dec  4 13:39 pip3.11*
drwxr-xr-x 2 root root  4096 Feb  7 15:45 __pycache__/
lrwxrwxrwx 1 root root     6 Feb  7 18:34 pydoc -> pydoc3*
lrwxrwxrwx 1 root root     9 Feb  7 18:34 pydoc3 -> pydoc3.11*
-rwxr-xr-x 1 root root    84 Dec  4 13:38 pydoc3.11*
lrwxrwxrwx 1 root root     7 Feb  7 18:34 python -> python3*
lrwxrwxrwx 1 root root    10 Feb  7 18:34 python3 -> python3.11*
-rwxr-xr-x 1 root root 72352 Dec  4 13:38 python3.11*
-rwxr-xr-x 1 root root  3040 Dec  4 13:38 python3.11-config*
lrwxrwxrwx 1 root root    17 Feb  7 18:34 python3-config -> python3.11-config*
lrwxrwxrwx 1 root root    14 Feb  7 18:34 python-config -> python3-config*
```

```
# cat /var/runtime/bootstrap
#!/bin/bash
# Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.

export AWS_EXECUTION_ENV=AWS_Lambda_python3.11

if [ -z "$AWS_LAMBDA_EXEC_WRAPPER" ]; then
  exec /var/lang/bin/python3.11 /var/runtime/bootstrap.py
else
  wrapper="$AWS_LAMBDA_EXEC_WRAPPER"
  if [ ! -f "$wrapper" ]; then
    echo "$wrapper: does not exist"
    exit 127
  fi
  if [ ! -x "$wrapper" ]; then
    echo "$wrapper: is not an executable"
    exit 126
  fi
    exec -- "$wrapper" /var/lang/bin/python3.11 /var/runtime/bootstrap.py
fi
```

```
# cat bootstrap.py
"""
Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
"""

import json
import logging
import os
import site
import sys
import time
import traceback
import warnings
import awslambdaric.__main__ as awslambdaricmain


def is_pythonpath_set():
    return "PYTHONPATH" in os.environ


def get_opt_site_packages_directory():
    return '/opt/python/lib/python{}.{}/site-packages'.format(sys.version_info.major, sys.version_info.minor)

def get_var_lang_site_package_directory():
    return '/var/lang/lib/python{}.{}/site-packages'.format(sys.version_info.major, sys.version_info.minor)

def get_opt_python_directory():
    return '/opt/python'


# set default sys.path for discoverability
# precedence: LAMBDA_TASK_ROOT -> /opt/python/lib/pythonN.N/site-packages -> /opt/python
def set_default_sys_path():
    if not is_pythonpath_set():
        sys.path.insert(0, get_var_lang_site_package_directory())
        sys.path.insert(0, get_opt_python_directory())
        sys.path.insert(0, get_opt_site_packages_directory())
#     'LAMBDA_TASK_ROOT' is function author's working directory
#     we add it first in order to mimic the default behavior of populating sys.path and make modules under 'LAMBDA_TASK_ROOT'
#     discoverable - https://docs.python.org/3/library/sys.html#sys.path
    sys.path.insert(0, os.environ['LAMBDA_TASK_ROOT'])


def add_default_site_directories():
#     Set 'LAMBDA_TASK_ROOT as site directory so that we are able to load all customer .pth files
    site.addsitedir(os.environ["LAMBDA_TASK_ROOT"])
    if not is_pythonpath_set():
        site.addsitedir(get_opt_site_packages_directory())
        site.addsitedir(get_opt_python_directory())

def set_default_pythonpath():
    if not is_pythonpath_set():
#         keep consistent with documentation: https://docs.aws.amazon.com/lambda/latest/dg/lambda-environment-variables.html
        os.environ["PYTHONPATH"] = os.environ["LAMBDA_RUNTIME_DIR"]


def main():
    set_default_sys_path()
    add_default_site_directories()
    set_default_pythonpath()
    awslambdaricmain.main([os.environ["LAMBDA_TASK_ROOT"], os.environ["_HANDLER"]])

if __name__ == '__main__':
    main()
```

```
# env
HOSTNAME=d682f4c64c18
TERM=xterm
LAMBDA_TASK_ROOT=/var/task
LD_LIBRARY_PATH=/var/lang/lib:/lib64:/usr/lib64:/var/runtime:/var/runtime/lib:/var/task:/var/task/lib:/opt/lib
PATH=/var/lang/bin:/usr/local/bin:/usr/bin/:/bin:/opt/bin
PWD=/var/runtime
LAMBDA_RUNTIME_DIR=/var/runtime
LANG=en_US.UTF-8
TZ=:/etc/localtime
SHLVL=1
HOME=/root
_=/usr/bin/env
OLDPWD=/root/glibc-2.39/build
```
