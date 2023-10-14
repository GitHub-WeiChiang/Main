10 - 分片
=====
* ### 何謂分片
    * ### 用於將資料平均分散在多部電腦中 (分散式資料庫架構)。
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
* ### Chunk 與平衡器
<br />

範例程式
=====
* ### 
<br />
