from gpsDatingApp.dao.DaoInterface import DaoInterface
from gpsDatingApp.models import lifeSharingOrder

import threading
lock = threading.Lock()

class LifeSharingOrderDaoSingleton(DaoInterface):

    __instance: DaoInterface = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    LifeSharingOrderDaoSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            LifeSharingOrderDaoSingleton.__isFirstInit = True

    def add(self, userId: str) -> bool:
        try:
            unit = lifeSharingOrder.objects.create(
                userId = userId
            )
            unit.save()
            
            return True
        except:
            return False

    def delete(self, userId: str) -> bool:
        try:
            unit = lifeSharingOrder.objects.get(userId = userId)
            unit.delete()
            return True
        except:
            return False

    def updateAll(self, userId: str, order: list = [0, 1, 2, 3, 4, 5]) -> bool:
        try:
            unit = lifeSharingOrder.objects.get(userId = userId)
            unit.order = order
            unit.save()
            return True
        except:
            return False

    def findByUserId(self, userId: str) -> list:
        try:
            unit = lifeSharingOrder.objects.get(userId = userId)
            return unit.order
        except:
            return None
