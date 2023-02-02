Chapter03 盤點 Asyncio
=====
* ### Asyncio 的原理簡單說就是在事件迴圈中執行一組任務，且任務可以自行決定控制權歸還給事件迴圈的時機。
* ### Python 非同步特性兩類受眾: 直接使用的開發者、框架開發者。
* ### 對開發者而言的 asyncio API 核心特性
    * ### 啟動 asyncio 事件迴圈。
    * ### 使用 async、await 定義、呼叫函式。
    * ### 建立迴圈中執行的任務。
    * ### 等待多工任務完成。
    * ### 在全部並行任務完成後關閉迴圈。
* ### QuickStart1.py 展示簡單的 asyncio 應用代碼。
* ### QuickStart2.py 展示簡化的 asyncio.run() 底層機制流程。
* ### coro 代表協程 (coroutine)，嚴格來說它是 async def 函式的呼叫結果，並不是函式本身。
* ### QuickStartExe.py 展示如何執行阻斷式函式。
* ### loop.run_in_executor(None, func): 用於包裝非 Coroutine 的函式。
    * ### 簡單來說 run_in_executor 會把一般的非異步函式包裝成一個獨立的線程，利用線程並不會被 I/O 所阻塞的特性。
    * ### 用於協調已實現的非 Asyncio 所撰寫之商業邏輯方法。
    * ### 立即让同步函数化身异步语法，使同步库的函数和调用链上的其它异步库的函数能够协同作战。
    * ### 本质是使 concurrent.futures.Future 对象变成了 asyncio 里面的可等待 Future 对象。
    * ### 毫无疑问它还是在线程里面运行的。
    * ### 主要作用不是把同步变成协程运行，而是让其拥有了异步 await 的用法，既能不阻塞当前事件循环，又能在同步函数执行完成 return 结果时拿到结果接着用。
    * ### 在异步环境 (被 async 修饰的异步函数) 里面，调用同步函数，将函数放到线程池运行防止阻塞整个事件循环的其他任务。
    * ### 第一個參數接受 Executor 實例，若使用預設則強制需顯性傳入 None，痾...設計缺陷 ?
* ### Asyncio 特性分層
    | 層次 | 概念 | 實作 |
    | --- | --- | --- |
    | 第九層 | 網路: 串流 | StreamReader, StreamWriter, asyncio.open_connection(), asyncio.start_server() |
    | 第八層 | 網路: TCP 與 UDP | Protocol |
    | 第七層 | 網路: 傳輸 | BaseTransport |
    | 第六層 | 工具 | asyncio.Queue |
    | 第五層 | 子行程與執行緒 | run_in_executor(), asyncio.subprocess |
    | 第四層 | Task | asyncio.Task, asyncio.create_task() |
    | 第三層 | Future | asyncio.Future |
    | 第二層 | 事件迴圈 | asyncio.run(), BaseEventLoop |
    | 第一層 | 協程 | async def, async with, async for, await |
* ### 第一層: 基礎層，支援協程，著名的非同步框架 Curio 與 Trio 都只依賴 Python 的原生協程，沒有使用 Asyncio 程式庫的其它部分。
* ### 第二層: 協程需要事件迴圈輔助才能執行 (因此 Curio 與 Trio 有自己的事件迴圈)，Asyncio 提供了迴圈的規範 AbstractEventLoop 與實作 BaseEventLoop。
    * ### 規範與實作的劃分，提供第三方開發者實現自己的事件迴圈 (uvloop 專案提供了比標準 Asyncio 模組更快的事件迴圈，且其只取代架構中迴圈的部分)。
* ### 第三四層: Future (父) 是 Task (子) 的父類別，Future 實例代表某種進行中的動作，可以透過事件迴圈通知取得結果，Task 代表事件迴圈中的協程。
    * ### Future 是迴圈感知 (loop aware)，Task 兼具迴圈感知與協程感知 (coroutine aware)。
    * ### 就開發者而言較常使用 Task，而對框架設計者而言，能夠接觸細節的 Future 可能是較好的選擇。
