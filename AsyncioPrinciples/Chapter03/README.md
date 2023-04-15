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
    | ~~v~~ | 第 9 層 | 網路: 串流 | StreamReader, StreamWriter, asyncio.open_connection(), asyncio.start_server() |
    |  | 第 8 層 | 網路: TCP 與 UDP | Protocol |
    |  | 第 7 層 | 網路: 傳輸 | BaseTransport |
    | v | 第 6 層 | 工具 | asyncio.Queue |
    | v | 第 5 層 | 子行程與執行緒 | run_in_executor(), asyncio.subprocess |
    |  | 第 4 層 | Task | asyncio.Task, asyncio.create_task() |
    |  | 第 3 層 | Future | asyncio.Future |
    | v | 第 2 層 | 事件迴圈 | asyncio.run(), BaseEventLoop |
    | v | 第 1 層 (基礎) | 協程 | async def, async with, async for, await |
    * ### 第 1 層: 基礎層，第三方框架設計的起點，之名非同步框架 Curio 與 Trio 都只使用了這一層，僅此這一層。
    * ### 第 2 層: 提供了迴圈的規範 AbstractEventLoop 與實作 BaseEventLoop，Curio 與 Trio 就各自實作了自己的事件迴圈，而 uvloop 提供了效能更好的迴圈實作 (只替換了此階層)。
    * ### 第 3, 4 層: 提供 Future (父類別) 與 Task (子類別)，其中 Task 為 Future 的子類別。
        * ### Future 實例代表某種進行中的動作，可以透過事件迴圈的通知取的結果。
        * ### Task 代表的是事件迴圈中運行的協程。
        * ### Future 是 "迴圈感知 (Loop Aware)"；而 Task 兼具 "迴圈感知 (Loop Aware)" 與 "協程感知 (Coroutine Aware)"。
        * ### 簡而言之，應用開發者常用 Task，框架開發者則視需求而定。
    * ### 第 5 層: 必需在個別執行緒，或甚至是個別行程中啟動、等待工作的特性。
    * ### 第 6 層: 具有非同步感知 (Async Aware) 的一些工具，asyncio.Queue 與執行緒安全的 queue.Queue 類似，差別在於 asyncio.Queue 在進行 get() 與 put() 時要配合 await 關鍵字，不可以在協程中直接使用 queue.Queue，因為它的 get() 會阻斷主執行緒。
    * ### 第 7 層: 如果你 / 妳不是框架設計者，不會使用到這層。
    * ### 第 8 層: 協定 API，相較於串流 API，具有更細的粒度。
    * ### 第 9 層: 串流 API，使用串流層的場合都可以使用協定層，當然串流層較易於使用。
* ### 使用 Asyncio 進行 I/O 應用程式開發 (非框架) 應該關注:
    * ### 第 1 層: 知道撰寫 async def 函式的方式，以及如何使用 await 來呼叫、執行其它協程。
    * ### 第 2 層: 瞭解啟動、關機以及與事件迴圈互動的方式。
    * ### 第 5 層: 在非同步應用程式中想使用阻斷式程式碼，執行器是必要的，畢竟現今第三方程式庫大多與非同步不相容。
    * ### 第 6 層: 若要提供資料給一或多個長時運行的協程，使用 asyncio.Queue 是最好的方式，就如同使用 queue.Queue 在執行緒間分派資料。
    * ### ~~第 9 層~~: 其實在使用第三方程式庫的情況下 (多數情況都是如此)，並不會使用到這一層。
* ### 協程
    * ### Python 3.4 導入了 asyncio，但在 Python 3.5 才加入 async def 與 await 協程語法。
    * ### Python 3.4 中是將產生器 (Generator) 作為協程使用，在一些較舊的程式碼中，會看到產生器韓式使用了 ```@asyncio.coroutine``` 裝飾，且包含了 yield from 陳述。
    * ### Python 3.5 的 async def 所建立的協程，被稱為 "原生協程"。
    * ### 以下將會示範相關的低階互動。
* ### 新的 async def 關鍵字
    ```
    # 標準庫 inspect 模組提供更好的內省 (introspective) 機制
    import inspect


    # 透過 async def 宣告函式
    async def f():
        return 123

    # 雖然把 async def 所宣告的函式稱為協程，
    # 但嚴格來說，它只是 "協程函式"。
    print(type(f))
    # <class 'function'>

    # iscoroutinefunction() 可以區別一般函式與協程函式
    print(inspect.iscoroutinefunction(f))
    # True
    ```
    * ### 如同當函數內包含了 yield 會被稱為產生器，實際上它也只是個函式，需在函式執行後才會傳回產生器，協程函式也是如此，必需呼叫 async def 函式，才能取得協程物件。
    ```
    import inspect


    async def f():
        return 123

    coro = f()

    print(type(coro))
    # <class 'coroutine'>

    print(inspect.iscoroutine(coro))
    # True
    ```
    * ### 協程是什麼 ? 協程是個物件，可以重啟被暫停的函式。
    * ### 有點耳熟捏 ? 協程類似產生器，也確實在 Python 3.5 前，是透過在一般的產生器上標註特定裝飾器，以搭配 asyncio 程式庫。
* ### Python 如何 "切換" 協程的執行 (如何取的傳回值)
    * ### 協程的 "返回" 其實是引發 "StopIteration" 例外。
    ```
    async def f():
        return 123

    coro = f()

    try:
        # 傳送 None 來起始協程，事件迴圈內不就是以這種方式處理，
        # 我們不用親自做這件事，
        # 可以使用 loop.create_task(coro) 或 await coro 來執行協程，
        # 迴圈的底層會執行 .send(None)。
        coro.send(None)
    except StopIteration as e:
        # 協程返回時，會引發 "StopIteration" 例外，
        # 可以透過例外的 value 屬性取得協程的傳回值，
        # 這也是底層的細節，在我們的觀點下，
        # async def 函式與普通函式相同，
        # 是透過 return 陳述來傳回值。
        print('The answer was:', e.value)
        # The answer was: 123
    ```
    * ### send() 和 StopIteration 個字定義了協程的起點與終點，且是由 "事件迴圈" 負責這些低階的內部操作，我們只需要排定迴圈要執行的協程即可。
