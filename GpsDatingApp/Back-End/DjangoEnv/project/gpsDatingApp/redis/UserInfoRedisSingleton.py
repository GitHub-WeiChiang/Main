from django.core.cache import cache

from gpsDatingApp.redis.RedisInterface import RedisInterface
from gpsDatingApp.otherConfig.LifeCycleConfig import LifeCycleConfig
from gpsDatingApp.dao.BasicInfoDaoSingleton import BasicInfoDaoSingleton
from gpsDatingApp.dao.AdvancedInfoDaoSingleton import AdvancedInfoDaoSingleton
from gpsDatingApp.dao.AvatarDaoSingleton import AvatarDaoSingleton
from gpsDatingApp.dao.LifeSharingDaoSingleton import LifeSharingDaoSingleton
from gpsDatingApp.dao.LifeSharingOrderDaoSingleton import LifeSharingOrderDaoSingleton
from gpsDatingApp.logger.Logger import Logger

import datetime

import threading
lock = threading.Lock()

class UserInfoRedisSingleton(RedisInterface):

    __instance: RedisInterface = None
    __isFirstInit: bool = False

    prefix: str = "uirs_"

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    UserInfoRedisSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            UserInfoRedisSingleton.__isFirstInit = True

    def setMutableBasicInfo(self, userId: str, nickname: str, interest: list) -> None:
        userInfoDict = self.get(userId)

        userInfoDict["nickname"]: str = nickname
        userInfoDict["interest"]: list = interest

        # add type prefix
        userId = UserInfoRedisSingleton.prefix + userId
        cache.set(userId, userInfoDict, timeout = LifeCycleConfig.INFO_TYPE_REDIS_DATA_LIFE_CYCLE)

    def setBasicInfo(self, userId: str, rolePermission: str, nickname: str, birthday: str, sex: str, interest: list) -> None:
        userInfoDict = self.get(userId)

        userInfoDict["rolePermission"]: str = rolePermission
        userInfoDict["nickname"]: str = nickname
        userInfoDict["birthday"]: str = birthday if type(birthday) == str else birthday.strftime("%Y-%m-%d")
        userInfoDict["sex"]: str = sex
        userInfoDict["interest"]: list = interest

        # add type prefix
        userId = UserInfoRedisSingleton.prefix + userId
        cache.set(userId, userInfoDict, timeout = LifeCycleConfig.INFO_TYPE_REDIS_DATA_LIFE_CYCLE)

    def setAdvancedInfo(self, userId: str, introduction: str, school: str, department: str, country: str, city: str) -> None:
        userInfoDict = self.get(userId)

        userInfoDict["introduction"]: str = introduction
        userInfoDict["school"]: str = school
        userInfoDict["department"]: str = department
        userInfoDict["country"]: str = country
        userInfoDict["city"]: str = city

        # add type prefix
        userId = UserInfoRedisSingleton.prefix + userId
        cache.set(userId, userInfoDict, timeout = LifeCycleConfig.INFO_TYPE_REDIS_DATA_LIFE_CYCLE)

    def setAvatar(self, userId: str, avatarUrl: str) -> None:
        userInfoDict = self.get(userId)

        userInfoDict["avatarUrl"]: str = avatarUrl

        # add type prefix
        userId = UserInfoRedisSingleton.prefix + userId
        cache.set(userId, userInfoDict, timeout = LifeCycleConfig.INFO_TYPE_REDIS_DATA_LIFE_CYCLE)

    def setLifeSharing(self, userId: str, lifeSharingUrls: list) -> None:
        userInfoDict = self.get(userId)

        userInfoDict["lifeSharingUrls"]: list = lifeSharingUrls

        # add type prefix
        userId = UserInfoRedisSingleton.prefix + userId
        cache.set(userId, userInfoDict, timeout = LifeCycleConfig.INFO_TYPE_REDIS_DATA_LIFE_CYCLE)

    def setLifeSharingOrder(self, userId: str, order: list) -> None:
        userInfoDict = self.get(userId)

        userInfoDict["order"]: list = order

        # add type prefix
        userId = UserInfoRedisSingleton.prefix + userId
        cache.set(userId, userInfoDict, timeout = LifeCycleConfig.INFO_TYPE_REDIS_DATA_LIFE_CYCLE)

    def set(self, userId: str, rolePermission: str, nickname: str, birthday: str, sex: str, interest: list, introduction: str, school: str, department: str, country: str, city: str, avatarUrl: str, lifeSharingUrls: list, order: list) -> None:
        # add type prefix
        userId = UserInfoRedisSingleton.prefix + userId

        # value
        userInfoDict: dict = {}
        # basicInfo
        userInfoDict["rolePermission"]: str = rolePermission
        userInfoDict["nickname"]: str = nickname
        userInfoDict["birthday"]: str = birthday if type(birthday) == str else birthday.strftime("%Y-%m-%d")
        userInfoDict["sex"]: str = sex
        userInfoDict["interest"]: list = interest
        # advancedInfo
        userInfoDict["introduction"]: str = introduction
        userInfoDict["school"]: str = school
        userInfoDict["department"]: str = department
        userInfoDict["country"]: str = country
        userInfoDict["city"]: str = city
        # avatar
        userInfoDict["avatarUrl"]: str = avatarUrl
        # lifeSharing
        userInfoDict["lifeSharingUrls"]: list = lifeSharingUrls
        # lifeSharingOrder
        userInfoDict["order"]: list = order

        cache.set(userId, userInfoDict, timeout = LifeCycleConfig.INFO_TYPE_REDIS_DATA_LIFE_CYCLE)

    def get(self, userId: str) -> dict:
        # add type prefix
        userIdKey = UserInfoRedisSingleton.prefix + userId

        if self.has(userId) == False:
            with lock:
                if self.has(userId) == False:
                    basicInfoUnit = BasicInfoDaoSingleton().findByUserId(userId)
                    if basicInfoUnit == None:
                        class BasicInfoUnit:
                            rolePermission: str = ""
                            nickname: str = ""
                            birthday: str = ""
                            sex: str = ""
                            interest: list = []
                        basicInfoUnit = BasicInfoUnit()

                    advancedInfoUnit = AdvancedInfoDaoSingleton().findByUserId(userId)
                    if advancedInfoUnit == None:
                        class AdvancedInfoUnit:
                            introduction: str = ""
                            school: str = ""
                            department: str = ""
                            country: str = ""
                            city: str = ""
                        advancedInfoUnit = AdvancedInfoUnit()
                    
                    avatarUrl = AvatarDaoSingleton().findByUserId(userId)
                    if avatarUrl == None:
                        avatarUrl = ""
                    
                    lifeSharingUrls = LifeSharingDaoSingleton().findByUserId(userId)
                    if lifeSharingUrls == None:
                        lifeSharingUrls = [None, None, None, None, None, None]

                    order = LifeSharingOrderDaoSingleton().findByUserId(userId)
                    if order == None:
                        order = [0, 1, 2, 3, 4, 5]
            
                    self.set(userId, basicInfoUnit.rolePermission, basicInfoUnit.nickname, basicInfoUnit.birthday, basicInfoUnit.sex, basicInfoUnit.interest, advancedInfoUnit.introduction, advancedInfoUnit.school, advancedInfoUnit.department, advancedInfoUnit.country, advancedInfoUnit.city, avatarUrl, lifeSharingUrls, order)

        userInfoDict: dict = cache.get(userIdKey)
        return userInfoDict

    def has(self, userId: str) -> bool:
        # add type prefix
        userId = UserInfoRedisSingleton.prefix + userId

        return cache.has_key(userId)

    def delete(self, userId: str) -> None:
        # add type prefix
        userId = UserInfoRedisSingleton.prefix + userId

        cache.delete(userId)

    def ttl(self, userId: str) -> int:
        # add type prefix
        userId = UserInfoRedisSingleton.prefix + userId

        return cache.ttl(userId)