* ### 第五層: 代表著必需在個別執行緒 (行程) 中啟動與等待工作的功能特性。
* ### 第六層: 代表著具有非同步感知 (async aware) 的工具 (e.g., asyncio.Queue)，asyncio.Queue 與執行緒安全的 Queue 類似，差別在於 asyncio 的版本在 get() 與 put() 時要配合 await 關鍵字，因為它的 get 會阻斷主執行緒。
* ### 第七八九層: 網路 I/O 層，包含高階串流 API (第九層) 與粒度更細的協定 API (第八層)，傳輸層 (第七層) 除非用於框架建立，否則在正常開發上不會使用。
* ### 重點關注
    * ### 第一層: async def 函式撰寫方式、使用 await 呼叫、協程執行。
    * ### 第二層: 了解啟動、關機、事件迴圈互動方式。
    * ### 第五層: 程式碼阻斷。
    * ### 第六層: 用於資料在一個或多個長時運行協程的提供，asyncio.Queue 使用協程替代 queue.Queue 的 get()。
    * ### 第九層: 處理 socket 溝通的簡單方式，串流 (也可以使用第三方程式庫取代第九層，像是 aiohttp)。
* ### 協程
    * ### Python 3.4 導入 asyncio，但只能透過產生器 (generator) 實作協程，可能會在程式碼中看到 @asyncio.coroutine 裝飾和 yield from 陳述。
    * ### Python 3.5 透過 async def 建立協程，也被稱為原生協程。
    ```
    async def f():
        return 123

    type(f)
    # <class 'function'>

    import inspect
    inspect.iscoroutinefunction(f)
    # True
    ```
    * ### 使用 async def 作為函式開頭。
    * ### 函式 f 型態為協程 "函式" (非同步函式終究是函式，如同 "皇后只能是皇后")，並非協程。
    * ### inspect 模組提供更好的內省 (introspective) 機制，iscoroutinefunction 用於區別一般函式與協程函式。
    * ### 如同產生器函式，產生器是產生器，函式是函式。
    ```
    def g():
        yield 123

    type(g)
    # <class 'function'>

    gen = g()
    type(gen)
    # <class 'generator'>
    ```
    ```
    coro = f()

    type(coro)
    # <class 'coroutine'>

    inspect.iscoroutine(coro)
    # True
    ```
    * ### 協程是一個物件，可以重啟被暫停的函式。
    * ### 協程的返回其實是引發 "StopIteration" 例外 (協程內部使用 send() 與 StopIteration)。
    ```
    async def f():
        return 123

    coro = f()

    try:
        coro.send(None)
    except StopIteration as e:
        print('The answer was:', e.value)
    ```
    * ### 透過 send 傳送 None 給啟始協程，事件迴圈內部就是這樣幹，我們不用處理，我們可以直接使用 loop.create_task(coro) 或是 await coro 來執行協程。
    * ### 協程返回時會引發 StopIteration 例外，可以透過 value 取得協程的傳回值，啊這也不關我們的事，是底層細節，我們可以直接在 async def 中透過 return 回傳。
    * ### send() 與 StopIteration 各自定義了協程執行的起點與終點，由事件迴圈負責這些底層操作。
* ### await 關鍵字: 只接受 awaitable 物件 (協程 or 實作 __await__() 且回傳迭代器的物件)
    ```
    async def f():
        await asyncio.sleep(1.0)
        return 123

    async def main():
        # 產生協程，意味著必須 await，當 f() 完成時，result 為 123。
        result = await f()
        return result
    ```
    * ### 事件迴圈內透過例外取消協程。
    ```
    coro = f()
    coro.send(None)

    # 使協程內部的 await 處引發例外。
    coro.throw(Exception, 'blah')
    ```
    * ### throw() 用於在 asyncio 內部取消任務。
    ```
    import asyncio

    async def f():
        try:
            while True:
                await asyncio.sleep(0)
        # 專門用於取消任務的例外類型
        except asyncio.CancelledError:
            print('I was cancelled!')
        else:
            return 111

    coro = f()
    coro.send(None)
    
    # 例外由外部注入協程，也就是被事件迴圈注入
    coro.throw(asyncio.CancelledError)
    ```
    ```
    import asyncio

    async def f():
        try:
            while True:
                await asyncio.sleep(0)
        except asyncio.CancelledError:
            print('Nope!')
            # 取消時又等待另一個 awaitable 物件
            while True:
                await asyncio.sleep(0)
        else:
            return 111

    coro = f()
    coro.send(None)
    # 協程並沒有被取消，但因為新協成而被暫停
    coro.throw(asyncio.CancelledError)
    # 又被重啟了
    coro.send(None)
    ```
    * ### 透過事件迴圈實作
    ```
    import asyncio

    async def f():
        await asyncio.sleep(0)
        return 111

    # 取得迴圈
    loop = asyncio.get_event_loop()
    coro = f()

    # 執行
    loop.run_until_complete(coro)
    ```
<br />
