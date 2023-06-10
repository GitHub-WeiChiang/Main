from abc import ABC, abstractmethod

# 顯示接口
class Display(ABC):
    # 更新溫度方法
    @abstractmethod
    def update(self, temperature):
        pass

# 實作 Display 接口
class CurrentTemperatureDisplay(Display):
    def update(self, temperature):
        print(f"Current Temperature: {temperature}")

# 實作 Display 接口
class TemperatureHistoryDisplay(Display):
    def update(self, temperature):
        print(f"Temperature History Updated with: {temperature}")

# 天氣站
class WeatherStation:
    # 對顯示設備的引用
    def __init__(self, current_temperature_display, temperature_history_display):
        self.temperature = None
        self.current_temperature_display = current_temperature_display
        self.temperature_history_display = temperature_history_display

    # 溫度更新方法
    def set_temperature(self, temperature):
        self.temperature = temperature
        self.current_temperature_display.update(temperature)
        self.temperature_history_display.update(temperature)


if __name__ == "__main__":
    # 創建顯示設備
    current_temperature_display = CurrentTemperatureDisplay()
    temperature_history_display = TemperatureHistoryDisplay()
    # 創建天氣站
    weather_station = WeatherStation(current_temperature_display, temperature_history_display)

    weather_station.set_temperature(25)
    weather_station.set_temperature(26)

    # 天氣站與顯示設備耦合性過高，
    # 如果需要添加新的顯示設備，
    # 需要在 weather_station 中修改成員變量，
    # 並於 set_temperature() 中修改具體邏輯，
    # 移除顯示設備亦然，
    # 這會使得代碼拓展與維護不易。