* ### 新的 await 關鍵字
    * ### 新的關鍵字 await (僅) 接受一個參數，也就是 awaitable 物件。
    * ### 可以用以下其中一種方式定義:
        * ### 協程 (也就是 async def 函式的呼叫結果)。
        * ### 實作 \_\_await\_\_() 方法的物件，該方法必需傳回迭代器 (這是遠古世紀的用法)。
    ```
    import asyncio


    async def f():
        await asyncio.sleep(1.0)
        return 123


    async def main():
        # 呼叫 f() 會產生協程，這意味著必需 await，
        # 當 f() 完成時，result 為 123。
        result = await f()
        return result

    asyncio.run(main())
    ```
* ### 如何提供例外給協程 (通常用於取消協程)
    * ### 在呼叫 task.cancel() 時，事件迴圈內部會使用 coro.throw() 在協程 "內部" 引發 asyncio.CancelledError。
    ```
    import asyncio


    async def f():
        await asyncio.sleep(0)


    # 透過協程函式 f() 建立新協程
    coro = f()
    coro.send(None)

    # 透過 coro.throw() 並提供例外類別與值，
    # 在協程內部的 await 處引發例外。
    coro.throw(Exception, 'blah')
    ```
* ### throw() 會用來 "取消任務 (在 asyncio 內部)"
    ```
    import asyncio


    async def f():
        try:
            while True:
                await asyncio.sleep(0)
        # 這個協程函式可以處理例外，處理對象為 asyncio 程式庫中，
        # 專門用於 "取消任務" 的例外類型 asyncio.CancelledError，
        # 注意，例外是由外部注入協程，也就是被事件迴圈注入，
        # 實際上，任務被取消時，任務包裹的協程內部就是發生 CancelledError。
        except asyncio.CancelledError:
            # 報告協程被取消了，
            print('I was cancelled!')
        else:
            return 111


    coro = f()

    # 模擬協程啟動
    coro.send(None)
    coro.send(None)

    # 模擬任務取消
    coro.throw(asyncio.CancelledError)

    # 正常離開協程 (asyncio.CancelledError 是專門用於 "取消任務" 的例外類型)
    # I was cancelled!
    ```
    * ### 任務的取消，就是基本的例外引發 (與處理)。
    * ### 假設在處理 CancelledError 時又進行另一個協程 (沒事別這樣幹，基本上也不會碰到底層就是了)
        ```
        import asyncio


        async def f():
            try:
                while True:
                    await asyncio.sleep(0)
            except asyncio.CancelledError:
                print('Nope!')
                while True:
                    # 在處理 CancelledError 時又等待另一個 awaitable 物件
                    await asyncio.sleep(0)
            else:
                return 111


        coro = f()
        coro.send(None)

        # 不意外的，協程會持續好好的活著，跟我不一樣...
        coro.throw(asyncio.CancelledError)
        # Nope!

        coro.send(None)
        ```
        * ### 反正如果需要撰寫底層代碼，別這麼做，當收到取消信號時，唯一的工作就是: 清理必要的資料，然後結束它的人生，我的也順便，而非忽略。
    * ### 到此為止都在扮演事件迴圈，親自處理底層 .send(None) 呼叫細節，使用 asyncio 的程式碼長這樣。
        ```
        import asyncio


        async def f():
            await asyncio.sleep(0)
            return 111


        # 取的迴圈
        loop = asyncio.get_event_loop()
        coro = f()

        # 執行協程直到完成，交由底層自行處理 .send(None) 等細節，
        # 並捕捉 StopIteration 例外完成協程，
        # 同時取得傳回值。
        loop.run_until_complete(coro)
        ```
* ### 事件迴圈
    * ### 事件迴圈會自行處理行程切換、StopIteration 捕捉等等的相關事件。
    * ### 「不直接處理事件迴圈，是可行的，開發上應該也要這麼做」，所以跳過這節吧 ?
    * ### 在開發任務上，應該盡可能使用 asyncio.run(coro) 起步走，並透過 await 來呼叫 asyncio 撰寫程式碼。
    * ### 但有時候還是必需以某種程度的方式與事件迴圈本身互動 (還可以卷別人)。
* ### 取得事件迴圈的方式
    * ### 建議: 在協程環境內呼叫 ```asyncio.get_running_loop()```。
    * ### ~~不建議: 在任何位置呼叫 ```asyncio.get_event_loop()```。~~
    * ### 建議的方式在 Python 3.7 才導入，所以還是理解一下不建議的比較好，因為可能在程式中看到它。
    ```
    import asyncio


    loop = asyncio.get_event_loop()
    loop2 = asyncio.get_event_loop()

    # 參考同一實例
    print(loop is loop2)
    # True
    ```
    * ### 如果要在協程函式內部取得迴圈實例，只要呼叫 get_running_loop() 或 get_event_loop()，不需要在函式間以 loop 為參數傳遞。
* ### 對於框架設計者來說，在函式上設計 loop 參數是比較好的選擇，防止使用者拿到相同的迴圈幹了些壞壞的事。
* ### "get_running_loop()" vs. "get_event_loop()"
    * ### get_event_loop() 只能在同一執行緒上作用，在新執行緒中單純呼叫 get_event_loop() 會失敗，除非特別透過 new_event_loop() 建立新迴圈，並且呼叫 set_event_loop() 設定為該執行緒的專用迴圈。
    * ### get_running_loop() 無論如何將會如期運作 (所以這是被 "建議" 的迴圈取得方式): 只要在某協程環境、任務，或者被這兩者呼叫的函式中，呼叫 get_running_loop()，它一定是提供目前運作中的事件迴圈。
    * ### get_running_loop() 有效的簡化背景任務的衍生。
* ### 在協程函式中建立一些任務且不等待任務完成
    ```
    import asyncio


    async def f():
        loop = asyncio.get_event_loop()
        for i in range():
            loop.create_task('<some other coro>')
    ```
    * ### 在協程中建立新任務，因為不會等待，可以確保任務不依賴協程函式 f() 的執行環境，在建立的任務完成前，f() 就會先行結束。
