FROM public.ecr.aws/lambda/provided:al2023

RUN dnf install -y tar xz wget gzip && \
    dnf install -y zlib-devel bzip2-devel readline-devel sqlite-devel openssl-devel tk-devel libffi-devel xz-devel libuuid-devel libdb-devel gdbm-devel && \
    dnf install -y gcc make

RUN cd && \
    wget https://www.python.org/ftp/python/3.11.6/Python-3.11.6.tgz && \
    tar xzvf ./Python-3.11.6.tgz

RUN cd && \
    mkdir -p .python-runtime && \
    cd Python-3.11.6 && \
    ./configure --disable-test-modules --prefix=$HOME/.python-runtime/ && \
    make -j 4 && \
    make install

