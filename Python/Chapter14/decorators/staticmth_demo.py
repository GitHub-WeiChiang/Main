__author__ = "ChiangWei"
__date__ = "2022/6/3"

from typing import Any, Type, Callable

class staticmth:
    def __init__(self, mth: Callable) -> None:
        self.mth = mth

    def __get__(self, instance: Any, owner: Type) -> Callable:
        return self.mth

class Some:
    @staticmth
    def doIt(a, b):
        print(a, b)

Some.doIt(1, 2)

s = Some()

s.doIt(1)
