__author__ = "ChiangWei"
__date__ = "2022/6/1"

from typing import Callable
from concurrent.futures import ThreadPoolExecutor, Future
from urllib.request import urlopen
import time

Consume = Callable[[Future], None]


def load_url(inner_url: str) -> bytes:
    with urlopen(inner_url) as u:
        return u.read()


def save(filename: str) -> Consume:
    def _save(inner_future):
        with open(filename, 'wb') as f:
            f.write(inner_future.result())
    return _save


with ThreadPoolExecutor() as executor:
    url = 'https://openhome.cc/Gossip/Python/'
    future = executor.submit(load_url, url)
    future.add_done_callback(save('Python.html'))
    while True:
        if future.running():
            print('.', end='')
            time.sleep(0.0001)
        else:
            break
