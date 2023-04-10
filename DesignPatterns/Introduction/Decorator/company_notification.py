from abc import ABC, abstractmethod

# Notifier interface (基本組件)
class Notifier(ABC):
    # 定義統一發送通知方法
    @abstractmethod
    def send(self, message: str):
        pass

# Concrete Component (具體組件)
class EmailNotifier(Notifier):
    # 實現通知方法
    def send(self, message: str):
        print(f"Sending Email message: {message}")

# Decorator abstract class (抽象裝飾器類)
class NotifierDecorator(Notifier):
    # 對 Notifier 引用
    def __init__(self, notifier: Notifier):
        self.notifier = notifier

    # 實現 send 方法
    def send(self, message: str):
        self.notifier.send(message)

# Concrete Decorator classes
class WeChatDecorator(NotifierDecorator):
    def __init__(self, notifier: Notifier):
        super().__init__(notifier)

    def send(self, message: str):
        super().send(message)
        print(f"Sending WeChat message: {message}")

class MobileDecorator(NotifierDecorator):
    def __init__(self, notifier: Notifier):
        super().__init__(notifier)

    def send(self, message: str):
        super().send(message)
        print(f"Sending Mobile message: {message}")

# class QQDecorator(NotifierDecorator):
#     def __init__(self, notifier: Notifier):
#         super().__init__(notifier)

#     def send(self, message: str):
#         super().send(message)
#         print(f"Sending QQ message: {message}")

# Client
if __name__ == "__main__":
    message = "Hello, this is a notification!"

    # Sending notifications using different combinations
    notifier = EmailNotifier()
    notifier = WeChatDecorator(notifier)
    notifier = MobileDecorator(notifier)

    # notifier = QQDecorator(notifier)

    notifier.send(message)
