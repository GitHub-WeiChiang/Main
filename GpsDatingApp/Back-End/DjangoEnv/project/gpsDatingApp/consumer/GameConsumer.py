import json

from django.utils import timezone
from datetime import datetime
from channels.generic.websocket import AsyncWebsocketConsumer

from gpsDatingApp.otherConfig.GroupNameConfig import GroupNameConfig
from gpsDatingApp.otherConfig.LifeCycleConfig import LifeCycleConfig
from gpsDatingApp.game.GameStateCode import GameStateCode
from gpsDatingApp.game.GameStateMachine import GameStateMachine
from gpsDatingApp.logger.Logger import Logger
from gpsDatingApp.redis.GameWsVerifyCodeRedisSingleton import GameWsVerifyCodeRedisSingleton
from gpsDatingApp.consumer.ConsumerInfo import ConsumerInfo
from gpsDatingApp.statusCode.StatusCode import StatusCode

class GameConsumer(AsyncWebsocketConsumer):
    # 物件變數
    # userId
    userId: str = ""
    # 上次接收時間
    lastHeartbeatTime: datetime = None

    async def connect(self):
        Logger.info("GameConsumer connect")

        # 參數宣告與提取
        userId: str = self.scope['url_route']['kwargs']['userId']
        gameWsVerifyCode: str = self.scope['url_route']['kwargs']['gameWsVerifyCode']

        # Logger.info(userId)
        # Logger.info(gameWsVerifyCode)

        # ==================================================

        # 提取驗證碼
        verifyCode: dict = GameWsVerifyCodeRedisSingleton().get(userId)

        # 檢查驗證碼是否提取成功
        if verifyCode == None:
            # Logger.info("GameConsumer connect VERIFY_CODE_NOT_EXIST")
            await self.close(code = StatusCode.GAME_WS_VERIFY_CODE_NOT_EXIST.value)
            return

        # 檢查驗證碼是否正確
        if gameWsVerifyCode != verifyCode:
            # Logger.info("GameConsumer connect VERIFY_CODE_ERROR")
            await self.close(code = StatusCode.GAME_WS_VERIFY_CODE_ERROR.value)
            return

        # ==================================================
        
        # 連線成功
        # Logger.info("GameConsumer connect success")

        # Join game room group
        await self.channel_layer.group_add(
            GroupNameConfig().GAME_ROOM_GROUP,
            self.channel_name
        )

        # Join game player indie group
        await self.channel_layer.group_add(
            GroupNameConfig().GAME_PLAYER_INDIE_GROUP + userId,
            self.channel_name
        )

        # 儲存相關資訊
        ConsumerInfo().gamePlayerIndieSet.add(userId)
        self.userId = userId

        # 刪除 redis 中的 verifyCode
        GameWsVerifyCodeRedisSingleton().delete(userId)

        # 儲存接收時間
        self.lastHeartbeatTime = timezone.now()
        
        await self.accept()

    async def disconnect(self, close_code):
        # Logger.info("GameConsumer disconnect")

        # Leave game room group
        await self.channel_layer.group_discard(
            GroupNameConfig().GAME_ROOM_GROUP,
            self.channel_name
        )

        # Leave game player indie group
        await self.channel_layer.group_discard(
            GroupNameConfig().GAME_PLAYER_INDIE_GROUP + self.userId,
            self.channel_name
        )

        # 刪除相關資訊
        ConsumerInfo().gamePlayerIndieSet.discard(self.userId)

    # Receive data from WebSocket
    async def receive(self, text_data):
        data_json: dict = None

        #　回傳值
        data: dict = {}

        try:
            data_json = json.loads(text_data)
        except:
            await self.close(code = StatusCode.WS_DP_BODY_TYPE_ERROR.value)
            return

        # Logger.info("someone join")
        # Logger.info(data_json)
        
        # 參數宣告
        city: str = data_json.get('city')
        district: str = data_json.get('district')
        coordinate: list = data_json.get('coordinate')

        # 檢查參數
        if city == None or district == None or coordinate == None:
            data["gameStateCode"] = GameStateCode.PARAMETER_ERROR
        # 加入遊戲失敗
        elif GameStateMachine().add(self.userId, city, district, coordinate) == False:
            data["gameStateCode"] = GameStateCode.JOIN_GAME_ERROR
        # 加入遊戲成功
        else:
            data["gameStateCode"] = GameStateCode.SUCCESS

        # 儲存接收時間
        self.lastHeartbeatTime = timezone.now()

        # Send data to WebSocket
        await self.send(text_data = json.dumps(data))

    # Receive data from room group
    async def sendNotify(self, event):
        data: dict = event['data']

        # Logger.info(self.userId)

        # 時間差 seconds
        timeDifference: datetime = timezone.now() - self.lastHeartbeatTime

        if timeDifference.seconds < LifeCycleConfig.GAME_CONSUMER_RECEIVE_INR_TIME_LIMIT:
            # Send data to WebSocket
            await self.send(text_data = json.dumps(data))
        else:
            # 斷開
            await self.close(code = StatusCode.HB_INR_TIME_OUT.value)
