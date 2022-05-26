__author__ = "ChiangWei"
__date__ = "2022/5/26"

from typing import Callable
import os

def list_all(dir: str, action: Callable[..., None]):
    for dirpath, dirnames, filenames in os.walk(dir):
        action(dirpath)
        for filename in filenames:
            action(f'{dirpath}\\{filename}')

list_all(r'D:\Oracle', print)
