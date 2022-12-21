# 寄送 Email 的功能類別
class EmailService:
    def send_notification(self, info):
        print(f'Email: {info}')

# 寄送 Message 的功能類別
class MessageService:
    def send_notification(self, info):
        print(f'Message: {info}')

# 使用寄送功能的服務類別
class NotificationService1:
    def send_notification(self, service_type, info):
        # 因為沒有抽象化的父類別，導致需要進行判斷
        if service_type == 'email':
            # 呼叫各自的執行代碼
            self.send_email(info)
        elif service_type == 'message':
            # 呼叫各自的執行代碼
            self.send_message(info)
    
    def send_email(self, info):
        es = EmailService()
        es.send_notification(info)
    
    def send_message(self, info):
        ms = MessageService()
        ms.send_notification(info)

ns = NotificationService1()
ns.send_notification('email', 'hello')
ns.send_notification('message', 'hello')
