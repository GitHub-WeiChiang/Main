import random

from google.oauth2 import id_token
from google.auth.transport import requests

from django.conf import settings

import threading
lock = threading.Lock()

class GoogleSignInSingleton():

    __instance: object = None
    __isFirstInit: bool = False

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    GoogleSignInSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            GoogleSignInSingleton.__isFirstInit = True

    def inspect(self, googleSignInToken: str) -> str:
        # 檢查 googleSignInToken 並取得 eamil
        try:
            idinfo = id_token.verify_oauth2_token(googleSignInToken, requests.Request(), settings.GOOGLE_SIGN_IN_CLIENT_ID)
            return idinfo["email"]
        except ValueError:
            return ""
