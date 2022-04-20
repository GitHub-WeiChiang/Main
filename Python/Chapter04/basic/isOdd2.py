__author__ = "ChiangWei"
__date__ = "2022/04/20"

import sys

number = int(sys.argv[1])
print('{} 為 {}'.format(number, '奇數' if number % 2 else '偶數'))
