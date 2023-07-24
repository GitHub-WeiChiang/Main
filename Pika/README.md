Pika
=====
* ### 01 - Message Queue 介紹與實際應用
* ### 02 - RabbitMQ 簡介與 5 種設計模式
* ### 03 - RabbitMQ 架設方法與網頁管理介面
* ### 04 - RabbitMQ x Python 程式實作範例
<br />

01 - Message Queue 介紹
=====
* ### 什麼是 Message Queue (MQ) ?
    * ### Message Queue (MQ) 是一種訊息傳遞仲介，擁有三個角色，分別提供不同程序 (process) 或不同系統 (system) 的非同步 (asynchronous) 溝通。
* ### MQ 的三種角色
    * ### Producer: 產生 Message 的角色，可能是程式、感測器 (sensor) 等，負責將訊息傳送給指定的 Broker。
    * ### Broker:  Queue 本身 (以不同名稱區分)，負責暫存訊息後依序傳送給 Consumer。
    * ### Consumer: 消化 Message 的角色 (或稱為 Worker)，負責主動拿取或被動接收 Broker 的訊息。
    * ### Message: 泛指在 Queue 之間流通的訊息 (或稱為任務)，包含 routing info (標籤) & body (內容)。
* ### 由於先進先出 (FIFO) 的特性，發送方 (Producer) 只要把訊息往 MQ (Broker) 裡面丟，接收方 (Consumer) 就能夠依序從 MQ (Broker) 中取出訊息 (Message)，使雙方能夠獨立運作，不需要放在同一套系統內。
* ### 使用 MQ 的好處
    * ### 任務緩衝: 短時間內的大量請求可能導致系統過載，特別是 CPU / GPU 運算吃重 (heavy computing) 的情況，MQ 的緩衝使 Producer 不需等待可直接向 Broker 發送 Message，而 Consumer 依自己的資源和算力從 Broker 取出適量的 Message。
    * ### 暫存容錯: 當 Consumer 意外關閉，未處理完的訊息因存在 MQ 內，並不會丟失。
    * ### 系統解耦: 架構設計上拆分為不同元件 (components) 獨立開發，三個角色無需部署在同一台機主機，不需知道彼此的 IP，也不需使用相同的程式語言。
    * ### 水平擴展: Producer 可分散在不同來源、裝置收集 (e.g. IoT Applications)；Consumer 可以按照需求和資源，運行在多台機器上，加速訊息 (任務) 的消化和處理。
* ### 常見工具
    * ### 開源: RabbitMQ、Redis、Kafka。
    * ### 雲端: Cloud Pub / Sub、Amazon SQS。
* ### 實際應用
    * ### 場景: 將商品資訊 (圖片 & 文字) 進行向量轉換，分為會使用到 CV 模型和 NLP 模型，由於 GPU 運算負擔比較重 (機器資源、計算時間等)，因此將系統拆分為 Producer 和 Consumer。
    * ### Producer 負責資料過濾 (data filtering) 與特徵提取 (feature extraction)。
    * ### Consumer 負責任務收集 (task collecting) 和向量轉換 (vectorization)。
    * ### 兩個系統彼此不會直接溝通，而是將 Message 透過 Broker 暫存與傳遞，分為 Image Queue 和 Text Queue，並可以根據目標完成時間來調整 Producer 和 Consumer 的數量，加速任務的消化。
<br />

02 - RabbitMQ 簡介與 5 種設計模式
=====
* ### RabbitMQ 簡介
    * ### 輕量級開源工具，支持 AMQP 0-9-1 等多種訊息傳遞協定。
    * ### 容易在本地端和雲端部署，滿足大規模 (分散式)、高可用性的需求。
    * ### 為大多數流行的程式語言提供了多樣的開發套件包。
    * ### 提供 Web 使用者介面來管理權限並監控各種狀態、指標。
* ### RabbitMQ 架構
    * ### Producer: 發送訊息的應用程式。
    * ### Queue: 儲存訊息的緩衝區。
    * ### Consumer: 接收訊息的應用程式。
    * ### Exchange
        * ### 透過綁定 (binding) 與 Queue 連結，負責接收來自 Producer 的訊息，然後將訊息推送給 Queue。
        * ### 透過定義其類型 (type) 判斷如何處理收到的訊息，推送給哪個 Queue ? 亦或是推送給多個 Queue ? 還是丟棄 ?
        * ### 其類型 (type) 分為: Direct、Topic 和 Fanout。
* ### RabbitMQ 設計模式
    * ### Simple
    * ### Worker
    * ### Publish / Subscribe
    * ### Routing
    * ### Topics
* ### Simple 模式
    * ### 最基本的一種模式，只有一個 Queue (定義 Queue 的名稱)，Producer 直接將訊息傳進這個 Queue (hello)，也只有一個 Consumer 從這個 Queue (hello) 取出訊息。
    * ### Tutorial -> [click me](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)
