__author__ = "ChiangWei"
__date__ = "2022/6/3"

from typing import Callable

PriceFunc = Callable[..., float]

def sidedish1(meal: PriceFunc) -> PriceFunc:
    return lambda: meal() + 30

@sidedish1
def friedchicken():
    return 49.0

print(friedchicken())