* ### Python 3.7 之前，必需取得 loop 實例才能排定 Task，導入 get_running_loop() 後，有些 asyncio 函式也會用到它，像是 asyncio.create_task()。
* ### Python 3.7 開始可以透過以下方式衍生非同步 Task
    ```
    import asyncio


    async def f():
        for i in range():
            asyncio.create_task('<some other coro>')
    ```
    * ### 還有一個低階函式 asyncio.ensure_future()，也能以和 create_task() 同樣的方式來衍生任務 (可能在遠古世紀的程式碼中看到它的身影)。
* ### Task 與 Future
    * ### 「最常使用的會是 Task，大部分情況下會使用 creat_task() 函式來運行協程」。
    * ### Future 是 Task 的父類別，提供了與迴圈互動的所有功能。
    * ### 差異
        * ### Future: 迴圈會管理 Future，它代表某活動在未來的完成狀態。
        * ### Task: 與上同理，只不過那個特定 "活動" 會是協程，例如使用 async def 函式與 create_task() 建立 Task。
    * ### 在 Future 實例建立時，開關是設定在 "未完成"，在一段時間後會是 "已完成"，可以透過 Future 的 done() 方法檢查其狀態。
        ```
        from asyncio import Future
        f = Future()
        print(f.done())
        # False
        ```
* ### Future 也可以進行以下的操作
    * ### 可以有 "結果" (使用 .set_result(value) 來設定，.result() 來取得)。
    * ### 可以用 .cancel() 來取消 (用 .cancelled() 檢查是否取消)。
    * ### 可設定回呼函式，在 Future 完成時會執行。
* ### 「最常使用的會是 Task」，然而 Future 無可避免地也會用到，例如在執行器中運行函式時，就會回傳 Future 實例，而非 Task。
    ```
    import asyncio


    # 建立簡單的 main 函式，稍後執行。
    async def main(f: asyncio.Future):
        await asyncio.sleep(1)

        # 在 Future 實例 f 設定結果。
        f.set_result('I have finished.')


    loop = asyncio.get_event_loop()

    # 手動建立 Future 實例，
    # 這個實例預設會與 loop 綁定，
    # 但沒有也不會繫結任何協程 (Task 才會這麼做)。
    fut = asyncio.Future()

    # 確認 Future 進行操作前的狀態。
    print(fut.done())
    # False

    # 排定 main() 協程，傳入 Future 實例，
    # main() 會睡個覺後設定 Future 實例，
    # 此時 main() 協程尚未開始運作，
    # 要等待迴圈運行後，協程才會開始執行。
    loop.create_task(main(fut))

    # 透過 run_until_complete 運行 Future 實例，
    # 協程開始執行。
    loop.run_until_complete(fut)

    # 確認 Future 當前狀態。
    print(fut.done())
    # True

    # 存取結果。
    print(fut.result())
    # I have finished.
    ```
    * ### 「注意，基本上不太會使用上述的示例代碼，並直接與 Future 互動」，只需理解即可，開發時幾乎是透過 Task 與 asyncio 互動。
    * ### 如果在 Task 實例上呼叫 set_result() 會發生什麼事 ? Python 3.8 之前可以這麼做，但現在不可以勒。
    * ### Task 實例是用來包裹協程物件，只有底層協程函式的內部才能設定結果。
        ```
        import asyncio

        from contextlib import suppress


        async def main(f: asyncio.Future):
            await asyncio.sleep(1)
            try:
                # 試著呼叫 set_result()，
                # 這時會引發 RuntimeError。
                f.set_result('I have finished.')
            except RuntimeError as e:
                print(f'No longer allowed: {e}')
                f.cancel()


        loop = asyncio.get_event_loop()

        # 建立 Task 實例 (用 sleep 產生一個協程，便於展示)
        fut = asyncio.Task(asyncio.sleep(1_000_000))

        print(fut.done())
        # False

        # No longer allowed: Task does not support set_result operation

        loop.create_task(main(fut))

        # 使用 with suppress() 來捕獲異常，
        # 當異常發生時程式碼不會中斷，
        # 而是忽略這個異常繼續執行下去。
        with suppress(asyncio.CancelledError):
            loop.run_until_complete(fut)

        print(fut.done())
        # True

        # 透過 cancelled() 取消任務，
        # 這會在底層的協程中引發 CancelledError。
        print(fut.cancelled())
        # True
        ```
* ### 建立 Task ? 確保 Future ? 從中選擇 !
    * ### 可以使用 asyncio.creat_task() 執行協程，在導入 asyncio.create_task() 前如果想做相同的事，必需先取得 loop 實例後使用 loop.create_task()。
    * ### 也可以使用模組層次的函式來達到相同目的: asyncio.ensure_future()。
    * ### 關於 ensure_future() 的說明
        * ### 如果 "傳入協程"，會傳回 Task 實例 (而協程會排定給事件迴圈)，就像呼叫 asyncio.create_task() 或 loop.create_task()，會傳回新的 Task 實例。
        * ### 如果 "傳入 Future (或者 Task 實例，因為 Task 是 Future 的子類別)"，會傳回同一實例，不做任何修改。
    ```
    import asyncio


    # 簡單協程函式
    async def f():
        pass


    # 建立協程物件
    coro = f()

    # 取的事件迴圈
    loop = asyncio.get_event_loop()

    # 將協程排定給迴圈，並取得新的 Task 實例。
    task = loop.create_task(coro)

    # 驗證型態
    assert isinstance(task, asyncio.Task)

    # 示範 ensure_future() 可以完成與 create_task() 相同動作，
    # 傳入協程並取得 Task 實例 (協程排定由迴圈執行)，
    # 如果傳入協程 coro，則結果與 create_task() 相同。
    new_task = asyncio.ensure_future(coro)

    # 驗證型態
    assert isinstance(new_task, asyncio.Task)

    # 將 Task 傳給 ensure_future()
    mystery_meat = asyncio.ensure_future(task)

    # 傳入與取回的物件，是同一個 Task 實例
    assert mystery_meat is task
    ```
    * ### 直接傳入 Future 實例 (包含 Task，它是它的子類別對吧 !)
        * ### 框架開發者可以使用 ensure_future() 設計較具彈性的 API。
        * ### 這樣彈性的 API 便於提供給直接使用的開發者。
    * ### ensure_future() 的用處是，如果有一個物件可能是協程或 Future 實例 (包含 Task，它是它的子類別對吧 !)，接下來想呼叫 Future 定義的某方法 (通常會是 cancel())，若物件是 Future 實例 (包含 Task，它是它的子類別對吧 !)，什麼都不用做，若是協程，就用 Task 包裹。
    * ### 如果是協程，想要排定執行的話，正確的 API 是 create_task()，呼叫 ensure_future() 的唯一時機是，想提供某個可接受協程或 Future 實例 (包含 Task，它是它的子類別對吧 !) 的 API (就像 asyncio 本身許多 API)，而打算做的事必須有個 Future。
