from abc import ABCMeta, abstractclassmethod

class DaoInterface(metaclass=ABCMeta):

    @abstractclassmethod
    def add(self) -> bool:
        pass

    @abstractclassmethod
    def delete(self) -> bool:
        pass

    @abstractclassmethod
    def updateAll(self) -> bool:
        pass