* ### Worker 模式
    * ### 此模式會有兩個以上的 Consumer (Worker)，從同一個 Queue 取出訊息，且 Consumer 彼此間不會取得相同的訊息，加速訊息處理 (消化) 速度。因此只要連接同一個 Queue，就可以在多台機器上 Consumer 平行處理。
    * ### 可透過 ```prefetch_count``` 參數，控制每個 Consumer (Worker) 每一次取出的訊息數量，假設 Producer 將 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 依序傳進 Queue:
        * ### prefetch_count = 1
            * ### C1 依序取得: 1、3、5、7、9
            * ### C2 依序取得: 2、4、6、8、10
        * ### prefetch_count = 2
            * ### C1 依序取得: (1, 2)、(5, 6)、(9, 10)
            * ### C2 依序取得: (3, 4)、(7, 8)
    * ### Tutorial -> [click me](https://www.rabbitmq.com/tutorials/tutorial-two-python.html)
* ### Publish / Subscribe 模式
    * ### 此模式顧名思義，就像 YT 訂閱功能，當頻道創作者發佈了新影片，所有訂閱者都會收到通知。
    * ### Producer 不會將訊息直接傳進 Queue，而是交給 Exchange (type=fanout)。
    * ### 由於 fanout 的特性，Exchange 會把訊息廣播給所有綁定的 Queue，每個 Consumer 就會接收到相同的訊息。
    * ### 當有另外的系統需要同步接收訊息，只需增加一組 Queue + Producer，綁定這個 Exchange 即可。
    * ### Tutorial -> [click me](https://www.rabbitmq.com/tutorials/tutorial-three-python.html)
* ### Routing 模式
    * ### 此模式同樣有一層 Exchange (type=direct)，但不同的是 direct 的特性。
    * ### Exchange 與 Queue 的綁定 (binding) 還會帶上 routing key，Producer 傳送訊息到 Exchange 時也會帶上 routing key。
    * ### 因此可以達到選擇性訊息分流，不同 Consumer 只需要接受到特定 routing 的訊息。
    * ### 日誌系統 (logging system) 就可以使用兩組 Queue
        * ### Q1 只有綁定一個 routing key (error)，因此負責寫檔 (log file) 的 C1 只會接收 error log messages，可節省硬碟 (disk) 空間。
        * ### Q2 則是綁定多個 routing key (info、warning、error)，負責打印到控制台 (console) 的 C2 仍然可輸出所有層級 (level) 的 log messages。
    * ### Tutorial -> [click me](https://www.rabbitmq.com/tutorials/tutorial-four-python.html)
* ### Topics 模式
    * ### 此模式與 Routing 模式很像，同樣有一層 Exchange (type=topic)，也透過 routing key 來分流訊息。
    * ### 差別在 topic 的特性能夠模糊綁定非固定的 routing key。
        * ### .(dot): 分隔的字串。
        * ### *(star): 只能代替一個單詞。
        * ### #(bash): 可以代替零個或多個單詞。
    * ### 舉例
        * ### Q1 以 ```.orange.``` 綁定。
        * ### Q2 以 ```*.*.rabbit``` 和 ```lazy.#``` 綁定。
        * ### ```quick.orange.rabbit```: Q1、Q2。
        * ### ```lazy.orange.elephant```: Q1、Q2。
        * ### ```quick.orange.fox```: Q1。
        * ### ```lazy.brown.fox```: Q2。
        * ### ```lazy.pink.rabbit```: Q2。
        * ### ```quick.brown.fox```: 沒人要它，哭哭好可憐。
    * ### 進階
        * ### ```orange```: 沒人要它，哭哭好可憐。
        * ### ```quick.orange.male.rabbit```: 沒人要它，哭哭好可憐。
        * ### ```lazy.orange.male.rabbit```: Q2。
    * ### Tutorial -> [click me](https://www.rabbitmq.com/tutorials/tutorial-five-python.html)
<br />

03 - RabbitMQ 架設方法與網頁管理介面
=====
* ### RabbitMQ 環境架設
    * ### Docker 指令
        ```
        # create and start container

        docker run --rm --name rabbitmq -p 5672:5672 -p 15672:15672 -e RABBITMQ_DEFAULT_USER=root -e RABBITMQ_DEFAULT_PASS=1234 rabbitmq:management
        ```
        * ### docker run: 執行容器。
        * ### --rm: 當容器終止時會自動刪除。
        * ### --name rabbitmq: 將容器命名為 rabbitmq。
        * ### -p 5672:5672: 將本機端的 5672 port 關聯到容器的 5672 port (RabbitMQ)。
        * ### -p 15672:15672: 將本機端的 15672 port 關聯到容器的 15672 port (Web UI)。
        * ### -e RABBITMQ_DEFAULT_USER=root: 宣告環境變數，連線到 RabbitMQ 的 username。
        * ### -e RABBITMQ_DEFAULT_PASS=1234: 宣告環境變數，連線到 RabbitMQ 的 password。
        * ### rabbitmq:management: 指定容器抓 Docker Hub 上的 RabbitMQ Official Images。
    * ### Docker Compose 指令
        ```
        # create and start container

        docker-compose -f docker-compose.yml up
        ```
