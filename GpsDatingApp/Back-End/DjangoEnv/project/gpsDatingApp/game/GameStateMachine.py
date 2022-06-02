# Singleton

import math

from channels.layers import get_channel_layer

from gpsDatingApp.game.StateMachine import StateMachine
from gpsDatingApp.game.GameState import GameState
from gpsDatingApp.game.ReadyState import ReadyState
from gpsDatingApp.game.JoinState import JoinState
from gpsDatingApp.game.PairState import PairState
from gpsDatingApp.game.BroadcastState import BroadcastState
from gpsDatingApp.game.FinishState import FinishState
from gpsDatingApp.game.GameConfig import GameConfig
from gpsDatingApp.game.PairPool import PairPool
from gpsDatingApp.game.OppositeSexPairPool import OppositeSexPairPool
from gpsDatingApp.game.SameSexPairPool import SameSexPairPool
from gpsDatingApp.game.GameStateCode import GameStateCode
from gpsDatingApp.redis.MatchingInfoRedisSingleton import MatchingInfoRedisSingleton
from gpsDatingApp.logger.Logger import Logger
from gpsDatingApp.otherConfig.GroupNameConfig import GroupNameConfig
from gpsDatingApp.consumer.ConsumerInfo import ConsumerInfo

import threading
lock = threading.Lock()

import asyncio
from gpsDatingApp.game.GameFlow import startUp