* ### 簡單來說，asyncio.ensure_future() 是設計框架的輔助函式，用常見的函式舉例:
    ```
    from typing import Any, List


    def listify(x: Any) -> List:
        if isinstance(x, (str, bytes)):
            return [x]
        try:
            return [_ for _ in x]
        except TypeError:
            return [x]
    ```
    * ### 無論指定的引數為何，函式都會嘗試將其轉為 list。
    * ### asyncio.ensure_future() 與此概念相同，函數會嘗試把引數轉會為 Future (或子類別) 型態。
    * ### 同常這類輔助函式較傾向予框架開發者使用。
    * ### 事實上 asyncio 標準程式庫模組，也基於上述理由運用了 ensure_future()，只要 API 文件中，函式的參數接受 "awaitable 物件"，內部可能就使用了 ensure_future() 來轉換參數。
    ```
    asyncio.gather(*aws, loop=None, ...)
    ```
    * ### aws 就代表 "awaitable 物件"，包含協程、Task 與 Future。
    * ### gather() 在內部使用了 ensure_future() 轉換型態: Task 與 Future 維持不變，而會為協程建立 Task。
    * ### 在應用開發任務上，若需要在事件迴圈中排定協程，應直接使用 asyncio.create_task() 而非 asyncio.ensure_future()。
* ### 非同步情境管理器: async with
    * ### 在協程支援上，情境管理器意外的方便，對於網路資源 (如: 連線)，許多情況都需要正確的定義開啟或是關閉的時機。
    * ### 理解 async with 的關鍵在於，情境管理器是由 "方法呼叫" 驅動，下為運作方式示例。
    ```
    class Connection:
        def __init__(self, host, port):
            self.host = host
            self.port = port

        # 相較於同步管理器使用 __enter__() 方法，
        # 這邊使用 __aenter__() 方法，
        # 且此方法必須是 async def 方法。
        async def __aenter__(self):
            self.conn = await get_conn(self.host, self.port)
            return self.conn

        # 相對於 __exit__()，這邊使用 __aexit__()，
        # 參數列和 __exit__() 是相同的，
        # 情境管理器的本體中若發生例外，
        # 會傳入對應引數。
        async def __aexit__(self, exc_type, exc, tb):
            await self.conn.close()
    ```
    * ### 使用 asyncio 的程式不代表其情境管理器一定要採取非同步，「如果在 "進入" 與 "離開" 方法時，需要 await 某東西，才需要非同步情境管理器」。
    * ### 此書的作者偷偷告訴我，他不太喜歡這種定義情境管理器的方式，因為 contextlib 中就有好用的 ```@contextmanager``` 裝飾器，固然也有了非同步版本的 ```@asynccontextmanager```。
* ### contextlib 的作法
    * ### ```@asynccontextmanager``` 的使用方式與 contextlib 標準程式庫中的 ```@contextmanager``` 類似。
    # ### 阻斷式的做法
        ```
        from contextlib import contextmanager

        # 將產生器函式傳入情境管理器
        @contextmanager
        def web_page(url):
            # -------- Enter Scope ---------

            # download_webpage() 是一個虛構的函式，
            # 表示從 URL 上取得資料，
            # 會是一個阻斷式的呼叫。
            data = download_webpage(url)

            # ------------------------------

            yield data

            # --------- Exit Scope ---------

            # 這也是一個虛構的函式，
            # 表示從 URL 取得資料後要進行的動作，
            # 也會是一個阻斷式呼叫。
            update_stats(url)


        # 使用情境管理器，
        # 此情境管理器隱藏網路呼叫 download_webpage() 等細節。
        with web_page('google.com') as data:
            # 此處也可能是阻斷的，取決於函式內容，
            # 函式功能可能是:
            # 1. 快到不阻斷 (快速的計算密集)
            # 2. 稍微阻斷 (快速的 I/O 密集，可能是磁碟存取，而非網路存取)
            # 3. 阻斷 (緩慢的  I/O 密集)
            # 4. 慢到靠北 (就慢到靠北，不然想怎樣)
            process(data)
        ```
    * ### 導入 Python 3.7 非同步感知特性
        ```
        from contextlib import asynccontextmanager

        # 使用方式與 @contextmanager 相同，
        # 除了被裝飾的函式需宣告為 async def，
        # 好啦使用方式有點不同。
        @asynccontextmanager
        async def web_page(url):
            # 假設 download_webpage() 可以被修改成 "異步" 的，
            # 此時就需要加上 await 關鍵字，
            # 讓事件迴圈可以執行任務切換，
            # 進行其餘任務的執行。
            data = await download_webpage(url)

            # 理論上此處應包含 try / finally 處理 (示例嘛... 偷個懶 !)，
            # yield 會使函式變成 "產生器函式"，
            # 而 async def 關鍵字，
            # 進一步使其成為 "非同步產生器函式"，
            # 當函式被呼叫時，會回傳 "非同步產生器"，
            # 可以透過 inspect 模組中的函式進行校驗，
            # 分別為 isasyncgenfunction() 與 isasyncgen()。
            yield data

            # 假設 update_stats() 已經修改為可產生協程，
            # 需加上 await 關鍵字。
            await update_stats(url)


        # 使用非同步情境管理器時，
        # 要使用 async with。
        async with web_page('google.com') as data:
            process(data)
        ```
        * ### 將阻斷函式修改為協程函式，並不是一件容易的事，這要從底層開始修改，從底層開始就要支援異步，但往往接手的專案並非如此。
        * ### 在接手現有專案或使用第三方程式庫時，常常會發現底層沒辦法更動 (可能是能力不足，或是跟我一樣懶)，這時候就要使用偉大的 "執行器" 了。
        * ### 這也就是所謂的，如果既有的程式可以運作，不一定要堅持導入 Async。
    * ### 非阻斷式做法
        * ### 當無法變更 download_webpage() 與 update_stats() 從阻斷式為異步時，就需要導入 "執行器"。
        ```
        import asyncio
        from contextlib import asynccontextmanager


        @asynccontextmanager
        async def web_page(url):
            loop = asyncio.get_event_loop()

            # 使用預設執行器，需傳入 None 為 excutor 的引數
            data = await loop.run_in_executor(None, download_webpage, url)

            yield data

            # 記得要 await 呦 (上面也是)，
            # 否則不會等待呼叫完成，
            # 而是直接繼續下一步。
            await loop.run_in_executor(None, update_stats, url)


        async with web_page('google.com') as data:
            process(data)
        ```
