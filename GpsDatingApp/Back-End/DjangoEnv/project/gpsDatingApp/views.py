import json

from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.utils import timezone
from django.conf import settings

from gpsDatingApp.statusCode.StatusCode import StatusCode
from gpsDatingApp.dao.ReservationDaoSingleton import ReservationDaoSingleton
from gpsDatingApp.dao.RegisterInfoDaoSingleton import RegisterInfoDaoSingleton
from gpsDatingApp.dao.ClusterCreateDaoSingleton import ClusterCreateDaoSingleton
from gpsDatingApp.dao.BasicInfoDaoSingleton import BasicInfoDaoSingleton
from gpsDatingApp.dao.AdvancedInfoDaoSingleton import AdvancedInfoDaoSingleton
from gpsDatingApp.dao.AccountStatusDaoSingleton import AccountStatusDaoSingleton
from gpsDatingApp.dao.AvatarDaoSingleton import AvatarDaoSingleton
from gpsDatingApp.dao.LifeSharingDaoSingleton import LifeSharingDaoSingleton
from gpsDatingApp.dao.LifeSharingOrderDaoSingleton import LifeSharingOrderDaoSingleton
from gpsDatingApp.dao.MatchingInfoDaoSingleton import MatchingInfoDaoSingleton
from gpsDatingApp.dao.DeleteCustomerInfoDaoFacadeSingleton import DeleteCustomerInfoDaoFacadeSingleton
from gpsDatingApp.dao.BlockadeListInfoDaoSingleton import BlockadeListInfoDaoSingleton
from gpsDatingApp.email.EmailCheckerSingleton import EmailCheckerSingleton
from gpsDatingApp.email.EmailSenderSingleton import EmailSenderSingleton
from gpsDatingApp.email.EmailTemplate import EmailTemplate
from gpsDatingApp.redis.ReservationVerifyCodeRedisSingleton import ReservationVerifyCodeRedisSingleton
from gpsDatingApp.redis.CreateAccountVerifyCodeRedisSingleton import CreateAccountVerifyCodeRedisSingleton
from gpsDatingApp.redis.LoginAccountVerifyCodeRedisSingleton import LoginAccountVerifyCodeRedisSingleton
from gpsDatingApp.redis.JwtAccessTokenRedisSingleton import JwtAccessTokenRedisSingleton
from gpsDatingApp.redis.JwtRefreshTokenRedisSingleton import JwtRefreshTokenRedisSingleton
from gpsDatingApp.redis.GameWsVerifyCodeRedisSingleton import GameWsVerifyCodeRedisSingleton
from gpsDatingApp.redis.ChatWsVerifyCodeRedisSingleton import ChatWsVerifyCodeRedisSingleton
from gpsDatingApp.redis.MatchingInfoRedisSingleton import MatchingInfoRedisSingleton
from gpsDatingApp.redis.FriendListInfoRedisSingleton import FriendListInfoRedisSingleton
from gpsDatingApp.redis.BlockadeListInfoRedisSingleton import BlockadeListInfoRedisSingleton
from gpsDatingApp.redis.UserInfoRedisSingleton import UserInfoRedisSingleton
from gpsDatingApp.redis.ReservationCounterRedisSingleton import ReservationCounterRedisSingleton
from gpsDatingApp.redis.ReservationRedisSingleton import ReservationRedisSingleton
from gpsDatingApp.randomCode.RandomCodeGeneratorSingleton import RandomCodeGeneratorSingleton
from gpsDatingApp.randomCode.RandomCodeType import RandomCodeType
from gpsDatingApp.logger.Logger import Logger
from gpsDatingApp.otherConfig.LifeCycleConfig import LifeCycleConfig
from gpsDatingApp.otherConfig.ListInitConfig import ListInitConfig
from gpsDatingApp.models import registerInfo
from gpsDatingApp.jwt.JwtSingleton import JwtSingleton
from gpsDatingApp.commonInspect.HttpRequestMethodInspectSingleton import HttpRequestMethodInspectSingleton
from gpsDatingApp.commonInspect.ReCaptchaInspectSingleton import ReCaptchaInspectSingleton
from gpsDatingApp.commonInspect.RefreshTokenInspectSingleton import RefreshTokenInspectSingleton
from gpsDatingApp.commonInspect.AccessTokenInspectSingleton import AccessTokenInspectSingleton
from gpsDatingApp.socialLogin.GoogleSignInSingleton import GoogleSignInSingleton
from gpsDatingApp.calculate.AgeCalculateSingleton import AgeCalculateSingleton
from gpsDatingApp.game.GameFlow import gameFlowSwitch
from gpsDatingApp.image.ImagePrepBuilder import ImagePrepBuilder

# Create your views here.

# ========================= TEST =========================

# 測試用
def test(request):
    Logger.info("connect test")

    responseDict: dict = {}

    ClusterCreateDaoSingleton().clusterCreate("xxx", timezone.now(), "", "", [0, 0])
    ClusterCreateDaoSingleton().clusterCreate("xxx", timezone.now(), "", "", [0, 0])

    responseDict["statusCode"] = StatusCode.SUCCESS
    # return render(request, "image-upload.html")
    return JsonResponse(responseDict)

# 刪除測試資料
def deleteTestData(request):
    Logger.info("connect deleteTestData")

    responseDict: dict = {}

    DeleteCustomerInfoDaoFacadeSingleton().deleteTestData("xxx")
    DeleteCustomerInfoDaoFacadeSingleton().deleteTestData("xxx")

    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 關閉 GameFlow 執行續
def closeGameFlowThread(request):
    Logger.info("connect closeGameFlowThread")

    responseDict: dict = {}

    gameFlowSwitch(True)

    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# ========================= WEB =========================

# page not found
def pageNotFound(request, exception):
    Logger.info("connect pageNotFound")
    return render(request, "index.html")

# 形象官網
def index(request):
    Logger.info("connect index")
    return render(request, "index.html")

