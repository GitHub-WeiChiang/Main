__author__ = "ChiangWei"
__date__ = "2022/04/21"

import sys
import random

def producer():
    while True:
        data = random.randint(0, 9)
        print('生產了：', data)
        yield data

def consumer():
    while True:
        data = yield
        print('消費了：', data)

def clerk(jobs, producer, consumer):
    print('執行 {} 次生產與消費'.format(jobs))
    p = producer()
    c = consumer()
    next(c)
    for i in range(jobs):
        print(i)
        data = next(p)
        c.send(data)

clerk(int(sys.argv[1]), producer, consumer)
