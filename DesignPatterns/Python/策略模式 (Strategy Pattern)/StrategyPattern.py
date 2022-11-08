__author__ = "ChiangWei"
__date__ = "2022/06/17"

from abc import ABCMeta, abstractmethod

class IVehicle(metaclass=ABCMeta):
    @abstractmethod
    def running(self):
        pass

class SharedBicycle(IVehicle):
    def running(self):
        print("騎共享單車 (輕快便捷)", end='')

class ExpressBus(IVehicle):
    def running(self):
        print("坐快速公交 (經濟綠色)", end='')

class Express(IVehicle):
    def running(self):
        print("打快車 (快速方便)", end='')

class Subway(IVehicle):
    def running(self):
        print("坐地鐵 (高效安全)", end='')

class Classmate:
    def __init__(self, name, vechicle):
        self.__name = name
        self.__vechicle = vechicle

    def attendTheDinner(self):
        print(self.__name + " ", end='')
        self.__vechicle.running()
        print(" 來參加聚餐！")

def testTheDinner():
    joe = Classmate("Joe", SharedBicycle())
    joe.attendTheDinner()
    helen = Classmate("Helen", Subway())
    helen.attendTheDinner()
    henry = Classmate("Henry", ExpressBus())
    henry.attendTheDinner()
    ruby = Classmate("Ruby", Express())
    ruby.attendTheDinner()

testTheDinner()
