class Card:
    balance = 10

    # 信用卡自己實作扣款動作
    def deduct(self, fee: float): 
        self.balance -= fee

class Customer:
    card = Card()

    # 顧客實作付款行為
    def pay(self, fee: float):
        self.card.deduct(fee)

class SurfShop2:
    def charge_customer(self, c: Customer, fee: float):
        # 衝浪店只與客戶進行溝通
        c.pay(fee)

customer = Customer()
SurfShop2().charge_customer(customer, 1.0)
