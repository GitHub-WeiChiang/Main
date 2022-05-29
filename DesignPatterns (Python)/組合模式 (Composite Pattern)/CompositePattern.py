__author__ = "ChiangWei"
__date__ = "2022/05/29"

from abc import ABCMeta, abstractmethod

class ComputerComponent(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def showInfo(self, indent = ""):
        pass

    def isComposite(self):
        return False

    def startup(self, indent = ""):
        print("%s%s 準備開始工作..." % (indent, self._name))

    def shutdown(self, indent = ""):
        print("%s%s 即將結束工作..." % (indent, self._name))

class CPU(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%sCPU:%s, 可以進行高速計算。" % (indent, self._name))

class MemoryCard(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s內存:%s,可以緩存數據，讀寫速度快。" % (indent, self._name))

class HardDisk(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s硬盤:%s,可以永久存儲數據，容量大。" % (indent, self._name) )

class GraphicsCard(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s顯卡:%s,可以高速計算和處理圖形圖像。" % (indent, self._name) )

class Battery(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s電源:%s,可以持續給主板和外接配件供電。" % (indent, self._name) )

class Fan(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s風扇:%s，輔助CPU散熱。" % (indent, self._name) )

class Displayer(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print("%s顯示器:%s，負責內容的顯示。" % (indent, self._name) )

class ComputerComposite(ComputerComponent):
    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def showInfo(self, indent):
        print("%s,由以下部件組成:" % (self._name) )
        indent += "\t"
        for element in self._components:
            element.showInfo(indent)

    def isComposite(self):
        return True

    def addComponent(self, component):
        self._components.append(component)

    def removeComponent(self, component):
        self._components.remove(component)

    def startup(self, indent):
        super().startup(indent)
        indent += "\t"
        for element in self._components:
            element.startup(indent)

    def shutdown(self, indent):
        super().shutdown(indent)
        indent += "\t"
        for element in self._components:
            element.shutdown(indent)

class Mainboard(ComputerComposite):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "主板:", end="")
        super().showInfo(indent)

class ComputerCase(ComputerComposite):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "機箱:", end="")
        super().showInfo(indent)

class Computer(ComputerComposite):
    def __init__(self, name):
        super().__init__(name)

    def showInfo(self, indent):
        print(indent + "電腦:", end="")
        super().showInfo(indent)

def testComputer():
    mainBoard = Mainboard("GIGABYTE Z170M M-ATX")
    mainBoard.addComponent(CPU("Intel Core i5-6600K"))
    mainBoard.addComponent(MemoryCard("Kingston Fury DDR4"))
    mainBoard.addComponent(HardDisk("Kingston V300 "))
    mainBoard.addComponent(GraphicsCard("Colorful iGame750"))

    computerCase = ComputerCase("SAMA MATX")
    computerCase.addComponent(mainBoard)
    computerCase.addComponent(Battery("Antec VP 450P"))
    computerCase.addComponent(Fan("DEEPCOOL 120T"))

    computer = Computer("Tony DIY电脑")
    computer.addComponent(computerCase)
    computer.addComponent(Displayer("AOC LV243XIP"))

    computer.showInfo("")
    print("\n開機過程:")
    computer.startup("")
    print("\n關機過程:")
    computer.shutdown("")

# testComputer()

class Component(metaclass=ABCMeta):
    def __init__(self, name):
        self._name = name

    def getName(self):
        return self._name

    def isComposite(self):
        return False

    @abstractmethod
    def feature(self, indent):
        pass

class Composite(Component):
    def __init__(self, name):
        super().__init__(name)
        self._components = []

    def addComponent(self, component):
        self._components.append(component)

    def removeComponent(self, component):
        self._components.remove(component)

    def isComposite(self):
        return True

    def feature(self, indent):
        print("name：%s" % self._name)
        indent += "\t"
        for component in self._components:
            print(indent, end="")
            component.feature(indent)

class ComponentImplA(Component):
    def __init__(self, name):
        super().__init__(name)

    def feature(self, indent):
        print("name：%s" % self._name)

def testComposite():
    tony = ComponentImplA("Tony")
    karry = ComponentImplA("Karry")
    composite = Composite("Composite")
    composite.addComponent(tony)
    composite.addComponent(karry)
    composite.feature("")

testComposite()
