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
    * ### 抽象的理解，每一個 Chunk 上都會被貼上分類標籤貼紙，而分類標籤貼紙上印有可接受的 Shard Key。
    * ### 一個 Chunk 並不是只能被貼上一張分類標籤貼紙，也就是說一個 Chunk 是可以收集不只一種 Shard Key 的資料。
    * ### 分片叢集會設定每個 Chunk 的大小，最小為 1 MB，最大為 1024 MB，預設為 64 MB。
    * ### 當一個 Chunk 無法容納 (滿了) 時，就會將其一分為二，成為 Chunk Split (應該類似於 InnoDB 的頁分裂)。
    * ### 假設有十筆資料，其中 Shard Key 分別各自為 ```L、L、M、M、S、S、S、XL、XL、XL```，此時內容相異數 (Cardinality) 為 4。
    * ### 叢集最多可建立的 Chunk 數量為 Cardinality，換言之，Cardinality 的數量就是最大 Chunk 數。
    * ### 一個 Chunk 可以被貼上多張分類標籤貼紙，而一張分類標籤貼紙只能被貼在一個 Chunk 上，這樣分片叢集才能夠決定資料的去處。
    * ### 當 Chunk 上的分類標籤貼紙只剩一張時，即便達到了分割標準也不會被分割，此時資料一樣能進入對應的 Chunk，但該 Chunk 也會越來越巨大。
    * ### 超過容量的 Chunk 會被標記 Jumbo，當出現被標記 Jumbo 的 Chunk 時，可能意味著 Shard Key 的選擇並不合適。
    * ### 在分片叢集中應要避免 Jumbo Chunk 的出現，Chunk 的容積過大會造成某一分片負荷過高，進而影響整理效率。
    * ### Jumbo 可以透過重設 Shard Key 緩解。
    * ### MongoDB 5.0 開始支援 Shard Key 的重設，Shard Key 的重設會使資料重新分配，面對大量資料時，還是需要一定的時間，故還是應盡可能避免 Jumbo Chunk 的生成。
    * ### 當某個分片主機上的 Chunk 數量不平均到某一門檻時，分片叢集中的 "平衡器" 會開始搬移 Chunk，直到各主機上的 Chunk 數量再度平衡為止。
    * ### 平衡器的搬移會依據兩個分片主機中的 Chunk 數量而觸發，例如當 Chunk 數量小於 20 且兩個分片主機的 Chunk 數量差異超過 2 時，就會開始平衡。
        | Chunk 數量 | 搬移閾值 |
        |----------|------|
        | < 20     | 2    |
        | 20 ~ 79  | 4    |
        | \>= 80   | 8    |
    * ### Chunk 搬移時，會先複製要搬移的 Chunk，待搬移完成後才會刪除原本的 Chunk (搬移過程會有資料筆數多於實際資料筆數的情況)。
    * ### 一次的搬移，被搬移的 Chunk 數量不會大於分片主機數量的一半。
    * ### 資料進行備份時需手動關閉平衡器，若平衡器正在搬移 Chunk 的同時進行資料備份，會造成備份出的資料與實際場景不同。
        ```
        // MongoDB Shell
        
        // 關閉平衡器
        sh.disableBalancing("<database>.<collector>")
        
        // 開啟平衡器
        sh.enableBalancing("<database>.<collector>")
        ```
<br />

範例程式
=====
* ### 
<br />
