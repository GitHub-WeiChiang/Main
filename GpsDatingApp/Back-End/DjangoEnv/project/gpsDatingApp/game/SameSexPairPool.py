from gpsDatingApp.game.PairPool import PairPool
from gpsDatingApp.logger.Logger import Logger

import threading
lock = threading.Lock()

class SameSexPairPool(PairPool):

    __instance: PairPool = None
    __isFirstInit: bool = False

    # 配對池
    pairPool: dict = None
    
    # 配對結果
    pairResult: list = None
    
    def __init__(self):
        self.pairPool = {}
        self.pairResult = []

    def clear(self) -> bool:
        self.pairPool = {}
        self.pairResult = []

        return True

    def addInPool(self, userId: str, city: str, district: str, pairkey: str) -> bool:
        userInfo: dict = {}
        userInfo["userId"]: str = userId
        userInfo["city"]: str = city
        userInfo["district"]: str = district

        # 將使用者放入 pairPool: dict 對應的 pairkey 中
        if pairkey not in self.pairPool:
            with lock:
                if pairkey not in self.pairPool:
                    self.pairPool[pairkey] = []
        self.pairPool[pairkey].append(userInfo)

        return True

    async def pairing(self) -> bool:
        # 迭代池內的所有配對佇列
        for key, value in self.pairPool.items():
            # 用於儲存第一次匹配失敗的 user 以進行第二次匹配 (只進行兩次)
            temp: list = []

            # 開始第一次匹配
            while len(value) >= 2:
                # 前後配
                userInfoA: dict = value.pop(0)
                userInfoB: dict = value.pop(0)

                # 配對成功
                if self.isPairing(userInfoA["userId"], userInfoB["userId"]) == True and await self.becomeFriends(userInfoA["userId"], userInfoB["userId"], userInfoA["city"], userInfoA["district"], key.split("_")[0], key.split("_")[1]) == True:
                    self.pairResult.append([userInfoA["userId"], userInfoB["userId"]])
                # 配對失敗
                else:
                    temp.append(userInfoA)
                    temp.append(userInfoB)

            # 開始第二次匹配
            while len(temp) >= 3:
                # 跳格配，避免配到同一人
                userInfoA: dict = temp.pop(0)
                userInfoB: dict = temp.pop(1)

                # 配對成功
                if self.isPairing(userInfoA["userId"], userInfoB["userId"]) == True and await self.becomeFriends(userInfoA["userId"], userInfoB["userId"], userInfoA["city"], userInfoA["district"], key.split("_")[0], key.split("_")[1]) == True:
                    self.pairResult.append([userInfoA["userId"], userInfoB["userId"]])

        return True
