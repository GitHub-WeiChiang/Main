# 攝氏溫度街口
class CelsiusTemperature:
    def getCTemperature(self):
        pass

# 華氏溫度類別
class FahrenheitTemperature:
    def __init__(self, temperature):
        self.temperature = temperature

    def getTemperature(self):
        return self.temperature

# 華氏轉攝氏溫度適配器類別 (繼承華氏溫度類別並實作攝氏溫度街口)
class FahrenheitToCelsiusAdapter(FahrenheitTemperature, CelsiusTemperature):
    def __init__(self, temperature):
        super().__init__(temperature)

    # 轉換過程
    def getCTemperature(self):
        return (super().getTemperature() - 32) * 5 / 9

f = FahrenheitTemperature(100)
c = FahrenheitToCelsiusAdapter(f.getTemperature())
print("The temperature is", c.getCTemperature(), "degrees Celsius.")
