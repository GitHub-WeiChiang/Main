__author__ = "ChiangWei"
__date__ = "2022/06/05"

from abc import ABCMeta, abstractmethod

class SocketEntity:
    def __init__(self, numOfPin, typeOfPin):
        self.__numOfPin = numOfPin
        self.__typeOfPin = typeOfPin

    def getNumOfPin(self):
        return self.__numOfPin

    def setNumOfPin(self, numOfPin):
        self.__numOfPin = numOfPin

    def getTypeOfPin(self):
        return self.__typeOfPin

    def setTypeOfPin(self, typeOfPin):
        self.__typeOfPin = typeOfPin


class ISocket(metaclass=ABCMeta):
    def getName(self):
        pass

    def getSocket(self):
        pass


class ChineseSocket(ISocket):
    def getName(self):
        return  "國際插座"

    def getSocket(self):
        return SocketEntity(3, "八字扁型")


class BritishSocket:
    def name(self):
        return  "英標插座"

    def socketInterface(self):
        return SocketEntity(3, "T 字方型")

class AdapterSocket(ISocket):
    def __init__(self, britishSocket):
        self.__britishSocket = britishSocket

    def getName(self):
        return  self.__britishSocket.name() + "轉換器"

    def getSocket(self):
        socket = self.__britishSocket.socketInterface()
        socket.setTypeOfPin("八字扁型")
        return socket

def canChargeforDigtalDevice(name, socket):
    if socket.getNumOfPin() == 3 and socket.getTypeOfPin() == "八字扁型":
        isStandard = "符合"
        canCharge = "可以"
    else:
        isStandard = "不符合"
        canCharge = "不能"

    print("[%s]：\n針腳數量：%d，針腳類型：%s； %s中國標準，%s給大陸的電子設備充電！" % (name, socket.getNumOfPin(), socket.getTypeOfPin(), isStandard, canCharge))

def testSocket():
    chineseSocket = ChineseSocket()
    canChargeforDigtalDevice(chineseSocket.getName(), chineseSocket.getSocket())

    britishSocket = BritishSocket()
    canChargeforDigtalDevice(britishSocket.name(), britishSocket.socketInterface())

    adapterSocket = AdapterSocket(britishSocket)
    canChargeforDigtalDevice(adapterSocket.getName(), adapterSocket.getSocket())

testSocket()

class Target(metaclass=ABCMeta):
    @abstractmethod
    def function(self):
        pass

class Adaptee:
    def speciaficFunction(self):
        print("被適配對象的特殊功能")

class Adapter(Target):
    def __init__(self, adaptee):
        self.__adaptee = adaptee

    def function(self):
        print("進行功能的轉換")
        self.__adaptee.speciaficFunction()
