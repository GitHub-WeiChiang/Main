from gpsDatingApp.redis.JwtAccessTokenRedisSingleton import JwtAccessTokenRedisSingleton
from gpsDatingApp.redis.JwtRefreshTokenRedisSingleton import JwtRefreshTokenRedisSingleton
from gpsDatingApp.randomCode.RandomCodeGeneratorSingleton import RandomCodeGeneratorSingleton
from gpsDatingApp.randomCode.RandomCodeType import RandomCodeType
from gpsDatingApp.cryptography.SimpleMerkleTreeSingleton import SimpleMerkleTreeSingleton
from gpsDatingApp.logger.Logger import Logger

import threading
lock = threading.Lock()

class JwtSingleton():

    __instance: object = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    JwtSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            JwtSingleton.__isFirstInit = True

    # 產生 jwt
    def generateJwt(self, userId: str) -> dict:
        jwt: dict = {}

        # access jwt
        accessJwtSecurityCode: str = RandomCodeGeneratorSingleton().generate(RandomCodeType.SIGNATURE_CODE)
        jwt["access"] = SimpleMerkleTreeSingleton().getTreeRootHash(userId, accessJwtSecurityCode)
        # 存入 redis
        JwtAccessTokenRedisSingleton().set(userId, accessJwtSecurityCode, jwt["access"])

        # refresh jwt
        refreshJwtSecurityCode: str = RandomCodeGeneratorSingleton().generate(RandomCodeType.SIGNATURE_CODE)
        jwt["refresh"] = SimpleMerkleTreeSingleton().getTreeRootHash(userId, refreshJwtSecurityCode)
        # 存入 redis
        JwtRefreshTokenRedisSingleton().set(userId, refreshJwtSecurityCode, jwt["refresh"])

        return jwt

    # 檢查 token 是否符合不可竄改性
    def isTokenIncorruptible(self, userId: str, clientToken: str, realTokenDict: dict) -> bool:
        return clientToken == SimpleMerkleTreeSingleton().getTreeRootHash(userId, realTokenDict["securityCode"])

    # 檢查 access token 是否有效
    def isTokenValid(self, userId: str, clientToken: str, realTokenDict: dict) -> bool:
        return clientToken == realTokenDict["token"]
