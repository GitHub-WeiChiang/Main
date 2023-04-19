Chapter09 Python 操作數據庫
=====
* ### 如何使用 Redis 實現異步隊列
    * ### 消費者 - 生產者模式 (簡單示例)
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
<br />
