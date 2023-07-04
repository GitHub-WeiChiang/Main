Pika
=====
* ### 01 - Message Queue 介紹與實際應用
<br />

01 - Message Queue 介紹與實際應用
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
