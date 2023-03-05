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
* ### 詳細內容可參考論文: A Critique of ANSI SQL Isolation Levels。
* ### Oracle 只支持 READ COMMITTED 與 SERIALIZABLE。
* ### MySQL 支持四種但與上述規範有些出入。
    ```
    SET [GLOBAL|SESSION] TRANSACTION ISOLATION LEVEL level;
    ```
* ### MVCC: 版本鏈 + ReadView (判斷版本可見性)。
* ### 當前系統中，如果最早生成的 ReadView 不再存取 undo 記錄檔以及打了刪除標記的記錄，則可以透過 purge 操作將他們刪除。
<br />
