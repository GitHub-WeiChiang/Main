from abc import ABC, abstractmethod

# 所有具體車型主接口
class Car(ABC):
    @abstractmethod
    def startEngine(self):
        pass

    @abstractmethod
    def turnOffEngine(self):
        pass

# 具體車型 A
class ModelA(Car):
    def startEngine(self):
        print("modelA startEngine")
        return True

    def turnOffEngine(self):
        print("modelA turnOffEngine")

# 具體車型 B
class ModelB(Car):
    def startEngine(self):
        print("modelB startEngine")
        return True
    
    def turnOffEngine(self):
        print("modelB turnOffEngine")

# 工廠接口
class CarFactory(ABC):
    # 創建方法 (抽象)
    @abstractmethod
    def makeCar(self):
        pass

# 具體工廠
class ModelAFactory(CarFactory):
    def makeCar(self):
        modelA = ModelA()

        # 創建實體車車
        if modelA.startEngine() == True:
            modelA.turnOffEngine()
            return modelA
        else:
            return None

# 具體工廠
class ModelBFactory(CarFactory):
    def makeCar(self):
        modelB = ModelB()

        # 創建實體車車
        if modelB.startEngine() == True:
            modelB.turnOffEngine()
            return modelB
        else:
            return None

# 客戶端代碼，汽車倉儲管理
class TuringStorage:
    carStorage = [None] * 10

    def importCars(self):
        factoryA = ModelAFactory()
        factoryB = ModelBFactory()

        for i in range(5):
            self.carStorage[i] = factoryA.makeCar()
        for i in range(5, 10):
            self.carStorage[i] = factoryB.makeCar()

storage = TuringStorage()
storage.importCars()
