from gpsDatingApp.dao.DaoInterface import DaoInterface
from gpsDatingApp.models import basicInfo

import threading
lock = threading.Lock()

class BasicInfoDaoSingleton(DaoInterface):

    __instance: DaoInterface = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    BasicInfoDaoSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            BasicInfoDaoSingleton.__isFirstInit = True

    def add(self, userId: str) -> bool:
        try:
            unit = basicInfo.objects.create(
                userId = userId
            )
            unit.save()
            
            return True
        except:
            return False

    def delete(self, userId: str) -> bool:
        try:
            unit = basicInfo.objects.get(userId = userId)
            unit.delete()

            return True
        except:
            return False

    def updateMutableInfo(self, userId: str, nickname: str, interest: list) -> bool:
        try:
            unit = basicInfo.objects.get(userId = userId)
            unit.nickname = nickname
            unit.interest = interest
            unit.save()

            return True
        except:
            return False

    def updateAll(self, userId: str, rolePermission: str, nickname: str, birthday: str, sex: str, interest: list) -> bool:
        try:
            unit = basicInfo.objects.get(userId = userId)
            unit.rolePermission = rolePermission
            unit.nickname = nickname
            unit.birthday = birthday
            unit.sex = sex
            unit.interest = interest
            unit.save()

            return True
        except:
            return False

    def findByUserId(self, userId: str) -> basicInfo:
        try:
            unit = basicInfo.objects.get(userId = userId)
            return unit
        except:
            return None
