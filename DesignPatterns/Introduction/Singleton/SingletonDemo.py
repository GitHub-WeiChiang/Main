# 客服中心員工類別
class Worker:
    def __init__(self, name):
        self.name = name
        
    def serve_customer(self):
        print(self.name + " is serving customer")

# 單例客服中心
class CustomerServiceCenter:
    # 儲存自己的實例
    __instance = None
    
    # 靜態獲取實例方法 (全局唯一訪問節點)
    @staticmethod
    def get_instance():
        # 判斷是否已經生成實例
        if CustomerServiceCenter.__instance is None:
            # 生成實例
            CustomerServiceCenter()
        
        # 回傳實例
        return CustomerServiceCenter.__instance
    
    def __init__(self):
        # 判斷是否重複 (非法) 生成
        if CustomerServiceCenter.__instance is not None:
            raise Exception("Singleton object cannot be initialized more than once")
        else:
            CustomerServiceCenter.__instance = self

        # 初始化資訊
        self.holiday = False

        self.holiday_workers = [
            Worker("holiday worker 1"), 
            Worker("holiday worker 2"), 
            Worker("holiday worker 3")
        ]

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

# 取得客服中心實例
service1 = CustomerServiceCenter.get_instance()
# 列印服務
service1.serve_customer()

# 取得客服中心實例
service2 = CustomerServiceCenter.get_instance()
# 列印服務
service2.serve_customer()

# 設定為假日
service2.set_holiday(True)

# 列印服務
service1.serve_customer()
service2.serve_customer()

try:
    # 非法生成
    CustomerServiceCenter()
except Exception as e:
    print(e)