* ### 非同步迭代器: async for
    * ### 傳統的同步迭代器
        ```
        class A:
            # 迭代器需實作 __iter__() 方法
            def __iter__(self):
                # 初始為 "開始" 狀態
                self.x = 0
                # __iter__() 方法必須回傳 iterable 物件，
                # 也就是實作 __next__() 方法，
                # 在此為同一個實例，
                # 因為 A 本身就實作了 __next__() 方法。
                return self

            # 在迭代期間 __next__() 方法會被持續呼叫
            def __next__(self):
                if self.x > 2:
                    # 發生 StopIteration 時就會停止
                    raise StopIteration
                else:
                    # 每次迭代需生成回傳值
                    self.x += 1
                
                return self.x


        for i in A():
            print(i)

        '''
        1
        2
        3
        '''
        ```
        * ### 如果 \_\_next\_\_() 是個 async def 協程函式，就可以 await 某種 I/O 密集操作。
    * ### 非同步迭代器需要具備以下條件:
        * ### 實作 def \_\_aiter\_\_()，不是 async def 呦 !
        * ### \_\_aiter\_\_() 傳回物件，必需實作 async def \_\_anext\_\_()。
        * ### \_\_anext\_\_() 必須回傳每次的迭代值，而完成時要引發 StopAsyncIteration。
    * ### 讀取 Redis 資料的非同步迭代器
        ```
        import asyncio

        from aioredis import create_redis


        async def main():
            # 使用 aioredis 中的高階介面取得連線
            redis = await create_redis(('localhost', 6379))

            # 假設以下的 key 在 redis 中對應的 value 很大
            keys = ['Americas', 'Africa', 'Europe', 'Asia']

            # async for 可以在等待下一個資料來到前暫停迭代本身
            async for value in OneAtATime(redis, keys):
                # 模擬取得值後所進行的 I/O 密集活動或是其它操作
                await do_something_with(value)


        class OneAtATime:
            # 初始化，取得 redis 連線實例與需迭代鍵陣列
            def __init__(self, redis, keys):
                self.redis = redis
                self.keys = keys

            # 不同於上一個範例使用 __iter__()，
            # 此處為 __aiter__()。
            def __aiter__(self):
                # 建立普通迭代器
                self.ikeys = iter(self.keys)
                # 回傳實作 __anext__() 的自己
                return self

            # 此處以宣告為 async def 的 __anext__() 方法，
            # 取代上一個範例用 def 宣告的 __next__() 方法。
            async def __anext__(self):
                try:
                    # 迭代取得 key
                    k = next(self.ikeys)
                except StopIteration:
                    # 當發生 StopIteration 時，
                    # 將其轉換為 StopAsyncIteration，
                    # 此為非同步迭代器內部用來停止的信號。
                    raise StopAsyncIteration
                
                # 取得該鍵在 redis 對應的值 (需 await 讓事件迴圈進行切換)
                value = await self.redis.get(k)
                return value


        asyncio.run(main())
        ```
* ### 更簡單的非同步產生器函式
    * ### 協程與產生器是完全不同的概念。
    * ### 非同步產生器在行為上，與一般的產生器更為接近。
    * ### 對迭代器來說，async for 會搭配非同步產生器，而 for 會搭配一般的產生器。
    * ### 使用非同步產生器函式定義前 redis 示例
        ```
        import asyncio

        from aioredis import create_redis


        async def main():
            redis = await create_redis(('localhost', 6379))
            keys = ['Americas', 'Africa', 'Europe', 'Asia']
            
            async for value in one_at_a_time(redis, keys):
                await do_something_with(value)


        # 透過 async def 宣告使其成為協程函式，
        # 而因當中包含 yield 關鍵字，
        # 所以稱為非同步產生器函式。
        async def one_at_a_time(redis, keys):
            for k in keys:
                value = await redis.get(k)
                yield value


        asyncio.run(main())
        ```
* ### 非同步包含式
    * ### 非同步的 list、dict 與 set 包含式
        ```
        import asyncio


        # 簡單的非同步產生器函式，
        # 可以指定上限使其迭代生成 tuple 回傳。
        async def doubler(n):
            for i in range(n):
                yield i, i * 2
                # 睡一下，畢竟這是非同步函式
                await asyncio.sleep(0.1)


        async def main():
            # 非同步的 list 包含式 (使用 async for)
            result = [x async for x in doubler(3)]
            print(result)

            # 非同步的 dict 包含式
            result = {x: y async for x, y in doubler(3)}
            print(result)

            # 非同步的 set 包含式
            result = {x async for x in doubler(3)}
            print(result)


        asyncio.run(main())

        '''
        [(0, 0), (1, 2), (2, 4)]
        {0: 0, 1: 2, 2: 4}
        {(2, 4), (1, 2), (0, 0)}
        '''
        ```
    * ### 也可以在包含式中使用 await。
    * ### 使 "包含式" 成為 "非同步包含式 (async comprehension)" 是透過 async for 而非 await。
    * ### 要讓 await 在包含式中合法，只要在協程函式本體中使用它即可，也就是 async def 宣告函式。
    * ### 在同一個 list 包含式中使用 await 與 async for，不過就是結合兩個獨立的概念。
    * ### 綜合應用
        ```
        import asyncio


        ＃ 簡單會睡覺協程函式
        async def f(x):
            await asyncio.sleep(0.1)
            return x + 100


        # 非同步產生器函式，
        # 稍後會在非同步 list 包含式中呼叫，
        # 透過 async for 來驅動迭代。
        async def factory(n):
            for x in range(n):
                await asyncio.sleep(0.1)

                # 非同步包含式執行時，會將 f 與迭代值 x 組成 tuple 後 yield，
                # 被傳回的 f 是協程函式，而非協程。
                yield f, x


        async def main():
            # 非同步包含式，同時含有 async for 與 await，
            # factory() 會傳回非同步函式器，迭代中會驅動它，
            # 因為是非同步產生器，不能只是用 for，
            # 需使用 async for，
            # 而呼叫回傳 tuple 中的 f() 會建立協程，
            # 所以必需它配 await 使用。
            results = [await f(x) async for f, x in factory(3)]

            print('results = ', results)


        asyncio.run(main())

        # results =  [100, 101, 102]
        ```
        * ### 上述示例表明，await 的使用與 async for 的使用互不相干。
