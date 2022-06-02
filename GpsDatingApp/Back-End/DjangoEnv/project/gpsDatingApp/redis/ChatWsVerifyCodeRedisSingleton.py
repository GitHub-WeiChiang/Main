from django.core.cache import cache

from gpsDatingApp.redis.RedisInterface import RedisInterface
from gpsDatingApp.otherConfig.LifeCycleConfig import LifeCycleConfig

import threading
lock = threading.Lock()

class ChatWsVerifyCodeRedisSingleton(RedisInterface):

    __instance: RedisInterface = None
    __isFirstInit: bool = False

    prefix: str = "cwvcrs_"

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    ChatWsVerifyCodeRedisSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            ChatWsVerifyCodeRedisSingleton.__isFirstInit = True

    def set(self, userId: str, verifyCode: str) -> None:
        # add type prefix
        userId = ChatWsVerifyCodeRedisSingleton.prefix + userId

        cache.set(userId, verifyCode, timeout = LifeCycleConfig.WS_VERIFY_CODE_TIME_LIMIT)

    def get(self, userId: str) -> str:
        # add type prefix
        userId = ChatWsVerifyCodeRedisSingleton.prefix + userId

        verifyCode: str = cache.get(userId)

        return verifyCode

    def has(self, userId: str) -> bool:
        # add type prefix
        userId = ChatWsVerifyCodeRedisSingleton.prefix + userId

        return cache.has_key(userId)

    def delete(self, userId: str) -> None:
        # add type prefix
        userId = ChatWsVerifyCodeRedisSingleton.prefix + userId
        
        cache.delete(userId)

    def ttl(self) -> None:
        pass
