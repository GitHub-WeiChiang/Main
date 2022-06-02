from gpsDatingApp.dao.DaoInterface import DaoInterface
from gpsDatingApp.models import avatar

import os

import threading
lock = threading.Lock()

class AvatarDaoSingleton(DaoInterface):

    __instance: DaoInterface = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    AvatarDaoSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            AvatarDaoSingleton.__isFirstInit = True

    def add(self, userId: str) -> bool:
        try:
            unit = avatar.objects.create(
                userId = userId
            )
            unit.save()
            
            return True
        except:
            return False

    def delete(self, userId: str) -> bool:
        try:
            # 刪除圖檔
            self.updateAll(userId)
            # 刪除資料庫紀錄
            unit = avatar.objects.get(userId = userId)
            unit.delete()
            return True
        except:
            return False

    def updateAll(self, userId: str, image = None) -> bool:
        try:
            unit = avatar.objects.get(userId = userId)

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

    def findByUserId(self, userId: str) -> str:
        try:
            unit = avatar.objects.get(userId = userId)
            return unit.image.url
        except:
            return None