* ### 適當地啟動與關機
    * ### 非同步的程式多半會是長時間運行、基於網路的應用程式，而在正確地啟動與關機這方面，真他媽有夠複雜。
    * ### 相較之下，啟動較為簡單。asyncio 應用程式的標準啟動方式是，定義一個 main() 協程函式，使用 asyncio.run() 來呼叫。
    * ### 關機就複雜多了，在 async def main() 結束後，會採取以下動作:
        * ### 收集未定 (pending) 狀態的任務物件 (如果 U 的話)。
        * ### 取消這些任務 (在各個運作中的協程內部引發 CancelledError，可以在協程函式本體中，決定是否使用 try / except 處理)
        * ### 將這些任務收集到 group 任務群集。
        * ### 使用 run_util_complete() 運行 group 群集，等待它們結束，也就是等到 CancelledError 引發，然後處理掉。
    * ### asyncio.run() 會處理這些步驟，但當自行建立第一個複雜的 asyncio 應用程式時，若能遵照一些慣例，在關機時或許能避免「Task was destroyed but it is pending (消毀了未定狀態的任務) !」之類的錯誤訊息。
    * ### 未定任務終結者
        ```
        import asyncio


        async def f(delay):
            await asyncio.sleep(delay)
            
            
        loop = asyncio.get_event_loop()

        # 睡一秒
        t1 = loop.create_task(f(1))
        # 睡兩秒
        t2 = loop.create_task(f(2))

        # 只會把任務 1 完成
        loop.run_until_complete(t1)

        loop.close()

        # Task was destroyed but it is pending!
        ```
        * ### 此錯誤訊息表示，迴圈關閉時仍存在未完成任務，而應避免這類錯誤訊息的發生，這也是為什麼關機程序在慣例上，要收集結束的任務、將它們取消，在它們結束後才關閉迴圈。
        * ### asyncio.run() 會完成這些動作。
        * ### 但理解處理的細節，可以讓我們具備處理更複雜的情況。
    * ### 非同步應用程式稱命週期
        ```
        import asyncio

        from asyncio import StreamReader, StreamWriter


        # 伺服器使用 echo() 協程函式，為每個連線建立協程，
        # 此函式使用 asymcio 的串流 API 進行網路處理。
        async def echo(reader: StreamReader, writer: StreamWriter):
            print('New connection.')

            try:
                # 使用無窮迴圈等待訊息以保持連線
                while data := await reader.readline():
                    # 將資料轉大寫後傳回給發送者
                    writer.write(data.upper())
                    await writer.drain()
                
                print('Leaving Connection.')
            # 如果任務被取消會顯示指定訊息
            except asyncio.CancelledError:
                print('Connection dropped!')


        async def main(host='127.0.0.1', port=8888):
            # 啟動 TCP 伺服器
            server = await asyncio.start_server(echo, host, port)
            async with server:
                await server.serve_forever()
        
        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print('Bye!')
        ```
        ```
        # 啟動伺服器
        # 有人連線
        New connection.
        # 有人斷線
        Leaving Connection.
        # 有人連線
        New connection.
        # 關閉伺服器
        Connection dropped!
        Bye!
        ```
        ```
        # 等待可以適當的恢復寫入到流。
        
        writer.write(data.upper())
        await writer.drain()

        # 與底層 I/O 寫緩衝區進行交互的流程控制方法。
        # 當緩衝區大小達高水位，drain() 會阻塞，
        # 直到恢復至低水位以恢復寫入。
        ```
        * ### 將上述示例想像成真實世界上已上線的應用程式，需將這些拋棄連線的事件，傳送給某個監控服務。
    * ### 在處理 CancelledError 時建立任務
        ```
        import asyncio

        from asyncio import StreamReader, StreamWriter


        async def send_event(msg: str):
            await asyncio.sleep(1)


        async def echo(reader: StreamReader, writer: StreamWriter):
            print('New connection.')

            try:
                while data := await reader.readline():
                    writer.write(data.upper())
                    await writer.drain()

                print('Leaving Connection.')
            except asyncio.CancelledError:
                msg = 'Connection dropped!'

                print(msg)

                asyncio.create_task(send_event(msg))


        async def main(host='127.0.0.1', port=8888):
            server = await asyncio.start_server(echo, host, port)
            async with server:
                await server.serve_forever()

        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print('Bye!')
        ```
        * ### 此示例假設會將事件發送給外部服務器。
        * ### 因為事件通知會涉及網路存取，為其建立獨立的非同步任務是常見的做法，使用 create_task() 函式達成多事務同時處理支持。
        * ### 然而這個示例有個臭蟲，當還有連線存在時停止了伺服器，會出現 "Task was destroyed but it is pending!" 錯誤訊息。
        * ### 這是因為，當前有效狀態中的任務會被收集而取消，此時 await 的也只有這些任務，之後 asyncio.run() 立即返回，而此示例在處理 CancelledError 時又建立了新任務。
        * ### 在處理 CancelledError 例外時的大方向原則為，避免嘗試建立新任務，如果一定要這麼做，必須在同一函式範疇中 await 新建的 Task 或 Future。
