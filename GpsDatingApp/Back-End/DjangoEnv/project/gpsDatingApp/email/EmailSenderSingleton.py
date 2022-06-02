from typing import List

from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from gpsDatingApp.statusCode.StatusCode import StatusCode

import threading
lock = threading.Lock()

class EmailSenderSingleton():

    __instance: object = None
    __isFirstInit: bool = False

    emailTemplateList: List[str] = [
        "reservation-success-email-template.html",
        "reservation-verify-email-template.html",
        "reservation-verify-email-template.html",
        "reservation-verify-email-template.html",
        # "register-verify-email-template.html",
        # "login-verify-email-template.html",
    ]

    emailTitleList: List[str] = [
        "chance.圈圈 事前預約成功通知",
        "chance.圈圈 事前預約驗證碼",
        "chance.圈圈 註冊驗證碼",
        "chance.圈圈 登入驗證碼"
    ]

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    EmailSenderSingleton.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            EmailSenderSingleton.__isFirstInit = True
    
    def send(self, email: str, kind: int, verifyCode: str = "") -> bool:
        context = {}

        if kind != 0 :
            context["verifyCode"] = verifyCode
        
        emailTemplate = render_to_string(
            EmailSenderSingleton.emailTemplateList[kind],
            context
        )

        email = EmailMessage (
            EmailSenderSingleton.emailTitleList[kind],  # 電子郵件標題
            emailTemplate,  # 電子郵件內容
            settings.EMAIL_HOST_USER,  # 寄件者
            [email]  # 收件者
        )

        email.content_subtype = "html"
        email.fail_silently = False
        
        try:
            email.send()
            return True
        except:
            return False
