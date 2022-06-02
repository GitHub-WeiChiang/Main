from datetime import datetime

from asgiref.sync import sync_to_async

from gpsDatingApp.dao.DaoInterface import DaoInterface
from gpsDatingApp.models import pairingRecord
from gpsDatingApp.logger.Logger import Logger

import threading
import traceback
lock = threading.Lock()

class PairingRecordDaoSingleton(DaoInterface):

    __instance: DaoInterface = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    PairingRecordDaoSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            PairingRecordDaoSingleton.__isFirstInit = True

    @sync_to_async
    def add(self, userIdA: str, userIdB: str, time: datetime, city: str, district: str, coordinateLng: float, coordinateLat: float) -> bool:
        try:
            unit = pairingRecord.objects.create(
                userIdA = userIdA,
                userIdB = userIdB,
                time = time,
                city = city,
                district = district,
                coordinateLng = coordinateLng,
                coordinateLat = coordinateLat
            )
            unit.save()
            
            return True
        except:
            return False

    def delete(self) -> bool:
        pass

    def updateAll(self) -> bool:
        pass
