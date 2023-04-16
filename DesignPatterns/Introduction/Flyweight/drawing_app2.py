from typing import Dict
from abc import ABC, abstractmethod

# 形狀接口
class Shape(ABC):
    # 畫圖通用抽象方法
    @abstractmethod
    def draw(self, x: int, y: int, radius: int):
        pass

# 圓形享元類別 (幫助存取共享狀態)
class CircleFlyweight(Shape):
    def __init__(self, color: str):
        # 此示例中，顏色為共享狀態
        self.color = color

    # 實現抽象方法
    def draw(self, x: int, y: int, radius: int):
        print(f'Drawing circle of color {self.color} at position ({x}, {y}) with radius {radius}')

# 形狀工廠
class ShapeFactory:
    # 用於存取被共用的實例，
    # 鍵為顏色，值為實例。
    _circle_map: Dict[str, CircleFlyweight] = {}

    @staticmethod
    def get_circle(color: str) -> CircleFlyweight:
        # 此處要注意多執行緒下可能重複生成單一實例的問題

        circle = ShapeFactory._circle_map.get(color)

        if circle is None:
            circle = CircleFlyweight(color)
            ShapeFactory._circle_map[color] = circle
            print(f'Creating circle of color: {color}')

        return circle

class DrawingApp2:
    @staticmethod
    def main():
        red_circle = ShapeFactory.get_circle("red")
        red_circle.draw(10, 10, 50)

        blue_circle = ShapeFactory.get_circle("blue")
        blue_circle.draw(20, 20, 60)

        another_red_circle = ShapeFactory.get_circle("red")
        another_red_circle.draw(30, 30, 40)

if __name__ == "__main__":
    DrawingApp2.main()
