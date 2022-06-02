from datetime import datetime

from gpsDatingApp.dao.DaoInterface import DaoInterface
from gpsDatingApp.models import registerInfo

import threading
lock = threading.Lock()

class RegisterInfoDaoSingleton(DaoInterface):

    __instance: DaoInterface = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    RegisterInfoDaoSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            RegisterInfoDaoSingleton.__isFirstInit = True

    def add(self, email: str, registerTime: datetime, registerCity: str, registerDistrict: str, registerCoordinate: list) -> bool:
        try:
            unit = registerInfo.objects.create(
                email = email,
                registerTime = registerTime,
                registerCity = registerCity,
                registerDistrict = registerDistrict,
                registerCoordinateLng = registerCoordinate[0],
                registerCoordinateLat = registerCoordinate[1]
            )
            unit.save()
            
            return True
        except:
            return False

    def delete(self, userId: str) -> bool:
        try:
            unit = registerInfo.objects.get(userId = userId)
            unit.delete()

            return True
        except:
            return False

    def updateAll(self) -> bool:
        pass

    def findByEmail(self, email: str) -> registerInfo:
        try:
            unit = registerInfo.objects.get(email = email)
            return unit
        except:
            return None

    def findByUserId(self, userId: str) -> registerInfo:
        try:
            unit = registerInfo.objects.get(userId = userId)
            return unit
        except:
            return None
