from abc import ABCMeta, abstractclassmethod

class RedisInterface(metaclass=ABCMeta):

    @abstractclassmethod
    def set(self) -> None:
        pass

    @abstractclassmethod
    def get(self) -> None:
        pass

    @abstractclassmethod
    def has(self) -> None:
        pass

    @abstractclassmethod
    def delete(self) -> None:
        pass

    @abstractclassmethod
    def ttl(self) -> None:
        pass
