# 紅綠燈狀態接口
class TrafficLightState:
    def handle(self, traffic_light):
        pass


# 紅燈狀態: 實作紅綠燈狀態接口
class RedState(TrafficLightState):
    def handle(self, traffic_light):
        print("Red Light: Stopped")
        traffic_light.state = GreenState()


# 黃燈狀態: 實作紅綠燈狀態接口
class YellowState(TrafficLightState):
    def handle(self, traffic_light):
        print("Yellow Light: Be prepared to stop")
        traffic_light.state = RedState()


# 綠燈狀態: 實作紅綠燈狀態接口
class GreenState(TrafficLightState):
    def handle(self, traffic_light):
        print("Green Light: Go")
        traffic_light.state = YellowState()


# 紅綠燈類別
class TrafficLight:
    def __init__(self):
        # 當前狀態: 預設為紅燈
        self.state = RedState()

    # 狀態切換
    def change(self):
        self.state.handle(self)


if __name__ == "__main__":
    # 創建紅綠燈實例
    traffic_light = TrafficLight()

    for _ in range(6):
        traffic_light.change()
