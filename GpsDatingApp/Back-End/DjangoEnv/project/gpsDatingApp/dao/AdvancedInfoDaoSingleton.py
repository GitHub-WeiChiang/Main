from gpsDatingApp.dao.DaoInterface import DaoInterface
from gpsDatingApp.models import advancedInfo

import threading
lock = threading.Lock()

class AdvancedInfoDaoSingleton(DaoInterface):

    __instance: DaoInterface = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    AdvancedInfoDaoSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            AdvancedInfoDaoSingleton.__isFirstInit = True

    def add(self, userId: str) -> bool:
        try:
            unit = advancedInfo.objects.create(
                userId = userId
            )
            unit.save()
            
            return True
        except:
            return False

    def delete(self, userId: str) -> bool:
        try:
            unit = advancedInfo.objects.get(userId = userId)
            unit.delete()

            return True
        except:
            return False

    def updateAll(self, userId: str, introduction: str, school: str, department: str, country: str, city: str) -> bool:
        try:
            unit = advancedInfo.objects.get(userId = userId)
            unit.introduction = introduction
            unit.school = school
            unit.department = department
            unit.country = country
            unit.city = city
            unit.save()

            return True
        except:
            return False

    def findByUserId(self, userId: str) -> advancedInfo:
        try:
            unit = advancedInfo.objects.get(userId = userId)
            return unit
        except:
            return None
