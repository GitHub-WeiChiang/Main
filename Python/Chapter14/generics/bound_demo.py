__author__ = "ChiangWei"
__date__ = "2022/6/3"

from typing import TypeVar
from abc import ABCMeta, abstractmethod

class Orderable(metaclass=ABCMeta):
    @abstractmethod
    def __lt__(self, other):
        pass

OT = TypeVar('OT', bound=Orderable)

class Ball(Orderable):
    def __init__(self, radius: int) -> None:
        self.radius = radius

    def __lt__(self, other):
        return self.radius < other.radius

def orderable_min(x: OT, y: OT) -> OT:
    return x if x < y else y

ball = orderable_min(Ball(1), Ball(2))
print(ball.radius)
