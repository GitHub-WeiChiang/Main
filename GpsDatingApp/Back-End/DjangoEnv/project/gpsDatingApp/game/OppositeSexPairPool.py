from gpsDatingApp.game.PairPool import PairPool
from gpsDatingApp.redis.UserInfoRedisSingleton import UserInfoRedisSingleton
from gpsDatingApp.logger.Logger import Logger

import threading
lock = threading.Lock()

class OppositeSexPairPool(PairPool):

    __instance: PairPool = None
    __isFirstInit: bool = False

    # 男配對池
    malePairPool: dict = None
    # 女配對池
    femalePairPool: dict = None

    # 配對結果
    pairResult: list = None
    
    def __init__(self):
        self.malePairPool = {}
        self.femalePairPool = {}
        self.pairResult = []

    def clear(self) -> bool:
        self.malePairPool = {}
        self.femalePairPool = {}
        self.pairResult = []

        return True

    def addInPool(self, userId: str, city: str, district: str, pairkey: str) -> bool:
        userInfo: dict = {}
        userInfo["userId"]: str = userId
        userInfo["city"]: str = city
        userInfo["district"]: str = district
        
        userSex: str = UserInfoRedisSingleton().get(userId)["sex"]

        if userSex == "Male":
            if pairkey not in self.malePairPool:
                with lock:
                    if pairkey not in self.malePairPool:
                        self.malePairPool[pairkey] = []
            self.malePairPool[pairkey].append(userInfo)
        else:
            if pairkey not in self.femalePairPool:
                with lock:
                    if pairkey not in self.femalePairPool:
                        self.femalePairPool[pairkey] = []
            self.femalePairPool[pairkey].append(userInfo)

        return True

    async def pairing(self) -> bool:
        # 迭代女配對池內的所有配對佇列
        for key in self.femalePairPool.keys():
            # 用於儲存第一次匹配失敗的 user 以進行第二次匹配 (只進行兩次)
            maleTemp: list = []
            femaleTemp: list = []

            # 開始第一次匹配
            while key in self.malePairPool and len(self.femalePairPool[key]) >= 1 and len(self.malePairPool[key]) >= 1:
                # 按序配
                userInfoA: str = self.femalePairPool[key].pop(0)
                userInfoB: str = self.malePairPool[key].pop(0)

                # 配對成功
                if self.isPairing(userInfoA["userId"], userInfoB["userId"]) == True and self.becomeFriends(userInfoA["userId"], userInfoB["userId"], userInfoA["city"], userInfoA["district"], key.split("_")[0], key.split("_")[1]) == True:
                    self.pairResult.append([userInfoA["userId"], userInfoB["userId"]])
                # 配對失敗
                else:
                    femaleTemp.append(userInfoA)
                    maleTemp.append(userInfoB)

            # 開始第二次匹配
            while len(femaleTemp) >= 2 and len(maleTemp) >= 2:
                # 交叉配，避免配到同一人
                userInfoA: str = femaleTemp.pop(0)
                userInfoB: str = maleTemp.pop(1)

                # 配對成功
                if self.isPairing(userInfoA["userId"], userInfoB["userId"]) == True and self.becomeFriends(userInfoA["userId"], userInfoB["userId"], userInfoA["city"], userInfoA["district"], key.split("_")[0], key.split("_")[1]) == True:
                    self.pairResult.append([userInfoA["userId"], userInfoB["userId"]])
        
        return True
