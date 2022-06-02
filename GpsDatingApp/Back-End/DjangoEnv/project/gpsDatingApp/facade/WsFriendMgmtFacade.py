from gpsDatingApp.dao.FriendListInfoDaoSingleton import FriendListInfoDaoSingleton
from gpsDatingApp.dao.BlockadeListInfoDaoSingleton import BlockadeListInfoDaoSingleton
from gpsDatingApp.redis.FriendListInfoRedisSingleton import FriendListInfoRedisSingleton
from gpsDatingApp.redis.BlockadeListInfoRedisSingleton import BlockadeListInfoRedisSingleton

import threading
lock = threading.Lock()

class WsFriendMgmtFacade():

    __instance: object = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    WsFriendMgmtFacade.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            WsFriendMgmtFacade.__isFirstInit = True

    # 新增好友
    async def addFriend(self, userId: str, addId: str) -> bool:
        with lock:
            friendList: list = FriendListInfoRedisSingleton().get(userId)
            friendList.append(addId)
            await FriendListInfoDaoSingleton().updateAll(userId, friendList)
            FriendListInfoRedisSingleton().set(userId, friendList)
            
            return True

    # 移除好友
    async def removeFriend(self, userId: str, removeId: str) -> bool:
        with lock:
            friendList: list = FriendListInfoRedisSingleton().get(userId)
            BlockadeList: list = BlockadeListInfoRedisSingleton().get(userId)

            friendList.remove(removeId)
            BlockadeList.append(removeId)

            await FriendListInfoDaoSingleton().updateAll(userId, friendList)
            await BlockadeListInfoDaoSingleton().updateAll(userId, BlockadeList)

            FriendListInfoRedisSingleton().set(userId, friendList)
            BlockadeListInfoRedisSingleton().set(userId, BlockadeList)

            return True

    # 好友清單
    def friendList(self, userId: str) -> list:
        with lock:
            return FriendListInfoRedisSingleton().get(userId)

    # 封鎖清單
    def blockadeList(self, userId: str) -> list:
        with lock:
            return BlockadeListInfoRedisSingleton().get(userId)
