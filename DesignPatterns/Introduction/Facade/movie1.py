# 投影器類別
class Projector:
    def on(self):
        print("Turning on the projector...")

    def off(self):
        print("Turning off the projector...")

# DVD 播放器類別
class DVDPlayer:
    def play(self):
        print("Playing the movie...")

    def stop(self):
        print("Stopping the movie...")

# 音響系統類別
class SoundSystem:
    def on(self):
        print("Turning on the sound system...")

    def off(self):
        print("Turning off the sound system...")

# 創建子系統
projector = Projector()
dvd_player = DVDPlayer()
sound_system = SoundSystem()

# 操作子系統
projector.on()
dvd_player.play()
sound_system.on()

# 若未來子系統數量增加，
# 客戶端需清楚知曉所需系統操作方式，
# 且操作過程相對繁瑣。
