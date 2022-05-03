__author__ = "ChiangWei"
__date__ = "2022/05/03"

import sys
from contextlib import suppress

with suppress(FileNotFoundError):
    for line in open(sys.argv[1]):
        print(line, end='')
