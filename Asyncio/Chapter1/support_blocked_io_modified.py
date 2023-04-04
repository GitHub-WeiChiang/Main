import asyncio
import time
import concurrent.futures


# 声明一个阻塞型任务
def blocked_task():
    for i in range(10):
        # 以 time.sleep 函数来模拟阻塞型 IO 逻辑的执行效果
        time.sleep(1)
        print(f"[{time.strftime('%X')}] Blocked task {i}")


# 声明一个异步任务
async def async_task():
    for i in range(2):
        await asyncio.sleep(5)
        print(f"[{time.strftime('%X')}] Async task {i}")


async def main():
    # 创建一个线程池执行器，该执行器所允许的最大线程数是 5
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    # 获取当前正在运行的事件循环对象，
    # 协程是由事件机制驱动的，而用于驱动协程的事件机制系统，
    # 在 Python 中被称为事件循环（Running Loop），
    # 通过该事件循环对象可以与其它线程或进程能行沟通
    current_running_loop = asyncio.get_running_loop()

    # 并发执行一个阻塞型任务和一个异步任务
    await asyncio.gather(
        # 通过函数 run_in_executor 可以让指定的函数运行在特定的执行器（Executor）中，
        # 例如线程池执行器（concurrent.futures.ThreadPoolExecutor）或进程池执行器（concurrent.futures.ProcessPoolExecutor)
        current_running_loop.run_in_executor(executor, blocked_task),
        async_task()
    )

if __name__ == "__main__":
    asyncio.run(main())
