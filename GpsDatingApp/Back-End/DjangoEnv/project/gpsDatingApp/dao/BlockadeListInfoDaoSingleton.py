from asgiref.sync import sync_to_async

from gpsDatingApp.dao.DaoInterface import DaoInterface
from gpsDatingApp.models import blockadeListInfo

import threading
lock = threading.Lock()

class BlockadeListInfoDaoSingleton(DaoInterface):

    __instance: DaoInterface = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    BlockadeListInfoDaoSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            BlockadeListInfoDaoSingleton.__isFirstInit = True

    def add(self, userId: str) -> bool:
        try:
            unit = blockadeListInfo.objects.create(
                userId = userId
            )
            unit.save()
            
            return True
        except:
            return False

    def delete(self, userId: str) -> bool:
        try:
            unit = blockadeListInfo.objects.get(userId = userId)
            unit.delete()

            return True
        except:
            return False

    @sync_to_async
    def updateAll(self, userId: str, blockadeList: list) -> bool:
        try:
            unit = blockadeListInfo.objects.get(userId = userId)
            unit.blockadeList = blockadeList
            unit.save()

            return True
        except:
            return False

    def findByUserId(self, userId: str) -> blockadeListInfo:
        try:
            unit = blockadeListInfo.objects.get(userId = userId)
            return unit
        except:
            return None