class GameStateMachine(StateMachine):

    __instance: object = None
    __isFirstInit: bool = False

    # 所有狀態
    readyState: GameState = None
    joinState: GameState = None
    pairState: GameState = None
    broadcastState: GameState = None
    finishState: GameState = None

    # 當前狀態
    gameState: GameState = None

    # 配對池陣列
    pairPoolList: list = None

    # 男女配對池
    heterosexualPairPool: PairPool = None
    # 男男配對池
    gayPairPool: PairPool = None
    # 女女配對池
    lesbianPairPool: PairPool = None
    # 隨便配對池
    otherPairPool: PairPool = None

    # 通道層
    channelLayer = None

    # 當前回合參與玩家集合 set()
    roundPlayerSet: set = None

    # 配對執行緒
    _thread = None

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    GameStateMachine.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            self.readyState = ReadyState(self)
            self.joinState = JoinState(self)
            self.pairState = PairState(self)
            self.broadcastState = BroadcastState(self)
            self.finishState = FinishState(self)

            self.gameState = self.readyState

            # 男女配對池
            self.heterosexualPairPool = OppositeSexPairPool()
            # 男男配對池
            self.gayPairPool = SameSexPairPool()
            # 女女配對池
            self.lesbianPairPool = SameSexPairPool()
            # 隨便配對池 (套用 SameSexPairPool，將所有使用者視為同性進行匹配)
            self.otherPairPool = SameSexPairPool()

            # 配對池陣列
            self.pairPoolList = []
            self.pairPoolList.append(self.heterosexualPairPool)
            self.pairPoolList.append(self.gayPairPool)
            self.pairPoolList.append(self.lesbianPairPool)
            self.pairPoolList.append(self.otherPairPool)

            # 通道層
            self.channelLayer = get_channel_layer()

            # 當前回合參與玩家集合
            self.roundPlayerSet = set()

            # 配對執行緒
            self._thread = threading.Thread(target = asyncio.run, args=(startUp(self),))
            self._thread.start()

            GameStateMachine.__isFirstInit = True

    # ================================================================================
    # ================================================================================
    # ================================================================================

    # 商業邏輯，供 GameState 類呼叫與內部呼叫
    async def joinStateNotify(self) -> bool:
        data: dict = {}
        data["gameState"] = self.currentState()

        await self.channelLayer.group_send(
            GroupNameConfig().GAME_ROOM_GROUP,
            {"type": "sendNotify", "data": data},
        )

    def addInPool(self, userId: str, city: str, district: str, coordinate: list) -> bool:
        matchingKind: int = MatchingInfoRedisSingleton().get(userId)["matchingKind"]
        pairkey: str = self.parsePairkey(coordinate)

        if matchingKind == 0:
            self.heterosexualPairPool.addInPool(userId, city, district, pairkey)
            return True
        if matchingKind == 1:
            self.gayPairPool.addInPool(userId, city, district, pairkey)
            return True
        if matchingKind == 2:
            self.lesbianPairPool.addInPool(userId, city, district, pairkey)
            return True
        if matchingKind == 3:
            self.otherPairPool.addInPool(userId, city, district, pairkey)
            return True

        return False

    def currentState(self) -> int:
        if self.gameState == self.readyState:
            return GameStateCode.READY_STATE

        if self.gameState == self.joinState:
            return GameStateCode.JOIN_STATE

        if self.gameState == self.pairState:
            return GameStateCode.PAIR_STATE

        if self.gameState == self.broadcastState:
            return GameStateCode.BROADCAST_STATE

        if self.gameState == self.finishState:
            return GameStateCode.FINISH_STATE

    async def pairing(self) -> bool:
        for pairPool in self.pairPoolList:
            await pairPool.pairing()

        return True

    async def broadcastPairingsResult(self) -> bool:
        for pairPool in self.pairPoolList:
            for result in pairPool.pairResult:
                userIdA: str = result[0]
                userIdB: str = result[1]

                # userA 是否保持連線，是，走 socket
                if userIdA in ConsumerInfo().gamePlayerIndieSet:
                    data: dict = {}
                    data["newFriend"]: bool = True
                    await self.channelLayer.group_send(
                        GroupNameConfig().GAME_PLAYER_INDIE_GROUP + userIdA,
                        {"type": "sendNotify", "data": data},
                    )
                # 否，不做事
                else:
                    pass

                # userB 是否保持連線，是，走 socket
                if userIdB in ConsumerInfo().gamePlayerIndieSet:
                    data: dict = {}
                    data["newFriend"]: bool = True
                    await self.channelLayer.group_send(
                        GroupNameConfig().GAME_PLAYER_INDIE_GROUP + userIdB,
                        {"type": "sendNotify", "data": data},
                    )
                # 否，不做事
                else:
                    pass

        return True

    def clear(self) -> bool:
        for pairPool in self.pairPoolList:
            pairPool.clear()

        self.roundPlayerSet.clear()

        return True

    def parsePairkey(self, coordinate: list) -> str:
        pairkey: str = ""

        longitude: int = math.floor(coordinate[0] * GameConfig().truncateExpressionOperant)
        latitude: int = math.floor(coordinate[1] * GameConfig().truncateExpressionOperant)

        lngMod: int = longitude % 10
        ladMod: int = latitude % 10

        lngStr: str = str((longitude - lngMod if lngMod < 5 else longitude + 5 - lngMod) / GameConfig().truncateExpressionOperant)
        latStr: str = str((latitude - ladMod if ladMod < 5 else latitude + 5 - ladMod) / GameConfig().truncateExpressionOperant)

        pairkey = lngStr + "_" + latStr

        return pairkey

    # ================================================================================
    # ================================================================================
    # ================================================================================

    # 其它狀態機行為，供 GameState 類呼叫
    def setState(self, gameState: GameState) -> bool:
        self.gameState = gameState

    def getReadyState(self) -> GameState:
        return self.readyState

    def getJoinState(self) -> GameState:
        return self.joinState

    def getPairState(self) -> GameState:
        return self.pairState

    def getBroadcastState(self) -> GameState:
        return self.broadcastState

    def getFinishState(self) -> GameState:
        return self.finishState

    # ================================================================================
    # ================================================================================
    # ================================================================================

    # 切換狀態的行為，除了 completeJoinState 供 GameFlow 呼叫，其餘全由內部呼叫
    def completeReadyState(self) -> bool:
        self.gameState.completeReadyState()

    def completeJoinState(self) -> bool:
        self.gameState.completeJoinState()

    def completePairState(self) -> bool:
        self.gameState.completePairState()

    def completeBroadcastState(self) -> bool:
        self.gameState.completeBroadcastState()

    def completeFinishState(self) -> bool:
        self.gameState.completeFinishState()

    # ================================================================================
    # ================================================================================
    # ================================================================================

    # 特定狀態下的行為，供外部呼叫，如: GameFlow、GameConsumer
    # -----

    def ready(self) -> bool:
        self.gameState.ready()
        self.completeReadyState()

    # -----

    async def join(self) -> bool:
        await self.gameState.join()
        # completeJoinState 由外部呼叫

    def add(self, userId: str, city: str, district: str, coordinate: list) -> bool:
        # 確認沒有重複加入
        if userId in self.roundPlayerSet:
            return False

        result: bool = self.gameState.add(userId, city, district, coordinate)

        if result == True:
            self.roundPlayerSet.add(userId)

        return result

    # -----

    async def pair(self) -> bool:
        await self.gameState.pair()
        self.completePairState()

    # -----

    async def broadcast(self) -> bool:
        await self.gameState.broadcast()
        self.completeBroadcastState()

    # -----

    def finish(self) -> bool:
        self.gameState.finish()
        self.completeFinishState()
