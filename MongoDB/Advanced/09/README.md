09 - 複寫
=====
* ### 何謂複寫 ?
    * ### 複寫 (Replication) 就是讓多的 MongoDB Server 擁有一樣的資料。
    * ### 透過複寫功能的啟用，可以將多個 Server 集合成一個群組，增為 "複寫集"。
    * ### 複寫集中的每個 Server 被稱為 "複寫集成員"，其所擁有的資料會自動同步並保證最終一致性。
    * ### 複寫集的主要功能是提高資料可用性，避免單點故障 (SPOF, Single Point of Failure) 問題。
    * ### 因複寫集成員擁有同樣的資料，客戶端在讀取資料時 (僅限讀取) 可以從不同主機讀取，避免請求集中於一部主機。
    * ### 複寫集的另一個目的: 可以使用交易 (Transaction)，使資料異動後有機會可以恢復到異動前狀態。
    * ### 理解更多 (11 - 交易) -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/MongoDB/Advanced/11)
* ### 複寫集成員
    * ### 三種角色: Primary (主要伺服器)、Secondary (次要伺服器)、Arbiter (仲裁者)。
    * ### Primary: 提供客戶端完整存取服務。
    * ### Secondary: 儲存並同步主要伺服器資料。
    * ### Arbiter: 在選舉時出來投票給合適成為 Primary 的成員，沒有其它用處了，也不儲存 Primary 資料。
    * ### 複寫集成員中只能有一個 Primary，可以有多個 Secondary，Arbiter 則可有可無 (若要配置 Arbiter 以一個為佳)。
    * ### 複寫集成員數量最少為 1 員，最多為 50 員，正式上線系統以至少 3 員為佳。
    * ### PSS (Primary - Secondary - Secondary) 三成員複寫集架構
    * ### PSA (Primary - Secondary - Arbiter) 三成員複寫集架構
<br />

範例程式
=====
* ### 
<br />
