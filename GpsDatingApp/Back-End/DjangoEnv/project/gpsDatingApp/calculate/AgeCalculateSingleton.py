import datetime

import threading
lock = threading.Lock()

class AgeCalculateSingleton():

    __instance: object = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    AgeCalculateSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            AgeCalculateSingleton.__isFirstInit = True

    def isAdult(self, birthday: str) -> bool:
        return self.calculate(birthday) >= 18

    def calculate(self, birthday: str) -> int:
        # 出生日期
        born: datetime.datetime = None

        try:
            # 將字串轉換為日期型態
            born = datetime.datetime.strptime(birthday, "%Y-%m-%d")
        except:
            return -1

        # 因為 UTC 慢 8 小時，加回
        today: datetime.date = (datetime.datetime.now() + datetime.timedelta(hours = 8)).date()
        # 計算年齡
        age: int = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        
        return age
