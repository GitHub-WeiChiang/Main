from abc import ABC, abstractmethod

class Light(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

class KitchenLight(Light):
    def on(self):
        print("Kitchen light is on")

    def off(self):
        print("Kitchen light is off")

class LivingRoomLight(Light):
    def on(self):
        print("Living room light is on")

    def off(self):
        print("Living room light is off")

# 增加命令接口: 包含執行與撤銷的抽象方法
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass

# 創建具項命令: 實現命令接口
class LightOnCommand(Command):
    def __init__(self, light):
        # 具體燈類別引用: 成員變量
        self.light = light

    def execute(self):
        self.light.on()

    def undo(self):
        self.light.off()

# 創建具項命令: 實現命令接口
class LightOffCommand(Command):
    def __init__(self, light):
        # 具體燈類別引用: 成員變量
        self.light = light

    def execute(self):
        self.light.off()

    def undo(self):
        self.light.on()

# 控制器類別
class RemoteControl:
    def set_command(self, command):
        self.command = command

    def press_button(self):
        self.command.execute()

    def press_undo(self):
        self.command.undo()

class LightController2:
    def main(self):
        # 創建具體燈類別
        living_room_light = LivingRoomLight()
        kitchen_light = KitchenLight()

        # 創建具體命令
        living_room_light_on = LightOnCommand(living_room_light)
        kitchen_light_off = LightOffCommand(kitchen_light)

        # 創建控制器
        remote = RemoteControl()

        # 使用控制器
        remote.set_command(living_room_light_on)
        remote.press_button()
        remote.press_undo()

        # 使用控制器
        remote.set_command(kitchen_light_off)
        remote.press_button()
        remote.press_undo()

if __name__ == "__main__":
    light_controller2 = LightController2()
    light_controller2.main()
