# 中介的抽象類別，用於高階類別與低階類別間的溝通
class CarManufactory:
    def rent(self, model: str):
        pass

# 這是一個低階類別，實作中介的抽象類別
class BMW(CarManufactory):
    def rent(self, model: str):
        print(f'BMW rented {model}')

# 這是一個低階類別，實作中介的抽象類別
class Mercedes(CarManufactory):
    def rent(self, model: str):
        print(f'Mercedes rented {model}')

# 這是一個新的低階類別，也實作中介的抽象類別
class Honda(CarManufactory):
    def rent(self, model: str):
        print(f'Honda rented {model}')

# 這是一個高階類別
class CarRentalAgency2:
    def rent_car(self, manufactory: CarManufactory, model: str):
        # 依賴於抽象類別，不太需要因應低階類別的改變而改變
        manufactory.rent(model)

agency = CarRentalAgency2()
agency.rent_car(BMW(), 'X5')
agency.rent_car(Mercedes(), 'GLE')
agency.rent_car(Honda(), 'Accord')
