from abc import ABC, abstractmethod

# 定義價格策略接口
class PricingStrategy(ABC):
    @abstractmethod
    def calculate_price(self, price):
        pass

# 小人價格策略: 實作 PricingStrategy
class ChildrenPricingStrategy(PricingStrategy):
    def calculate_price(self, price):
        # 50% discount for children
        return price * 0.5

# 成人價格策略: 實作 PricingStrategy
class AdultPricingStrategy(PricingStrategy):
    def calculate_price(self, price):
        # no discount for adults
        return price

# 老人價格策略: 實作 PricingStrategy
class SeniorPricingStrategy(PricingStrategy):
    def calculate_price(self, price):
        # 20% discount for seniors
        return price * 0.8

# 青人價格策略: 實作 PricingStrategy
class TeenagerPricingStrategy(PricingStrategy):
    def calculate_price(self, price):
        # 25% discount for teenagers
        return price * 0.75

# 假人價格策略: 實作 PricingStrategy
class HolidayPricingStrategy(PricingStrategy):
    def calculate_price(self, price):
        # 10% discount on holidays for everyone
        return price * 0.9

class PriceCalculator:
    def __init__(self, strategy):
        # 接收策略對象
        self.strategy = strategy

    def calculate(self, price):
        # 使用所接收之策略對象的方法
        return self.strategy.calculate_price(price)

if __name__ == '__main__':
    # 創建價格計算器並傳入小人價格策略
    calculator = PriceCalculator(ChildrenPricingStrategy())
    print(f"Children price: {calculator.calculate(100)}")

    # 創建價格計算器並傳入成人價格策略
    calculator = PriceCalculator(AdultPricingStrategy())
    print(f"Adult price: {calculator.calculate(100)}")

    # 創建價格計算器並傳入老人價格策略
    calculator = PriceCalculator(SeniorPricingStrategy())
    print(f"Senior price: {calculator.calculate(100)}")

    # 創建價格計算器並傳入青人價格策略
    calculator = PriceCalculator(TeenagerPricingStrategy())
    print(f"Teenager price: {calculator.calculate(100)}")

    # 創建價格計算器並傳入假人價格策略
    calculator = PriceCalculator(HolidayPricingStrategy())
    print(f"Holiday price: {calculator.calculate(100)}")

    # 使用策略模式後，策略的添加 (擴展) 與刪除將變得相對輕鬆，
    # 只需傳入不同的策略，而無需修改 PriceCalculator 類別與其 calculate() 方法，
    # 在維護上也會相對容易。
