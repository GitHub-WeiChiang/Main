Chapter09 Python 操作數據庫
=====
* ### 如何使用 Redis 實現異步隊列
    * ### 消費者 - 生產者模式 (簡單示例 1)
        ```
        import time
        import redis

        pool = redis.ConnectionPool(host="localhost", port=6379, db=1, decode_responses=True)

        r = redis.Redis(connection_pool=pool)


        def product(j):
            if r.llen("queue") > 2:
                print("隊列已滿")
                time.sleep(1)
                product(j)
            else:
                r.lpush("queue", "queue " + str(j))
                print("隊列注入")
                time.sleep(0.5)


        if __name__ == '__main__':
            for i in range(10):
                product(i)
        ```
        ```
        import time
        import redis
        import threading

        pool = redis.ConnectionPool(host="localhost", port=6379, db=1, decode_responses=True)

        r = redis.Redis(connection_pool=pool)


        def consumer():
            while True:
                data = r.brpop("queue")
                time.sleep(2)

                if data is None:
                    print("Wait")
                    time.sleep(0.5)
                else:
                    print(data)


        if __name__ == '__main__':
            threading.Thread(target=consumer, args=()).start()
        ```
    * ### 消費者 - 生產者模式 (簡單示例 2)
        ```
        import redis

        class RedisTask(object):
            def __init__(self,info):
                self.rcon = redis.StrictRedis(host='localhost', db=1)
                self.queue = info


            def listen_task(self):
                while True:
                    # 填 0 为阻塞等待，填大于 0 的数字为超时等待，
                    # 超过时间没有消息接收到则 task 为 None。
                    task = self.rcon.blpop(self.queue, 0)
                    print(task)

        if __name__ == '__main__':
            info = 'abc'
            redis_task = RedisTask(info)
            redis_task .listen_task()
        ```
        * ### blpop: 移出并获取列表的第一个元素， 如果列表没有元素会阻塞列表直到等待超时或发现可弹出元素为止。
    * ### 發布者 - 訂閱者模式 (簡單示例)
        ```
        import time
        import redis

        pool = redis.ConnectionPool(host="localhost", port=6379, db=1, decode_responses=True)

        r = redis.Redis(connection_pool=pool)


        if __name__ == '__main__':
            for i in range(10):
                r.publish("queue", i)
                print("注入")
                time.sleep(1)
        ```
        ```
        import redis
        import threading

        pool = redis.ConnectionPool(host="localhost", port=6379, db=1, decode_responses=True)

        r = redis.Redis(connection_pool=pool)


        def subscriber(num: int):
            sub = r.pubsub()
            sub.subscribe("queue")

            # 订阅多个频道使用 psubscribe 方法並傳入陣列
            sub.psubscribe("queue")

            for message in sub.listen():
                if message['type'] == 'message':
                    print(num, message['channel'], message['data'])


        if __name__ == '__main__':
            for i in range(2):
                threading.Thread(target=subscriber, args=(i,)).start()
        ```
        * ### 关键方法: pubsub、publish、subscribe、psubscribe。
* ### 數據庫的讀寫分離
    * ### 為什麼要進行數據庫讀寫分離 ?
        * ### 因寫入耗時大於查詢耗時，大量寫入場景會長時戰用數據連接，此時查詢操作需等待寫入操作結束，會嚴重影響查詢效率。
    * ### 什麼是數據庫讀寫分離 ?
        * ### 將數據庫寫入操作與查詢操作分別放在兩個不同的數據庫，主數據庫用於增刪改操作，由主數據庫通過數據同步從數據庫中進行查詢操作。
        * ### 一主寫，多從讀。
    * ### 讀寫分離的作用 ?
        * ### 適用於讀操作遠大於寫操作場景，可以緩解主數據庫壓力，提高數據讀取效能，主要用於解決數據讀操作耗時瓶頸。
    * ### 讀寫分離實現方式 ?
        * ### 程序代碼方式
            * ### 在程序代碼中進行數據庫配置與指定。
            * ### 區分寫入操作與讀取操作數據庫。
            * ### 實作簡單，便於應用在小中型場景。
            * ### 系統架構若調整則代碼需連動調整。
            * ### 不適用於大型場景。
        * ### 中間件方式
            * ### 透過獨立系統對數據庫進行管理，實現讀寫分離。
            * ### 中間件對業務服務器提供 SQL 兼容。
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/PythonInterview/Chapter09/ReadWriteSplitting.png)
* ### 三種刪除操作 drop、truncate 和 delete 有什麼區別 ?
    * ### drop
        * ### 數據庫定義語言，屬於數據庫層級。
        * ### 刪除數據表數據與數據表結構。
        * ### 無日誌記錄、無法處發觸發器、無法恢復。
    * ### truncate
        * ### 數據庫定義語言，屬於數據表層級。
        * ### 僅刪除數據表數據，並不會刪除數據表結構。
        * ### 無日誌記錄、無法處發觸發器、可恢復 (不能透過事務回滾方式)。
    * ### delete
        * ### 數據庫操作語言，屬於記錄層級。
        * ### 根據條件限制，刪除符合限制數據 (理所當然不會刪除表結構)。
        * ### 執行過程會記錄日誌，可以透過事務回滾方式恢復。
    * ### 小節
        * ### 刪除全家: drop。
        * ### 刪除全數據: truncate。
        * ### 刪除特定數據: delete。
* ### Redis 持久化機制是什麼 ? 有哪幾種方式
    * ### 持久化設置是為了保障當服務器內存因故障或是重啟被清空時 Redis 中的數據並不丟失。
    * ### RDB
        * ### 不適用於大數巨集場景。
        * ### 持久化過程耗時較長。
        * ### 備份過程 Redis 處於停止服務狀態 (幾百毫秒至一秒)。
        * ### 發生故障時丟失數據較多。
    * ### AOF
        * ### 發生故障時丟失數據較少，適合災難性場景數據恢復。
        * ### AOF 日誌文件相較於 RDB 數據快照檔案更大。
        * ### 綜合效能 AOF 劣於 RDB。
    * ### [理解更多](https://github.com/GitHub-WeiChiang/main/tree/master/Questions/Question009)
<br />
