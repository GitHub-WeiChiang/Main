__author__ = "ChiangWei"
__date__ = "2022/05/04"

import sys

def console_input(prompt: str) -> str:
    sys.stdout.write(prompt)
    sys.stdout.flush()
    return sys.stdin.readline()

name = console_input('請輸入名稱：')
print('哈囉, ', name)
