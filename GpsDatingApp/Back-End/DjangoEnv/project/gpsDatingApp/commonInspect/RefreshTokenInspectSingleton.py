from gpsDatingApp.statusCode.StatusCode import StatusCode
from gpsDatingApp.jwt.JwtSingleton import JwtSingleton

import threading
lock = threading.Lock()

class RefreshTokenInspectSingleton():

    __instance: object = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    RefreshTokenInspectSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            RefreshTokenInspectSingleton.__isFirstInit = True

    def inspect(self, userId: str, refresh: str, refreshTokenDict) -> int:
        # 檢查 refresh Token 是否過期
        if refreshTokenDict == None:
            return StatusCode.REFRESH_TOKEN_NOT_EXIST_OR_EXPIRE

        # 檢查 refresh Token 是否被竄改
        if JwtSingleton().isTokenIncorruptible(userId, refresh, refreshTokenDict) == False:
            return StatusCode.REFRESH_TOKEN_NOT_INCORRUPTIBLE

        # 檢查 refresh Token 是否有效
        if JwtSingleton().isTokenValid(userId, refresh, refreshTokenDict) == False:
            return StatusCode.REFRESH_TOKEN_INVALID

        return StatusCode.SUCCESS