# 事前預約
def reservation(request):
    Logger.info("connect reservation")
    
    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    email: str = ""
    recaptcha_response: str = ""

    # 檢查參數
    try:
        email = request_json['email']
        recaptcha_response = request_json['g-recaptcha-response']
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # ReCaptcha Inspect
    if ReCaptchaInspectSingleton().inspect(recaptcha_response) == False:
        responseDict["statusCode"] = StatusCode.RECAPTCHA_VERIFY_ERROR
        return JsonResponse(responseDict)
    
    # 檢查 email 格式
    if EmailCheckerSingleton().check(email) == False:
        responseDict["statusCode"] = StatusCode.EMAIL_FORMAT_ERROR
        return JsonResponse(responseDict)

    # 檢查是否已預約
    # if ReservationDaoSingleton().findByEmail(email) != None:
    if email in ReservationRedisSingleton().get():
        responseDict["statusCode"] = StatusCode.EMAIL_ALREADY_EXISTS
        return JsonResponse(responseDict)

    # 檢查是否已申請驗證碼
    if ReservationVerifyCodeRedisSingleton().has(email) == True:
        # 提取驗證碼
        verifyCodeDict: dict = ReservationVerifyCodeRedisSingleton().get(email)

        # 剩餘驗證次數
        responseDict["lastVerifyTimes"] = LifeCycleConfig.RESERVATION_VERIFY_TIMES_LIMIT - verifyCodeDict["errorTimes"]
        # 倒數秒數
        responseDict["timeToLive"] = ReservationVerifyCodeRedisSingleton().ttl(email)

        responseDict["statusCode"] = StatusCode.VERIFY_CODE_ALREADY_EXISTS
        return JsonResponse(responseDict)

    # 產生驗證碼
    verifyCode: str = RandomCodeGeneratorSingleton().generate(RandomCodeType.SHORT_VERIFY_CODE)

    # 檢查是否寄送成功
    if EmailSenderSingleton().send(email, EmailTemplate.RESERVATION_VERIFY, verifyCode) == False:
        responseDict["statusCode"] = StatusCode.EMAIL_DELIVER_FAIL
        return JsonResponse(responseDict)

    # 存入 redis
    ReservationVerifyCodeRedisSingleton().set(email, verifyCode)
    # 剩餘驗證次數
    responseDict["lastVerifyTimes"] = LifeCycleConfig.RESERVATION_VERIFY_TIMES_LIMIT
    # 倒數秒數
    responseDict["timeToLive"] = ReservationVerifyCodeRedisSingleton().ttl(email)
    
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 事前預約驗證
def reservationVerify(request):
    Logger.info("connect reservationVerify")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    email: str = ""
    reserveCity: str = ""
    verifyCode: str = ""

    # 檢查參數
    try:
        email = request_json['email']
        reserveCity = request_json["reserveCity"]
        verifyCode = request_json['verifyCode']
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)
    
    # 檢查 email 格式
    if EmailCheckerSingleton().check(email) == False:
        responseDict["statusCode"] = StatusCode.EMAIL_FORMAT_ERROR
        return JsonResponse(responseDict)

    # 檢查是否已預約
    # if ReservationDaoSingleton().findByEmail(email) != None:
    if email in ReservationRedisSingleton().get():
        responseDict["statusCode"] = StatusCode.EMAIL_ALREADY_EXISTS
        return JsonResponse(responseDict)

    # 提取驗證碼
    verifyCodeDict: dict = ReservationVerifyCodeRedisSingleton().get(email)
    
    # 檢查驗證碼是否提取成功
    if verifyCodeDict == None:
        responseDict["statusCode"] = StatusCode.VERIFY_CODE_NOT_EXIST_OR_EXPIRE
        return JsonResponse(responseDict)

    # 檢查驗證碼是否正確
    if verifyCodeDict["verifyCode"] != verifyCode:
        verifyCodeDict["errorTimes"] += 1

        # 檢查驗證次數
        if verifyCodeDict["errorTimes"] == LifeCycleConfig.RESERVATION_VERIFY_TIMES_LIMIT:
            ReservationVerifyCodeRedisSingleton().delete(email)
            responseDict["statusCode"] = StatusCode.VERIFY_CODE_ERROR_EXCESSIVE
            responseDict["lastVerifyTimes"] = 0
            return JsonResponse(responseDict)

        # 修正已錯次數
        ReservationVerifyCodeRedisSingleton().set(email, verifyCodeDict["verifyCode"], verifyCodeDict["errorTimes"], ReservationVerifyCodeRedisSingleton().ttl(email))
        # 剩餘驗證次數
        responseDict["lastVerifyTimes"] = LifeCycleConfig.RESERVATION_VERIFY_TIMES_LIMIT - verifyCodeDict["errorTimes"]

        responseDict["statusCode"] = StatusCode.VERIFY_CODE_ERROR
        return JsonResponse(responseDict)

    # 檢查預約地點是否合法
    if reserveCity not in ListInitConfig().REZ_CNTR_INFO_INIT_FORMAT.keys():
        responseDict["statusCode"] = StatusCode.VAR_VALUE_ILLEGAL
        return JsonResponse(responseDict)

    # 檢查是否寄送成功
    if EmailSenderSingleton().send(email, EmailTemplate.RESERVATION_SUCCESS) == False:
        responseDict["statusCode"] = StatusCode.EMAIL_DELIVER_FAIL
        return JsonResponse(responseDict)

    # 建立欄位並存入資料庫
    if ReservationDaoSingleton().add(email, timezone.now(), reserveCity) == False:
        responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
        return JsonResponse(responseDict)

    # 更新 redis
    ReservationCounterRedisSingleton().count(reserveCity)
    ReservationRedisSingleton().add(email)
    
    # 刪除 redis 驗證碼紀錄
    ReservationVerifyCodeRedisSingleton().delete(email)
    
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 事前預約計數資訊
def reservationCounterInfo(request):
    Logger.info("connect reservationInfo")

    responseDict: dict = {}

    responseDict["reservationCounterInfo"] = ReservationCounterRedisSingleton().get()
    return JsonResponse(responseDict)

# ========================= APP =========================

# 伺服器狀態
def operatingStatus(request):
    Logger.info("connect operatingStatus")

    responseDict: dict = {}

    responseDict["statusCode"] = StatusCode.SUCCESS
    # responseDict["statusCode"] = StatusCode.UNDER_MAINTENANCE
    return JsonResponse(responseDict)

