import json

from django.utils import timezone
from datetime import datetime
from channels.generic.websocket import AsyncWebsocketConsumer

from gpsDatingApp.otherConfig.GroupNameConfig import GroupNameConfig
from gpsDatingApp.otherConfig.LifeCycleConfig import LifeCycleConfig
from gpsDatingApp.game.GameStateCode import GameStateCode
from gpsDatingApp.logger.Logger import Logger
from gpsDatingApp.redis.ChatWsVerifyCodeRedisSingleton import ChatWsVerifyCodeRedisSingleton
from gpsDatingApp.redis.FriendListInfoRedisSingleton import FriendListInfoRedisSingleton
from gpsDatingApp.redis.BlockadeListInfoRedisSingleton import BlockadeListInfoRedisSingleton
from gpsDatingApp.consumer.ConsumerInfo import ConsumerInfo
from gpsDatingApp.statusCode.StatusCode import StatusCode
from gpsDatingApp.redis.MaleChatRecordRegisterRedisSingleton import MaleChatRecordRegisterRedisSingleton
from gpsDatingApp.redis.FemaleChatRecordRegisterRedisSingleton import FemaleChatRecordRegisterRedisSingleton
from gpsDatingApp.redis.UserInfoRedisSingleton import UserInfoRedisSingleton
from gpsDatingApp.facade.WsFriendMgmtFacade import WsFriendMgmtFacade

