# 飛機類別
class Airplane:
    def __init__(self, name):
        self.name = name

    # 發送信息方法
    def send(self, message, receiver):
        print(f'{self.name} sends message to {receiver.name}: {message}')
        receiver.receive(message, self)

    # 接收信息方法
    def receive(self, message, sender):
        print(f'{self.name} receives message from {sender.name}: {message}')


if __name__ == '__main__':
    # 創建飛機實例
    airplane1 = Airplane('Airplane1')
    airplane2 = Airplane('Airplane2')
    airplane3 = Airplane('Airplane3')

    # 調用各自 send 方法傳遞訊息
    airplane1.send('Hello, Airplane2!', airplane2)
    airplane2.send('Hello, Airplane3!', airplane3)
    airplane3.send('Hello, Airplane1!', airplane1)

    # 當飛機數量增加，多架飛機間的通信，
    # 每架飛機需要能夠參照到其它的飛機，
    # 會使系統複雜度增加，並且管理性與可維護性較低。
