Question016 - asyncio.run() 背後的細節秘密「事件迴圈」是什麼 ?
=====
* ### 大部分基於 Asyncio 的函式，建議使用 async.run() 來執行。
* ### 它的細節是...
```
import asyncio
import time

async def main():
    print(f"{time.ctime()} Hello!")
    await asyncio.sleep(1.0)
    print(f"{time.ctime()} Goodbye!")

if __name__ == '__main__':
    # 取得事件迴圈實例。
    loop = asyncio.get_event_loop()

    # 排定需執行的協程任務，回傳的 task 可用於監控任務狀態。
    task = loop.create_task(main())

    # 阻斷當前執行緒，並使事件迴圈執行。
    loop.run_until_complete(task)

    # 如果 main 的阻斷失效，收集事件迴圈中全部的任務。
    pending = asyncio.all_tasks(loop=loop)

    # 將任務取消。
    for task in pending:
        task.cancel()

    # 從任務集合中取得尚未完成的任務。
    group = asyncio.gather(*pending, return_exceptions=True)

    # 阻斷當前執行緒，並使事件迴圈執行。
    loop.run_until_complete(group)

    # 關閉事件迴圈。
    loop.close()
```
* ### 只有一個執行緒在底層執行一個事件迴圈，不斷檢查任務，若有阻斷會找出下一個可執行任務，記得最後要關閉事件迴圈。
<br />