# email 建立帳戶
def emailCreateAccount(request):
    Logger.info("connect emailCreateAccount")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    email: str = ""

    # 檢查參數
    try:
        email = request_json['email']
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 檢查 email 格式
    if EmailCheckerSingleton().check(email) == False:
        responseDict["statusCode"] = StatusCode.EMAIL_FORMAT_ERROR
        return JsonResponse(responseDict)

    # 檢查是否已建立帳戶
    if RegisterInfoDaoSingleton().findByEmail(email) != None:
        responseDict["statusCode"] = StatusCode.EMAIL_ALREADY_EXISTS
        return JsonResponse(responseDict)

    # 檢查是否已申請驗證碼
    if CreateAccountVerifyCodeRedisSingleton().has(email) == True:
        # 提取驗證碼
        verifyCodeDict: dict = CreateAccountVerifyCodeRedisSingleton().get(email)

        # 剩餘驗證次數
        responseDict["lastVerifyTimes"] = LifeCycleConfig.CREATE_ACCOUNT_VERIFY_TIMES_LIMIT - verifyCodeDict["errorTimes"]
        # 倒數秒數
        responseDict["timeToLive"] = CreateAccountVerifyCodeRedisSingleton().ttl(email)

        responseDict["statusCode"] = StatusCode.VERIFY_CODE_ALREADY_EXISTS
        return JsonResponse(responseDict)

    # 產生驗證碼
    verifyCode: str = RandomCodeGeneratorSingleton().generate(RandomCodeType.LONG_VERIFY_CODE)

    # 檢查是否寄送成功
    if EmailSenderSingleton().send(email, EmailTemplate.REGISTER_VERIFY, verifyCode) == False:
        responseDict["statusCode"] = StatusCode.EMAIL_DELIVER_FAIL
        return JsonResponse(responseDict)

    # 存入 redis
    CreateAccountVerifyCodeRedisSingleton().set(email, verifyCode)
    # 剩餘驗證次數
    responseDict["lastVerifyTimes"] = LifeCycleConfig.CREATE_ACCOUNT_VERIFY_TIMES_LIMIT
    # 倒數秒數
    responseDict["timeToLive"] = CreateAccountVerifyCodeRedisSingleton().ttl(email)

    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# email 建立帳戶驗證
def emailCreateAccountVerify(request):
    Logger.info("connect emailCreateAccountVerify")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    email: str = ""
    registerCity: str = ""
    registerDistrict: str = ""
    registerCoordinate: list = []
    verifyCode: str = ""

    # 檢查參數
    try:
        email = request_json['email']
        registerCity = request_json["registerCity"]
        registerDistrict = request_json["registerDistrict"]
        registerCoordinate = request_json["registerCoordinate"]
        verifyCode = request_json['verifyCode']
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 檢查參數長度
    if len(registerCoordinate) != 2:
        responseDict["statusCode"] = StatusCode.PARAMETER_LEN_ERROR
        return JsonResponse(responseDict)

    # 檢查 email 格式
    if EmailCheckerSingleton().check(email) == False:
        responseDict["statusCode"] = StatusCode.EMAIL_FORMAT_ERROR
        return JsonResponse(responseDict)

    # 檢查是否已建立帳戶
    if RegisterInfoDaoSingleton().findByEmail(email) != None:
        responseDict["statusCode"] = StatusCode.EMAIL_ALREADY_EXISTS
        return JsonResponse(responseDict)

    # 提取驗證碼
    verifyCodeDict: dict = CreateAccountVerifyCodeRedisSingleton().get(email)

    # 檢查驗證碼是否提取成功
    if verifyCodeDict == None:
        responseDict["statusCode"] = StatusCode.VERIFY_CODE_NOT_EXIST_OR_EXPIRE
        return JsonResponse(responseDict)

    # 檢查驗證碼是否正確
    if verifyCodeDict["verifyCode"] != verifyCode:
        verifyCodeDict["errorTimes"] += 1

        # 檢查驗證次數
        if verifyCodeDict["errorTimes"] == LifeCycleConfig.CREATE_ACCOUNT_VERIFY_TIMES_LIMIT:
            CreateAccountVerifyCodeRedisSingleton().delete(email)
            responseDict["statusCode"] = StatusCode.VERIFY_CODE_ERROR_EXCESSIVE
            responseDict["lastVerifyTimes"] = 0
            return JsonResponse(responseDict)

        # 修正已錯次數
        CreateAccountVerifyCodeRedisSingleton().set(email, verifyCodeDict["verifyCode"], verifyCodeDict["errorTimes"], CreateAccountVerifyCodeRedisSingleton().ttl(email))
        # 剩餘驗證次數
        responseDict["lastVerifyTimes"] = LifeCycleConfig.CREATE_ACCOUNT_VERIFY_TIMES_LIMIT - verifyCodeDict["errorTimes"]

        responseDict["statusCode"] = StatusCode.VERIFY_CODE_ERROR
        return JsonResponse(responseDict)

    # 建立資料表群集
    if ClusterCreateDaoSingleton().clusterCreate(email, timezone.now(), registerCity, registerDistrict, registerCoordinate) == False:
        responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
        return JsonResponse(responseDict)
    
    # 刪除 redis 驗證碼紀錄
    CreateAccountVerifyCodeRedisSingleton().delete(email)

    ListInitConfig().devTeamUserId()

    responseDict["userId"] = str(RegisterInfoDaoSingleton().findByEmail(email).userId)

    # 若為首次註冊不需更新 Jwt Refresh Time，因其已於建立資料庫群集時寫入
    responseDict["jwt"] = JwtSingleton().generateJwt(responseDict["userId"])

    responseDict["isCompleteFirstSetting"] = AccountStatusDaoSingleton().findByUserId(responseDict["userId"]).isCompleteFirstSetting
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# email 登入帳戶
def emailLoginAccount(request):
    Logger.info("connect emailLoginAccount")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    email: str = ""

    # 檢查參數
    try:
        email = request_json['email']
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 檢查 email 格式
    if EmailCheckerSingleton().check(email) == False:
        responseDict["statusCode"] = StatusCode.EMAIL_FORMAT_ERROR
        return JsonResponse(responseDict)

    # 檢查帳戶是否存在
    if RegisterInfoDaoSingleton().findByEmail(email) == None:
        responseDict["statusCode"] = StatusCode.ACCOUNT_DOES_NOT_EXIST
        return JsonResponse(responseDict)

    # 檢查是否已申請驗證碼
    if LoginAccountVerifyCodeRedisSingleton().has(email) == True:
        # 提取驗證碼
        verifyCodeDict: dict = LoginAccountVerifyCodeRedisSingleton().get(email)

        # 剩餘驗證次數
        responseDict["lastVerifyTimes"] = LifeCycleConfig.LOGIN_ACCOUNT_VERIFY_TIMES_LIMIT - verifyCodeDict["errorTimes"]
        # 倒數秒數
        responseDict["timeToLive"] = LoginAccountVerifyCodeRedisSingleton().ttl(email)

        responseDict["statusCode"] = StatusCode.VERIFY_CODE_ALREADY_EXISTS
        return JsonResponse(responseDict)

    # 產生驗證碼
    verifyCode: str = RandomCodeGeneratorSingleton().generate(RandomCodeType.LONG_VERIFY_CODE)

    # 檢查是否寄送成功
    if EmailSenderSingleton().send(email, EmailTemplate.LOGIN_VERIFY, verifyCode) == False:
        responseDict["statusCode"] = StatusCode.EMAIL_DELIVER_FAIL
        return JsonResponse(responseDict)

    # 存入 redis
    LoginAccountVerifyCodeRedisSingleton().set(email, verifyCode)
    # 剩餘驗證次數
    responseDict["lastVerifyTimes"] = LifeCycleConfig.LOGIN_ACCOUNT_VERIFY_TIMES_LIMIT
    # 倒數秒數
    responseDict["timeToLive"] = LoginAccountVerifyCodeRedisSingleton().ttl(email)

    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# email 登入帳戶驗證
