from gpsDatingApp.dao.DaoInterface import DaoInterface

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

import threading
lock = threading.Lock()

class DeleteCustomerInfoDaoFacadeSingleton(DaoInterface):

    __instance: DaoInterface = None
    __isFirstInit: bool = False

    registerInfoDaoSingleton: RegisterInfoDaoSingleton = None
    basicInfoDaoSingleton: BasicInfoDaoSingleton = None
    advancedInfoDaoSingleton: AdvancedInfoDaoSingleton = None
    matchingInfoDaoSingleton: MatchingInfoDaoSingleton = None
    friendListInfoDaoSingleton: FriendListInfoDaoSingleton = None
    blockadeListInfoDaoSingleton: BlockadeListInfoDaoSingleton = None
    accountStatusDaoSingleton: AccountStatusDaoSingleton = None
    avatarDaoSingleton: AvatarDaoSingleton = None
    reservationDaoSingleton: ReservationDaoSingleton = None
    lifeSharingDaoSingleton: LifeSharingDaoSingleton = None
    lifeSharingOrderDaoSingleton: LifeSharingOrderDaoSingleton = None

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    DeleteCustomerInfoDaoFacadeSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            self.registerInfoDaoSingleton = RegisterInfoDaoSingleton()
            self.basicInfoDaoSingleton = BasicInfoDaoSingleton()
            self.advancedInfoDaoSingleton = AdvancedInfoDaoSingleton()
            self.matchingInfoDaoSingleton = MatchingInfoDaoSingleton()
            self.friendListInfoDaoSingleton = FriendListInfoDaoSingleton()
            self.blockadeListInfoDaoSingleton = BlockadeListInfoDaoSingleton()
            self.accountStatusDaoSingleton = AccountStatusDaoSingleton()
            self.avatarDaoSingleton = AvatarDaoSingleton()
            self.reservationDaoSingleton = ReservationDaoSingleton()
            self.lifeSharingDaoSingleton = LifeSharingDaoSingleton()
            self.lifeSharingOrderDaoSingleton = LifeSharingOrderDaoSingleton()

            DeleteCustomerInfoDaoFacadeSingleton.__isFirstInit = True

    def deleteTestData(self, email: str) -> bool:
        try:
            # 提取 userId
            userId: str = self.registerInfoDaoSingleton.findByEmail(email).userId

            # 刪除資料
            self.registerInfoDaoSingleton.delete(userId)
            self.basicInfoDaoSingleton.delete(userId)
            self.advancedInfoDaoSingleton.delete(userId)
            self.matchingInfoDaoSingleton.delete(userId)
            self.friendListInfoDaoSingleton.delete(userId)
            self.blockadeListInfoDaoSingleton.delete(userId)
            self.accountStatusDaoSingleton.delete(userId)
            self.avatarDaoSingleton.delete(userId)
            self.lifeSharingDaoSingleton.deleteAll(userId)
            self.lifeSharingOrderDaoSingleton.delete(userId)
            self.reservationDaoSingleton.delete(email)
        except:
            return False
        
        return True

    def add(self) -> bool:
        pass

    def delete(self) -> bool:
        pass

    def updateAll(self) -> bool:
        pass
