__author__ = "ChiangWei"
__date__ = "2022/6/3"

from typing import Callable
from functools import wraps

PriceFunc = Callable[..., float]

def sidedish1(meal: PriceFunc) -> PriceFunc:
    @wraps(meal)
    def wrapper():
        return meal() + 30
    return wrapper

@sidedish1
def friedchicken():
    return 49.0

print(friedchicken())

print(friedchicken)
