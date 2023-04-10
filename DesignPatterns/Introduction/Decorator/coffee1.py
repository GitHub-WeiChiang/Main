from abc import ABC, abstractmethod

# 咖啡接口
class Coffee(ABC):
    # 定義價格計算方式
    @abstractmethod
    def cost(self):
        pass

# 基本咖啡
class SimpleCoffee(Coffee):
    def cost(self):
        return 2

# 咖啡加奶
class CoffeeWithMilk(Coffee):
    def cost(self):
        return 2 + 0.5

# 咖啡加糖
class CoffeeWithSugar(Coffee):
    def cost(self):
        return 2 + 0.25

# 咖啡加奶加糖
class CoffeeWithMilkAndSugar(Coffee):
    def cost(self):
        return 2 + 0.5 + 0.25

# 若後期持續增加咖啡選項，
# 就需創建大量子類別，
# 程式碼不但臃腫凌亂，
# 相對也較難以管理。
