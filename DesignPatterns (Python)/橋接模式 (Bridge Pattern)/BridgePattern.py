__author__ = "ChiangWei"
__date__ = "2022/07/02"

from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    def __init__(self, color):
        self._color = color

    @abstractmethod
    def getShapeType(self):
        pass

    def getShapeInfo(self):
        return self._color.getColor() + "的" + self.getShapeType()

class Rectange(Shape):
    def __init__(self, color):
        super().__init__(color)

    def getShapeType(self):
        return "矩形"

class Ellipse(Shape):
    def __init__(self, color):
        super().__init__(color)

    def getShapeType(self):
        return "橢圓"

class Color(metaclass=ABCMeta):
    @abstractmethod
    def getColor(self):
        pass

class Red(Color):
    def getColor(self):
        return "紅色"

class Green(Color):
    def getColor(self):
        return "綠色"

def testShap():
    redRect = Rectange(Red())
    print(redRect.getShapeInfo())
    greenRect = Rectange(Green())
    print(greenRect.getShapeInfo())

    redEllipse = Ellipse(Red())
    print(redEllipse.getShapeInfo())
    greenEllipse = Ellipse(Green())
    print(greenEllipse.getShapeInfo())

testShap()
