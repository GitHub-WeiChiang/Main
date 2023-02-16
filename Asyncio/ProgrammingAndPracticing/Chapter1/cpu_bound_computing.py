import asyncio
import concurrent.futures

from numba import jit
import time


# 一种计算圆周率算法，
# 通过 JIT 加速，更高效地执行 CPU 密集型运算，
# 計算圓周率小數點後十位。
# ...
# 有沒有下面這一行的差異: 有 (16 s)、沒有 (14 min)
@jit
def compute_pi():
    # 因为 Python 程序执行速度是比较慢的，
    # 在做 CPU 密集型运算时显得更加吃力，
    # 在这里进行了 JIT 加速，
    # 原理就是在执行这段代码时先编译成机器码再执行，
    # 可以大大提高程序的运行速度，
    # 如果该程序在您电脑上运行所需时间仍然较长，
    # 可适当调低 count 的数值
    count = 100000
    part = 1.0 / count
    inside = 0.0
    for i in range(1, count):
        for j in range(1, count):
            x = part * i
            y = part * j
            if x * x + y * y <= 1:
                inside += 1
    pi = inside / (count * count) * 4
    return pi


async def print_pi(pool):
    print(f"[{time.strftime('%X')}] Started to compute PI")

    # 将计算圆周率（CPU密集型）的代码交给进程池执行器执行
    pi = await asyncio.get_running_loop().run_in_executor(
        pool,
        compute_pi
    )

    print(f"[{time.strftime('%X')}] {pi}")


async def task():
    for i in range(5):
        print(f"[{time.strftime('%X')}] Step {i}")
        await asyncio.sleep(1)


async def main():
    # 声明一个进程池执行器对象，与线程池执行器一样只需要声明一次，可以在多处使用
    pool = concurrent.futures.ProcessPoolExecutor()

    await asyncio.gather(
        # 将线程池对象 pool 传入给 print_pi 函数，
        # 由 print_pi 函数执行 CPU 密集型代码逻辑，
        # 并且我们将 CPU 密集型代码与异步代码并行执行
        print_pi(pool),
        task()
    )


if __name__ == '__main__':
    asyncio.run(main())
