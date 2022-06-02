# Singleton

import threading
lock = threading.Lock()

class GroupNameConfig():

    __instance = None
    __isFirstInit: bool = False

    # 組態
    GAME_ROOM_GROUP: str = "gameRoomGroup"
    GAME_PLAYER_INDIE_GROUP: str = "gamePlayerIndieGroup_"
    CHAT_PLAYER_INDIE_GROUP: str = "chatPlayerIndieGroup_"

    def __new__(cls):
        if not cls.__instance:
            with lock:
                if not cls.__instance:
                    GroupNameConfig.__instance = super().__new__(cls)
        return cls.__instance
    
    def __init__(self):
        if not self.__isFirstInit:
            GroupNameConfig.__isFirstInit = True
