__author__ = "ChiangWei"
__date__ = "2022/5/31"

from typing import Dict
import threading


def set_to1(inner_data: Dict[str, int]):
    while True:
        inner_data['Justin'] = 1
        if inner_data['Justin'] != 1:
            raise ValueError(f'setTo1 資料不一致：{inner_data}')


def set_to2(inner_data: Dict[str, int]):
    while True:
        inner_data['Justin'] = 2
        if inner_data['Justin'] != 2:
            raise ValueError(f'setTo2 資料不一致：{inner_data}')


data: Dict[str, int] = {}

t1 = threading.Thread(target=set_to1, args=(data, ))
t2 = threading.Thread(target=set_to2, args=(data, ))

t1.start()
t2.start()
