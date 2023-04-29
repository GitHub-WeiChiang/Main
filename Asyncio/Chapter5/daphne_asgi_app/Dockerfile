FROM python:3-slim

# 因为安装 daphne 过程中可能需要编译原生代码，所以需要安装 gcc 编译器
RUN apt update&&apt install -y gcc make
RUN pip3 install -i https://pypi.tuna.tsinghua.edu.cn/simple daphne
