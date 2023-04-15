class Projector:
    def on(self):
        print("Turning on the projector...")

    def off(self):
        print("Turning off the projector...")

class DVDPlayer:
    def play(self):
        print("Playing the movie...")

    def stop(self):
        print("Stopping the movie...")

class SoundSystem:
    def on(self):
        print("Turning on the sound system...")

    def off(self):
        print("Turning off the sound system...")

# 新增家庭劇院外觀類別
class HomeTheaterFacade:
    def __init__(self, projector, dvd_player, sound_system):
        # 建立子系統的引用
        self.projector = projector
        self.dvd_player = dvd_player
        self.sound_system = sound_system

    # 操作巨集: 開始觀看。
    def watch_movie(self):
        self.projector.on()
        self.dvd_player.play()
        self.sound_system.on()

    # 操作巨集: 停止觀看。
    def stop_movie(self):
        self.projector.off()
        self.dvd_player.stop()
        self.sound_system.off()

# 創建子系統
projector = Projector()
dvd_player = DVDPlayer()
sound_system = SoundSystem()

# 傳入子系統
home_theater = HomeTheaterFacade(projector, dvd_player, sound_system)

# 呼叫操作巨集
home_theater.watch_movie()

# 有效簡化客戶端的操作，
# 客戶無需了解子系統運作原理，
# 當子系統有變動時，
# 客戶無需進行任何更改
# 也提供了可維護性。
