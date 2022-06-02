from django.core.cache import cache

from gpsDatingApp.redis.RedisInterface import RedisInterface
from gpsDatingApp.otherConfig.LifeCycleConfig import LifeCycleConfig
from gpsDatingApp.dao.BlockadeListInfoDaoSingleton import BlockadeListInfoDaoSingleton

import threading
lock = threading.Lock()

class BlockadeListInfoRedisSingleton(RedisInterface):

    __instance: RedisInterface = None
    __isFirstInit: bool = False

    prefix: str = "blirs_"

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    BlockadeListInfoRedisSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            BlockadeListInfoRedisSingleton.__isFirstInit = True

    def set(self, userId: str, blockadeList: list) -> None:
        # add type prefix
        userId = BlockadeListInfoRedisSingleton.prefix + userId

        # value
        value: list = blockadeList
        
        cache.set(userId, value, timeout = LifeCycleConfig.INFO_TYPE_REDIS_DATA_LIFE_CYCLE)

    def get(self, userId: str) -> list:
        # add type prefix
        userIdKey = BlockadeListInfoRedisSingleton.prefix + userId

        if self.has(userId) == False:
            with lock:
                if self.has(userId) == False:
                    unit = BlockadeListInfoDaoSingleton().findByUserId(userId)

                    if unit == None:
                        return []
                    
                    self.set(userId, unit.blockadeList)

        blockadeList: list = cache.get(userIdKey)
        return blockadeList

    def has(self, userId: str) -> bool:
        # add type prefix
        userId = BlockadeListInfoRedisSingleton.prefix + userId

        return cache.has_key(userId)

    def delete(self, userId: str) -> None:
        # add type prefix
        userId = BlockadeListInfoRedisSingleton.prefix + userId

        cache.delete(userId)

    def ttl(self, userId: str) -> int:
        # add type prefix
        userId = BlockadeListInfoRedisSingleton.prefix + userId

        return cache.ttl(userId)
