# 這是一個低階類別
class BMW:
    def rent_bmw(self, model: str):
        print(f'BMW rented {model}')

# 這是一個低階類別
class Mercedes:
    def rent_mercedes(self, model: str):
        print(f'Mercedes rented {model}')

# 這是一個高階類別
class CarRentalAgency:
    def rent_car(self, brand: str, model: str):
        # 因為高階類別與低階類別直接關聯，導致不好的設計
        if brand == 'BMW':
            BMW().rent_bmw(model)
        elif brand == 'Mercedes':
            Mercedes().rent_mercedes(model)

agency = CarRentalAgency()
agency.rent_car('BMW', 'X5')
agency.rent_car('Mercedes', 'GLE')
