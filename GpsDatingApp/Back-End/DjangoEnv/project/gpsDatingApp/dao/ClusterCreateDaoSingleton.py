from datetime import datetime

from gpsDatingApp.dao.RegisterInfoDaoSingleton import RegisterInfoDaoSingleton
from gpsDatingApp.dao.BasicInfoDaoSingleton import BasicInfoDaoSingleton
from gpsDatingApp.dao.AdvancedInfoDaoSingleton import AdvancedInfoDaoSingleton
from gpsDatingApp.dao.MatchingInfoDaoSingleton import MatchingInfoDaoSingleton
from gpsDatingApp.dao.FriendListInfoDaoSingleton import FriendListInfoDaoSingleton
from gpsDatingApp.dao.BlockadeListInfoDaoSingleton import BlockadeListInfoDaoSingleton
from gpsDatingApp.dao.AccountStatusDaoSingleton import AccountStatusDaoSingleton
from gpsDatingApp.dao.AvatarDaoSingleton import AvatarDaoSingleton
from gpsDatingApp.dao.ReservationDaoSingleton import ReservationDaoSingleton
from gpsDatingApp.dao.LifeSharingDaoSingleton import LifeSharingDaoSingleton
from gpsDatingApp.dao.LifeSharingOrderDaoSingleton import LifeSharingOrderDaoSingleton
from gpsDatingApp.logger.Logger import Logger

import threading
lock = threading.Lock()

class ClusterCreateDaoSingleton():

    __instance = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    ClusterCreateDaoSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            ClusterCreateDaoSingleton.__isFirstInit = True

    def clusterCreate(self, email: str, registerTime: datetime, registerCity: str, registerDistrict: str, registerCoordinate: list) -> bool:
        # 建立 Register Info
        if RegisterInfoDaoSingleton().add(email, registerTime, registerCity, registerDistrict, registerCoordinate) == False:
            return False

        # 提取 userId
        userId: str = RegisterInfoDaoSingleton().findByEmail(email).userId
        
        # 建立資料表群集
        if BasicInfoDaoSingleton().add(userId) == False:
            RegisterInfoDaoSingleton().delete(userId)
            return False
        if AdvancedInfoDaoSingleton().add(userId) == False:
            RegisterInfoDaoSingleton().delete(userId)
            BasicInfoDaoSingleton().delete(userId)
            return False
        if MatchingInfoDaoSingleton().add(userId) == False:
            RegisterInfoDaoSingleton().delete(userId)
            BasicInfoDaoSingleton().delete(userId)
            AdvancedInfoDaoSingleton().delete(userId)
            return False
        if FriendListInfoDaoSingleton().add(userId) == False:
            RegisterInfoDaoSingleton().delete(userId)
            BasicInfoDaoSingleton().delete(userId)
            AdvancedInfoDaoSingleton().delete(userId)
            MatchingInfoDaoSingleton().delete(userId)
            return False
        if BlockadeListInfoDaoSingleton().add(userId) == False:
            RegisterInfoDaoSingleton().delete(userId)
            BasicInfoDaoSingleton().delete(userId)
            AdvancedInfoDaoSingleton().delete(userId)
            MatchingInfoDaoSingleton().delete(userId)
            FriendListInfoDaoSingleton().delete(userId)
            return False
        if AccountStatusDaoSingleton().add(userId, registerTime) == False:
            RegisterInfoDaoSingleton().delete(userId)
            BasicInfoDaoSingleton().delete(userId)
            AdvancedInfoDaoSingleton().delete(userId)
            MatchingInfoDaoSingleton().delete(userId)
            FriendListInfoDaoSingleton().delete(userId)
            BlockadeListInfoDaoSingleton().delete(userId)
            return False
        if AvatarDaoSingleton().add(userId) == False:
            RegisterInfoDaoSingleton().delete(userId)
            BasicInfoDaoSingleton().delete(userId)
            AdvancedInfoDaoSingleton().delete(userId)
            MatchingInfoDaoSingleton().delete(userId)
            FriendListInfoDaoSingleton().delete(userId)
            BlockadeListInfoDaoSingleton().delete(userId)
            AccountStatusDaoSingleton().delete(userId)
            return False
        if LifeSharingDaoSingleton().add(userId) == False:
            RegisterInfoDaoSingleton().delete(userId)
            BasicInfoDaoSingleton().delete(userId)
            AdvancedInfoDaoSingleton().delete(userId)
            MatchingInfoDaoSingleton().delete(userId)
            FriendListInfoDaoSingleton().delete(userId)
            BlockadeListInfoDaoSingleton().delete(userId)
            AccountStatusDaoSingleton().delete(userId)
            AvatarDaoSingleton().delete(userId)
            return False
        if LifeSharingOrderDaoSingleton().add(userId) == False:
            RegisterInfoDaoSingleton().delete(userId)
            BasicInfoDaoSingleton().delete(userId)
            AdvancedInfoDaoSingleton().delete(userId)
            MatchingInfoDaoSingleton().delete(userId)
            FriendListInfoDaoSingleton().delete(userId)
            BlockadeListInfoDaoSingleton().delete(userId)
            AccountStatusDaoSingleton().delete(userId)
            AvatarDaoSingleton().delete(userId)
            LifeSharingDaoSingleton().deleteAll(userId)
            return False

        ReservationDaoSingleton().updateIsRegister(email)
        
        return True
