__author__ = "ChiangWei"
__date__ = "2022/6/1"

import multiprocessing
from multiprocessing.synchronize import Lock


def f(inner_lock: Lock, i: int):
    with inner_lock:
        print('hello world', i)
        print('hello world', i + 1)


if __name__ == '__main__':
    lock: Lock = multiprocessing.Lock()

    for num in range(100):
        multiprocessing.Process(target=f, args=(lock, num)).start()
