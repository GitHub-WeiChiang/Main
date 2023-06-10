from abc import ABC, abstractmethod

# 觀察者接口
class Observer(ABC):
    @abstractmethod
    def update(self, temperature):
        pass

# 實作觀察者接口
class CurrentTemperatureDisplay(Observer):
    def update(self, temperature):
        print(f"Current Temperature: {temperature}")

# 實作觀察者接口
class TemperatureHistoryDisplay(Observer):
    def update(self, temperature):
        print(f"Temperature History Updated with: {temperature}")

# 主題接口
class Subject(ABC):
    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass

# 氣象站實作主題接口
class WeatherStation(Subject):
    def __init__(self):
        self.temperature = None
        # 觀察者集合
        self.observers = []

    def add_observer(self, observer):
        self.observers.append(observer)

    def remove_observer(self, observer):
        self.observers.remove(observer)

    # 設定溫度
    def set_temperature(self, temperature):
        self.temperature = temperature
        # 同時調用 notify_observers() 方法
        self.notify_observers()

    # 遍歷並通知所有在集合中 (已註冊) 的觀察者
    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.temperature)

        # 無論有多少觀察者，
        # 透過 add_observer() 與 remove_observer() 方法，
        # 都無需修改 notify_observers() 方法邏輯。


if __name__ == "__main__":
    # 創建氣象站
    weather_station = WeatherStation()

    # 創建顯示器
    current_temperature_display = CurrentTemperatureDisplay()
    temperature_history_display = TemperatureHistoryDisplay()

    # 註冊顯示器
    weather_station.add_observer(current_temperature_display)
    weather_station.add_observer(temperature_history_display)

    # 測試
    weather_station.set_temperature(25)
    weather_station.set_temperature(26)

    # 此設計雖然看起來較為複雜，
    # 但實際上的維護與擴展其實較為容易，
    # 因為可以透過 add_observer() 與 remove_observer() 方法，
    # 在運行時期動態的添加或移除實作觀察者接口的類別 (顯示器)，
    # 而非只能在編譯時期決定。
