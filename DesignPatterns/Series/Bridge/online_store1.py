# 產品
class Book:
    # 信用卡付款
    def purchaseWithCreditCard(self, creditCard):
        creditCard.processPayment()
        print("Purchased book")

    # 微信付款
    def purchaseWithWeChat(self, payPalAccount):
        payPalAccount.processPayment()
        print("Purchased book")


# 產品
class Electronics:
    # 信用卡付款
    def purchaseWithCreditCard(self, creditCard):
        creditCard.processPayment()
        print("Purchased electronics")

    # 微信付款
    def purchaseWithWeChat(self, payPalAccount):
        payPalAccount.processPayment()
        print("Purchased electronics")


# 信用卡付款方式
class CreditCardPayment:
    def processPayment(self):
        print("Processing credit card payment")


# 微信付款方式
class WeChatPayment:
    def processPayment(self):
        print("Processing wechat payment")


if __name__ == "__main__":
    # 初始化產品
    book = Book()
    electronics = Electronics()

    # 初始化付款方式
    creditCardPayment = CreditCardPayment()
    wechatPayment = WeChatPayment()

    # 付款
    book.purchaseWithCreditCard(creditCardPayment)
    electronics.purchaseWithCreditCard(creditCardPayment)
    book.purchaseWithWeChat(wechatPayment)
    electronics.purchaseWithWeChat(wechatPayment)

    # 此時若要增加新的付款方式 (如: 現金支付)，
    # 則每個產品都要增加新的付款方式方法，
    # 這不是一個好的做法呢...