def emailLoginAccountVerify(request):
    Logger.info("connect emailLoginAccountVerify")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    email: str = ""
    verifyCode: str = ""

    # 檢查參數
    try:
        email = request_json['email']
        verifyCode = request_json['verifyCode']
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 檢查 email 格式
    if EmailCheckerSingleton().check(email) == False:
        responseDict["statusCode"] = StatusCode.EMAIL_FORMAT_ERROR
        return JsonResponse(responseDict)

    # 檢查帳戶是否存在
    if RegisterInfoDaoSingleton().findByEmail(email) == None:
        responseDict["statusCode"] = StatusCode.ACCOUNT_DOES_NOT_EXIST
        return JsonResponse(responseDict)

    # 提取驗證碼
    verifyCodeDict: dict = LoginAccountVerifyCodeRedisSingleton().get(email)

    # 檢查驗證碼是否提取成功
    if verifyCodeDict == None:
        responseDict["statusCode"] = StatusCode.VERIFY_CODE_NOT_EXIST_OR_EXPIRE
        return JsonResponse(responseDict)

    # 檢查驗證碼是否正確
    if verifyCodeDict["verifyCode"] != verifyCode:
        verifyCodeDict["errorTimes"] += 1

        # 檢查驗證次數
        if verifyCodeDict["errorTimes"] == LifeCycleConfig.LOGIN_ACCOUNT_VERIFY_TIMES_LIMIT:
            LoginAccountVerifyCodeRedisSingleton().delete(email)
            responseDict["statusCode"] = StatusCode.VERIFY_CODE_ERROR_EXCESSIVE
            responseDict["lastVerifyTimes"] = 0
            return JsonResponse(responseDict)

        # 修正已錯次數
        LoginAccountVerifyCodeRedisSingleton().set(email, verifyCodeDict["verifyCode"], verifyCodeDict["errorTimes"], LoginAccountVerifyCodeRedisSingleton().ttl(email))
        # 剩餘驗證次數
        responseDict["lastVerifyTimes"] = LifeCycleConfig.LOGIN_ACCOUNT_VERIFY_TIMES_LIMIT - verifyCodeDict["errorTimes"]

        responseDict["statusCode"] = StatusCode.VERIFY_CODE_ERROR
        return JsonResponse(responseDict)

    # 刪除 redis 驗證碼紀錄
    LoginAccountVerifyCodeRedisSingleton().delete(email)

    responseDict["userId"] = str(RegisterInfoDaoSingleton().findByEmail(email).userId)

    # Update Last Jwt Refresh Time
    if AccountStatusDaoSingleton().updateLastJwtRefreshTime(responseDict["userId"], timezone.now()) == False:
        responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
        return JsonResponse(responseDict)
    responseDict["jwt"] = JwtSingleton().generateJwt(responseDict["userId"])
    
    responseDict["isCompleteFirstSetting"] = AccountStatusDaoSingleton().findByUserId(responseDict["userId"]).isCompleteFirstSetting
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# Google Sign-In
def googleSignIn(request):
    Logger.info("connect googleSignIn")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    googleSignInToken: str = ""

    # 檢查參數
    try:
        googleSignInToken = request_json['googleSignInToken']
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 參數宣告並檢查 googleSignInToken 後取得 eamil
    email: str = GoogleSignInSingleton().inspect(googleSignInToken)

    # 檢查是否順利取得 email
    if email == "":
        responseDict["statusCode"] = StatusCode.GOOGLE_SIGN_IN_TOKEN_ERROR
        return JsonResponse(responseDict)

    # 檢查 email 格式
    if EmailCheckerSingleton().check(email) == False:
        responseDict["statusCode"] = StatusCode.EMAIL_FORMAT_ERROR
        return JsonResponse(responseDict)

    # 提取使用者資訊
    userRegisterInfo: registerInfo = RegisterInfoDaoSingleton().findByEmail(email)

    # 檢查是否已註冊
    if userRegisterInfo == None:
        # 參數宣告
        registerCity: str = ""
        registerDistrict: str = ""
        registerCoordinate: list = []

        # 檢查參數
        try:
            registerCity = request_json["registerCity"]
            registerDistrict = request_json["registerDistrict"]
            registerCoordinate = request_json["registerCoordinate"]
        except:
            responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
            return JsonResponse(responseDict)

        # 檢查參數長度
        if len(registerCoordinate) != 2:
            responseDict["statusCode"] = StatusCode.PARAMETER_LEN_ERROR
            return JsonResponse(responseDict)

        # 建立資料表群集
        if ClusterCreateDaoSingleton().clusterCreate(email, timezone.now(), registerCity, registerDistrict, registerCoordinate) == False:
            responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
            return JsonResponse(responseDict)

        ListInitConfig().devTeamUserId()

        responseDict["isFirstLogin"] = True
    else:
        responseDict["isFirstLogin"] = False

    responseDict["userId"] = str(RegisterInfoDaoSingleton().findByEmail(email).userId)

    # Update Last Jwt Refresh Time，若為首次註冊不需更新 Jwt Refresh Time，因其已於建立資料庫群集時寫入
    if responseDict["isFirstLogin"] == False and AccountStatusDaoSingleton().updateLastJwtRefreshTime(responseDict["userId"], timezone.now()) == False:
        responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
        return JsonResponse(responseDict)
    
    responseDict["jwt"] = JwtSingleton().generateJwt(responseDict["userId"])

    responseDict["isCompleteFirstSetting"] = AccountStatusDaoSingleton().findByUserId(responseDict["userId"]).isCompleteFirstSetting
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 刷新 jwt
def jwtRefresh(request):
    Logger.info("connect jwtRefresh")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    userId: str = ""
    refresh: str = ""

    # 檢查參數
    try:
        userId = request_json['userId']
        refresh = request_json["refresh"]
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 提取 Jwt Access Token
    accessTokenDict: dict = JwtAccessTokenRedisSingleton().get(userId)

    # 檢查 access Token 是否過期
    if accessTokenDict != None:
        responseDict["statusCode"] = StatusCode.ACCESS_TOKEN_NOT_EXPIRE
        return JsonResponse(responseDict)

    # 提取 Jwt Refresh Token
    refreshTokenDict: dict = JwtRefreshTokenRedisSingleton().get(userId)

    # refresh Token inspect
    refreshTokenInspect: int = RefreshTokenInspectSingleton().inspect(userId, refresh, refreshTokenDict)
    if refreshTokenInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = refreshTokenInspect
        return JsonResponse(responseDict)

    # Update Last Jwt Refresh Time
    if AccountStatusDaoSingleton().updateLastJwtRefreshTime(userId, timezone.now()) == False:
        responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
        return JsonResponse(responseDict)
    responseDict["jwt"] = JwtSingleton().generateJwt(userId)
    
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 基本資訊更新
def basicInfoUpdate(request):
    Logger.info("connect basicInfoUpdate")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    userId: str = ""
    access: str = ""

    # 檢查參數
    try:
        userId = request_json['userId']
        access = request_json["access"]
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 提取 Jwt Access Token
    accessTokenDict: dict = JwtAccessTokenRedisSingleton().get(userId)
    
    # access Token inspect
    accessTokenInspect: int = AccessTokenInspectSingleton().inspect(userId, access, accessTokenDict)
    if accessTokenInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = accessTokenInspect
        return JsonResponse(responseDict)

    # 動態參數宣告
    nickname: str = request_json.get("nickname")
    interest: list = request_json.get("interest")

    # 檢查動態參數
    if nickname == None and interest == None:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 檢查參數長度
    if interest != None and len(interest) < 3 or len(interest) > 5 or len(nickname) < 1 or len(nickname) > 20:
        responseDict["statusCode"] = StatusCode.PARAMETER_LEN_ERROR
        return JsonResponse(responseDict)

    # 補足動態參數
    nickname = UserInfoRedisSingleton().get(userId)["nickname"] if nickname == None else nickname
    interest = UserInfoRedisSingleton().get(userId)["interest"] if interest == None else interest

    # 更新基本資料
    if BasicInfoDaoSingleton().updateMutableInfo(userId, nickname, interest) == False:
        responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
        return JsonResponse(responseDict)

    # 更新 redis
    UserInfoRedisSingleton().setMutableBasicInfo(userId, nickname, interest)

    responseDict["nickname"] = nickname
    responseDict["interest"] = interest

    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 進階資訊更新
