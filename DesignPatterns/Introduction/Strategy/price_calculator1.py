from enum import Enum


# 客戶類型列舉
class CustomerType(Enum):
    CHILD = 1
    ADULT = 2
    SENIOR = 3


# 價格計算器
class PriceCalculator:
    # 價格計算方法: 接受兩個參數 (原始價格、客戶類型)
    @staticmethod
    def calculate_price(price, customer_type):
        # 50% discount for children
        if customer_type == CustomerType.CHILD:
            return price * 0.5
        # no discount for adults
        elif customer_type == CustomerType.ADULT:
            return price
        # 20% discount for seniors
        elif customer_type == CustomerType.SENIOR:
            return price * 0.8
        else:
            raise ValueError('Invalid customer type')


if __name__ == "__main__":
    calculator = PriceCalculator()
    print("Children price: ", calculator.calculate_price(100, CustomerType.CHILD))
    print("Adult price: ", calculator.calculate_price(100, CustomerType.ADULT))
    print("Senior price: ", calculator.calculate_price(100, CustomerType.SENIOR))

    # 這樣的設計若想添加新的客戶類型，
    # 或是在節假日時想改變現有的價格計算策略，
    # 此時 calculate_price() 方法將會被頻繁的改動，
    # 這會造成 PriceCalculator 類別維護上的不易。
