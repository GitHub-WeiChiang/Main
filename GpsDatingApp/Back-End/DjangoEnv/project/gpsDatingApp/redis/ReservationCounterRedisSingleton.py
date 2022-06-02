from django.core.cache import cache

from gpsDatingApp.redis.RedisInterface import RedisInterface
from gpsDatingApp.dao.ReservationDaoSingleton import ReservationDaoSingleton
from gpsDatingApp.otherConfig.ListInitConfig import ListInitConfig
from gpsDatingApp.otherConfig.LifeCycleConfig import LifeCycleConfig

import threading
lock = threading.Lock()

class ReservationCounterRedisSingleton(RedisInterface):

    __instance: RedisInterface = None
    __isFirstInit: bool = False

    prefix: str = "rcrs"

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    ReservationCounterRedisSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            ReservationCounterRedisSingleton.__isFirstInit = True

    def set(self, reservationCounterInfo: dict) -> None:
        cache.set(self.prefix, reservationCounterInfo, timeout = LifeCycleConfig.INFO_TYPE_REDIS_DATA_LIFE_CYCLE)

    def count(self, city: str) -> None:
        # 避免死結
        if self.has() == False:
            self.get()

        with lock:
            reservationCounterInfo: dict = self.get()

            reservationCounterInfo[city] = reservationCounterInfo[city] + 1

            self.set(reservationCounterInfo)

    def get(self) -> dict:
        if self.has() == False:
            with lock:
                if self.has() == False:
                    value: dict = dict(ListInitConfig().REZ_CNTR_INFO_INIT_FORMAT)

                    unitList: list = ReservationDaoSingleton().getAll()
                    for unit in unitList:
                        value[unit.reserveCity] = value[unit.reserveCity] + 1

                    self.set(value)

        reservationCounterInfo: dict = cache.get(self.prefix)
        return reservationCounterInfo

    def has(self) -> bool:
        return cache.has_key(self.prefix)

    def delete(self) -> None:
        pass

    def ttl(self) -> None:
        pass
    