# 創建一個汽車類別，內部與車子動力及車色類別聚合
class Car:
    # 因透過聚合方式，即便動力與烤漆選擇增加，也不會造成類別爆炸
    enery = None
    color = None
    
    def __init__(self, energy, color):
        self.enery = energy
        self.color = color
    
    def move(self):
        print(f'{self.enery.__str__()} {self.color.__str__()}')

# 汽車動力接口
class Energy:
    pass

# 汽車烤漆接口
class Color:
    pass

# 實作能源介面
class Gasoline(Energy):
    def __str__(self): return 'gasoline'

class Electric(Energy):
    def __str__(self): return 'electric'

# 實作烤漆介面
class Red(Color):
    def __str__(self): return 'red'

class Blue(Color):
    def __str__(self): return 'blue'

Car(Gasoline(), Red()).move()
Car(Electric(), Blue()).move()
