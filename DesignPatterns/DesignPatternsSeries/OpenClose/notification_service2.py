# 新增一個接口 (抽象類別)
class NotificationService:
    def send_notification(self, info):
        pass

# 各個通知類型需實作該接口
class EmailService(NotificationService):
    def send_notification(self, info):
        print(f'Email: {info}')

# 各個通知類型需實作該接口
class MessageService(NotificationService):
    def send_notification(self, info):
        print(f'Message: {info}')

# 各個通知類型需實作該接口
class WeChatService(NotificationService):
    def send_notification(self, info):
        print(f'WeChat: {info}')

class NotificationService2:
    def send_notification(self, notification_service, info):
        # 透過多型，執行每一個類別的方法
        notification_service.send_notification(info)

ns = NotificationService2()
# 依照需求傳入各個實作訊息傳遞的類別
ns.send_notification(EmailService(), 'hello')
ns.send_notification(MessageService(), 'hello')
ns.send_notification(WeChatService(), 'hello')

