__author__ = "ChiangWei"
__date__ = "2022/05/28"

from abc import ABCMeta, abstractmethod

# class ReceiveParcel(metaclass=ABCMeta):
#     def __init__(self, name):
#         self.__name = name

#     def getName(self):
#         return self.__name

#     @abstractmethod
#     def receive(self, parcelContent):
#         pass

# class TonyReception(ReceiveParcel):
#     def __init__(self, name, phoneNum):
#         super().__init__(name)
#         self.__phoneNum = phoneNum

#     def getPhoneNum(self):
#         return self.__phoneNum

#     def receive(self, parcelContent):
#         print("貨物主人:%s，手機號：%s" % (self.getName(), self.getPhoneNum()) )
#         print("接收到一個包裹，包裹內容:%s" % parcelContent)


# class WendyReception(ReceiveParcel):
#     def __init__(self, name, receiver):
#         super().__init__(name)
#         self.__receiver = receiver

#     def receive(self, parcelContent):
#         print("我是%s的朋友，我來幫他代收快遞！" % (self.__receiver.getName() + "") )
#         if(self.__receiver is not None):
#             self.__receiver.receive(parcelContent)
#         print("代收人:%s" % self.getName())

# def testReceiveParcel():
#     tony = TonyReception("Tony", "18512345678")
#     print("Tony接收:")
#     tony.receive("雪地靴")
#     print()

#     print("Wendy代收:")
#     wendy = WendyReception("Wendy", tony)
#     wendy.receive("雪地靴")

# testReceiveParcel()

class Subject(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def request(self, content = ''):
        pass


class RealSubject(Subject):
    def request(self, content):
        print("RealSubject todo something...")


class ProxySubject(Subject):
    def __init__(self, name, subject):
        super().__init__(name)
        self._realSubject = subject

    def request(self, content = ''):
        self.preRequest()
        if(self._realSubject is not None):
            self._realSubject.request(content)
        self.afterRequest()

    def preRequest(self):
        print("preRequest")

    def afterRequest(self):
        print("afterRequest")

# def testProxy():
#     realObj = RealSubject('RealSubject')
#     proxyObj = ProxySubject('ProxySubject', realObj)
#     proxyObj.request()

# testProxy()

class TonyReception(Subject):
    def __init__(self, name, phoneNum):
        super().__init__(name)
        self.__phoneNum = phoneNum

    def getPhoneNum(self):
        return self.__phoneNum

    def request(self, content):
        print("貨物主人:%s，手機號：%s" % (self.getName(), self.getPhoneNum()))
        print("接收到一個包裹，包裹內容:%s" % str(content))


class WendyReception(ProxySubject):
    def __init__(self, name, receiver):
        super().__init__(name, receiver)

    def preRequest(self):
        print("我是%s的朋友，我來幫他代收快遞！" % (self._realSubject.getName() + ""))

    def afterRequest(self):
        print("代收人:%s" % self.getName())

def testReceiveParcel():
    tony = TonyReception("Tony", "18512345678")
    print("Tony接收:")
    tony.request("雪地靴")
    print()

    print("Wendy代收:")
    wendy = WendyReception("Wendy", tony)
    wendy.request("雪地靴")

testReceiveParcel()