def advancedInfoUpdate(request):
    Logger.info("connect advancedInfoUpdate")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    userId: str = ""
    access: str = ""

    # 檢查參數
    try:
        userId = request_json['userId']
        access = request_json["access"]
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 提取 Jwt Access Token
    accessTokenDict: dict = JwtAccessTokenRedisSingleton().get(userId)
    
    # access Token inspect
    accessTokenInspect: int = AccessTokenInspectSingleton().inspect(userId, access, accessTokenDict)
    if accessTokenInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = accessTokenInspect
        return JsonResponse(responseDict)

    # 動態參數宣告
    introduction: str = request_json.get("introduction")
    school: str = request_json.get("school")
    department: str = request_json.get("department")
    country: str = request_json.get("country")
    city: str = request_json.get("city")

    # 檢查動態參數
    if introduction == None and school == None and department == None and country == None and city == None:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 檢查動態參數 introduction 長度
    if introduction != None and len(introduction) > 60:
        responseDict["statusCode"] = StatusCode.PARAMETER_LEN_ERROR
        return JsonResponse(responseDict)

    # 補足動態參數，並檢查值是否合法 (學校、類組、國家、城市)
    introduction = UserInfoRedisSingleton().get(userId)["introduction"] if introduction == None else introduction
    
    school = UserInfoRedisSingleton().get(userId)["school"] if school == None else school
    if school not in ListInitConfig().ADV_INFO_SCH:
        responseDict["statusCode"] = StatusCode.VAR_VALUE_ILLEGAL
        return JsonResponse(responseDict)

    department = UserInfoRedisSingleton().get(userId)["department"] if department == None else department
    if department not in ListInitConfig().ADV_INFO_DEPT:
        responseDict["statusCode"] = StatusCode.VAR_VALUE_ILLEGAL
        return JsonResponse(responseDict)

    country = UserInfoRedisSingleton().get(userId)["country"] if country == None else country
    if country not in ListInitConfig().ADV_INFO_CY:
        responseDict["statusCode"] = StatusCode.VAR_VALUE_ILLEGAL
        return JsonResponse(responseDict)

    city = UserInfoRedisSingleton().get(userId)["city"] if city == None else city
    if city not in ListInitConfig().ADV_INFO_CITY:
        responseDict["statusCode"] = StatusCode.VAR_VALUE_ILLEGAL
        return JsonResponse(responseDict)

    # 更新進階資料
    if AdvancedInfoDaoSingleton().updateAll(userId, introduction, school, department, country, city) == False:
        responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
        return JsonResponse(responseDict)

    # 更新 redis
    UserInfoRedisSingleton().setAdvancedInfo(userId, introduction, school, department, country, city)

    responseDict["introduction"] = introduction
    responseDict["school"] = school
    responseDict["department"] = department
    responseDict["country"] = country
    responseDict["city"] = city

    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 頭像更新
