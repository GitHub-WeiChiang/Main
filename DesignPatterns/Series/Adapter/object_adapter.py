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

# 華氏轉攝氏溫度適配器類別 (實作攝氏溫度街口)
class FahrenheitToCelsiusAdapter(CelsiusTemperature):
    # 實例化時取得華氏溫度類別實例
    def __init__(self, fahrenheit):
        # 物件適配器相較於類別適配器，有更低的耦合度
        self.fahrenheit = fahrenheit

    # 轉換過程 (適配器)
    def getCTemperature(self):
        return (self.fahrenheit.getTemperature() - 32) * 5 / 9

if __name__ == '__main__':
    f = FahrenheitTemperature(100)
    c = FahrenheitToCelsiusAdapter(f)
    print("The temperature is", c.getCTemperature(), "degrees Celsius.")
