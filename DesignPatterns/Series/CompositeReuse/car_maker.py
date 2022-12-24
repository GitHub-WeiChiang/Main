# 透過動能作為分類進行汽車類別設計
class GasolineCar:
    def move(self):
        print('gasoline move')

class ElectricCar:
    def move(self):
        print('electric move')

# 幫車子上色透過繼承方式實現
# 一種車有兩個顏色，兩種車就有四個子類別
# 一種車有四個顏色，兩種車就有八個子類別
# 未來如果增加車色，會造成類別量大爆炸
class RedGasolineCar(GasolineCar):
    def move(self):
        print('red gasoline move')

class BlueGasolineCar(GasolineCar):
    def move(self):
        print('blue gasoline move')

c = RedGasolineCar()
c.move()
