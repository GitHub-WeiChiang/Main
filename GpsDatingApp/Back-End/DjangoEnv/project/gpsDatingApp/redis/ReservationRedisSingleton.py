from django.core.cache import cache

from gpsDatingApp.redis.RedisInterface import RedisInterface
from gpsDatingApp.dao.ReservationDaoSingleton import ReservationDaoSingleton
from gpsDatingApp.otherConfig.LifeCycleConfig import LifeCycleConfig

import threading
lock = threading.Lock()

class ReservationRedisSingleton(RedisInterface):

    __instance: RedisInterface = None
    __isFirstInit: bool = False

    prefix: str = "rrs"

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    ReservationRedisSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            ReservationRedisSingleton.__isFirstInit = True

    def set(self, reservationEamilSet: set) -> None:
        cache.set(self.prefix, reservationEamilSet, timeout = LifeCycleConfig.INFO_TYPE_REDIS_DATA_LIFE_CYCLE)

    def add(self, email: str) -> None:
        # 避免死結
        if self.has() == False:
            self.get()
        
        with lock:
            reservationEamilSet: set = self.get()

            reservationEamilSet.add(email)

            self.set(reservationEamilSet)

    def get(self) -> set:
        if self.has() == False:
            with lock:
                if self.has() == False:
                    reservationEamilSet: set = set()

                    unitList: list = ReservationDaoSingleton().getAll()
                    for unit in unitList:
                        reservationEamilSet.add(unit.email)

                    self.set(reservationEamilSet)
        
        reservationEamilSet: set = cache.get(self.prefix)
        return reservationEamilSet

    def has(self) -> None:
        return cache.has_key(self.prefix)

    def delete(self) -> None:
        pass

    def ttl(self) -> None:
        pass
