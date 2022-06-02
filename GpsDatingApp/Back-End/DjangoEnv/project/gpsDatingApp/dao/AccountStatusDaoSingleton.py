from datetime import datetime

from gpsDatingApp.dao.DaoInterface import DaoInterface
from gpsDatingApp.models import accountStatus

import threading
lock = threading.Lock()

class AccountStatusDaoSingleton(DaoInterface):

    __instance: DaoInterface = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    AccountStatusDaoSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            AccountStatusDaoSingleton.__isFirstInit = True

    def add(self, userId: str, lastJwtRefreshTime: datetime) -> bool:
        try:
            unit = accountStatus.objects.create(
                userId = userId,
                lastJwtRefreshTime = lastJwtRefreshTime
            )
            unit.save()
            
            return True
        except:
            return False

    def delete(self, userId: str) -> bool:
        try:
            unit = accountStatus.objects.get(userId = userId)
            unit.delete()

            return True
        except:
            return False

    def updateAll(self) -> bool:
        pass

    def updateEnableFunction(self, userId: str, enableFunction: list) -> bool:
        try:
            unit = accountStatus.objects.get(userId = userId)
            unit.enableFunction = enableFunction
            unit.save()

            return True
        except:
            return False

    def updateLastJwtRefreshTime(self, userId: str, lastJwtRefreshTime: datetime) -> bool:
        try:
            unit = accountStatus.objects.get(userId = userId)
            unit.lastJwtRefreshTime = lastJwtRefreshTime
            unit.save()

            return True
        except:
            return False

    def updateIsCompleteFirstSetting(self, userId: str) -> bool:
        try:
            unit = accountStatus.objects.get(userId = userId)
            unit.isCompleteFirstSetting = True
            unit.save()

            return True
        except:
            return False

    def findByUserId(self, userId: str) -> accountStatus:
        try:
            unit = accountStatus.objects.get(userId = userId)
            return unit
        except:
            return None
