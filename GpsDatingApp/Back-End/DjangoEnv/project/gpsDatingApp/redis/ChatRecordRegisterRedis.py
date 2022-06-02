from django.core.cache import cache
from datetime import datetime

from gpsDatingApp.redis.RedisInterface import RedisInterface
from gpsDatingApp.logger.Logger import Logger

import threading
lock = threading.Lock()

class ChatRecordRegisterRedis(RedisInterface):

    def set(self, userId: str, sender: str, message: str, time: datetime) -> None:
        userIdKey = self.prefix + userId

        if self.has(userId) == False:
            with lock:
                if self.has(userId) == False:
                    cache.set(userIdKey, [], timeout = None)

        with lock:
            messageInfoList: list = self.get(userId)

            messageInfo: dict = {}
            messageInfo["sender"] = sender
            messageInfo["message"] = message
            messageInfo["time"] = time.strftime("%Y-%m-%d %H:%M:%S")

            messageInfoList.append(messageInfo)

            cache.set(userIdKey, messageInfoList, timeout = None)

    def get(self, userId: str) -> list:
        # add type prefix
        userId = self.prefix + userId

        messageInfoList: list = cache.get(userId)

        return messageInfoList

    def has(self, userId: str) -> bool:
        # add type prefix
        userId = self.prefix + userId

        return cache.has_key(userId)

    def delete(self, userId: str) -> None:
        # add type prefix
        userId = self.prefix + userId
        
        cache.delete(userId)

    def clear(self, userId: str) -> None:
        with lock:
            # add type prefix
            userId = self.prefix + userId
            
            cache.set(userId, [], timeout = None)

    def ttl(self) -> None:
        pass
