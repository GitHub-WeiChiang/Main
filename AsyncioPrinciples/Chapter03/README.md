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
    * ### 若使用 asyncio.run() 就無需自行撰寫上述步驟:
        ```
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
        ```
* ### Asyncio 的另一個基本功能: 如何執行阻斷式的函式。在協調式多工中，要讓 I/O 密集式函式彼此協調，意味著要使用 await 關鍵字將環境切換回迴圈，但在你 / 妳所接手的專案中，多數並沒有導入 Asyncio，應該如何面對這類阻斷式程式庫呢 ? 可以透過基於執行緒的執行器 (Executor) !
    ```
    import time
    import asyncio


    async def main():
        print(f'{time.ctime()} Hello!')
        await asyncio.sleep(1.0)
        print(f'{time.ctime()} Goodbye!')


    # 這傢伙因為具有阻斷式操作，註定無法成為協程，
    # 不能夠在主執行緒 (執行著 asyncio 迴圈) 的任何地方呼叫此函式，
    # 但是可以在某個執行器運行此函式。
    def blocking():
        # 這是一個阻斷的操作，阻斷主執行緒與迴圈
        time.sleep(0.5)
        print(f'{time.ctime()} Hello from a thread!')


    loop = asyncio.get_event_loop()
    task = loop.create_task(main())

    # 當必需在個別執行緒或甚至個別行程中執行某事，可以使用 loop.run_in_executor，
    # 其不會阻斷主執行緒，只會排定執行器作業，
    # 並回傳 Future，這意味著此方法在另一個協程函式中執行時可以 await，
    # 呼叫 run_until_complete() 後 (事件迴圈開始處理事件)，
    # 就會開始運行執行器作業。
    loop.run_in_executor(None, blocking)
    loop.run_until_complete(task)

    # 此處 pending 集合中並不包含 run_in_executor() 建立的 blocking()，
    # all_tasks() 傳回的清單只會包含 Task 不會包含 Future。
    pending = asyncio.all_tasks(loop=loop)
    for task in pending:
        task.cancel()
    group = asyncio.gather(*pending, return_exceptions=True)
    loop.run_until_complete(group)
    loop.close()
    ```
    * ### run_in_executor() 的第一個參數接受 Executor 實例，不幸的，想用預設值就必需傳入 None，至於為什麼 Asyncio 的開發團隊不使用關鍵字引數呢...，就如同為什麼我年輕的時候不好好讀書呢...。 
    * ### 若使用 asyncio.run() 就無需自行撰寫上述步驟:
        ```
        import asyncio
        import time


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
            # 获取当前正在运行的事件循环对象，
            # 协程是由事件机制驱动的，而用于驱动协程的事件机制系统，
            # 在 Python 中被称为事件循环（Running Loop），
            # 通过该事件循环对象可以与其它线程或进程能行沟通
            current_running_loop = asyncio.get_running_loop()

            # 并发执行一个阻塞型任务和一个异步任务
            await asyncio.gather(
                # 通过函数 run_in_executor 可以让指定的函数运行在特定的执行器（Executor）中，
                # 例如线程池执行器（concurrent.futures.ThreadPoolExecutor）或进程池执行器（concurrent.futures.ProcessPoolExecutor)
                current_running_loop.run_in_executor(None, blocked_task),
                async_task()
            )

        if __name__ == '__main__':
            asyncio.run(main())
        ```
* ### Asyncio 之塔
    | 應用開發者 | 層次 | 概念 | 實作 |
    | - | - | - | - |
    |  | 第 9 層 | 網路: 串流 | StreamReader, StreamWriter, asyncio.open_connection(), asyncio.start_server() |
    |  | 第 8 層 | 網路: TCP 與 UDP | Protocol |
    |  | 第 7 層 | 網路: 傳輸 | BaseTransport |
    | v | 第 6 層 | 工具 | asyncio.Queue |
    | v | 第 5 層 | 子行程與執行緒 | run_in_executor(), asyncio.subprocess |
    |  | 第 4 層 | Task | asyncio.Task, asyncio.create_task() |
    |  | 第 3 層 | Future | asyncio.Future |
    | v | 第 2 層 | 事件迴圈 | asyncio.run(), BaseEventLoop |
    | v | 第 1 層 (基礎) | 協程 | async def, async with, async for, await |
<br />
