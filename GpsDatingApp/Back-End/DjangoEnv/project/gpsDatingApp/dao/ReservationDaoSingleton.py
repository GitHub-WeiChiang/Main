from datetime import datetime

from gpsDatingApp.dao.DaoInterface import DaoInterface
from gpsDatingApp.models import reservation

import threading
lock = threading.Lock()

class ReservationDaoSingleton(DaoInterface):

    __instance: DaoInterface = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    ReservationDaoSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            ReservationDaoSingleton.__isFirstInit = True

    def add(self, email: str, reserveTime: datetime, reserveCity: str) -> bool:
        try:
            unit = reservation.objects.create(
                email = email,
                reserveTime = reserveTime,
                reserveCity = reserveCity
            )
            unit.save()
            
            return True
        except:
            return False

    def delete(self, email: str) -> bool:
        try:
            unit = reservation.objects.get(email = email)
            unit.delete()

            return True
        except:
            return False

    def updateAll(self) -> bool:
        pass

    def updateIsRegister(self, email: str) -> bool:
        try:
            unit = reservation.objects.get(email = email)
            unit.isRegister = True
            unit.save()
            
            return True
        except:
            return False

    def findByEmail(self, email: str) -> reservation:
        try:
            unit = reservation.objects.get(email = email)
            return unit
        except:
            return None

    def getAll(self) -> list:
        try:
            unitList = reservation.objects.all()
            return unitList
        except:
            return []
