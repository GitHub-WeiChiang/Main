__author__ = "ChiangWei"
__date__ = "2022/06/19"

from abc import ABCMeta, abstractmethod

class Coffee(metaclass=ABCMeta):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    @abstractmethod
    def getTaste(self):
        pass

class LatteCaffe(Coffee):
    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "輕柔而香醇"

class MochaCoffee(Coffee):
    def __init__(self, name):
        super().__init__(name)

    def getTaste(self):
        return "絲滑與醇厚"

class Coffeemaker:
    @staticmethod
    def makeCoffee(coffeeBean):
        if(coffeeBean == "拿鐵咖啡豆"):
            coffee = LatteCaffe("拿鐵咖啡")
        elif(coffeeBean == "摩卡咖啡豆"):
            coffee = MochaCoffee("摩卡咖啡")
        else:
            raise ValueError("不支持的參數：%s" % coffeeBean)
        return coffee

def testCoffeeMaker():
    latte = Coffeemaker.makeCoffee("拿鐵咖啡豆")
    print("%s已為您準備好了，口感：%s。請慢慢享用！" % (latte.getName(), latte.getTaste()) )
    mocha = Coffeemaker.makeCoffee("摩卡咖啡豆")
    print("%s已為您準備好了，口感：%s。請慢慢享用！" % (mocha.getName(), mocha.getTaste()))

testCoffeeMaker()
