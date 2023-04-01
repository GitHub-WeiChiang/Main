from abc import ABC, abstractmethod
from math import pi

# 組件接口
class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

# 具體實現
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return pi * self.radius * self.radius

# 具體實現
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side * self.side

# 組合類
class ShapeGroup(Shape):
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
        self.shapes.append(shape)

    # 遍歷子組件
    def get_area(self):
        total_area = 0
        for shape in self.shapes:
            total_area += shape.get_area()
        return total_area

if __name__ == "__main__":
    # 第一個子組件群
    circle = Circle(5)
    square = Square(4)

    # 放入第一個組合類
    shape_group1 = ShapeGroup()
    shape_group1.add_shape(circle)
    shape_group1.add_shape(square)

    # 第二個子組件群
    circle2 = Circle(3)
    # 放入第二個組合類
    shape_group2 = ShapeGroup()
    shape_group2.add_shape(circle2)

    # 根組合類
    main_group = ShapeGroup()
    # 搜集所有組合類
    main_group.add_shape(shape_group1)
    main_group.add_shape(shape_group2)

    print("Total area:", main_group.get_area())
