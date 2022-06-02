from gpsDatingApp.redis.ChatRecordRegisterRedis import ChatRecordRegisterRedis

import threading
lock = threading.Lock()

class FemaleChatRecordRegisterRedisSingleton(ChatRecordRegisterRedis):

    __instance: ChatRecordRegisterRedis = None
    __isFirstInit: bool = False

    prefix: str = "fcrrrs_"

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    FemaleChatRecordRegisterRedisSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            FemaleChatRecordRegisterRedisSingleton.__isFirstInit = True
