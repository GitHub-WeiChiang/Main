__author__ = "ChiangWei"
__date__ = "2022/04/20"

import sys

odds = [arg for arg in sys.argv[1:] if int(arg) % 2]
print(odds)