* ### gather() 的 return_exceptions=True 是什麼 ?
    * ### 函式簽署的預設是 gather(..., return exceptions=False)，而這個預設在多數情況 (包括關機處理) 是有問題的，因而 asyncio.run() 內部使用 gather() 時，指定了 return_exceptions=True。
    * ### 觀察
        * ### run_until_complete() 會執行指定的 Future，在關機期間，它執行的對象就是 gather() 傳回的 Future。
        * ### 如果該 Future 發生例外，run_until_complete() 也會發生例外，這代表迴圈會停止。
        * ### 如果 run_until_complete() 運行一個 Future 群組，任一子任務中發生例外，而該子任務沒有處理的話，例外也會在該 Future 群組引發 (此處例外也包含了 CancelledError)。
        * ### 如果某些任務處理了 CancelledError，而其它任務沒有，迴圈不會因此停止，也就是全部任務做完前，迴圈不會停下來。
        * ### 就關機而言，這是不合理的，無論某些任務是否引發例外，都希望群組中全部任務結束後，才結束 run_until_complete()。
        * ### 因此，我們需 設定 gather(..., return exceptions=False)，使 Future 群組把來自子任務的例外是為傳回值，也就不會往外傳播而干擾 run_until_complete()。
    * ### 重點就在於: return exceptions=False 與 run_until_complete() 間的關係，以此方式捕捉例外，會有不是很好的結果，可能忽略了一些例外，因為現在任務群組把例外處理掉了，如果擔心這個問題，可以從 run_until_complete() 取的輸出清單，掃描是否有 Exception 的子類型。
        ```
        import asyncio


        async def f(delay):
            # 如果輸入 0 就糟糕惹
            await asyncio.sleep(1 / delay)
            return delay


        loop = asyncio.get_event_loop()

        for i in range(10):
            loop.create_task(f(i))

        pending = asyncio.all_tasks(loop=loop)
        group = asyncio.gather(*pending, return_exceptions=True)
        results = loop.run_until_complete(group)

        print(f'Results: {results}')

        loop.close()

        # Results: [7, 3, 4, 1, 5, 8, ZeroDivisionError('division by zero'), 6, 2, 9]
        ```
        * ### 如果沒有設定 return_exceptions=True 的話，run_until_complete() 中的 ZeroDivisionError 會拋出並中斷迴圈，妨礙其他任務的完成。
* ### 信號
    * ### 先前的範例使用 KeyboardInterrupt 示範中斷迴圈的方式 (Ctrl - C)，在 asyncio.run() 內部，拋出 KeyboardInterrupt 相當於解除了 loop.run_until_complete() 的阻斷，讓後續的關機程序得以執行。
    * ### KeyboardInterrupt 對應的是 SIGINT 信號，在網路服務中，處理中斷時更常用的信號其實是 SIGTERM。
    * ### asyncio 內建了信號處理方面的支援，其複雜到靠北靠北 (double 靠北)。
    * ### 先看看下一個示例的輸出
        ```
        <Your app is running>
        <Your app is running>
        Got signal: SIGINT, shutting down.
        ```
        * ### 最後一行表示了按下 Ctrl - C 終止程式，來看看 SIGINT 與 SIGTERM 在處理上的陷阱。
        ```
        import asyncio


        async def main():
            while True:
                print('<Your app is running>')
                await asyncio.sleep(1)


        if __name__ == '__main__':
            loop = asyncio.get_event_loop()
            task = loop.create_task(main())

            try:
                loop.run_until_complete(task)
            # 此案例只有 Ctrl - C 會中斷迴圈
            except KeyboardInterrupt:
                print('Got signal: SIGINT, shutting down.')

            tasks = asyncio.all_tasks(loop=loop)

            for t in tasks:
                t.cancel()

            group = asyncio.gather(*tasks, return_exceptions=True)

            loop.run_until_complete(group)

            loop.close()
        ```
    * ### 假設
        * ### 有同事要求除了 SIGINT 也要把 SIGTERM 作為關機信號來處理。
        * ### 實際應用程式中，必需在 main() 協程中進行清理，必需處理 CancelledError，而捕捉例外後的處理會耗費數秒才能結束。
        * ### 如果收到數次信號，在接收到第一個關機信號後、結束應用程式前，必需忽略任何新信號。
    * ### 可處理 SIGINT 與 SIGTERM 且只會停止迴圈一次
        ```
        import asyncio

        # 匯入標準程式庫
        from signal import SIGINT, SIGTERM


        async def main():
            try:
                while True:
                    print('<Your app is running>')
                    await asyncio.sleep(1)
            # 收到取消信號後，持續執行三秒的顯示
            except asyncio.CancelledError:
                for i in range(3):
                    print('<Your app is shutting down...>')
                    await asyncio.sleep(1)


        # 收到信號時的迴呼處理器
        def handler(sig):
            # 停止迴圈，此行會解除 loop.run_forever() 的阻斷，
            # 以執行後續未定任務的收集與取消，
            # 以及 run_until_complete() 等關機程序。
            loop.stop()
            
            print(f'Got signal: {sig!s}, shutting down.')
            
            # 為了在處於關機程序時，不被其他信號干擾，
            # 將 SIGTERM 信號處理器從迴圈中移除。
            # 主要是因為處理器會在 run_until_complete() 階段再次呼叫 loop.stop()，
            # 這會干擾關機處理。
            loop.remove_signal_handler(SIGTERM)
            # 如果只是單純移除 SIGINT，
            # KeyboardInterrupt 會變成 SIGINT 的處理器，
            # 取而代之的，設定一個空 lambda 函式作為處理器，
            # 如此就不會引發 KeyboardInterrupt，
            # 同時 SIGINT 也失去作用。
            loop.add_signal_handler(SIGINT, lambda: None)


        if __name__ == '__main__':
            loop = asyncio.get_event_loop()
            
            # 將信號處理器綁定給迴圈，
            # 如果在此不變更處理器，
            # Python 預設的 SIGINT 處理器會引發 KeyboardInterrupt。
            for sig in (SIGTERM, SIGINT):
                loop.add_signal_handler(sig, handler, sig)
                
            loop.create_task(main())
            
            # run_forever() 阻斷執行，
            # 直到某個東西停止迴圈，
            # 此示例中 SIGINT 或 SIGTERM 送至行程，
            # handler() 中會停止迴圈。
            loop.run_forever()
            
            tasks = asyncio.all_tasks(loop=loop)
            
            for t in tasks:
                t.cancel()
                
            group = asyncio.gather(*tasks, return_exceptions=True)
            
            loop.run_until_complete(group)
            
            loop.close()

        
        '''
        <Your app is running>
        <Your app is running>
        Got signal: Signals.SIGINT, shutting down.
        <Your app is shutting down...>
        <Your app is shutting down...>
        '''
        ```
        * ### 此時即便在關機處理期間，按下 Ctrl - C，當 main() 協程最後完成前，什麼事都不會發生。
    * ### 上述示例，致力於控制事件迴圈的生命週期，而「在應用開發實務上，應該使用方便的 asyncio.run()」。
        ```
        import asyncio

        from signal import SIGINT, SIGTERM


        async def main():
            loop = asyncio.get_running_loop()

            for sig in (SIGTERM, SIGINT):
                # 在 main 中改變信號處理行為
                loop.add_signal_handler(sig, handler, sig)

            try:
                while True:
                    print('<Your app is running>')
                    await asyncio.sleep(1)
            except asyncio.CancelledError:
                for i in range(3):
                    print('<Your app is shutting down...>')
                    await asyncio.sleep(1)


        def handler(sig):
            loop = asyncio.get_running_loop()

            # 不能像之前的範例一樣停止迴圈，
            # 因為在 main() 任務完成前就停止迴圈會收到警訊，
            # 相對地只能取消任務，
            # 讓 main() 的任務結束，
            # 之後 asyncio.run() 內部就會進行清理。
            for task in asyncio.all_tasks(loop=loop):
                task.cancel()

            print(f'Got signal: {sig!s}, shutting down.')
            
            loop.remove_signal_handler(SIGTERM)
            loop.add_signal_handler(SIGINT, lambda: None)


        if __name__ == '__main__':
            asyncio.run(main())


        '''
        <Your app is running>
        <Your app is running>
        Got signal: Signals.SIGINT, shutting down.
        <Your app is shutting down...>
        <Your app is shutting down...>
        '''
        ```
