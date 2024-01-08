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
* ### 選擇片鍵 Shard Key
    * ### 分片的目的是為了加快資料存取的時間，分散式資料庫並不希望資料存取都集中在某一部主機，最好是一半一半。
    * ### 決定哪些資料儲存在哪不分片主機是依靠資料排序 (其為決定資料如何切開的重要依據)。
    * ### 資料在資料庫中的排序方式憑藉的是索引。
    * ### 一個資料表可以建立很多索引，但資料切割的方式只能有一種，在眾多排序方式中被選擇作為資料分割依據的排序方式就稱為 "片鍵 Shard Key"。
    * ### 若所選 Shard Key 使得部分主機相當於備份用途，沒有負擔任何存取需求，則該 Shard Key 就是一個不好的 Shard Key，壞 Shard Key。
    * ### 若找不到合適的 Shard Key，可以選擇一個欄位 (例如時間欄位或 _id 欄位) 新增一個 hashed 索引用於 Shard Key。
    * ### 好的 Shard Key 在理想上要能夠平均分散存取目標於不同分片主機上，反之壞的 Shard Key 會使存取集中於某一分片主機。
    * ### "_id" 欄位作為 Shard Key 本質上是合適的，因其內容不重複特性，使得內容相異數 (Cardinality) 會非常高。
    * ### 因 "_id" 欄位由預設的 ObjectId() 函數生成，此函數為單調遞增函數，所以排序後的新值一定位於端點，若要使用 _id 為 Shard Key，應使用 Hashed Shard Key。
    * ### Hashed Shard Key 必須先建立 hashed 索引，建立指令如下 (Compass 不支援)，索引建立完成後就可以使用 ```sh.shardCollection()``` 選擇 "_id" 欄位為 Shard Key。
        ```
        // MongoDB Shell
        
        // 在指定資料庫的集合中創建一個哈希索引，
        // 索引的目標字段是 "_id" 並且使用 "hashed" 選項，
        // 使 MongoDB 用哈希函數對 "_id" 字段的值進行哈希處理以便更好地支持分片操作，
        // 哈希分片可以平均地分散數據有助於提高性能和擴展性。
        db.collection.createIndex({"_id": "hashed"})
        // 將指定資料庫的集合配置為分片集合，
        // 通過使用哈希分片鍵 "_id" 使 MongoDB 根據 "_id" 字段的哈希值將數據分散到不同的分片上，
        // 實現數據的平均分布 (理想) 以減少單一分片上的數據量，
        // 從而提高性能和擴展性。
        sh.shardCollection("db.collection", {"_id": "hashed"})
        ```
    * ### 分片之後的資料查詢操作模式: 廣播操作 (Broadcast) 與目標操作 (Targeted Operations)。
    * ### 廣播操作 (Broadcast)
        * ### 查詢條件中 "不包含 Shard Key"。
        * ### 因無法確定資料所在位置，僅能使用廣播方式詢問每一部分片主機。
        * ### 需等待每部分片主機皆回應，才能將結果回傳，耗時較長。
        * ### 若查詢條件又不包含被設定索引的欄位，各分片主機還需以線性搜尋方式遍歷各 Chunk 中的資料。
    * ### 目標操作 (Targeted Operations)
        * ### 查詢條件中 "包含 Shard Key"。
        * ### 直接針對特定分片主機進行資料讀取。
    * ### 思考: 當 "_id" 作 Shard Key，會頻繁地使用其為查詢條件嗎 (尤其該內容為 ObjectId 時)。
        * ### 通常似乎是 "不會" (進而產生下方敘述)。
        * ### 使用 "_id" 作 Shard Key 僅僅是讓資料有效地分散在各分片主機。
        * ### 使用 "_id" 作 Shard Key 對於查詢效率上並沒有任何優勢。
        * ### 因此 MongoDB 的 Shard Key 支援 "複合式片鍵"。 
    * ### MongoDB 的 Shard Key 支援 "複合式片鍵" (搭配 "_id" 時，"_id" 需設定 hashed 索引並放在後面)。
        ```
        // MongoDB Shell
        
        // 創建一個包含字段 name 和 _id 的複合索引，
        // name 字段使用升序索引，而 _id 字段使用哈希索引。
        db.collection.createIndex({"name": 1, "_id": "hashed"})
        // 將集合分片，分散數據存儲至多個 MongoDB 分片伺服器，實現水平擴展，
        // {"name": 1, "_id": "hashed"} 為用於分片的鍵，
        // MongoDB 將使用 name 字段和 _id 字段的值來確定文檔應該存儲在哪個分片上。
        sh.shardCollection("db.collection", {"name": 1, "_id": "hashed"})
        ```
* ### 模擬部署演練
    * ### 分片叢集組成: 兩個分片主機、一個 Config Server 與兩個 Router。
    * ### 複寫集架構: PSS。
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/MongoDB/Advanced/10/Architecture.png)
<br />

範例程式
=====
* ### 
<br />
