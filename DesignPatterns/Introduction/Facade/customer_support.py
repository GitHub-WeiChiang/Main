from enum import Enum

# 子系統: 支付
class Payment:
    def __init__(self, amount):
        self.amount = amount

    def get_amount(self):
        return self.amount

class RefundStatus(Enum):
    SUCCESS = 1
    FAILURE = 2

# 子系統: 計費
class Billing:
    def get_payment_for_order(self, order_id):
        # Simple Implementation
        return Payment(50.0)

    def process_refund(self, payment):
        # Simple Implementation
        if payment.get_amount() > 0:
            return RefundStatus.SUCCESS
        else:
            return RefundStatus.FAILURE

# 子系統: 運送
class Shipping:
    def update_shipping_address(self, order_id, new_address):
        print(f"Shipping address for order {order_id} updated to: {new_address}")

# 子系統: 訂單問題
class Issue:
    def __init__(self, description):
        self.description = description

    def get_description(self):
        return self.description

# 子系統: 訊息交互
class CustomerService:
    def notify_customer(self, message):
        print(f"Notification sent to customer: {message}")

    def escalate_to_manager(self, issue):
        print(f"Issue escalated to manager: {issue.get_description()}")

# 外觀模式: 包含子系統引用，提供封裝運作原理的交互方法
class CustomerSupportFacade:
    def __init__(self, billing, shipping, customer_service):
        # 子系統引用
        self.billing = billing
        self.shipping = shipping
        self.customer_service = customer_service

    # 退款申請: 客戶僅需知道 order_id 即可，無需關心具體實現細節
    def handle_refund_request(self, order_id):
        payment = self.billing.get_payment_for_order(order_id)
        refund_status = self.billing.process_refund(payment)
        self.customer_service.notify_customer(f"Refund status: {refund_status}")

    # 修改地址
    def change_shipping_address(self, order_id, new_address):
        self.shipping.update_shipping_address(order_id, new_address)
        self.customer_service.notify_customer("Shipping address updated")

    # 傳送問題
    def escalate_to_manager(self, issue_description):
        issue = Issue(issue_description)
        self.customer_service.escalate_to_manager(issue)

class CustomerSupportClient:
    @staticmethod
    def main():
        # 創建子系統
        billing = Billing()
        shipping = Shipping()
        customer_service = CustomerService()

        # 建立外觀並傳入子系統
        customer_support = CustomerSupportFacade(billing, shipping, customer_service)
        # 退款申請
        customer_support.handle_refund_request(12345)
        # 修改地址
        customer_support.change_shipping_address(12345, "123 New Street, New York, NY 10001")
        # 提出問題
        customer_support.escalate_to_manager("Product not working properly")

if __name__ == "__main__":
    CustomerSupportClient.main()
