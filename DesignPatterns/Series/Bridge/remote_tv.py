from abc import ABC, abstractmethod

# 遙控器抽象類，定義遙控器該具備的功能，並引用設備接口
class RemoteControl(ABC):
    def __init__(self, device):
        self.device = device

    @abstractmethod
    def powerOn(self):
        pass

    @abstractmethod
    def powerOff(self):
        pass

    @abstractmethod
    def volumeUp(self):
        pass

    @abstractmethod
    def volumeDown(self):
        pass

# 設備接口，定義設備需自行實作的功能
class Device(ABC):
    @abstractmethod
    def powerOn(self):
        pass

    @abstractmethod
    def powerOff(self):
        pass

    @abstractmethod
    def setVolume(self, volume):
        pass

    @abstractmethod
    def getVolume(self):
        pass

# 具體設備，實作設備方法內容
class TV(Device):
    def __init__(self):
        self.volume = 50

    def powerOn(self):
        print("TV is on.")

    def powerOff(self):
        print("TV is off.")

    def setVolume(self, volume):
        if volume > 100:
            self.volume = 100
        elif volume < 0:
            self.volume = 0
        else:
            self.volume = volume
        print("TV volume set to", self.volume)

    def getVolume(self):
        return self.volume

# 具體設備，實作設備方法內容
class DVDPlayer(Device):
    def __init__(self):
        self.volume = 50

    def powerOn(self):
        print("DVD player is on.")

    def powerOff(self):
        print("DVD player is off.")

    def setVolume(self, volume):
        if volume > 100:
            self.volume = 100
        elif volume < 0:
            self.volume = 0
        else:
            self.volume = volume
        print("DVD player volume set to", self.volume)

    def getVolume(self):
        return self.volume

# 具體遙控器
class BasicRemote(RemoteControl):
    def __init__(self, device):
        super().__init__(device)

    def powerOn(self):
        print("Basic Remote: power on ->", end=" ")
        self.device.powerOn()

    def powerOff(self):
        print("Basic Remote: power off ->", end=" ")
        self.device.powerOff()

    def volumeUp(self):
        self.device.setVolume(self.device.getVolume() + 10)

    def volumeDown(self):
        self.device.setVolume(self.device.getVolume() - 10)

# 具體遙控器
class AdvancedRemote(RemoteControl):
    def __init__(self, device):
        super().__init__(device)

    def powerOn(self):
        print("Advanced Remote: power on ->", end=" ")
        self.device.powerOn()

    def powerOff(self):
        print("Advanced Remote: power off ->", end=" ")
        self.device.powerOff()

    def volumeUp(self):
        self.device.setVolume(self.device.getVolume() + 5)

    def volumeDown(self):
        self.device.setVolume(self.device.getVolume() - 5)


if __name__ == "__main__":
    tv = TV()
    dvdPlayer = DVDPlayer()

    basicRemote = BasicRemote(tv)
    basicRemote.powerOn()
    basicRemote.powerOff()
    basicRemote.volumeUp()
    basicRemote.volumeDown()

    advancedRemote = AdvancedRemote(dvdPlayer)
    advancedRemote.powerOn()
    advancedRemote.powerOff()
    advancedRemote.volumeUp()
    advancedRemote.volumeDown()

    basicRemote = BasicRemote(dvdPlayer)
    basicRemote.powerOn()
    basicRemote.powerOff()
    basicRemote.volumeUp()
    basicRemote.volumeDown()

    # 此時無論是要增加新設備或是新遙控器，
    # 都可以獨立新增無需修改另一方的代碼。
