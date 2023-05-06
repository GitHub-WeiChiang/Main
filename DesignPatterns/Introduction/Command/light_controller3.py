from abc import ABC, abstractmethod
from typing import List

class Light(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    # 多了調整亮度的抽象方法
    @abstractmethod
    def increase_brightness(self):
        pass

class KitchenLight(Light):
    def on(self):
        print("Kitchen light is on")

    def off(self):
        print("Kitchen light is off")

    def increase_brightness(self):
        print("Kitchen light brightness increased")

class LivingRoomLight(Light):
    def on(self):
        print("Living room light is on")

    def off(self):
        print("Living room light is off")

    def increase_brightness(self):
        print("Living room light brightness increased")

class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

class LightOnCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

class LightOffCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

# 創建新命令供客戶端調用
class LightIncreaseCommand(Command):
    def __init__(self, light):
        self.light = light

    def execute(self):
        self.light.increase_brightness()

    def undo(self):
        # Implement an appropriate undo operation, such as decreasing brightness
        print("TODO")

class Fan:
    def on(self):
        print("Fan is on")

    def off(self):
        print("Fan is off")

class FanOnCommand(Command):
    def __init__(self, fan):
        self.fan = fan

    def execute(self):
        self.fan.on()

    def undo(self):
        self.fan.off()

class AllLightsOffCommand(Command):
    def __init__(self, lights: List[Light]):
        self.lights = lights

    def execute(self):
        for light in self.lights:
            light.off()

    def undo(self):
        for light in self.lights:
            light.on()

class RemoteControl:
    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

    def press_undo(self):
        self.command.undo()

class LightController3:
    def main(self):
        living_room_light = LivingRoomLight()
        kitchen_light = KitchenLight()
        fan = Fan()

        living_room_light_on = LightOnCommand(living_room_light)
        kitchen_light_off = LightOffCommand(kitchen_light)
        # 創建新命令: 亮度調整
        kitchen_light_increase = LightIncreaseCommand(kitchen_light)
        # 創建新命令: 風扇
        fan_on = FanOnCommand(fan)
        # 創建巨集命令: 一次執行多個命令
        all_lights_off = AllLightsOffCommand([living_room_light, kitchen_light])

        # 控制器無需進行任何更動
        remote = RemoteControl()

        remote.set_command(living_room_light_on)
        remote.press_button()
        remote.press_undo()

        remote.set_command(kitchen_light_off)
        remote.press_button()
        remote.press_undo()

        # 傳入新命令
        remote.set_command(kitchen_light_increase)
        remote.press_button()

        remote.set_command(fan_on)
        remote.press_button()

        remote.set_command(all_lights_off)
        remote.press_button()

if __name__ == "__main__":
    light_controller3 = LightController3()
    light_controller3.main()
