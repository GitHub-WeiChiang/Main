__author__ = "ChiangWei"
__date__ = "2022/04/20"

import sys

number = int(sys.argv[1])
if number % 2:
    print('f{number} 為奇數')
else:
    print(f'{number} 為偶數')
