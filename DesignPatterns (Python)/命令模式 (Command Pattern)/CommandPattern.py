__author__ = "ChiangWei"
__date__ = "2022/05/22"

from abc import ABCMeta, abstractmethod

class Chef():
    def steamFood(self, originalMaterial):
        print("%s清蒸中..." % originalMaterial)
        return "清蒸" + originalMaterial

    def stirFriedFood(self, originalMaterial):
        print("%s爆炒中..." % originalMaterial)
        return "香辣炒" + originalMaterial

class Order(metaclass=ABCMeta):
    def __init__(self, name, originalMaterial):
        self._chef = Chef()
        self._name = name
        self._originalMaterial = originalMaterial

    def getDisplayName(self):
        return self._name + self._originalMaterial

    @abstractmethod
    def processingOrder(self):
        pass

class SteamedOrder(Order):
    def __init__(self, originalMaterial):
        super().__init__("清蒸", originalMaterial)

    def processingOrder(self):
        if(self._chef is not None):
            return self._chef.steamFood(self._originalMaterial)
        return ""

class SpicyOrder(Order):
    def __init__(self, originalMaterial):
        super().__init__("香辣炒", originalMaterial)

    def processingOrder(self):
        if (self._chef is not None):
            return self._chef.stirFriedFood(self._originalMaterial)
        return ""

class Waiter:
    def __init__(self, name):
        self.__name = name
        self.__order = None

    def receiveOrder(self, order):
        self.__order = order
        print("服務員%s：您的 %s 訂單已經收到,請耐心等待" % (self.__name, order.getDisplayName()))

    def placeOrder(self):
        food = self.__order.processingOrder()
        print("服務員%s：您的餐 %s 已經準備好，請您慢用!" % (self.__name, food))

class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass

class CommandImpl(Command):
    def __init__(self, receiver):
        self.__receiver = receiver

    def execute(self):
        self.__receiver.doSomething()

class Receiver:
    def doSomething(self):
        print("do something...")

class Invoker:
    def __init__(self):
        self.__command = None

    def setCommand(self, command):
        self.__command = command

    def action(self):
        if self.__command is not None:
            self.__command.execute()

def testOrder():
    waiter = Waiter("Anna")

    steamedOrder = SteamedOrder("大閘蟹")
    print("客戶David：我要一份 %s" % steamedOrder.getDisplayName())
    waiter.receiveOrder(steamedOrder)
    waiter.placeOrder()
    print()

    spicyOrder = SpicyOrder("大閘蟹")
    print("客戶Tony：我要一份 %s" % spicyOrder.getDisplayName())
    waiter.receiveOrder(spicyOrder)
    waiter.placeOrder()

def client():
    invoker = Invoker()
    command = CommandImpl(Receiver())
    invoker.setCommand(command)
    invoker.action()

testOrder()
client()
