from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

    def resize(self):
        print("Resizing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

    def resize(self):
        print("Resizing a rectangle")

def main():
    circle = Circle()
    rectangle = Rectangle()

    circle.draw()
    rectangle.draw()

    circle.resize()
    rectangle.resize()

if __name__ == "__main__":
    main()

    # 若需要添加新操作，例如圖形旋轉與面積計算，
    # 需要在抽象接口中添加新的方法宣告，
    # 後在實作該接口的類中進行實作。