def avatarUpdate(request):
    Logger.info("connect avatarUpdate")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)
    
    # 參數宣告
    userId: str = ""
    access: str = ""
    image = None

    # 檢查參數
    try:
        userId = request.POST["userId"]
        access = request.POST["access"]
        image = request.FILES["image"]
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 提取 Jwt Access Token
    accessTokenDict: dict = JwtAccessTokenRedisSingleton().get(userId)
    
    # access Token inspect
    accessTokenInspect: int = AccessTokenInspectSingleton().inspect(userId, access, accessTokenDict)
    if accessTokenInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = accessTokenInspect
        return JsonResponse(responseDict)

    # 檢查圖片格式
    if image.name.split(".")[-1].lower() not in ["jpg", "png", "gif", "jpeg", "heic"]:
        responseDict["statusCode"] = StatusCode.FILE_TYPE_ERROR
        return JsonResponse(responseDict)

    # 檢查圖片大小
    if image.size >= settings.MAX_FILE_SIZE:
        responseDict["statusCode"] = StatusCode.FILE_SIZE_EXCEED
        return JsonResponse(responseDict)

    # 圖片儲存前預處理
    image = ImagePrepBuilder(image).format().sample().save().close().getInMemoryImage()
    
    # 儲存 avatar
    if AvatarDaoSingleton().updateAll(userId, image) == False:
        responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
        return JsonResponse(responseDict)

    # 更新 redis
    UserInfoRedisSingleton().setAvatar(userId, AvatarDaoSingleton().findByUserId(userId))
    
    responseDict["avatarUrl"] = UserInfoRedisSingleton().get(userId)["avatarUrl"]
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 配對資訊更新
def matchingInfoUpdate(request):
    Logger.info("connect matchingInfoUpdate")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    userId: str = ""
    access: str = ""

    # 檢查參數
    try:
        userId = request_json['userId']
        access = request_json["access"]
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 提取 Jwt Access Token
    accessTokenDict: dict = JwtAccessTokenRedisSingleton().get(userId)
    
    # access Token inspect
    accessTokenInspect: int = AccessTokenInspectSingleton().inspect(userId, access, accessTokenDict)
    if accessTokenInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = accessTokenInspect
        return JsonResponse(responseDict)

    # 動態參數宣告
    matchingAge: list = request_json.get("matchingAge")
    matchingKind: int = request_json.get("matchingKind")

    # 檢查動態參數
    if matchingAge == None and matchingKind == None:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 補足動態參數
    matchingAge = MatchingInfoRedisSingleton().get(userId)["matchingAge"] if matchingAge == None else matchingAge
    matchingKind = MatchingInfoRedisSingleton().get(userId)["matchingKind"] if matchingKind == None else matchingKind

    # 檢查參數長度
    if len(matchingAge) != 2:
        responseDict["statusCode"] = StatusCode.PARAMETER_LEN_ERROR
        return JsonResponse(responseDict)

    # 檢查配對種類邏輯
    matchingKindInspect: int = MatchingInfoDaoSingleton().matchingKindBusinessLogicInspect(userId, matchingAge, matchingKind)
    if matchingKindInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = matchingKindInspect
        return JsonResponse(responseDict)

    # 更新配對資訊
    if MatchingInfoDaoSingleton().updateAll(userId, matchingAge, matchingKind) == False:
        responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
        return JsonResponse(responseDict)

    # 更新 redis
    MatchingInfoRedisSingleton().set(userId, matchingAge, matchingKind)

    responseDict["matchingAge"] = matchingAge
    responseDict["matchingKind"] = matchingKind
    
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 生活分享更新
def lifeSharingUpdate(request):
    Logger.info("connect lifeSharingUpdate")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    userId: str = ""
    access: str = ""

    # 檢查參數
    try:
        userId = request.POST["userId"]
        access = request.POST["access"]
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 提取 Jwt Access Token
    accessTokenDict: dict = JwtAccessTokenRedisSingleton().get(userId)

    # access Token inspect
    accessTokenInspect: int = AccessTokenInspectSingleton().inspect(userId, access, accessTokenDict)
    if accessTokenInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = accessTokenInspect
        return JsonResponse(responseDict)

    # 抓取特殊參數
    images: list = []
    for i in range(LifeSharingDaoSingleton().numOfSheets):
        images.append(request.FILES.get("image" + str(i)))

    # 檢查特殊參數
    hasSpecParam: bool = False
    for i in images:
        if i != None:
            hasSpecParam = True
            break
    if hasSpecParam == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 檢查圖片格式與大小
    for i in range(LifeSharingDaoSingleton().numOfSheets):
        if images[i] == None:
            continue
        if images[i].name.split(".")[-1].lower() not in ["jpg", "png", "gif", "jpeg", "heic"]:
            responseDict["statusCode"] = StatusCode.FILE_TYPE_ERROR
            return JsonResponse(responseDict)
        if images[i].size >= settings.MAX_FILE_SIZE:
            responseDict["statusCode"] = StatusCode.FILE_SIZE_EXCEED
            return JsonResponse(responseDict)
    
    # 圖片儲存前預處理
    for i in range(LifeSharingDaoSingleton().numOfSheets):
        if images[i] == None:
            continue
        else:
            images[i] = ImagePrepBuilder(images[i]).format().sample().save().close().getInMemoryImage()

    # 儲存生活分享圖
    for i in range(LifeSharingDaoSingleton().numOfSheets):
        if images[i] != None and LifeSharingDaoSingleton().update(userId, i, images[i]) == False:
            responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
            return JsonResponse(responseDict)

    # 更新 redis
    UserInfoRedisSingleton().setLifeSharing(userId, LifeSharingDaoSingleton().findByUserId(userId))

    # 生活分享 url 陣列
    lifeSharingUrls: list = UserInfoRedisSingleton().get(userId)["lifeSharingUrls"]
    # 放入 default lifeSharing url
    for i in range(LifeSharingDaoSingleton().numOfSheets):
        lifeSharingUrls[i] = settings.MEDIA_DEFAULT_LIFESHARING_PNG_URL if lifeSharingUrls[i] == None else lifeSharingUrls[i]

    # # 生活分享 url 輔助陣列
    # lifeSharingFlags: list = [True, True, True, True, True, True]
    # for i in range(LifeSharingDaoSingleton().numOfSheets):
    #     if lifeSharingUrls[i] == None:
    #         lifeSharingFlags[i] = False

    responseDict["lifeSharingUrls"] = lifeSharingUrls
    # responseDict["lifeSharingFlags"] = lifeSharingFlags
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 生活分享順序更新
def lifeSharingOrderUpdate(request):
    Logger.info("connect lifeSharingOrderUpdate")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    userId: str = ""
    access: str = ""
    order: list = []

    # 檢查參數
    try:
        userId = request_json['userId']
        access = request_json["access"]
        order = request_json["order"]
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 檢查參數長度
    if order != None and len(order) != 6:
        responseDict["statusCode"] = StatusCode.PARAMETER_LEN_ERROR
        return JsonResponse(responseDict)

    # 提取 Jwt Access Token
    accessTokenDict: dict = JwtAccessTokenRedisSingleton().get(userId)
    
    # access Token inspect
    accessTokenInspect: int = AccessTokenInspectSingleton().inspect(userId, access, accessTokenDict)
    if accessTokenInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = accessTokenInspect
        return JsonResponse(responseDict)

    # 儲存顯示順序
    if order != None and LifeSharingOrderDaoSingleton().updateAll(userId, order) == False:
        responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
        return JsonResponse(responseDict)

    # 更新 redis
    UserInfoRedisSingleton().setLifeSharingOrder(userId, LifeSharingOrderDaoSingleton().findByUserId(userId))

    responseDict["order"] = UserInfoRedisSingleton().get(userId)["order"]
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 快速設定
def quickSetting(request):
    Logger.info("connect quickSetting")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    userId: str = ""
    access: str = ""
    nickname: str = ""
    birthday: str = ""
    sex: str = ""
    interest: list = None
    matchingAge: list = []
    matchingKind: int = -1

    # 檢查參數
    try:
        userId = request_json["userId"]
        access = request_json["access"]
        nickname = request_json["nickname"]
        birthday = request_json["birthday"]
        sex = request_json["sex"]
        interest = request_json["interest"]
        matchingAge = request_json["matchingAge"]
        matchingKind = request_json["matchingKind"]
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 檢查參數長度
    if len(interest) < 3 or len(interest) > 5 or len(matchingAge) != 2 or len(nickname) < 1 or len(nickname) > 20:
        responseDict["statusCode"] = StatusCode.PARAMETER_LEN_ERROR
        return JsonResponse(responseDict)

    # 提取 Jwt Access Token
    accessTokenDict: dict = JwtAccessTokenRedisSingleton().get(userId)
    
    # access Token inspect
    accessTokenInspect: int = AccessTokenInspectSingleton().inspect(userId, access, accessTokenDict)
    if accessTokenInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = accessTokenInspect
        return JsonResponse(responseDict)

    # 檢查年齡
    if AgeCalculateSingleton().isAdult(birthday) == False:
        responseDict["statusCode"] = StatusCode.PARAMETER_SETTING_BUSINESS_LOGIC_ERROR
        return JsonResponse(responseDict)

    # 檢查配對種類邏輯
    matchingKindInspect: int = MatchingInfoDaoSingleton().matchingKindBusinessLogicInspect(userId, matchingAge, matchingKind)
    if matchingKindInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = matchingKindInspect
        return JsonResponse(responseDict)

    # 更新基本資料
    if BasicInfoDaoSingleton().updateAll(userId, "Guest" if userId not in ListInitConfig().DEV_TEAM_USERID else "Developer", nickname, birthday, sex, interest) == False:
        responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
        return JsonResponse(responseDict)

    # 更新配對資訊
    if MatchingInfoDaoSingleton().updateAll(userId, matchingAge, matchingKind) == False:
        responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
        return JsonResponse(responseDict)

    # 更新 redis
    UserInfoRedisSingleton().setBasicInfo(userId, "Guest" if userId not in ListInitConfig().DEV_TEAM_USERID else "Developer", nickname, birthday, sex, interest)
    MatchingInfoRedisSingleton().set(userId, matchingAge, matchingKind)

    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 首次頭像更新
