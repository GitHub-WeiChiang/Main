Question016 - asyncio.run() 背後的細節秘密「事件迴圈」是什麼 ?
=====
* ### 大部分基於 Asyncio 的函式，建議使用 async.run() 來執行。
* ### 所以它的細節是...
```
import asyncio

async def func():
    # 做點什麼孩子

# 取得事件迴圈
loop = asyncio.get_event_loop()
# 建立迴圈中的任務
task = loop.create_task(func())
# 執行直到任務完成 (阻斷動作)
loop.run_until_complete(task)
# 關閉事件迴圈
loop.close()
```
* ### 只有一個執行緒在底層執行一個事件回圈，不斷檢查任務，若有阻斷會找出下一個可執行任務，記得最後要關閉，否則 run_until_complete 會一直阻斷下去。
* ### 流程就是: 取得事件迴圈 -> 建立任務 -> 把任務丟進去 -> 開始日複一日年復一年，跟人生一樣 -> 關閉升天。
<br />
