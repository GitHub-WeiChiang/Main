# Singleton

import math

import threading
lock = threading.Lock()

class GameConfig():

    __instance: object = None
    __isFirstInit: bool = False

    # 抓取到小數點第幾位
    takeNumberOfDecimalPlaces: int = 4
    # 無條件捨去運算式運算元
    truncateExpressionOperant: float = math.pow(10, takeNumberOfDecimalPlaces)
    # 加入狀態時間限制
    joinStateTimeLimit: int = 5
    # 緩衝時間
    bufferTime: int = 1

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    GameConfig.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            GameConfig.__isFirstInit = True
