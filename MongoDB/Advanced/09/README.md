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
    * ### 複寫集成員數量最少為 1 員，最多為 50 員，正式上線系統以至少 3 員為佳 (具有一個容錯能力)。
    * ### PSS (Primary - Secondary - Secondary) 三成員複寫集架構
        * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/MongoDB/Advanced/09/PSS.png)
        * ### 任一 Secondary 壞掉並不影響整體運作。
        * ### 若 Primary 壞掉，剩餘的兩個 Secondary 會投票選出一個新的 Primary 使服務繼續運行。
    * ### PSA (Primary - Secondary - Arbiter) 三成員複寫集架構
        * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/MongoDB/Advanced/09/PSA.png)
        * ### Secondary 或 Arbiter 任一壞掉並不影響整體運作。
        * ### 若 Primary 壞掉，剩下唯一的 Secondary 會變成 Primary 使服務繼續運行。
    * ### 複寫集成數量若為 1，其必定是 Primary 且無容錯能力與備援功能。
    * ### 複寫集成數量若為 2，且配置為 Primary + Secondary，任一成員故障都會導致服務中斷，但具有資料備份能力。
    * ### 複寫集成數量若為 2，且配置為 Primary + Arbiter，則無容錯能力與備援功能，是個沒有意義的複寫集，與我的人生一樣。
* ### 選舉與投票
    * ### 選舉的最大的秘密，很多人都猜不透看不瞭解，選舉最大的秘密，就是票多的贏票少的輸，就這麼簡單。
    * ### 選舉的目的是為了生成 Primary，擁有超過一半票數的成員會當選。
    * ### 在三成員複寫集中，要成為 Primary 至少需要兩票。
    * ### 在兩成員複寫集中 (Primary + Secondary)，若 Secondary 故障會觸發選舉，此時 Primary 只能拿到自己投給自己的一票，低於一半的票數，故會被降級成 Secondary，導致服務中斷，反之亦然。
    * ### 而無論是 PSS 或 PSA，如果只有一個成員故障，剩餘的兩個成員一定可以選出 Primary 使服務繼續運行，差別僅在於 Arbiter 永遠都不會成為 Primary。
    | 成員數 | Primary 的最小得票數 | 容忍損壞數 |
    |-----|----------------|-------|
    | 1   | 1              | 0     |
    | 2   | 2              | 0     |
    | 3   | 2              | 1     |
    | 4   | 3              | 1     |
    | 5   | 3              | 2     |
    | 6   | 4              | 2     |
    | 7   | 4              | 3     |
    * ### 為了提高 Primary 生成的速度 (選舉效率)，一個複寫集中最多只有 7 個成員可以投票，預設是前 7 個加入的成員。
    * ### 選舉機制啟動的觸發:
        * ### 新成員加入時。
        * ### 複寫集初始化時。
        * ### 手動降級 Primary 或修改複寫集設定時 (例如調整得票優先權)。
        * ### Primary 未回應心跳協定時 (預設為 10 秒)。
<br />

範例程式
=====
* ### 
<br />
