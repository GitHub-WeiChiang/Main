import abc
from typing import List, Set

class Calculator:
    @abc.abstractmethod
    def stringToList(self, input_str) -> List(str):
        raise NotImplementedError

# 子類別若覆寫父類別方法，其返回值資料型態應為父類別方法返回值資料型態相同或是其型態之子類別。
class SuperCalculator(Calculator):
    # return type doesn't match
    def stringToList(self, input_str) -> Set(str):
        pass
