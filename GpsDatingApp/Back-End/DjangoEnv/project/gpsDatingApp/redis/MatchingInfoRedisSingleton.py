from django.core.cache import cache

from gpsDatingApp.redis.RedisInterface import RedisInterface
from gpsDatingApp.otherConfig.LifeCycleConfig import LifeCycleConfig
from gpsDatingApp.dao.MatchingInfoDaoSingleton import MatchingInfoDaoSingleton

import threading
lock = threading.Lock()

class MatchingInfoRedisSingleton(RedisInterface):

    __instance: RedisInterface = None
    __isFirstInit: bool = False

    prefix: str = "mirs_"

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    MatchingInfoRedisSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            MatchingInfoRedisSingleton.__isFirstInit = True

    def set(self, userId: str, matchingAge: list, matchingKind: int) -> None:
        # add type prefix
        userId = MatchingInfoRedisSingleton.prefix + userId

        # value
        value: dict = {}
        value["matchingAge"]: list = matchingAge
        value["matchingKind"]: int = matchingKind
        
        cache.set(userId, value, timeout = LifeCycleConfig.INFO_TYPE_REDIS_DATA_LIFE_CYCLE)

    def get(self, userId: str) -> dict:
        # add type prefix
        userIdKey = MatchingInfoRedisSingleton.prefix + userId

        if self.has(userId) == False:
            with lock:
                if self.has(userId) == False:
                    unit = MatchingInfoDaoSingleton().findByUserId(userId)

                    if unit == None:
                        return {}
                    
                    self.set(userId, unit.matchingAge, unit.matchingKind)

        matchingInfoDict: dict = cache.get(userIdKey)
        return matchingInfoDict

    def has(self, userId: str) -> bool:
        # add type prefix
        userId = MatchingInfoRedisSingleton.prefix + userId

        return cache.has_key(userId)

    def delete(self, userId: str) -> None:
        # add type prefix
        userId = MatchingInfoRedisSingleton.prefix + userId

        cache.delete(userId)

    def ttl(self, userId: str) -> int:
        # add type prefix
        userId = MatchingInfoRedisSingleton.prefix + userId

        return cache.ttl(userId)
