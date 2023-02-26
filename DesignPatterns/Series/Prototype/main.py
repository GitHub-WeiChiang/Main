from abc import ABC, abstractmethod

# 抽象類，定義球拍所需的參數
class RacketPrototype(ABC):
    def __init__(self, brand, model, weight, balancePoint):
        self.brand = brand
        self.model = model
        self.weight = weight
        self.balancePoint = balancePoint

    # 定義克隆抽象方法
    @abstractmethod
    def clone(self):
        pass

# 具體原型類
class WilsonTennisRacket(RacketPrototype):
    def __init__(self, brand, model, weight, balancePoint):
        super().__init__(brand, model, weight, balancePoint)

    # 完善克隆方法
    def clone(self):
        print("Wilson clone: {} {} {} {}".format(self.brand, self.model, self.weight, self.balancePoint))
        return WilsonTennisRacket(self.brand, self.model, self.weight, self.balancePoint)

# 具體原型類
class HeadTennisRacket(RacketPrototype):
    def __init__(self, brand, model, weight, balancePoint):
        super().__init__(brand, model, weight, balancePoint)

    # 完善克隆方法
    def clone(self):
        print("Head clone: {} {} {} {}".format(self.brand, self.model, self.weight, self.balancePoint))
        return HeadTennisRacket(self.brand, self.model, self.weight, self.balancePoint)

# 原型管理器
class TennisRacketPrototypeManager:
    # 型號為 Key，實體物件為 Value
    racketMap = {}

    # 取得該型號的複製品
    @staticmethod
    def getClonedRacket(model):
        r = TennisRacketPrototypeManager.racketMap.get(model)
        return r.clone()

    # 初始化各個模型
    @staticmethod
    def buildProtypes():
        r1 = WilsonTennisRacket("Wilson", "Pro Staff", 320.0, 32.5)
        TennisRacketPrototypeManager.racketMap["pro staff"] = r1

        h1 = HeadTennisRacket("Head", "Graphene 360 Speed", 320.0, 32.5)
        TennisRacketPrototypeManager.racketMap["graphene 360"] = h1

def main():
    # 建立模型 Sample
    TennisRacketPrototypeManager.buildProtypes()

    # 取的複製品
    a = TennisRacketPrototypeManager.getClonedRacket("pro staff")
    b = TennisRacketPrototypeManager.getClonedRacket("pro staff")
    c = TennisRacketPrototypeManager.getClonedRacket("pro staff")
    
    print(id(a))
    print(id(b))
    print(id(c))

    print(a == b)
    print(b == c)
    print(c == a)
    
if __name__ == '__main__':
    main()
