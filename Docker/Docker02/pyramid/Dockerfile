FROM python:3.10.8

COPY ./pyramid.py /pyramid.py

# NTRYPOINT 命令的目的和 CMD 一样，都是在指定容器启动时的程序和参数。
ENTRYPOINT ["python3", "pyramid.py"]

# CMD 指定的是容器的默认命令，其命令可以被覆盖。
CMD ["5"]
