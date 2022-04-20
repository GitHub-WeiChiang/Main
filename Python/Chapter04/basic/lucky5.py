__author__ = "ChiangWei"
__date__ = "2022/04/20"

import random

number = 0

while number != 5:
    number = random.randint(0, 9)
    print(number)
    if number == 5:
        print('I hit 5....Orz')

