# Singleton

from gpsDatingApp.game.GameState import GameState
from gpsDatingApp.game.StateMachine import StateMachine
from gpsDatingApp.logger.Logger import Logger

import threading
lock = threading.Lock()

class PairState(GameState):

    __instance: object = None
    __isFirstInit: bool = False

    gameStateMachine: StateMachine = None

    def __new__(cls, gameStateMachine: StateMachine = None):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    PairState.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self, gameStateMachine: StateMachine = None):
        if not self.__isFirstInit:
            self.gameStateMachine = gameStateMachine
            
            PairState.__isFirstInit = True

    # 切換狀態的行為，除了 completeJoinState 供 GameFlow 呼叫，其餘全由內部呼叫
    def completeReadyState(self) -> bool:
        return False

    def completeJoinState(self) -> bool:
        return False

    def completePairState(self) -> bool:
        self.gameStateMachine.setState(self.gameStateMachine.getBroadcastState())

        return True

    def completeBroadcastState(self) -> bool:
        return False

    def completeFinishState(self) -> bool:
        return False

    # 特定狀態下的行為，供外部呼叫，如: GameFlow、views
    # -----
    def ready(self) -> bool:
        return False

    # -----

    def join(self) -> bool:
        return False

    def add(self, userId: str, city: str, district: str, coordinate: list) -> bool:
        return False

    # -----

    async def pair(self) -> bool:
        # do something
        await self.gameStateMachine.pairing()

        return True

    # -----

    def broadcast(self) -> bool:
        return False

    # -----

    def finish(self) -> bool:
        return False