def firstAvatarUpdate(request):
    Logger.info("connect firstAvatarUpdate")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)
    
    # 參數宣告
    userId: str = ""
    access: str = ""
    image = None

    # 檢查參數
    try:
        userId = request.POST["userId"]
        access = request.POST["access"]
        image = request.FILES["image"]
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 提取 Jwt Access Token
    accessTokenDict: dict = JwtAccessTokenRedisSingleton().get(userId)
    
    # access Token inspect
    accessTokenInspect: int = AccessTokenInspectSingleton().inspect(userId, access, accessTokenDict)
    if accessTokenInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = accessTokenInspect
        return JsonResponse(responseDict)

    # 檢查是否已完成首次設定
    if AccountStatusDaoSingleton().findByUserId(userId).isCompleteFirstSetting == True:
        responseDict["statusCode"] = StatusCode.ALREADY_COMPLETED_FIRST_SETTING
        return JsonResponse(responseDict)

    # 檢查圖片格式
    if image.name.split(".")[-1].lower() not in ["jpg", "png", "gif", "jpeg", "heic"]:
        responseDict["statusCode"] = StatusCode.FILE_TYPE_ERROR
        return JsonResponse(responseDict)

    # 檢查圖片大小
    if image.size >= settings.MAX_FILE_SIZE:
        responseDict["statusCode"] = StatusCode.FILE_SIZE_EXCEED
        return JsonResponse(responseDict)

    # 圖片儲存前預處理
    image = ImagePrepBuilder(image).format().sample().save().close().getInMemoryImage()

    # 儲存 avatar
    if AvatarDaoSingleton().updateAll(userId, image) == False:
        responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
        return JsonResponse(responseDict)

    # 更新 isCompleteFirstSetting
    if AccountStatusDaoSingleton().updateIsCompleteFirstSetting(userId) == False:
        responseDict["statusCode"] = StatusCode.DATABASE_ACCESS_EXCEPTION
        return JsonResponse(responseDict)

    # 更新 redis
    UserInfoRedisSingleton().setAvatar(userId, AvatarDaoSingleton().findByUserId(userId))

    responseDict["avatarUrl"] = UserInfoRedisSingleton().get(userId)["avatarUrl"]
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 遊戲 ws 驗證碼申請
def gameWsVerifyCodeApply(request):
    Logger.info("connect gameWsVerifyCodeApply")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    userId: str = ""
    access: str = ""

    # 檢查參數
    try:
        userId = request_json['userId']
        access = request_json["access"]
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 提取 Jwt Access Token
    accessTokenDict: dict = JwtAccessTokenRedisSingleton().get(userId)
    
    # access Token inspect
    accessTokenInspect: int = AccessTokenInspectSingleton().inspect(userId, access, accessTokenDict)
    if accessTokenInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = accessTokenInspect
        return JsonResponse(responseDict)

    # 產生驗證碼
    verifyCode: str = RandomCodeGeneratorSingleton().generate(RandomCodeType.SHORT_VERIFY_CODE)

    # 存入 redis
    GameWsVerifyCodeRedisSingleton().set(userId, verifyCode)

    responseDict["gameWsVerifyCode"] = verifyCode
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 聊天 ws 驗證碼申請
def chatWsVerifyCodeApply(request):
    Logger.info("connect chatWsVerifyCodeApply")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    userId: str = ""
    access: str = ""

    # 檢查參數
    try:
        userId = request_json['userId']
        access = request_json["access"]
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 提取 Jwt Access Token
    accessTokenDict: dict = JwtAccessTokenRedisSingleton().get(userId)
    
    # access Token inspect
    accessTokenInspect: int = AccessTokenInspectSingleton().inspect(userId, access, accessTokenDict)
    if accessTokenInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = accessTokenInspect
        return JsonResponse(responseDict)

    # 產生驗證碼
    verifyCode: str = RandomCodeGeneratorSingleton().generate(RandomCodeType.SHORT_VERIFY_CODE)

    # 存入 redis
    ChatWsVerifyCodeRedisSingleton().set(userId, verifyCode)

    responseDict["chatWsVerifyCode"] = verifyCode
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# # 封鎖好友
# def blockUser(request):
#     Logger.info("connect blockUser")

