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
<br />
