__author__ = "ChiangWei"
__date__ = "2022/6/3"

from typing import Any, Tuple, Dict, Type, Callable

Bases = Tuple[Type]
Attrs = Dict[str, Callable]

def abstract(func):
    func.__isabstract__ = True
    return func

def absmths(cls, mths):
    cls.__abstractmethods__ = frozenset(mths)

class Abstract(type):
    def __new__(mcls, clsname: str, bases: Bases, attrs: Attrs) -> Any:
        cls = super(mcls, mcls).__new__(mcls, clsname, bases, attrs)

        abstracts = {name for name, value in attrs.items()
                       if getattr(value, "__isabstract__", False)}

        for parent in bases:
            for name in getattr(parent, "__abstractmethods__", set()):
                value = getattr(cls, name, None)
                if getattr(value, "__isabstract__", False):
                    abstracts.add(name)

        absmths(cls, abstracts)

        return cls

class AbstractX(metaclass=Abstract):
    @abstract
    def doSome(self):
        pass

x = AbstractX()
