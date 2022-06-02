# Abstract Class

from abc import ABCMeta, abstractclassmethod
from django.utils import timezone

from gpsDatingApp.redis.MatchingInfoRedisSingleton import MatchingInfoRedisSingleton
from gpsDatingApp.redis.UserInfoRedisSingleton import UserInfoRedisSingleton
# from gpsDatingApp.redis.FriendListInfoRedisSingleton import FriendListInfoRedisSingleton
from gpsDatingApp.calculate.AgeCalculateSingleton import AgeCalculateSingleton
# from gpsDatingApp.dao.FriendListInfoDaoSingleton import FriendListInfoDaoSingleton
from gpsDatingApp.dao.PairingRecordDaoSingleton import PairingRecordDaoSingleton
from gpsDatingApp.logger.Logger import Logger
from gpsDatingApp.facade.WsFriendMgmtFacade import WsFriendMgmtFacade

class PairPool(metaclass=ABCMeta):

    @abstractclassmethod
    def addInPool(self, userId: str, pairkey: str) -> bool:
        pass

    @abstractclassmethod
    def pairing(self) -> list:
        pass

    @abstractclassmethod
    def clear(self) -> list:
        pass

    def isPairing(self, userIdA: str, userIdB: str) -> bool:
        # 檢查彼此 matchingAge
        birthdayA: str = UserInfoRedisSingleton().get(userIdA)["birthday"]
        birthdayB: str = UserInfoRedisSingleton().get(userIdB)["birthday"]

        ageA: int = AgeCalculateSingleton().calculate(birthdayA)
        ageB: int = AgeCalculateSingleton().calculate(birthdayB)

        matchingAgeA: list = MatchingInfoRedisSingleton().get(userIdA)["matchingAge"]
        matchingAgeB: list = MatchingInfoRedisSingleton().get(userIdB)["matchingAge"]

        if ageB < matchingAgeA[0] or matchingAgeA[1] < ageB or ageA < matchingAgeB[0] or matchingAgeB[1] < ageA:
            return False

        # 檢查是否曾經配對過
        # friendListA: list = FriendListInfoRedisSingleton().get(userIdA)
        # friendListB: list = FriendListInfoRedisSingleton().get(userIdB)
        friendListA: list = WsFriendMgmtFacade().friendList(userIdA)
        friendListB: list = WsFriendMgmtFacade().friendList(userIdB)

        if userIdA in friendListB or userIdB in friendListA:
            return False

        return True

    async def becomeFriends(self, userIdA: str, userIdB: str, city: str, district: str, coordinateLng: float, coordinateLat: float) -> bool:
        Logger.info("becomeFriends")
        
        # friendListA: list = FriendListInfoRedisSingleton().get(userIdA)
        # friendListB: list = FriendListInfoRedisSingleton().get(userIdB)

        # Logger.info(friendListA)
        # Logger.info(friendListB)

        # friendListA.append(userIdB)
        # friendListB.append(userIdA)

        # await FriendListInfoDaoSingleton().updateAll(userIdA, friendListA)
        # await FriendListInfoDaoSingleton().updateAll(userIdB, friendListB)

        # FriendListInfoRedisSingleton().set(userIdA, friendListA)
        # FriendListInfoRedisSingleton().set(userIdB, friendListB)

        await WsFriendMgmtFacade().addFriend(userIdA, userIdB)
        await WsFriendMgmtFacade().addFriend(userIdB, userIdA)

        await PairingRecordDaoSingleton().add(userIdA, userIdB, timezone.now(), city, district, coordinateLng, coordinateLat)

        return True
