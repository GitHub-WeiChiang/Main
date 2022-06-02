import urllib
import json

from django.conf import settings

import threading
lock = threading.Lock()

class ReCaptchaInspectSingleton():

    __instance: object = None
    __isFirstInit: bool = False

    url: str = settings.GOOGLE_RECAPTCHA_URL
    secret: str = settings.GOOGLE_RECAPTCHA_SECRET_KEY

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    ReCaptchaInspectSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            ReCaptchaInspectSingleton.__isFirstInit = True

    def inspect(self, recaptcha_response: str) -> bool:
        values = {
            'secret': ReCaptchaInspectSingleton.secret,
            'response': recaptcha_response
        }

        data = urllib.parse.urlencode(values).encode()
        req = urllib.request.Request(ReCaptchaInspectSingleton.url, data = data)
        response = urllib.request.urlopen(req)
        result = json.loads(response.read().decode())
        
        return result['success']
