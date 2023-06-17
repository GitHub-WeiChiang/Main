# 狀態接口: 定義需要實作的行為
class State:
    def walk(self):
        pass

    def run(self):
        pass

    def jump(self):
        pass

    def idle(self):
        pass


# 閒置狀態類別: 實作狀態接口
class IdleState(State):
    def __init__(self, character):
        self.character = character

    def walk(self):
        self.character.state = self.character.walking_state
        print("The character is now walking.")

    def run(self):
        print("The character cannot run right now.")

    def jump(self):
        print("The character cannot jump right now.")

    def idle(self):
        print("The character is already idle.")


# 行走狀態類別: 實作狀態接口
class WalkingState(State):
    def __init__(self, character):
        self.character = character

    def walk(self):
        print("The character is already walking.")

    def run(self):
        self.character.state = self.character.running_state
        print("The character is now running.")

    def jump(self):
        print("The character cannot jump right now.")

    def idle(self):
        self.character.state = self.character.idle_state
        print("The character is now idle.")


# 跑步狀態類別: 實作狀態接口
class RunningState(State):
    def __init__(self, character):
        self.character = character

    def walk(self):
        print("The character cannot walk right now.")

    def run(self):
        print("The character is already running.")

    def jump(self):
        self.character.state = self.character.jumping_state
        print("The character is now jumping.")

    def idle(self):
        self.character.state = self.character.idle_state
        print("The character is now idle.")


# 跳躍狀態類別: 實作狀態接口
class JumpingState(State):
    def __init__(self, character):
        self.character = character

    def walk(self):
        print("The character cannot walk right now.")

    def run(self):
        print("The character cannot run right now.")

    def jump(self):
        print("The character is already jumping.")

    def idle(self):
        self.character.state = self.character.idle_state
        print("The character is now idle.")


# 角色類別
class Character:
    def __init__(self):
        # 創建所有狀態並傳入自身參考
        self.idle_state = IdleState(self)
        self.walking_state = WalkingState(self)
        self.running_state = RunningState(self)
        self.jumping_state = JumpingState(self)

        # 設定預設狀態
        self.state = self.idle_state

    def walk(self):
        self.state.walk()

    def run(self):
        self.state.run()

    def jump(self):
        self.state.jump()

    def idle(self):
        self.state.idle()


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

    # 在這段狀態模式的示例代碼中，
    # 狀態轉換的邏輯和可執行行為被相互隔離，
    # 分離的狀態與行為，
    # 有利於提升狀態轉換邏輯修改與狀態新增刪除的便利性，
    # 且消除了條件判斷語句，間接提升了代碼的可閱讀性。
