# Singleton

import threading
import time
import asyncio

from gpsDatingApp.game.StateMachine import StateMachine
from gpsDatingApp.game.GameConfig import GameConfig
from gpsDatingApp.logger.Logger import Logger

# 是否結束
isClose: bool = False

def gameFlowSwitch(switch: bool) -> bool:
    global isClose
    isClose = switch
    return isClose

async def goToSleep(howManySecond: int):
    start = time.time()
    while time.time() - start < howManySecond:
        pass

async def startUp(gameStateMachine: StateMachine):
    global isClose

    while isClose == False:
        # Logger.info("ready state")
        gameStateMachine.ready()

        # Logger.info("join state")
        await gameStateMachine.join()

        # Logger.info("wait 5 sec for user to join")
        # time.sleep(GameConfig().joinStateTimeLimit)
        await asyncio.sleep(GameConfig().joinStateTimeLimit)
        # await goToSleep(GameConfig().joinStateTimeLimit)
        gameStateMachine.completeJoinState()

        # Logger.info("pair state")
        await gameStateMachine.pair()

        # Logger.info("broadcast state")
        await gameStateMachine.broadcast()

        # Logger.info("finish state")
        gameStateMachine.finish()

        # 緩衝
        # time.sleep(GameConfig().bufferTime)
        await asyncio.sleep(GameConfig().bufferTime)
        # await goToSleep(GameConfig().bufferTime)

    Logger.info("game flow close")
