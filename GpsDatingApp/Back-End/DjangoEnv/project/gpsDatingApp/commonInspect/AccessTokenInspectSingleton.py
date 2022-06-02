from gpsDatingApp.statusCode.StatusCode import StatusCode
from gpsDatingApp.jwt.JwtSingleton import JwtSingleton
from gpsDatingApp.logger.Logger import Logger

import threading
lock = threading.Lock()

class AccessTokenInspectSingleton():

    __instance: object = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    AccessTokenInspectSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            AccessTokenInspectSingleton.__isFirstInit = True

    def inspect(self, userId: str, access: str, accessTokenDict: str) -> int:
        # 檢查 access Token 是否過期
        if accessTokenDict == None:
            return StatusCode.ACCESS_TOKEN_NOT_EXIST_OR_EXPIRE

        # 檢查 access Token 是否被竄改
        if JwtSingleton().isTokenIncorruptible(userId, access, accessTokenDict) == False:
            return StatusCode.ACCESS_TOKEN_NOT_INCORRUPTIBLE

        # 檢查 access Token 是否有效
        if JwtSingleton().isTokenValid(userId, access, accessTokenDict) == False:
            return StatusCode.ACCESS_TOKEN_INVALID

        return StatusCode.SUCCESS
