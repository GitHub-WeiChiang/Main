# Interface

from abc import ABCMeta, abstractclassmethod

class GameState(metaclass=ABCMeta):
    # 切換狀態的行為，除了 completeJoinState 供 GameFlow 呼叫，其餘全由內部呼叫
    @abstractclassmethod
    def completeReadyState(self) -> bool:
        pass

    @abstractclassmethod
    def completeJoinState(self) -> bool:
        pass

    @abstractclassmethod
    def completePairState(self) -> bool:
        pass

    @abstractclassmethod
    def completeBroadcastState(self) -> bool:
        pass

    @abstractclassmethod
    def completeFinishState(self) -> bool:
        pass

    # 特定狀態下的行為，供外部呼叫，如: GameFlow、views
    # -----
    @abstractclassmethod
    def ready(self) -> bool:
        pass

    # -----

    @abstractclassmethod
    def join(self) -> bool:
        pass

    @abstractclassmethod
    def add(self, userId: str, city: str, district: str, coordinate: list) -> bool:
        pass

    # -----
    
    @abstractclassmethod
    def pair(self) -> bool:
        pass

    # -----

    @abstractclassmethod
    def broadcast(self) -> bool:
        pass

    # -----
    
    @abstractclassmethod
    def finish(self) -> bool:
        pass
