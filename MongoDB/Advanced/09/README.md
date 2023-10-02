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
<br />

範例程式
=====
* ### 
<br />