#     responseDict: dict = {}

#     # Http Request Method Inspect
#     if HttpRequestMethodInspectSingleton().inspect(request) == False:
#         responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
#         return JsonResponse(responseDict)

#     # Get data from POST request
#     request_json: dict = None
#     try:
#         request_json = json.load(request)
#     except:
#         responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
#         return JsonResponse(responseDict)

#     # 參數宣告
#     userId: str = ""
#     access: str = ""
#     blockadeUserId: str = ""

#     # 檢查參數
#     try:
#         userId = request_json['userId']
#         access = request_json["access"]
#         blockadeUserId = request_json["blockadeUserId"]
#     except:
#         responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
#         return JsonResponse(responseDict)

#     # 提取 Jwt Access Token
#     accessTokenDict: dict = JwtAccessTokenRedisSingleton().get(userId)
    
#     # access Token inspect
#     accessTokenInspect: int = AccessTokenInspectSingleton().inspect(userId, access, accessTokenDict)
#     if accessTokenInspect != StatusCode.SUCCESS:
#         responseDict["statusCode"] = accessTokenInspect
#         return JsonResponse(responseDict)

#     # 提取封鎖陣列
#     blockadeList: list = BlockadeListInfoRedisSingleton().get(userId)

#     # 封鎖對象是否已封鎖
#     if blockadeUserId in blockadeList:
#         responseDict["statusCode"] = StatusCode.DATA_ALREADY_EXISTS
#         return JsonResponse(responseDict)

#     # 提取好友陣列
#     friendList: list = FriendListInfoRedisSingleton().get(userId)

#     # 封鎖對象是否為好友
#     if blockadeUserId not in friendList:
#         responseDict["statusCode"] = StatusCode.FRIEND_NOT_EXIST
#         return JsonResponse(responseDict)

#     # 將封鎖對象加入封鎖清單
#     blockadeList.append(blockadeUserId)

#     # 寫入資料庫
#     BlockadeListInfoDaoSingleton().updateAll(userId, blockadeList)
#     #寫入 redis
#     BlockadeListInfoRedisSingleton().set(userId, blockadeList)

#     responseDict["friendList"] = FriendListInfoRedisSingleton().get(userId)
#     responseDict["blockadeList"] = BlockadeListInfoRedisSingleton().get(userId)
#     responseDict["statusCode"] = StatusCode.SUCCESS
#     return JsonResponse(responseDict)

# 使用者資訊獲得
def userInfoAcquisition(request):
    Logger.info("connect userInfoAcquisition")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    userId: str = ""
    access: str = ""
    acquisitionUserId: str = ""

    # 檢查參數
    try:
        userId = request_json['userId']
        access = request_json["access"]
        acquisitionUserId = request_json["acquisitionUserId"]
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 提取 Jwt Access Token
    accessTokenDict: dict = JwtAccessTokenRedisSingleton().get(userId)
    
    # access Token inspect
    accessTokenInspect: int = AccessTokenInspectSingleton().inspect(userId, access, accessTokenDict)
    if accessTokenInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = accessTokenInspect
        return JsonResponse(responseDict)

    # 檢查 acquisitionUserId 是否為自己或是好友
    if userId != acquisitionUserId and acquisitionUserId not in FriendListInfoRedisSingleton().get(userId):
        responseDict["statusCode"] = StatusCode.FRIEND_NOT_EXIST
        return JsonResponse(responseDict)

    # 使用者資訊
    userInfo: dict = UserInfoRedisSingleton().get(acquisitionUserId)
    # 放入 default lifeSharing url
    for i in range(LifeSharingDaoSingleton().numOfSheets):
        userInfo["lifeSharingUrls"][i] = settings.MEDIA_DEFAULT_LIFESHARING_PNG_URL if userInfo["lifeSharingUrls"][i] == None else userInfo["lifeSharingUrls"][i]

    # # 生活分享 url 輔助陣列
    # lifeSharingFlags: list = [True, True, True, True, True, True]
    # for i in range(LifeSharingDaoSingleton().numOfSheets):
    #     if userInfo["lifeSharingUrls"][i] == None:
    #         lifeSharingFlags[i] = False

    responseDict["userInfo"] = userInfo
    # responseDict["userInfo"]["lifeSharingFlags"] = lifeSharingFlags
    responseDict["userInfo"]["age"] = AgeCalculateSingleton().calculate(responseDict["userInfo"]["birthday"])
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)

# 查看自己設定
def viewOneselfSetting(request):
    Logger.info("connect viewOneselfSetting")

    responseDict: dict = {}

    # Http Request Method Inspect
    if HttpRequestMethodInspectSingleton().inspect(request) == False:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_METHODS_ERROR
        return JsonResponse(responseDict)

    # Get data from POST request
    request_json: dict = None
    try:
        request_json = json.load(request)
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_BODY_TYPE_ERROR
        return JsonResponse(responseDict)

    # 參數宣告
    userId: str = ""
    access: str = ""

    # 檢查參數
    try:
        userId = request_json['userId']
        access = request_json["access"]
    except:
        responseDict["statusCode"] = StatusCode.HTTP_REQUEST_PARAMETER_ERROR
        return JsonResponse(responseDict)

    # 提取 Jwt Access Token
    accessTokenDict: dict = JwtAccessTokenRedisSingleton().get(userId)
    
    # access Token inspect
    accessTokenInspect: int = AccessTokenInspectSingleton().inspect(userId, access, accessTokenDict)
    if accessTokenInspect != StatusCode.SUCCESS:
        responseDict["statusCode"] = accessTokenInspect
        return JsonResponse(responseDict)

    responseDict["sex"] = UserInfoRedisSingleton().get(userId)["sex"]
    responseDict["matchingInfo"] = MatchingInfoRedisSingleton().get(userId)
    responseDict["statusCode"] = StatusCode.SUCCESS
    return JsonResponse(responseDict)
