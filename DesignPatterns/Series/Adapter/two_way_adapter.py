# 攝氏溫度街口
class CelsiusTemperature:
    def get_temperature(self):
        pass

# 華氏溫度街口
class FahrenheitTemperature:
    def get_temperature(self):
        pass

# 攝氏溫度類別
class Celsius(CelsiusTemperature):
    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

# 華氏溫度類別
class Fahrenheit(FahrenheitTemperature):
    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature

# 雙向適配器類別 (實作兩個街口)
class TwoWayAdapter(CelsiusTemperature, FahrenheitTemperature):
    def __init__(self, celsius=None, fahrenheit=None):
        if celsius:
            self.celsius = celsius
            # 生成另一個溫度類別實例 (並進行溫度轉換)
            self.fahrenheit = Fahrenheit(celsius.get_temperature() * 9 / 5 + 32)
        else:
            self.fahrenheit = fahrenheit
            # 生成另一個溫度類別實例 (並進行溫度轉換)
            self.celsius = Celsius((fahrenheit.get_temperature() - 32) * 5 / 9)

    def get_celsius_temperature(self):
        return self.celsius.get_temperature()

    def get_fahrenheit_temperature(self):
        return self.fahrenheit.get_temperature()


celsius = Celsius(25)
fahrenheit = Fahrenheit(77)

adapter1 = TwoWayAdapter(celsius=celsius)
adapter2 = TwoWayAdapter(fahrenheit=fahrenheit)

print("Celsius temperature:", adapter1.get_celsius_temperature())
print("Fahrenheit temperature:", adapter1.get_fahrenheit_temperature())

print("Celsius temperature:", adapter2.get_celsius_temperature())
print("Fahrenheit temperature:", adapter2.get_fahrenheit_temperature())
