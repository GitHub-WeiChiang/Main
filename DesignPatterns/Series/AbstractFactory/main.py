from abc import ABC, abstractmethod

# 抽象的產品類型
class Sedan(ABC):
    @abstractmethod
    def turn_on_head_light(self) -> None:
        pass

class SUV(ABC):
    @abstractmethod
    def turn_on_head_light(self) -> None:
        pass

# 具體的產品類別
class BMWM5(Sedan):
    def turn_on_head_light(self) -> None:
        print("BMWM5 head light")

class BMWX5(SUV):
    def turn_on_head_light(self) -> None:
        print("BMWX5 head light")

class TeslaModelS(Sedan):
    def turn_on_head_light(self) -> None:
        print("Tesla ModelS head light")

class TeslaModelY(SUV):
    def turn_on_head_light(self) -> None:
        print("Tesla ModelY head light")

# 抽象工廠
class CarFactory(ABC):
    @abstractmethod
    def create_sedan(self) -> Sedan:
        pass

    @abstractmethod
    def create_suv(self) -> SUV:
        pass

# 具體的產品工廠
class BMWFactory(CarFactory):
    def create_sedan(self) -> Sedan:
        return BMWM5()

    def create_suv(self) -> SUV:
        return BMWX5()

class TeslaFactory(CarFactory):
    def create_sedan(self) -> Sedan:
        return TeslaModelS()
    
    def create_suv(self) -> SUV:
        return TeslaModelY()

# 客戶端
class BrandBooth:
    sedan: Sedan = None
    suv: SUV = None

    # 接收一個工廠
    def __init__(self, factory: CarFactory):
        # 實例的取得
        self.sedan = factory.create_sedan()
        self.suv = factory.create_suv()
    
    def show_time(self):
        self.sedan.turn_on_head_light()
        self.suv.turn_on_head_light()
    
if __name__ == '__main__':
    # 實作工廠
    bmw_factory = BMWFactory()
    # 將工廠交給客戶
    bmw_booth = BrandBooth(bmw_factory)
    # 使用所生成的物件
    bmw_booth.show_time()
    
    # 實作工廠
    tesla_factory = TeslaFactory()
    # 將工廠交給客戶
    tesla_booth = BrandBooth(tesla_factory)
    # 使用所生成的物件
    tesla_booth.show_time()
