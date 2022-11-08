__author__ = "ChiangWei"
__date__ = "2022/05/09"

class MyBeautifulGril1(object):
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            MyBeautifulGril1.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            print("遇見" + name + "，我一見鍾情！")
            MyBeautifulGril1.__isFirstInit = True
        else:
            print("遇見" + name + "，我置若罔聞！")

    def showMyHeart(self):
        print(self.__name + "就我心中的唯一！")

serine = MyBeautifulGril1("serine")
serine.showMyHeart()
subin = MyBeautifulGril1("subin")
subin.showMyHeart()
print("id(serine): ", id(serine), ", id(subin): ", id(subin))

print()

class Singleton1(object):
    __instance = None
    __isFirstInit = False

    def __new__(cls, name):
        if not cls.__instance:
            Singleton1.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, name):
        if not self.__isFirstInit:
            self.__name = name
            Singleton1.__isFirstInit = True

    def getName(self):
        return self.__name

tony = Singleton1("Tony")
karry = Singleton1("Karry")
print(tony.getName(), karry.getName())
print("id(tony):", id(tony), "id(karry):", id(karry))
print("tony == karry:", tony == karry)

print()

class Singleton2(type):
    def __init__(cls, what, bases=None, dict=None):
        super().__init__(what, bases, dict)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class CustomClass(metaclass=Singleton2):
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

tony = CustomClass("Tony")
karry = CustomClass("Karry")
print(tony.getName(), karry.getName())
print("id(tony):", id(tony), "id(karry):", id(karry))
print("tony == karry:", tony == karry)

print()

def singletonDecorator(cls, *args, **kwargs):
    instance = {}

    def wrapperSingleton(*args, **kwargs):
        if cls not in instance:
            instance[cls] = cls(*args, **kwargs)
        return instance[cls]

    return wrapperSingleton

@singletonDecorator
class Singleton3:
    def __init__(self, name):
        self.__name = name

    def getName(self):
        return self.__name

tony = Singleton3("Tony")
karry = Singleton3("Karry")
print(tony.getName(), karry.getName())
print("id(tony):", id(tony), "id(karry):", id(karry))
print("tony == karry:", tony == karry)

print()

@singletonDecorator
class MyBeautifulGril2(object):
    def __init__(self, name):
        self.__name = name
        if self.__name == name:
            print("遇見" + name + "，我一見鍾情！")
        else:
            print("遇見" + name + "，我置若罔聞！")

    def showMyHeart(self):
        print(self.__name + "就我心中的唯一！")

def TestLove():
    serine = MyBeautifulGril2("serine")
    serine.showMyHeart()
    subin = MyBeautifulGril2("subin")
    subin.showMyHeart()
    print("id(serine):", id(serine), " id(subin):", id(subin))

TestLove()
