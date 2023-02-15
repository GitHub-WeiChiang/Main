import asyncio
import time


# 使用 async 关键字声明一个异步函数
async def main():
    print(f"{time.strftime('%X')} Hello")

    # 使用 await 关键字休眠当前协程
    # 透過 await 等待一個可等待對象 (Awaitable)
    await asyncio.sleep(1)

    print(f"{time.strftime('%X')} World")

if __name__ == '__main__':
    # 透過 asyncio.run 運行
    # 協程中所有事務都是由事件驅動
    asyncio.run(main())
