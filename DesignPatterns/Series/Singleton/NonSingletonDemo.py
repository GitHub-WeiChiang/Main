# 客服中心員工類別
class Worker:
    def __init__(self, name):
        self.name = name
        
    def serve_customer(self):
        print(self.name + " is serving customer")

# 客服中心
class CustomerServiceCenter:
    def __init__(self, holiday):
        # 是否為假日
        self.holiday = holiday

        # 假日上班員工
        self.holiday_workers = [
            Worker("holiday worker 1"), 
            Worker("holiday worker 2"), 
            Worker("holiday worker 3")
        ]

        # 平日上班員工
        self.non_holiday_workers = [
            Worker("non-holiday worker 1"), 
            Worker("non-holiday worker 2"), 
            Worker("non-holiday worker 3")
        ]
        
    # 設定是否為假日
    def set_holiday(self, holiday):
        self.holiday = holiday
    
    # 依照班別進行服務
    def serve_customer(self):
        if self.holiday:
            # Service by holiday workers
            for worker in self.holiday_workers:
                worker.serve_customer()
        else:
            # Service by non-holiday workers
            for worker in self.non_holiday_workers:
                worker.serve_customer()

# 取得客服中心實例並設定為非假日
customer_service1 = CustomerServiceCenter(False)
# 列印服務
customer_service1.serve_customer()

# 取得客服中心實例並設定為非假日
customer_service2 = CustomerServiceCenter(False)
# 列印服務
customer_service2.serve_customer()

# 設定為假日
customer_service1.set_holiday(True)

# 列印服務
customer_service1.serve_customer()
customer_service2.serve_customer()
