from abc import ABC, abstractmethod

# 咖啡接口
class Coffee(ABC):
    # 定義價格計算方式
    @abstractmethod
    def cost(self):
        pass

# 基本咖啡實作接口
class SimpleCoffee(Coffee):
    # 實現價格計算方式
    def cost(self):
        return 2

# 咖啡裝飾器 (讓配料繼承)
class CoffeeDecorator(Coffee):
    # 接受其它咖啡對象
    def __init__(self, coffee):
        self.coffee = coffee

    # 在咖啡的基礎上添加額外的內容
    def cost(self):
        return self.coffee.cost()

# 加奶裝飾
class MilkDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    # 額外的內容
    def cost(self):
        return self.coffee.cost() + 0.5

# 加糖裝飾
class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        super().__init__(coffee)

    # 額外的內容
    def cost(self):
        return self.coffee.cost() + 0.25

if __name__ == "__main__":
    coffee = SimpleCoffee()
    coffee_with_milk = MilkDecorator(coffee)
    coffee_with_milk_and_sugar = SugarDecorator(coffee_with_milk)

    print("Coffee cost: ", coffee.cost())
    print("Coffee with Milk cost: ", coffee_with_milk.cost())
    print("Coffee with Milk and Sugar cost: ", coffee_with_milk_and_sugar.cost())

# 可以動態添加新功能，
# 有效提升可擴展性與可維護性。
