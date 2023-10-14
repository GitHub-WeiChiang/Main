10 - 分片
=====
* ### 何謂分片
    * ### 用於將資料平均分散 (不是備份) 在多部電腦中 (分散式資料庫架構)。
    * ### 分片必需架構於複寫之上。
* ### 分片叢集組成: Router + Shard + Config
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/MongoDB/Advanced/10/ShardedCluster.png)
    * ### Router
        * ### 稱為 App Server，為分片叢集的入口 (客戶端與其連線)。
        * ### 可以在分片叢集中部署多台 App Server，透過附載平衡分散客戶端連線。
    * ### Shard
        * ### 稱為分片主機，其將實際儲存資料。
        * ### 資料會被平均分散 (理想) 在各個分片主機上。
        * ### 分片主機本身必需為複寫集架構。
        * ### 理解更多 -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/SystemsDesign/Chapter05)
    * ### Config Server
        * ### 用於記錄每個分片主機上擁有的資料，當 Router 收到資料存取要求時，會先向 Config Server 確認要查詢的資料位於哪個分片主機，以及要寫入的資料應送往哪個分片主機。
        * ### Config Server 本身必需為複寫集架構，且不可包含 Arbiter。
* ### Chunk (貨櫃) 與平衡器
    * ### 分片並不是以資料筆數為單位，而是以 Chunk 這種抽象的概念為單位。
    * ### Chunk 的容量可以進行設定，每個 Chunk 的容量將一致，資料分散的實際操作以其為單位。
    * ### 理想上每個分片主機上的 Chunk 數量應該趨近於一致。
    * ### 資料應屬於哪一個 Chunk 並不是隨機的而是具有特定的分類方式。
    * ### 資料無論是新增或是變動，都會重新的被放置到正確的 Chunk。
    * ### Chunk 應該放置的資料類型，由 "片鍵 (Shard Key)" 決定，而片鍵其實就是資料中的欄位。
    * ### 分片叢集會設定每個 Chunk 的大小，最小為 1 MB，最大為 1024 MB，預設為 64 MB。
    * ### 當一個 Chunk 無法容納 (滿了) 時，就會將其一分為二，成為 Chunk Split (應該類似於 InnoDB 的頁分裂)。
    * ### 
<br />

範例程式
=====
* ### 
<br />
