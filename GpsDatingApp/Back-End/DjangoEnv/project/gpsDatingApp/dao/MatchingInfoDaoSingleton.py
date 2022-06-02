from gpsDatingApp.dao.DaoInterface import DaoInterface
from gpsDatingApp.models import matchingInfo
from gpsDatingApp.dao.BasicInfoDaoSingleton import BasicInfoDaoSingleton
from gpsDatingApp.statusCode.StatusCode import StatusCode
from gpsDatingApp.models import basicInfo

import threading
lock = threading.Lock()

class MatchingInfoDaoSingleton(DaoInterface):

    __instance: DaoInterface = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    MatchingInfoDaoSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            MatchingInfoDaoSingleton.__isFirstInit = True

    def add(self, userId: str) -> bool:
        try:
            unit = matchingInfo.objects.create(
                userId = userId
            )
            unit.save()
            
            return True
        except:
            return False

    def delete(self, userId: str) -> bool:
        try:
            unit = matchingInfo.objects.get(userId = userId)
            unit.delete()

            return True
        except:
            return False

    def matchingKindBusinessLogicInspect(self, userId: str, matchingAge: list, matchingKind: int) -> int:
        userBasicInfo: basicInfo = BasicInfoDaoSingleton().findByUserId(userId)

        if userBasicInfo == None:
            return StatusCode.DATABASE_ACCESS_EXCEPTION

        # 檢查歲數範圍
        if matchingAge[0] < 18:
            return StatusCode.PARAMETER_SETTING_BUSINESS_LOGIC_ERROR

        # 若是男生卻選女女配對種類
        if userBasicInfo.sex == "Male" and matchingKind == 2:
            return StatusCode.PARAMETER_SETTING_BUSINESS_LOGIC_ERROR

        # 若是女生卻選男男配對種類
        if userBasicInfo.sex == "Female" and matchingKind == 1:
            return StatusCode.PARAMETER_SETTING_BUSINESS_LOGIC_ERROR

        return StatusCode.SUCCESS

    def updateAll(self, userId: str, matchingAge: list, matchingKind: int) -> bool:
        try:
            unit = matchingInfo.objects.get(userId = userId)
            unit.matchingAge = matchingAge
            unit.matchingKind = matchingKind
            unit.save()

            return True
        except:
            return False

    def updateMatchingAge(self, userId: str, matchingAge: list) -> bool:
        try:
            unit = matchingInfo.objects.get(userId = userId)
            unit.matchingAge = matchingAge
            unit.save()

            return True
        except:
            return False

    def updateMatchingKind(self, userId: str, matchingKind: list) -> bool:
        try:
            unit = matchingInfo.objects.get(userId = userId)
            unit.matchingKind = matchingKind
            unit.save()

            return True
        except:
            return False

    def findByUserId(self, userId: str) -> matchingInfo:
        try:
            unit = matchingInfo.objects.get(userId = userId)
            return unit
        except:
            return None
