from abc import ABC, abstractmethod

# 付款方式接口 (橋接的關鍵)
class Payment(ABC):
    # 定義付款方式要實現的方法
    @abstractmethod
    def processPayment(self):
        pass

# 具體付款方式
class CreditCardPayment(Payment):
    # 實現具體方法
    def processPayment(self):
        print("Processing credit card payment")

# 具體付款方式
class WeChatPayment(Payment):
    # 實現具體方法
    def processPayment(self):
        print("Processing wechat payment")

# 抽象商品類
class Product(ABC):
    def __init__(self, payment: Payment):
        # 成員變量 (付款方式)
        self.payment = payment

    # 付款方式 (購買產品的方法)
    @abstractmethod
    def purchase(self):
        pass

# 具體產品
class Book(Product):
    def __init__(self, payment: Payment):
        super().__init__(payment)

    # 實現抽象方法
    def purchase(self):
        self.payment.processPayment()
        print("Purchased book")

# 具體產品
class Electronics(Product):
    def __init__(self, payment: Payment):
        super().__init__(payment)

    # 實現抽象方法
    def purchase(self):
        self.payment.processPayment()
        print("Purchased electronics")

if __name__ == "__main__":
    # 付款方式
    creditCardPayment = CreditCardPayment()
    wechatPayment = WeChatPayment()

    book = Book(creditCardPayment)
    book.purchase()

    electronics = Electronics(creditCardPayment)
    electronics.purchase()

    book2 = Book(wechatPayment)
    book2.purchase()

    # 此時若要增加新的付款方式 (如: 現金支付)，
    # 不需要更動產品類別內部的任合代碼。
