Chapter21 一筆記錄的多副面孔 -- 交易隔離等級和 MVCC
=====
* ### 系統中的同一時刻最多只允許一個交易運行，其他交易只有在該交易執行完成之後才可以開始運行，這種執行方式稱為 "串列執行"。
* ### 在某個交易存取某個資料時，對要求其他試圖存取相同資料的交易進行限制，讓他們進行排隊，當該交易提交之後，其他交易才能繼續存取這個資料，這樣可以讓併發執行的交易的執行結果與串列執行的結果一樣，這種執行方式稱為 "可序列化執行"。
* ### 交易併發即時執行遇到的一致性問題
    * ### 髒寫入 (Dirty Write): (A 寫) -> (B 寫) -> (B 寫) -> (A 寫)。
    * ### 中途讀取 (Dirty Read): (A 寫) -> (B 讀) -> (B 讀) -> (A 寫)。
    * ### 不可重複讀取 (Non - Repeatable Read): (A 讀) -> (B 寫) -> (B 寫) -> (A 讀)。
    * ### 虛設項目讀取 (Phantom): (A 讀數量) -> (B 增刪) -> (A 讀數量)。
* ### SQL 標準中的 4 種隔離等級
    | 隔離等級 | 中途讀取 | 不可重複讀取 | 虛設項目讀取 |
    | --- | --- | --- | --- |
    | READ UNCOMMITTED | 可能 | 可能 | 可能 |
    | READ COMMITTED | 不可能 | 可能 | 可能 |
    | REPEATABLE READ | 不可能 | 不可能 | 可能 |
    | SERIALIZABLE | 不可能 | 不可能 | 不可能 |
* ### MySQL 預設隔離等級為 REPEATABLE READ。
* ### 詳細內容可參考論文: A Critique of ANSI SQL Isolation Levels。
* ### Oracle 只支持 READ COMMITTED 與 SERIALIZABLE。
* ### MySQL 支持四種但與上述規範有些出入。
    ```
    SET [GLOBAL|SESSION] TRANSACTION ISOLATION LEVEL level;
    ```
* ### 版本鏈 (詳細內容請參閱書籍 21-14 頁)
    * ### 聚簇索引記錄包含兩個必要隱藏列
        * ### trx_id: 交易 id。
        * ### roll_pointer: 指向上一版的 undo 記錄檔指標。
    * ### 不可以在兩個交易中交換更新同一筆記錄，會造成髒寫入，InnoDB 用鎖來避免髒寫入問題，在第一個交易更新某筆記錄前，就會給這筆記錄加鎖，另一個交易再次更新該紀錄時就需要等待第一個交易提交，把鎖釋放之後才可以繼續更新。
    * ### 每次更新紀錄後，都會將舊值放到一筆 undo 記錄檔中，隨著更新次數的增多，所有的版本都會 roll_pointer 串接成一條鏈接串列，稱為 "版本鏈"。
    * ### "版本鏈" 的頭節點就是目前記錄的最新值，每個版本中還包含生成該版本時對應的交易 id。
    * ### 之後就可以利用這個紀錄的版本鏈來控制併發交易存取相同紀錄時的行為，這種機制被稱為 "多版本併發控制 (MVCC，Multi - Version Concurrency Control)"。
* ### ReadView (判斷版本可見性)
    * ### READ UNCOMMITTED: 可以讀到未提交交易修改過的紀錄，所以直接讀取紀錄的最新版就好了。
    * ### SERIALIZABLE: 使用加鎖方式存取紀錄。
    * ### READ COMMITTED 與 REPEATABLE READ: 必須保證讀到已經提交的交易修改過的紀錄，也就是說假如另一個交易已經修改了紀錄但尚未提交，則不能直接讀取最新版本的紀錄。
    * ### 核心問題為: 需要判斷版本鏈中的哪個版本是當前交易可見的，主要透過 "ReadView (一致性視圖)" 完成。
* ### ReadView 重要參數
    * ### m_ids: 生成 ReadView 時，當前系統中活躍的讀寫交易的交易 ID 清單。
    * ### min_trx_id: 生成 ReadView 時，當前系統中活躍的讀寫交易中最小的交易 ID，也就是 m_ids 中的最小值。
    * ### max_trx_id: 生成 ReadView 時，系統應該分配給下一個交易的交易 ID 值。
    * ### creator_trx_id: 生成該 ReadView 的交易 ID。
* ### 透過 ReadView 判斷版本是否可見
    * ### 被存取版本的 trx_id 與 ReadView 中 creator_trx_id 相同，表示當前交易在存取他自己修改過的紀錄，所以改版本可以被當前交易存取。
    * ### 被存取版本的 trx_id 小於 ReadView 中 creator_trx_id，表明生成該版本的交易，在當前交易生成 ReadView 前已提交，所以該版本可以被當前交易存取。
    * ### 被存取版本的 trx_id 大於 ReadView 中 creator_trx_id，表明生成該版本的交易，在當前交易生成 ReadView 後才開啟，所以該版本不可以被當前交易存取。
    * ### 被存取版本的 trx_id 在 ReadView 的 min_trx_id 與 max_trx_id 之間，則需要判斷 trx_id 是否在 m_ids 清單中，如果在，說明創建 ReadView 時生成該版本的交易還是活躍的，該版本不可以被存取，如果不在，說明創建 ReadView 時生成該版本的交易已經被提交，該版本可以被存取。
    * ### 如果某個版本的資料對當前交易不可見，那就順著版本鏈找到下一個版本的資料，並繼續執行上面的步驟來判斷紀錄的可見性。
* ### ReadView 生成時機
    * ### READ COMMITTED: 每次讀取資料前都生成一個 ReadView。
    * ### REPEATABLE READ: 在第一次讀取資料時，生成一個 ReadView。
* ### 當前系統中，如果最早生成的 ReadView 不再存取 undo 記錄檔以及打了刪除標記的記錄，則可以透過 purge 操作將他們刪除。
<br />
