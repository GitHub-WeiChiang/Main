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
<br />
