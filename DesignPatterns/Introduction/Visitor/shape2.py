from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def accept(self, visitor):
        pass

class Circle(Shape):
    def accept(self, visitor):
        visitor.visit_circle(self)

class Rectangle(Shape):
    def accept(self, visitor):
        visitor.visit_rectangle(self)

# 訪問者接口
class Visitor(ABC):
    # 訪問圓形
    @abstractmethod
    def visit_circle(self, circle):
        pass

    # 訪問長方形
    @abstractmethod
    def visit_rectangle(self, rectangle):
        pass

# 具體訪問者: 實作訪問者接口
class DrawVisitor(Visitor):
    def visit_circle(self, circle):
        print("Drawing a circle")

    def visit_rectangle(self, rectangle):
        print("Drawing a rectangle")

# 具體訪問者: 實作訪問者接口
class ResizeVisitor(Visitor):
    def visit_circle(self, circle):
        print("Resizing a circle")

    def visit_rectangle(self, rectangle):
        print("Resizing a rectangle")

def main():
    # 圖形
    circle = Circle()
    rectangle = Rectangle()

    # 訪問者
    draw_visitor = DrawVisitor()
    resize_visitor = ResizeVisitor()

    # 傳入 draw 行為
    circle.accept(draw_visitor)
    rectangle.accept(draw_visitor)

    # 傳入 resize 行為
    circle.accept(resize_visitor)
    rectangle.accept(resize_visitor)

if __name__ == "__main__":
    main()

    # 當需要新功能時，僅需創建新的 Visitor 類別，
    # 無需修改 Shape 接口與具體圖形類。
