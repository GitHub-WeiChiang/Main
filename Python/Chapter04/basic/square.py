__author__ = "ChiangWei"
__date__ = "2022/04/20"

import sys

squares = [int(arg) ** 2 for arg in sys.argv[1:]]
print(squares)