* ### 進入 
    * ### RabbitMQ -> [click me](http://localhost:15672)
    * ### Overview: RabbitMQ Server 的重要資訊和指標。
    * ### Connections: 當前 RabbitMQ Server 上所有 Clients 的連線狀態與網路資訊。
    * ### Channels: 當前 RabbitMQ Server 上所有 Channels 的訊息吞吐量。
    * ### Exchanges: 查看與管理功能，預設已建立數種 Type 的 Exchanges。
    * ### Queues: 查看並管理每一條 Queue 的訊息 (messages) 狀態與吞吐量。
    * ### 新增 Queue: 輸入自訂 Queue name（唯一值），並設定必要及可選的參數。
        * ### Durablity
            * ### Durable: 關閉或重啟後訊息還會留存。
            * ### Transient: 關閉或重啟後不留存。
        * ### Auto delete
            * ### Yes: Queue 會在所有 Consumer 都中斷連接時自行刪除。
        * ### Aruguments
            * ### Message TTL: Queue 裡的訊息在多少時間 (毫秒) 內若沒有被取用就會被丟棄。
            * ### Auto expire: Queue 在多少時間 (毫秒) 內若都沒有被使用就會自動刪除。
            * ### Single active connsumer: 該 Queue 是否只能有一個存活的 Consumer。
            * ### Max length: Queue 最多保存的訊息量，若超過會從頭端 (FIFO) 丟棄訊息。
            * ### Max length bytes: Queue 最多保存的訊息長度，若超過會從頭端 (FIFO) 丟棄訊息。
                * ### 若 Max length 為 1000，代表 Queue 最多能保存 1000 則訊息。
                * ### 若 Max length bytes 為 10000，單一訊息 12 bytes，代表最多只能存 10000 / 12 = 833 則訊息。
    * ### Queue 的訊息可能會因為過期 (MMessage TTL) 或超過限制 (Max length) 被丟棄，透過以下兩個 Arguments 設定這些訊息要被重新推送至哪裡。
        * ### Dead letteer exchange: 被丟棄的訊息要被推送進入的 Exchange。
        * ### Dead letteer routing key: Dead letteer exchange 要綁定 (binding) Queue 的 Routing key。
    * ### 管理 Queue (點選進入 Queue 內容頁面)
        * ### 查看 Messages 的詳細資訊和速率指標。
        * ### 設定 Queue 要綁定 (binding) 的 Exchange 和 Routing key。
        * ### 查看連接的 Consumer。
        * ### 推送訊息、取出一至多則訊息。
        * ### 刪除 (delete) 整條 Queue。
        * ### 清空 (purge) 整條 Queue 裡的訊息。
        * ### 嘗試推送 (Publish) 與取出 (Get) 訊息。
    * ### Admin: 管理與新增 Users。
<br />

04 - RabbitMQ x Python 程式實作範例
=====
* ### Installation
    ```
    pip install pika
  
    pip install aio-pika
    ```
* ### 三種從 RabbitMQ Broker 消費 (consume) 訊息的方法
    * ### Using channel.basic_get() to consume a message: 開發者手動調用取出訊息。
        ```
        channel.queue_declare(queue='hello')
    
        channel.basic_get(queue='hello', auto_ack=True)
        method, properties, body = channel.basic_get(queue='hello', auto_ack=True)
        print(f" [x] Received {body.decode()}")
    
        connection.close()
        ```
    * ### Using channel.basic_consume() to consume messages: 持續監聽。
        ```
        channel.queue_declare(queue='hello')
        
        def callback(ch, method, properties, body):
            print(f" [x] Received {body.decode()}")
        
        channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)
        
        print(' [*] Waiting for messages. To exit press CTRL+C')
        channel.start_consuming()
        
        try:
            channel.start_consuming()
        except KeyboardInterrupt:
            channel.stop_consuming()
        
        connection.close()
        ```
    * ### Using channel.consume() generator to consume messages: 定時接收 (無訊息接收到 None)。
        ```
        channel.queue_declare(queue='hello')
        
        for method, properties, body in channel.consume(queue='hello', auto_ack=True, inactivity_timeout=10):
        
            print(f" [x] Received {body.decode()}")
        
            if method == None and properties == None and body == None:
                break
        
        connection.close()
        ```
<br />
