"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

from gpsDatingApp.logger.Logger import Logger

from gpsDatingApp.views import test
from gpsDatingApp.views import deleteTestData

from gpsDatingApp.views import pageNotFound
from gpsDatingApp.views import index
from gpsDatingApp.views import reservation
from gpsDatingApp.views import reservationVerify
from gpsDatingApp.views import reservationCounterInfo

from gpsDatingApp.views import operatingStatus
from gpsDatingApp.views import emailCreateAccount
from gpsDatingApp.views import emailCreateAccountVerify
from gpsDatingApp.views import emailLoginAccount
from gpsDatingApp.views import emailLoginAccountVerify
from gpsDatingApp.views import googleSignIn
from gpsDatingApp.views import jwtRefresh
from gpsDatingApp.views import basicInfoUpdate
from gpsDatingApp.views import advancedInfoUpdate
from gpsDatingApp.views import avatarUpdate
from gpsDatingApp.views import matchingInfoUpdate
from gpsDatingApp.views import lifeSharingUpdate
from gpsDatingApp.views import lifeSharingOrderUpdate
from gpsDatingApp.views import quickSetting
from gpsDatingApp.views import firstAvatarUpdate
from gpsDatingApp.views import closeGameFlowThread
from gpsDatingApp.views import gameWsVerifyCodeApply
from gpsDatingApp.views import chatWsVerifyCodeApply
# from gpsDatingApp.views import blockUser
from gpsDatingApp.views import userInfoAcquisition
from gpsDatingApp.views import viewOneselfSetting

urlpatterns = [
    # path('admin/', admin.site.urls),

    # ========== TEST ==========

    # 測試用
    # path('test', test),

    # 刪除測試資料
    # path('delete/test/data', deleteTestData),

    # 關閉 GameFlow 執行續
    # path('close/game/flow/thread', closeGameFlowThread),

    # ========== WEB ==========

    # 形象官網
    # url(r'^$', index),
    path('', index),

    # 事前預約
    path(settings.DOMAIN_SUFFIX + 'reservation', reservation),

    # 事前預約驗證
    path(settings.DOMAIN_SUFFIX + 'reservation/verify', reservationVerify),

    # 事前預約計數資訊
    path(settings.DOMAIN_SUFFIX + 'reservation/counter/info', reservationCounterInfo),

    # ========== APP ==========

    # 伺服器狀態
    path(settings.DOMAIN_SUFFIX + 'operating/status', operatingStatus),

    # email 建立帳戶
    path(settings.DOMAIN_SUFFIX + 'email/create/account', emailCreateAccount),

    # email 建立帳戶驗證
    path(settings.DOMAIN_SUFFIX + 'email/create/account/verify', emailCreateAccountVerify),

    # email 登入帳戶
    path(settings.DOMAIN_SUFFIX + 'email/login/account', emailLoginAccount),

    # email 登入帳戶驗證
    path(settings.DOMAIN_SUFFIX + 'email/login/account/verify', emailLoginAccountVerify),

    # Google Sign-In
    path(settings.DOMAIN_SUFFIX + 'google/sign-in', googleSignIn),

    # 刷新 jwt
    path(settings.DOMAIN_SUFFIX + 'jwt/refresh', jwtRefresh),

    # 基本資訊更新
    path(settings.DOMAIN_SUFFIX + 'basic/info/update', basicInfoUpdate),

    # 進階資訊更新
    path(settings.DOMAIN_SUFFIX + 'advanced/info/update', advancedInfoUpdate),

    # 頭像更新
    path(settings.DOMAIN_SUFFIX + 'avatar/update', avatarUpdate),

    # 配對資訊更新
    path(settings.DOMAIN_SUFFIX + 'matching/info/update', matchingInfoUpdate),

    # 生活分享更新
    path(settings.DOMAIN_SUFFIX + 'life/sharing/update', lifeSharingUpdate),

    # 生活分享順序更新
    path(settings.DOMAIN_SUFFIX + 'life/sharing/order/update', lifeSharingOrderUpdate),

    # 快速設定
    path(settings.DOMAIN_SUFFIX + 'quick/setting', quickSetting),

    # 首次頭像更新
    path(settings.DOMAIN_SUFFIX + 'first/avatar/update', firstAvatarUpdate),

    # 遊戲 ws 驗證碼申請
    path(settings.DOMAIN_SUFFIX + 'game/ws/verify/code/apply', gameWsVerifyCodeApply),

    # 聊天 ws 驗證碼申請
    path(settings.DOMAIN_SUFFIX + 'chat/ws/verify/code/apply', chatWsVerifyCodeApply),

    # # 封鎖好友
    # path(settings.DOMAIN_SUFFIX + 'block/user', blockUser),

    # 使用者資訊獲得
    path(settings.DOMAIN_SUFFIX + 'user/info/acquisition', userInfoAcquisition),

    # 查看自己設定
    path(settings.DOMAIN_SUFFIX + 'view/oneself/setting', viewOneselfSetting),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# handler
handler404 = pageNotFound

# # 配對執行緒 (已停用並移至 GameStateMachine)
# import threading
# import asyncio

# from gpsDatingApp.game.GameFlow import startUp
# from gpsDatingApp.game.GameStateMachine import GameStateMachine

# _thread = threading.Thread(target = asyncio.run, args=(startUp(GameStateMachine()),))
# _thread.start()
