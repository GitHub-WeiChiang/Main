import re

import threading
lock = threading.Lock()

class EmailCheckerSingleton():

    __instance: object = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    EmailCheckerSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            EmailCheckerSingleton.__isFirstInit = True

    def check(self, email: str) -> bool:
        p = re.compile(r"[^@]+@[^@]+\.[^@]+")
        if not p.match(email):
            return False
        else:
            return True
