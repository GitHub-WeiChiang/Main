# 信用卡類別
class Card:
    balance = 10

# 客戶類別，持有信用卡
class Customer:
    card = Card()

    def get_card(self):
        return self.card

# 衝浪店類別，與客戶溝通
class SurfShop:
    def charge_customer(self, c: Customer, fee: float):
        # 拿取客戶的信用卡，耦合過高，因為衝浪店和不應該直接溝通的信用卡溝通
        c.get_card().balance -= fee
        print(c.get_card().balance)

customer = Customer()
SurfShop().charge_customer(customer, 1.0)
