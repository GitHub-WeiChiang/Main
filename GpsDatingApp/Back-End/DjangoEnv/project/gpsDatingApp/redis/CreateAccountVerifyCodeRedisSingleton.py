from django.core.cache import cache

from gpsDatingApp.redis.RedisInterface import RedisInterface
from gpsDatingApp.otherConfig.LifeCycleConfig import LifeCycleConfig

import threading
lock = threading.Lock()

class CreateAccountVerifyCodeRedisSingleton(RedisInterface):

    __instance: RedisInterface = None
    __isFirstInit: bool = False

    prefix: str = "cavcrs_"

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    CreateAccountVerifyCodeRedisSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            CreateAccountVerifyCodeRedisSingleton.__isFirstInit = True

    def set(self, email: str, verifyCode: str, errorTimes: int = 0, timeout: int = LifeCycleConfig.CREATE_ACCOUNT_VERIFY_CODE_TIME_LIMIT) -> None:
        # add type prefix
        email = CreateAccountVerifyCodeRedisSingleton.prefix + email

        # value
        value: dict = {}
        value["verifyCode"]: str = verifyCode
        value["errorTimes"]: int = errorTimes

        cache.set(email, value, timeout = timeout)

    def get(self, email: str) -> dict:
        # add type prefix
        email = CreateAccountVerifyCodeRedisSingleton.prefix + email

        verifyCodeDict: dict = cache.get(email)

        return verifyCodeDict

    def has(self, email: str) -> bool:
        # add type prefix
        email = CreateAccountVerifyCodeRedisSingleton.prefix + email

        return cache.has_key(email)

    def delete(self, email: str) -> None:
        # add type prefix
        email = CreateAccountVerifyCodeRedisSingleton.prefix + email
        
        cache.delete(email)

    def ttl(self, email: str) -> int:
        # add type prefix
        email = CreateAccountVerifyCodeRedisSingleton.prefix + email

        return cache.ttl(email)