class ChatConsumer(AsyncWebsocketConsumer):
    # 物件變數
    # userId
    userId: str = ""
    # 上次心跳時間
    lastHeartbeatTime: datetime = None

    async def connect(self):
        # Logger.info("ChatConsumer connect")

        # 參數宣告與提取
        userId: str = self.scope['url_route']['kwargs']['userId']
        chatWsVerifyCode: str = self.scope['url_route']['kwargs']['chatWsVerifyCode']

        # Logger.info(userId)
        # Logger.info(chatWsVerifyCode)

        # ==================================================

        # 提取驗證碼
        verifyCode: dict = ChatWsVerifyCodeRedisSingleton().get(userId)

        # 檢查驗證碼是否提取成功
        if verifyCode == None:
            await self.close(code = StatusCode.CHAT_WS_VERIFY_CODE_NOT_EXIST.value)
            return

        # 檢查驗證碼是否正確
        if chatWsVerifyCode != verifyCode:
            await self.close(code = StatusCode.CHAT_WS_VERIFY_CODE_ERROR.value)
            return

        # ==================================================
        
        # 連線成功
        # Logger.info("ChatConsumer connect success")

        # Join chat player indie group
        await self.channel_layer.group_add(
            GroupNameConfig().CHAT_PLAYER_INDIE_GROUP + userId,
            self.channel_name
        )

        # 儲存相關資訊
        ConsumerInfo().chatPlayerIndieSet.add(userId)
        self.userId = userId

        # 刪除 redis 中的 verifyCode
        ChatWsVerifyCodeRedisSingleton().delete(userId)
        
        await self.accept()

    async def disconnect(self, close_code):
        # Logger.info("ChatConsumer disconnect")

        # Leave game player indie group
        await self.channel_layer.group_discard(
            GroupNameConfig().CHAT_PLAYER_INDIE_GROUP + self.userId,
            self.channel_name
        )

        # 刪除相關資訊
        ConsumerInfo().chatPlayerIndieSet.discard(self.userId)

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
        
        # 參數宣告與接收
        heartbeat: bool = data_json.get('heartbeat')
        friendInfoListApply: bool = data_json.get('friendInfoListApply')
        chatRecordApply: bool = data_json.get('chatRecordApply')
        clearChatRecord: bool = data_json.get('clearChatRecord')
        messageInfo: dict = data_json.get('messageInfo')
        blockadeId: str = data_json.get('blockadeId')

        # 心跳包
        if heartbeat == True:
            self.lastHeartbeatTime = timezone.now()

        # 好友清單申請
        if friendInfoListApply == True:
            # data["friendList"] = FriendListInfoRedisSingleton().get(self.userId)
            # data["blockadeList"] = BlockadeListInfoRedisSingleton().get(self.userId)
            friendList: list = WsFriendMgmtFacade().friendList(self.userId)

            friendInfoList: list = []

            for friendId in friendList:
                friendInfo: dict = {}

                friendInfo["userId"] = friendId
                friendInfo["nickname"] = UserInfoRedisSingleton().get(friendId)["nickname"]
                friendInfo["avatarUrl"] = UserInfoRedisSingleton().get(friendId)["avatarUrl"]

                friendInfoList.append(friendInfo)

            data["friendInfoList"] = friendInfoList

        # 聊天紀錄申請 (離線時的暫存)
        if chatRecordApply == True:
            # 聊天附載分流，男
            if UserInfoRedisSingleton().get(self.userId)["sex"] == "Male":
                data["messageInfoList"] = MaleChatRecordRegisterRedisSingleton().get(self.userId)
            # 聊天附載分流，女
            elif UserInfoRedisSingleton().get(self.userId)["sex"] == "Female":
                data["messageInfoList"] = FemaleChatRecordRegisterRedisSingleton().get(self.userId)

        # 清空聊天紀錄 (離線時的暫存)
        if clearChatRecord == True:
            # 聊天附載分流，男
            if UserInfoRedisSingleton().get(self.userId)["sex"] == "Male":
                MaleChatRecordRegisterRedisSingleton().clear(self.userId)
            # 聊天附載分流，女
            elif UserInfoRedisSingleton().get(self.userId)["sex"] == "Female":
                FemaleChatRecordRegisterRedisSingleton().clear(self.userId)
        
        # 訊息資訊
        if messageInfo != None:
            # 參數宣告
            receiver: str = messageInfo.get("receiver")

            message = messageInfo.get("message")
            if type(message) != str:
                await self.close(code = StatusCode.CHAT_WS_REQUEST_PARAMETER_ERROR.value)

            time: datetime = timezone.now()

            # 提取好友陣列
            # friendList: list = FriendListInfoRedisSingleton().get(self.userId)
            friendList: list = WsFriendMgmtFacade().friendList(self.userId)
            # 提取封鎖陣列
            # blockadeList: list = BlockadeListInfoRedisSingleton().get(self.userId)
            blockadeList: list = WsFriendMgmtFacade().blockadeList(self.userId)
            # 檢查是否為好友
            # if receiver in friendList and receiver not in blockadeList:
            if receiver != None and message!= None and receiver in friendList:
                # make message info list
                msgData: dict = {}
                msgData["messageInfoList"]: list = []

                messageInfo: dict = {}
                messageInfo["sender"] = self.userId
                messageInfo["message"] = message
                messageInfo["time"] = time.strftime("%Y-%m-%d %H:%M:%S")

                msgData["messageInfoList"].append(messageInfo)

                messageInfoAck: dict = {}
                messageInfoAck["receiver"] = receiver
                messageInfoAck["message"] = message
                messageInfoAck["time"] = time.strftime("%Y-%m-%d %H:%M:%S")

                # 若 messageInfo 內容正常且 receiver 保持連線
                if receiver in ConsumerInfo().chatPlayerIndieSet:
                    await self.channel_layer.group_send(
                        GroupNameConfig().CHAT_PLAYER_INDIE_GROUP + receiver,
                        {"type": "sendNotify", "data": msgData},
                    )
                # 若 messageInfo 內容正常但 receiver 斷線
                elif receiver not in ConsumerInfo().chatPlayerIndieSet:
                    # 聊天附載分流，男
                    if UserInfoRedisSingleton().get(receiver)["sex"] == "Male":
                        MaleChatRecordRegisterRedisSingleton().set(receiver, self.userId, message, time)
                    # 聊天附載分流，女
                    elif UserInfoRedisSingleton().get(receiver)["sex"] == "Female":
                        FemaleChatRecordRegisterRedisSingleton().set(receiver, self.userId, message, time)
                # messageInfo 內容有誤
                else:
                    await self.close(code = StatusCode.CHAT_WS_REQUEST_PARAMETER_ERROR.value)
                    return
                data["messageInfoAck"] = messageInfoAck
            elif receiver in blockadeList:
                pass
            else:
                await self.close(code = StatusCode.CHAT_WS_REQUEST_PARAMETER_ERROR.value)
                return

        # 封鎖好友
        if blockadeId != None:
            # 提取封鎖陣列
            blockadeList: list = WsFriendMgmtFacade().blockadeList(self.userId)
            # 封鎖對象是否已封鎖
            if blockadeId in blockadeList:
                await self.close(code = StatusCode.CHAT_WS_REQUEST_PARAMETER_ERROR.value)
                return
            
            # 提取好友陣列
            friendList: list = WsFriendMgmtFacade().friendList(self.userId)
            # 封鎖對象是否為好友
            if blockadeId not in friendList:
                await self.close(code = StatusCode.CHAT_WS_REQUEST_PARAMETER_ERROR.value)
                return

            # 封鎖好友
            await WsFriendMgmtFacade().removeFriend(self.userId, blockadeId)

        # Send data to WebSocket
        await self.send(text_data = json.dumps(data))

    # Receive data from room group
    async def sendNotify(self, event):
        data: dict = event['data']

        # Logger.info(self.userId)

        # 時間差 seconds
        timeDifference: datetime = timezone.now() - self.lastHeartbeatTime

        if timeDifference.seconds < LifeCycleConfig.CHAT_CONSUMER_RECEIVE_INR_TIME_LIMIT:
            # Send data to WebSocket
            await self.send(text_data = json.dumps(data))
        elif "messageInfoList" in data:
            # 儲存對話資訊
            # 聊天附載分流，男
            if UserInfoRedisSingleton().get(self.userId)["sex"] == "Male":
                MaleChatRecordRegisterRedisSingleton().set(self.userId, data["messageInfoList"]["sender"], data["messageInfoList"]["message"], data["messageInfoList"]["time"])
            # 聊天附載分流，女
            elif UserInfoRedisSingleton().get(self.userId)["sex"] == "Female":
                FemaleChatRecordRegisterRedisSingleton().set(self.userId, data["messageInfoList"]["sender"], data["messageInfoList"]["message"], data["messageInfoList"]["time"])
            # 斷開
            await self.close(code = StatusCode.HB_INR_TIME_OUT.value)
