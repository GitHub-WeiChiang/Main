Pika
=====
* ### 01 - Message Queue 介紹
* ### 02 - RabbitMQ 簡介與 5 種設計模式
* ### 03 - RabbitMQ 架設方法與網頁管理介面
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
<br />
