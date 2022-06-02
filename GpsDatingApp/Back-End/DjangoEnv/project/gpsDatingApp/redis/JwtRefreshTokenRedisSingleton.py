from django.core.cache import cache

from gpsDatingApp.redis.RedisInterface import RedisInterface
from gpsDatingApp.otherConfig.LifeCycleConfig import LifeCycleConfig

import threading
lock = threading.Lock()

class JwtRefreshTokenRedisSingleton(RedisInterface):

    __instance: RedisInterface = None
    __isFirstInit: bool = False

    prefix: str = "jrtrs_"

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    JwtRefreshTokenRedisSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            JwtRefreshTokenRedisSingleton.__isFirstInit = True

    def set(self, userId: str, securityCode: str, token: str) -> None:
        # add type prefix
        userId = JwtRefreshTokenRedisSingleton.prefix + userId

        # value
        value: dict = {}
        value["securityCode"]: str = securityCode
        value["token"]: str = token

        cache.set(userId, value, timeout = LifeCycleConfig.JWT_REFRESH_TOKEN_TIME_LIMIT)

    def get(self, userId: str) -> dict:
        # add type prefix
        userId = JwtRefreshTokenRedisSingleton.prefix + userId

        refreshTokenDict: dict = cache.get(userId)
        return refreshTokenDict

    def has(self, userId: str) -> bool:
        # add type prefix
        userId = JwtRefreshTokenRedisSingleton.prefix + userId

        return cache.has_key(userId)

    def delete(self, userId: str) -> None:
        # add type prefix
        userId = JwtRefreshTokenRedisSingleton.prefix + userId

        cache.delete(userId)

    def ttl(self, userId: str) -> int:
        # add type prefix
        userId = JwtRefreshTokenRedisSingleton.prefix + userId

        return cache.ttl(userId)
