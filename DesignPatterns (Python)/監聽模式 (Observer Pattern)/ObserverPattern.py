__author__ = "ChiangWei"
__date__ = "2022/04/17"

# from abc import ABCMeta, abstractmethod

# class WaterHeater:
#     def __init__(self):
#         self.__observers = []
#         self.__temperature = 25

#     def getTemperature(self):
#         return self.__temperature

#     def setTemperature(self, temperature):
#         self.__temperature = temperature
#         print("當前溫度為: " + str(self.__temperature) + "°C")
#         self.notifies()

#     def addObserver(self, observer):
#         self.__observers.append(observer)

#     def notifies(self):
#         for o in self.__observers:
#             o.update(self)

# class Observer(metaclass=ABCMeta):
#     @abstractmethod
#     def update(self, waterHeater):
#         pass

# class WashingMode(Observer):
#     def update(self, waterHeater):
#         if waterHeater.getTemperature() >= 50 and waterHeater.getTemperature() < 70:
#             print("水已燒好！溫度正好，可以用來洗澡了。")

# class DrinkingMode(Observer):
#     def update(self, waterHeater):
#         if waterHeater.getTemperature() >= 100:
#             print("水已燒開！可以用來飲用了。")

# heater = WaterHeater()

# washingObser = WashingMode()
# drinkingObser = DrinkingMode()

# heater.addObserver(washingObser)
# heater.addObserver(drinkingObser)

# heater.setTemperature(40)
# heater.setTemperature(60)
# heater.setTemperature(100)

from abc import ABCMeta, abstractmethod

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, observable, object):
        pass

class Observable:
    def __init__(self):
        self.__observers = []

    def addObserver(self, observer):
        self.__observers.append(observer)

    def removeObserver(self, observer):
        self.__observers.remove(observer)

    def notifyObservers(self, object=0):
        for o in self.__observers:
            o.update(self, object)

class WaterHeater(Observable):
    def __init__(self):
        super().__init__()
        self.__temperature = 25

    def getTemperature(self):
        return self.__temperature

    def setTemperature(self, temperature):
        self.__temperature = temperature
        print("當前溫度是: " + str(self.__temperature) + "°C")
        self.notifyObservers()

class WashingMode(Observer):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 50 and observable.getTemperature() < 70:
            print("水已燒好！溫度正好，可以用來洗澡了。")

class DrinkingMode(Observer):
    def update(self, observable, object):
        if isinstance(observable, WaterHeater) and observable.getTemperature() >= 100:
            print("水已燒開！可以用來飲用了。")

heater = WaterHeater()

washingObser = WashingMode()
drinkingObser = DrinkingMode()

heater.addObserver(washingObser)
heater.addObserver(drinkingObser)

heater.setTemperature(40)
heater.setTemperature(60)
heater.setTemperature(100)
