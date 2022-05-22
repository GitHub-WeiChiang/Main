__author__ = "ChiangWei"
__date__ = "2022/05/22"

from copy import copy, deepcopy

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def showMyself(self):
        print("我是" + self.__name + ",年齡" + str(self.__age) + ".")

    def coding(self):
        print("我是碼農，我用程序改變世界，Coding...")

    def reading(self):
        print("閱讀使我快樂！知識使我成長！如飢似渴地閱讀是生活的一部分...")

    def fallInLove(self):
        print("春風吹，月亮明，花前月下好相約...")

    def clone(self):
        return copy(self)

class PetStore:
    def __init__(self, name):
        self.__name = name
        self.__petList = []

    def setName(self, name):
        self.__name = name

    def showMyself(self):
        print("%s 寵物店有以下寵物：" % self.__name)
        for pet in self.__petList:
            print(pet + "\t", end="")
        print()

    def addPet(self, pet):
        self.__petList.append(pet)

class Clone:
    def clone(self):
        return copy(self)

    def deepClone(self):
        return deepcopy(self)

class Person2(Clone):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def showMyself(self):
        print("我是" + self.__name + ",年齡" + str(self.__age) + ".")

    def coding(self):
        print("我是碼農，我用程序改變世界，Coding...")

    def reading(self):
        print("閱讀使我快樂！知識使我成長！如飢似渴地閱讀是生活的一部分...")

    def fallInLove(self):
        print("春風吹，月亮明，花前月下好相約...")

def testClone():
    tony = Person("Tony", 27)
    tony.showMyself()
    tony.coding()

    tony1 = tony.clone()
    tony1.showMyself()
    tony1.reading()

    tony2 = tony.clone()
    tony2.showMyself()
    tony2.fallInLove()

def testPetStore():
    petter = PetStore("Petter")
    petter.addPet("小狗Coco")
    print("petter：", end="")
    petter.showMyself()
    print()

    petter1 = deepcopy(petter)
    petter1.addPet("小猫Amy")
    print("petter1：", end="")
    petter1.showMyself()
    print("petter：", end="")
    petter.showMyself()
    print()

    petter2 = copy(petter)
    petter2.addPet("小兔Ricky")
    print("petter2：", end="")
    petter2.showMyself()
    print("petter：", end="")
    petter.showMyself()

def testList():
    list = [1, 2, 3];
    list1 = list;
    print("id(list):", id(list))
    print("id(list1):", id(list1))
    print("修改之前：")
    print("list:", list)
    print("list1:", list1)
    list1.append(4);
    print("修改之後：")
    print("list:", list)
    print("list1:", list1)

testClone()
testPetStore()
testList()
