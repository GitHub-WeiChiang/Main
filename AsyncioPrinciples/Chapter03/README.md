Chapter03 盤點 Asyncio
=====
* ### 在 Python "並行" 程式設計上，Asyncio 提供了另一個比多執行緒更輕量的選擇，Asyncio 的原理簡單來說，是在事件迴圈中執行一組任務，主要的不同點在於，任務可以自行決定控制權歸還給事件迴圈的時機。
* ### Asyncio 中常用的就只有七個函式，摘要如下:
    * ### 啟動 asyncio 事件迴圈
    * ### 使用 async、await 定義、呼叫函式
    * ### 建立迴圈中執行的任務
    * ### 等待多工任務完成
    * ### 在全部並行任務完成後關閉迴圈
* ### 如何運用迴圈進行基於事件的程式設計
    ```
    import asyncio
    import time


    async def main():
        print(f'{time.ctime()} Hello!')
        await asyncio.sleep(1.0)
        print(f'{time.ctime()} Goodbye!')


    # run() 函式用於執行 async def 定義的函式，
    # 以及協程中可以呼叫的其它函式，
    # 例如 main() 中的 sleep()。
    asyncio.run(main())
    ```
    * ### 大多數基於 Asyncio 的程式碼，只會使用這邊看到的 run() 函式。
* ### 認識 run() 函式背後的簡化版機制 (不是其真正的實作，只是簡略的高階觀念)
    ```
    import asyncio
    import time


    async def main():
        print(f"{time.ctime()} Hello!")
        await asyncio.sleep(1.0)
        print(f"{time.ctime()} Goodbye!")


    # 取得迴圈實例。
    loop = asyncio.get_event_loop()

    # 排定迴圈中要執行的協程，
    # 傳回給 task 的物件可以用來監控任務的狀態，
    # 例如該任務是還在執行亦或是已經完成，
    # 也可以用來取得已完成協程的結果值，
    # 使用 task.cancel() 可以取消任務。
    task = loop.create_task(main())

    # 阻斷目前的執行緒 (通常是主執行緒)，
    # loop.run_until_complete() 會令迴圈持續執行，
    # 直到指定的 coro 完成為止 (才會繼續往下執行)，
    # 迴圈執行期間，其它排定在迴圈中的任務也會執行。
    loop.run_until_complete(task)

    # 若程式的主要 (main) 部分不構成阻斷，
    # 無論是因為收到行程信號或是有程式碼呼叫了 loop.stop() 停止迴圈，
    # run_until_complete() 後續的程式碼就會執行，
    # 慣例上的標準做法首先會收集尚未完成的任務並將其取消。
    pending = asyncio.all_tasks(loop=loop)
    for task in pending:
        task.cancel()

    # 後使用 loop.run_until_complete() 直到這些任務完成。
    group = asyncio.gather(*pending, return_exceptions=True)
    loop.run_until_complete(group)

    # 通常是最後一個操作，在一個已停止的迴圈上呼叫，
    # 用於清空佇列並關閉執行器，
    # 停止的迴圈可以重啟，然後最好是把關閉的迴圈丟了，
    # asyncio.run() 內部會在 return 前關閉迴圈，
    # 每次呼叫 run() 時都會建立新的事件迴圈。
    loop.close()
    ```
    * ### ```coro``` 代表的是協程 (coroutine)，嚴格來說是 async def 函式的呼叫結果，而非函式本身。
    * ### 若使用 asyncio.run() 就無需自行撰寫上述步驟。
<br />
