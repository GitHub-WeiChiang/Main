# Singleton

import threading
lock = threading.Lock()

class ConsumerInfo():

    __instance: object = None
    __isFirstInit: bool = False

    gamePlayerIndieSet: set = set()
    chatPlayerIndieSet: set = set()

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    ConsumerInfo.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            ConsumerInfo.__isFirstInit = True
