import concurrent.futures

from asyncio import futures


def run_in_executor(self, executor, func, *args):
    self._check_closed()

    if self._debug:
        self._check_callback(func, 'run_in_executor')

    if executor is None:
        # 如果傳入 None，默認創建線程池執行器執行代碼
        # 也可以傳入自定義的線程池執行器
        executor = self._default_executor
        if executor is None:
            executor = concurrent.futures.ThreadPoolExecutor()
            self._default_executor = executor

    return futures.wrap_future(executor.submit(func, *args), loop=self)
