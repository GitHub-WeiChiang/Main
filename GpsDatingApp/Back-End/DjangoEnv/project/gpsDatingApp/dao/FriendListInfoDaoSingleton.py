from asgiref.sync import sync_to_async

from gpsDatingApp.dao.DaoInterface import DaoInterface
from gpsDatingApp.logger.Logger import Logger
from gpsDatingApp.models import friendListInfo

import threading
import traceback
lock = threading.Lock()

class FriendListInfoDaoSingleton(DaoInterface):

    __instance: DaoInterface = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    FriendListInfoDaoSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            FriendListInfoDaoSingleton.__isFirstInit = True

    def add(self, userId: str) -> bool:
        try:
            unit = friendListInfo.objects.create(
                userId = userId
            )
            unit.save()
            
            return True
        except:
            return False

    def delete(self, userId: str) -> bool:
        try:
            unit = friendListInfo.objects.get(userId = userId)
            unit.delete()

            return True
        except:
            return False

    @sync_to_async
    def updateAll(self, userId: str, friendList: list) -> bool:
        try:
            unit = friendListInfo.objects.get(userId = userId)
            unit.friendList = friendList
            unit.save()

            return True
        except:
            return False

    def findByUserId(self, userId: str) -> friendListInfo:
        try:
            unit = friendListInfo.objects.get(userId = userId)
            return unit
        except:
            return None
