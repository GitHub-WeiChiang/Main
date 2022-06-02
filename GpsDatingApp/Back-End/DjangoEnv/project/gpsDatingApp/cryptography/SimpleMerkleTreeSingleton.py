import hashlib

import threading
lock = threading.Lock()

class SimpleMerkleTreeSingleton():

    __instance: object = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    SimpleMerkleTreeSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            SimpleMerkleTreeSingleton.__isFirstInit = True

    def getTreeRootHash(self, userId: str, securityCode: str) -> str:
        userIdHash: str = hashlib.sha256(userId.encode('utf-8')).hexdigest()
        securityCodeHash: str = hashlib.sha256(securityCode.encode('utf-8')).hexdigest()

        temp: str = userIdHash + securityCodeHash

        treeRootHash: str = str(hashlib.sha256(temp.encode('utf-8')).hexdigest())
        return treeRootHash
