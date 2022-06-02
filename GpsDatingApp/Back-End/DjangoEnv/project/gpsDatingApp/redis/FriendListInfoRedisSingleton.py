from django.core.cache import cache

from gpsDatingApp.redis.RedisInterface import RedisInterface
from gpsDatingApp.otherConfig.LifeCycleConfig import LifeCycleConfig
from gpsDatingApp.dao.FriendListInfoDaoSingleton import FriendListInfoDaoSingleton

import threading
lock = threading.Lock()

class FriendListInfoRedisSingleton(RedisInterface):

    __instance: RedisInterface = None
    __isFirstInit: bool = False

    prefix: str = "flirs_"

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    FriendListInfoRedisSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            FriendListInfoRedisSingleton.__isFirstInit = True

    def set(self, userId: str, friendList: list) -> None:
        # add type prefix
        userId = FriendListInfoRedisSingleton.prefix + userId

        # value
        value: list = friendList
        
        cache.set(userId, value, timeout = LifeCycleConfig.INFO_TYPE_REDIS_DATA_LIFE_CYCLE)

    def get(self, userId: str) -> list:
        # add type prefix
        userIdKey = FriendListInfoRedisSingleton.prefix + userId

        if self.has(userId) == False:
            with lock:
                if self.has(userId) == False:
                    unit = FriendListInfoDaoSingleton().findByUserId(userId)

                    if unit == None:
                        return []
                    
                    self.set(userId, unit.friendList)

        friendList: list = cache.get(userIdKey)
        return friendList

    def has(self, userId: str) -> bool:
        # add type prefix
        userId = FriendListInfoRedisSingleton.prefix + userId

        return cache.has_key(userId)

    def delete(self, userId: str) -> None:
        # add type prefix
        userId = FriendListInfoRedisSingleton.prefix + userId

        cache.delete(userId)

    def ttl(self, userId: str) -> int:
        # add type prefix
        userId = FriendListInfoRedisSingleton.prefix + userId

        return cache.ttl(userId)
