from abc import ABC, abstractmethod

# 中介者接口
class Mediator(ABC):
    # 信息發送抽象方法
    @abstractmethod
    def send(self, message, sender):
        pass

# 飛機類
class Airplane:
    def __init__(self, name, mediator):
        self.name = name
        # 中介者參照
        self.mediator = mediator

    def send(self, message):
        print(f'{self.name} sends message: {message}')
        # 由中介者進行信息的轉發
        self.mediator.send(message, self)

    def receive(self, message):
        print(f'{self.name} receives message: {message}')

# 具體中介者類別 (空中交通指揮中心)
class AirTrafficControl(Mediator):
    def __init__(self):
        # 飛機列表: 用於註冊飛機
        self.airplanes = []

    # 註冊飛機
    def register_airplane(self, airplane):
        self.airplanes.append(airplane)

    # 簡單信息轉發方法
    def send(self, message, sender):
        # 迭代飛機列表
        for airplane in self.airplanes:
            # 將信息發送給除了自己以外的飛機
            if airplane is not sender:
                # 發送信息
                airplane.receive(message)


if __name__ == '__main__':
    # 創建中介者
    atc = AirTrafficControl()

    # 創建飛機
    airplane1 = Airplane('Airplane1', atc)
    airplane2 = Airplane('Airplane2', atc)
    airplane3 = Airplane('Airplane3', atc)

    # 註冊飛機
    atc.register_airplane(airplane1)
    atc.register_airplane(airplane2)
    atc.register_airplane(airplane3)

    # 發送信息
    airplane1.send('Hello, everyone!')
    airplane2.send('Hello, everyone!')
    airplane3.send('Hello, everyone!')

    # 每架飛機不需要具有其它飛機的參照，
    # 只需要與中介者溝通與交互，
    # 飛機的添加與刪除只需要針對中介者進行操作，
    # 無需改動飛機的代碼，
    # 極大簡化系統維護與管理的難易度，
    # 通過中心化信息處理，
    # 可以更容易的控制與調度飛機間的通信，
    # 提高系統靈活性與可拓展性。
