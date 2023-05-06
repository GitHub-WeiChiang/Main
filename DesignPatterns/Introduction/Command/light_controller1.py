from abc import ABC, abstractmethod

# 電燈接口
class Light(ABC):
    # 抽象方法
    @abstractmethod
    def on(self):
        pass

    # 抽象方法
    @abstractmethod
    def off(self):
        pass

# 具體電燈: 實現電燈接口中的抽象方法
class LivingRoomLight(Light):
    def on(self):
        print("Living room light is on")

    def off(self):
        print("Living room light is off")

# 具體電燈: 實現電燈接口中的抽象方法
class KitchenLight(Light):
    def on(self):
        print("Kitchen light is on")

    def off(self):
        print("Kitchen light is off")

class LightController1:
    def main(self):
        living_room_light = LivingRoomLight()
        kitchen_light = KitchenLight()

        # 此操作方法使電燈具象類別與客戶端耦合過強，
        # 客戶端需要了解每個具象類別的實現細節。
        kitchen_light.on()
        kitchen_light.off()
        living_room_light.on()
        living_room_light.off()

if __name__ == "__main__":
    light_controller1 = LightController1()
    light_controller1.main()
