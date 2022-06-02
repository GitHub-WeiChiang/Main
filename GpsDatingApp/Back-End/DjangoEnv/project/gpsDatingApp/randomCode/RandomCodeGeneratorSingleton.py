import random

import threading
lock = threading.Lock()

class RandomCodeGeneratorSingleton():

    __instance: object = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    RandomCodeGeneratorSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            RandomCodeGeneratorSingleton.__isFirstInit = True

    def generate(self, randomCodeType: int) -> str:
        verifyCode = ""
        i: int = 0
        while i < randomCodeType:
            j = random.choice(range(12))
            verifyCode += chr(random.choice(range(48, 58))) if j < 4 else chr(random.choice(range(65, 91))) if j < 8 else chr(random.choice(range(97, 123)))
            i += 1
        return verifyCode
