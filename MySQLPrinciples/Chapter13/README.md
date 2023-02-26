Chapter13 兵馬未動，糧草先行 -- InnoDB 統計資料是如何收集的
=====
* ### InnoDB 儲存資料統計方式
    * ### 永久性地儲存統計資料: 儲存在磁碟，伺服器重啟資料仍存在。
    * ### 非永久性地儲存統計資料: 儲存在記憶體，伺服器重啟需重新收集。
* ### 系統變數 innodb_stats_persistent
    * ### 控制統計資料儲存位置。
    * ### MySQL 5.6.6 之前，預設為 OFF，儲存於記憶體。
    * ### MySQL 5.6.6 開始，預設為 ON，儲存於磁碟。
* ### 以表為單位收集和儲存統計資料，各表的統計資料可以分別儲存。
* ### 屬性 STATS_PERSISTENT
    * ### 為 1，該表統計資料存於磁碟。
    * ### 為 0，該表統計資料存於記憶體。
    * ### STATS_PERSISTENT 的預設值為 innodb_stats_persistent。
* ### 基於磁碟的永久性統計資料
    * ### 儲存於磁碟，本質上是儲存於 innodb_table_stats 與 innodb_index_stats 兩張表。
    * ### innodb_table_stats 表: 儲存表的統計資料，一筆記錄對應一張表。
    * ### innodb_index_stats 表: 儲存表的索引資料，一筆記錄對應一索引。
* ### innodb_table_stats 的欄位 (此表主鍵為複合主鍵，database_name + table_name)
    ```
    SELECT * FROM mysql.innodb_table_stats;
    ```
    * ### database_name: 資料庫名稱。
    * ### table_name: 表名。
    * ### last_update: 最後更新時間。
    * ### n_rows: 記錄筆數 (估計值)。
    * ### clustered_index_size: 聚簇索引佔用頁面數量 (估計值)。
    * ### sum_of_other_index_sizes: 其它索引佔用頁面數量 (估計值)。
* ### n_rows 統計項的收集
    * ### 從聚簇索引選取數個葉子節點頁面。
    * ### 統計各頁面記錄數。
    * ### 計算平均值。
    * ### 乘上總頁面數求得 n_rows 預估值。
    * ### 系統變數 inodb_stats_persistent_sqmple_pages 為頁面取樣數量依據，越大耗時越久但越精確，越小耗時越少相對不精確，預設為 20。
    * ### 可針對單表設定取樣數量。
* ### clustered_index_size 與 sum_of_other_index_sizes 統計項的收集
    * ### 一個索引佔用兩的段 ("葉子節點段" 與 "非葉子節點段"，"段" 是 "區集合" + "零散頁")。
    * ### 從資料字典找到表的各個索引對應的根頁面 (儲存於系統表 SYS_INDEXES)。
    * ### 找到葉子節點和非葉子節點對應的 Segment Header，每個索引跟頁面的 Page Header 都包含兩個欄位。
        * ### PAGE_BTR_SEG_LEAF: B+ 樹葉子節點段 Segment Header 資訊。
        * ### PAGE_BTR_SEG_TOP: B+ 樹非葉子節點段 Segment Header 資訊。
    * ### 從兩者的 Segment Header 找到對應這兩個段的 INODE Entry。
    * ### 針對 INODE Entry 找出該段所有零散頁面位址與 FREE、NOT_FULL 和 FULL 鏈結串列基節點。
    * ### 統計零散頁數量，後從 FREE、NOT_FULL 和 FULL 鏈結串列的 List Length 讀取該段佔用的區數量 (一個區為 64 個頁，當然一個區中的頁可能沒有全部使用，所以這是一個估計值，實際值可能比此值來的小)。
* ### innodb_index_stats 的欄位 (主鍵為 Composite Primary Key，database_name + table_name + index_name + stat_name)
    ```
    SELECT * FROM mysql.innodb_index_stats WHERE table_name = 'table name';
    ```
    * ### database_name: 資料庫名稱。
    * ### table_name: 表名。
    * ### index_name: 索引名。
    * ### last_update: 最後更新時間。
    * ### stat_name: 統計項名稱。
    * ### stat_value: 統計項值。
    * ### sample_size: 生成統計資料的取樣頁面數。
    * ### stat_description: 統計項描述。
* ### 索引的統計項 (stat_name)
    * ### n_leaf_pages: 該索引葉子節點佔用頁面數量。
    * ### size: 該索引共佔用總頁面量 (葉子與非葉子且不管是否使用)。
    * ### n_diff_pfxNN: 對應的索引列之不重複值。
* ### 定期更新統計資料
    * ### 系統變數 innodb_stats_auto_recalc
        * ### 決定伺服器是否自動重新計算統計資料。
        * ### 預設為 ON。
        * ### 當發生變動的記錄數量超過表大小的百分之 10，就會重新計算並更新上述兩表。
        * ### 統計資料表的更新是非同步的，也就是會有延遲。
    * ### 手動呼叫 ANALYZE TABLE 更新統計資訊 (立即重新計算)
        ```
        ANALYZE TABLE table_name;
        ```
    * ### 如果真的有需求，也可以手動設定。
        ```
        # 指定修改值
        UPDATE innodb_table_stats
        SET n_rows = 1
        WHERE table_name = 'table name';

        # 刷新
        FLUSH TABLE table_name
        ```
    * ### 註: InnoDB 預設以表為單位收集和儲存統計資料，可以針對不同的表設定獨立的 innodb_stats_auto_recalc。
* ### 基於記憶體的非永久性統計資料
    * ### 取樣的頁面數量由系統變數 innodb_stats_transient_sample_pages 控制，預設為 8。
    * ### 因重新計算頻率增加，可能導致執行計畫的生成結果經常不同。
    * ### MySQL 基本上不太使用此種方法。
* ### innodb_stats_method 的使用 (NULL 在不重複值計算上的策略)
    * ### 值為 nulls_equal: 預設值，所有的 NULL 是相等的。
    * ### 值為 nulls_unequal: 所有的 NULL 是不相等的。
    * ### 值為 nulls_ignored: 忽略 NULL 值。
<br />
