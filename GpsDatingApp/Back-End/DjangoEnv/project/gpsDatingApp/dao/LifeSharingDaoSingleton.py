from gpsDatingApp.dao.DaoInterface import DaoInterface
from gpsDatingApp.models import lifeSharing

import os

import threading
lock = threading.Lock()

class LifeSharingDaoSingleton(DaoInterface):

    __instance: DaoInterface = None
    __isFirstInit: bool = False

    numOfSheets: int = 6

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    LifeSharingDaoSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            LifeSharingDaoSingleton.__isFirstInit = True

    def add(self, userId: str) -> bool:
        for i in range(self.numOfSheets):
            try:
                unit = lifeSharing.objects.create(
                    userId = userId,
                    num = i
                )
                unit.save()
            except:
                for j in range(i):
                    lifeSharing.objects.get(userId = userId, num = j)
                    unit.delete()
                return False
        return True

    def delete(self) -> bool:
        pass

    def deleteAll(self, userId: str) -> bool:
        for i in range(self.numOfSheets):
            try:
                # 刪除圖檔
                self.update(userId, i)
                # 刪除資料庫紀錄
                unit = lifeSharing.objects.get(userId = userId, num = i)
                unit.delete()
            except:
                pass
        return True

    def update(self, userId: str, num: int, image = None) -> bool:
        try:
            unit = lifeSharing.objects.get(userId = userId, num = num)

            # 暫存舊的圖片
            oldImage = unit.image

            # 換上新圖片
            unit.image = image
            unit.save()

            # 判斷有無舊圖記錄
            if oldImage == "":
                return True

            # 將 url 解譯為檔案路徑
            pathArr = oldImage.url.split("/")
            fileName: str = ""
            for i in pathArr:
                fileName = os.path.join(fileName, i)
            
            # 刪除舊圖檔
            if os.path.exists(fileName):
                os.remove(fileName)

            return True
        except:
            return False

    def findByUserId(self, userId: str) -> list:
        lifeSharingUrls: list = []

        for i in range(self.numOfSheets):
            lifeSharingUrls.append(self.findByUserIdAndNum(userId, i))

        return lifeSharingUrls

    def findByUserIdAndNum(self, userId: str, num: int) -> str:
        try:
            unit = lifeSharing.objects.get(userId = userId, num = num)
            return unit.image.url
        except:
            return None

    def updateAll(self) -> bool:
        pass