* ### 關機期間等待執行器
    * ### 在很前面的範例提到，把阻斷式 time.sleep() 的呼叫時間，設定的比 asyncio.sleep() 呼叫短，是為了讓範例比較簡單，因為執行器工作會比 main() 協程更快完成，程式就能正確關機。
    * ### 如果不這麼做呢 ?
    * ### 執行器花更多時間才結束
        ```
        import time
        import asyncio


        async def main():
            loop = asyncio.get_running_loop()
            loop.run_in_executor(None, blocking)
            print(f'{time.ctime()} Hello!')
            await asyncio.sleep(1.0)
            print(f'{time.ctime()} Goodbye!')


        def blocking():
            time.sleep(1.5)
            print(f"{time.ctime()} Hello from a thread!")


        asyncio.run(main())
        ```
        * ### 此示例會報錯 (RuntimeError)。
        * ### 報錯理論:
            * ### run_in_executor() 沒有建立 Task 實例，它傳回的是 Future。
            * ### 這表示 asyncio.run() 中用來收集、取消的「有效任務」集合中，不包含該 Future。
            * ### 因此 run_in_executor() 不會等待執行器作業完成。
            * ### asyncio.run() 中的 loop.close() 內部會引發 RuntimeError。
        * ### Python 3.9 中改進了上述的問題，所以就不會報錯了。
    * ### 來看看有哪些方案可以採用，以解決上述問題。
    * ### 方案 A: 在協程中包裝執行器呼叫
        ```
        import time
        import asyncio


        async def main():
            loop = asyncio.get_running_loop()
            future = loop.run_in_executor(None, blocking)
            try:
                print(f'{time.ctime()} Hello!')
                await asyncio.sleep(1.0)
                print(f'{time.ctime()} Goodbye!')
            finally:
                # 確定 main() 函式結束前，
                # 一定要等待 Future 完成。
                await future


        def blocking():
            time.sleep(2.0)
            print(f"{time.ctime()} Hello from a thread!")


        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print('Bye!')
        ```
    * ### 方案 B: 將執行器 Future 加入任務收集群組
        ```
        import time
        import asyncio


        # 輔助函式會等待 Future 完成，
        # 即便發生 CancelledError。
        async def make_coro(future):
            try:
                return await future
            except asyncio.CancelledError:
                return await future


        async def main():
            loop = asyncio.get_running_loop()
            future = loop.run_in_executor(None, blocking)
            # 取的 run_in_executor() 傳回的 Future，
            # 傳給新定義的 make_coro() 輔助函式。
            asyncio.create_task(make_coro(future))
            print(f'{time.ctime()} Hello!')
            await asyncio.sleep(1.0)
            print(f'{time.ctime()} Goodbye!')


        def blocking():
            time.sleep(2.0)
            print(f"{time.ctime()} Hello from a thread!")


        try:
            asyncio.run(main())
        except KeyboardInterrupt:
            print('Bye!')
        ```
    * ### 方案 C: 就像露營一樣，自行準備迴圈與執行器
        ```
        import time
        import asyncio

        from concurrent.futures import ThreadPoolExecutor as Executor


        async def main():
            print(f'{time.ctime()} Hello!')
            await asyncio.sleep(1.0)
            print(f'{time.ctime()} Goodbye!')
            loop.stop()


        def blocking():
            time.sleep(2.0)
            print(f"{time.ctime()} Hello from a thread!")


        loop = asyncio.get_event_loop()
        # 自行建立執行器實例
        executor = Executor()
        # 指定自訂執行器為迴圈預設
        loop.set_default_executor(executor)
        loop.create_task(main())
        # 一如繼往的執行阻斷函式
        future = loop.run_in_executor(None, blocking)
        try:
            loop.run_forever()
        except KeyboardInterrupt:
            print('Cancelled')
        tasks = asyncio.all_tasks(loop=loop)
        for t in tasks:
            t.cancel()
        group = asyncio.gather(*tasks, return_exceptions=True)
        loop.run_until_complete(group)
        # 明確等待執行器工作結束
        executor.shutdown(wait=True)
        loop.close()
        ```
<br />
