__author__ = "ChiangWei"
__date__ = "2022/04/20"

import sys

name = 'Guest'
if len(sys.argv) > 1:
    name = sys.argv[1]
print(f'Hello, {name}')
