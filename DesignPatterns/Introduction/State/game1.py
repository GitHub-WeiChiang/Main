# 角色類別
class Character:
    def __init__(self):
        # 狀態變量: 用於記錄當前狀態 (預設為 idle 閒置)，
        # 運行方法 (行為) 時，
        # 需因應當前狀態採取不同行動。
        self.state = "idle"

    def walk(self):
        if self.state == "idle":
            self.state = "walking"
            print("The character is now walking.")
        else:
            print("The character cannot walk right now.")

    def run(self):
        if self.state == "walking":
            self.state = "running"
            print("The character is now running.")
        else:
            print("The character cannot run right now.")

    def jump(self):
        if self.state == "running":
            self.state = "jumping"
            print("The character is now jumping.")
        else:
            print("The character cannot jump right now.")

    def idle(self):
        self.state = "idle"
        print("The character is now idle.")


if __name__ == "__main__":
    # 創建角色實例
    character = Character()

    # The character is now walking.
    character.walk()
    # The character is now running.
    character.run()
    # The character is now jumping.
    character.jump()
    # The character is now idle.
    character.idle()

    # The character cannot run right now.
    character.run()
    # The character cannot jump right now.
    character.jump()

    # 狀態轉換的邏輯與行為，
    # 皆強耦合於 Character 類別中，
    # 若狀態轉換邏輯需要修改，
    # 亦或是有狀態的新增與刪除，
    # 都需要不斷地修改 Character 類別，
    # 這不但違反了開閉原則，
    # 也間接導致 Character 類別在維護與拓展上的不便。
