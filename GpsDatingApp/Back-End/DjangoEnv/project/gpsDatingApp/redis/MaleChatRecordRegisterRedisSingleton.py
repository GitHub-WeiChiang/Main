from gpsDatingApp.redis.ChatRecordRegisterRedis import ChatRecordRegisterRedis

import threading
lock = threading.Lock()

class MaleChatRecordRegisterRedisSingleton(ChatRecordRegisterRedis):

    __instance: ChatRecordRegisterRedis = None
    __isFirstInit: bool = False

    prefix: str = "mcrrrs_"

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    MaleChatRecordRegisterRedisSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            MaleChatRecordRegisterRedisSingleton.__isFirstInit = True
