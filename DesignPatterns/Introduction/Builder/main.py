# 启用 Python 中的 "类型注解" 功能
from __future__ import annotations
from abc import ABC, abstractmethod

# 奶茶父類別
class Milktea:
    _price = None
    _topping = 'boba'
    _tea = 'regularMilktea'
    _sugar = 100

    def __init__(self) -> None:
        self._price = 7.0
    
    def getPrice(self):
        return self._price

# 具體奶茶類
class SignatureMilktea(Milktea):
    def __init__(self) -> None:
        self._price = 5.7

# 具體奶茶類
class OolongMilktea(Milktea):
    def __init__(self) -> None:
        self._price = 4.5

# 定義創建奶茶的基本步驟接口 (Builder 提供逐步創建產品的步驟)
class MilkteaBuilder(ABC):
    @abstractmethod
    def reset(self) -> None:
        pass

    @abstractmethod
    def add_topping(self) -> None:
        pass

    @abstractmethod
    def add_tea(self) -> None:
        pass

    @abstractmethod
    def add_suger_level(self) -> None:
        pass

    @abstractmethod
    def get_product(self) -> None:
        pass

# 創建特定奶茶的具體生成器 (實現 MilkteaBuilder 接口)
class SignatureMilkteaBuilder(MilkteaBuilder):
    def reset(self) -> None:
        self._product = SignatureMilktea()

    def add_topping(self) -> None:
        self._product._topping = 'boba'

    def add_tea(self) -> None:
        self._product._tea = 'signature tea'

    def add_suger_level(self) -> None:
        self._product._sugar = 100
    
    def get_product(self) -> None:
        print(f'Signature milktea: {self._product._topping} {self._product._tea} {self._product._sugar}')
        return self._product

# 創建特定奶茶的具體生成器 (實現 MilkteaBuilder 接口)
class OolongMilkteaBuilder(MilkteaBuilder):
    def reset(self) -> None:
        self._product = OolongMilktea()

    def add_topping(self) -> None:
        self._product._topping = 'grass jelly'

    def add_tea(self) -> None:
        self._product._tea = 'oolong'

    def add_suger_level(self) -> None:
        self._product._sugar = 50
    
    def get_product(self) -> None:
        print(f'Oolong milktea: {self._product._topping} {self._product._tea} {self._product._sugar}')
        return self._product

# 創建自定義客製化奶茶的具體生成器 (實現 MilkteaBuilder 接口)
class CustomizedMilkteaBuilder:
    _product = None

    def reset(self) -> None:
        self._product = Milktea()

    def add_topping(self, topping: str) -> None:
        self._product._topping = topping

    def add_tea(self, tea: str) -> None:
        self._product._tea = tea

    def add_suger_level(self, sugar_level: int) -> None:
        self._product._sugar = sugar_level
    
    def get_product(self) -> None:
        print(f'Customized milktea: {self._product._topping} {self._product._tea} {self._product._sugar}')
        return self._product   

# 創建可複用的特定產品 (簡化創建步驟)
class MilkteaDirector:
    _milktea_builder = None

    def __init__(self, builder: MilkteaBuilder) -> None:
        self._milktea_builder = builder
    
    def change_builder(self, builder: MilkteaBuilder) -> None:
        self._milktea_builder = builder
    
    def make_milktea(self) -> Milktea:
        self._milktea_builder.reset()
        self._milktea_builder.add_topping()
        self._milktea_builder.add_tea()
        self._milktea_builder.add_suger_level()
        return self._milktea_builder.get_product()
    
    def make(self, type: str) -> Milktea:
        if type == 'signature':
            self.change_builder(SignatureMilkteaBuilder())
        elif type == 'oolong':
            self.change_builder(OolongMilkteaBuilder())
        return self.make_milktea()

if __name__ == '__main__':
    director = MilkteaDirector(SignatureMilkteaBuilder())
    director.make_milktea()
    director.change_builder(OolongMilkteaBuilder())
    director.make_milktea()
    director.make('signature')
    director.make('oolong')

    builder = CustomizedMilkteaBuilder()
    builder.reset()
    builder.add_topping('boba')
    builder.add_tea('Oolong')
    builder.add_suger_level(10)
    builder.get_product()
