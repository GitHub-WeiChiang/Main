import asyncio
from typing import Any


class AsyncFunWrapper:
    def __init__(self, blocked_fun) -> None:
        super().__init__()

        # 记录阻塞型 IO 函数，便于后续调用
        self._blocked_fun = blocked_fun

    def __call__(self, *args):
        """
        重载函数调用运算符，
        将阻塞型 IO 的调用过程异步化，
        并返回一个可等待对象 (Awaitable)，
        通过重载运算符实现包装逻辑的好处是，
        不用一个一个去实现阻塞型 IO 的所有成员函数，
        从而大大节省了代码量。
        """

        return asyncio.get_running_loop().run_in_executor(
            None,
            self._blocked_fun,
            *args
        )


class AIOWrapper:
    def __init__(self, blocked_file_io) -> None:
        super().__init__()

        # 在包装器对象中记录阻塞型 IO 对象外界通过包装器调用其成员函数时，
        # 事实上是分成两步进行
        # 第一步
        # 获取指定的成员 (该成员是一个可被调用 Callable 的对象)
        # 第二步
        # 对该成员进行调用
        self._blocked_file_io = blocked_file_io

    # 重载访问成员的运算符
    def __getattribute__(self, name: str) -> Any:
        """
        在外界通过包装器 (AIOWrapper) 访问成员操作时，
        创建一个异步函数包装器 (AsyncFunWrapper)，
        目的是将函数调用过程异步化
        """
        return AsyncFunWrapper(
            super().__getattribute__(
                "_blocked_file_io"
            ).__getattribute__(name)
        )


async def open_async(*args) -> AIOWrapper:
    """
    当外界调用该函数时，将返回一个包装器 (AIOWrapper) 对象，
    该包装器包装了一个阻塞型 IO 对象
    """
    return AIOWrapper(
        # 通过 run_in_executor 函数执行阻塞型 IO 的 open 函数，
        # 并转发外界传入的参数
        await asyncio.get_running_loop().run_in_executor(
            None, open, *args
        )
    )
