Chapter19 說過的話就一定要做到 -- redo 記錄檔
=====
* ### 如何保證交易的持久性 ? 有一個粗暴的做法，只要交易提交就刷新到磁碟...
    * ### 刷新一個完整的資料頁太浪費了，InnoDB 以頁為單位進行磁碟 I/O 讀取，如果只是修改了一個位元組，就要刷新 16 KB 的資料到磁碟上，不要鬧了。
    * ### 隨機 I/O 會是一個問題，一行敘述可能修改到多個頁面，而頁面在物理上不一定相連的，隨機 I/O 遠比順序 I/O 要來得慢，尤其是在機械硬碟上更是明顯。
* ### 其實只要讓提交的交易對資料庫中資料所做的修改能夠永久生效即可，達到即便系統崩潰也能恢復的目標即可，沒有必要頻繁刷新頁面，僅需記錄修改內容。
* ### 每當交易提交時，只刷新修改的記錄到磁碟中。
* ### 記錄著交易修改內容的的檔案，被稱為 "重作記錄檔 (redo log)"，也稱為 "redo 記錄檔"。
* ### 僅刷新 "redo 記錄檔" 而非 "資料頁" 的好處:
    * ### redo 記錄檔佔用空非常小 (基本只有表格空間 ID、頁號、偏移量與更新值)。
    * ### redo 記錄檔是順序寫入磁碟的 (這意味著 順序 I/O)。
* ### redo 記錄檔格式
    ```
    (type)(space ID)(page number)(offset)(data)
    ```
    * ### type: redo 記錄檔類型 (MySQL 5.7.22 版中 InnoDB 共有 53 種類型)
    * ### space ID: 表格空間 ID。
    * ### page number: 頁號。
    * ### offset: 表頁面中的偏移量。
    * ### data: redo 記錄檔具體內容。
* ### 先來看一個案例
    * ### 如果沒有為某個表顯性的定義主鍵，且表中也沒有定義不允許儲存 NULL 值的 UNIQUE 鍵，那麼 InnoDB 會為表增加一個名為 row_id 的隱藏列作為主鍵。
    * ### 資料庫伺服器在記憶體中維護一個 "全域變數"。
    * ### 每當包含 row_id 隱藏列的表中插入一筆記錄，就將全域變數值作為 row_id 列值，並把 "全域變數" 加 1。
    * ### 每當 "全域變數" 為 256 的倍數，就將該變數刷新到系統表格空間頁號為 7 的頁面中一個名為 Max Row ID 的屬性 (避免頻繁寫入磁碟，"Max Row ID" 相關敘述可參考 Chapter09)。
    * ### 當系統啟動時，會將 Max Row ID 載入到記憶體中，並將該值加上 256 後指定給 "全域變數" (因為如果上次關機時，"全域變數" 並非 256 的倍數未被刷新至磁碟)。
    * ### 此案例會在 Buffer Pool 中完成，InnoDB 會針對此次修改以 redo 格式記錄。
    * ### 當交易提交後，即使系統崩潰，也可以將頁面恢復成崩潰前的狀態。
    * ### 上述的 redo 記錄檔非常簡單，就是某個頁面的某個偏移量的位置修改了幾個位元組的值以及具體修改內容。
    * ### 這種簡單的 redo 記錄檔被稱為物理記錄檔。
* ### redo 記錄檔根據在頁面中寫入的資料量劃分了幾種不同的類型
    * ### MLOG_1BYTE: 表示在頁面的某個偏移量處寫入了 1 位元組的 redo 記錄檔類型。
    * ### MLOG_2BYTE: 表示在頁面的某個偏移量處寫入了 2 位元組的 redo 記錄檔類型。
    * ### MLOG_4BYTE: 表示在頁面的某個偏移量處寫入了 4 位元組的 redo 記錄檔類型。
    * ### MLOG_8BYTE: 表示在頁面的某個偏移量處寫入了 8 位元組的 redo 記錄檔類型。
    * ### MLOG_WRITE_BYTE: 表示在頁面的某個偏移量處寫入一個位元組序列。
    * ### 前述的 Max Row ID 是使用 MLOG_8BYTE 類型。
    * ### 除了 MLOG_WRITE_BYTE 外，其餘類型格式大致相同，只是具體資料包含的位元組數不同而已。
    * ### MLOG_WRITE_BYTE 類型記錄檔格式如下 (多了一個 len 欄位記錄佔用位元組量)
        ```
        (type)(space ID)(page number)(offset)(len)(data)
        ```
    * ### MLOG_WRITE_BYTE 看似可以通用，但是，佔空間啊孩子。
* ### 執行一行敘述可能會修改多張頁面，包含系統資料頁面與使用者資料頁面 (也就是聚簇索引和二級索引對應的 B+ 樹)。
* ### 敘述對 B+ 樹所做的更新
    * ### 表中包含多少個索引，一筆 INSERT 敘述就可能更新多少棵 B+ 樹。
    * ### 針對某一顆 B+ 樹而言，既可能更新葉子節點頁面，也可能更新內節點頁面，甚至發生新頁面申請 (頁面分裂) 操作。
* ### 在將記錄插入到索引時，即便不用進行頁面分裂，除了更新該葉子節點的頁面記錄 (MLOG_WRITE_BYTE) 外，還有 File Header、Page Header、Page Directory 等部分。
* ### 這意味著，每往葉子節點代表的資料頁中插入一筆記錄，還有一堆東西要更新:
    * ### 可能更新 Page Directory 中的 slot 資訊。
    * ### 可能更新 Page Header 各種頁面統計資訊。
        * ### PAGE_N_DIR_SLOTS: 槽數量。
        * ### PAGE_HEAP_TOP: 未使用空間最小位址。
        * ### PAGE_N_HEAP: 當頁記錄數量。
        * ### 還有很多呢...
    * ### 還有，資料頁中的記錄按照索引由小到大排序病透過單向鏈結串列組成，插入一筆記錄還需要更新上一筆記錄的 next_record 屬性。
* ### 總之，將一筆記錄插入頁面，要修改很多很多地方，若僅使用上述的 redo 記錄檔類型作記錄，可以有以下兩種作法:
    * ### 在每個修改的地方都記錄一筆 redo 記錄檔，不過這可能造成 redo 記錄檔佔用的空間比整個頁面佔用的空間還多 (太多地方要修改了)。
    * ### 將整個頁面的第一個被修改的位元組到最後一個被修改的位元組之間的資料當成一筆物理 redo 記錄檔中的具體資料 (這麼浪費空間要不乾脆直接更新一整頁算了)。
* ### 為因應上述問題，InnoDB 工程師提出了些新的 redo 記錄檔類型 (下省略 MLOG_ 前綴)
    * ### REC_INSERT: 插入一筆非緊湊行格式 (REDUNDANT) 記錄。
    * ### COMP_REC_INSERT: 插入一筆緊湊行格式 (COMPACT、DYNAMIC、COMPRESSED) 記錄。
    * ### COMP_PAGE_CREATE: 創建一個儲存緊湊行格式記錄頁面。
    * ### COMP_REC_DELETE: 刪除一筆緊湊行格式記錄。
    * ### COMP_LIST_START_DELETE: 刪除頁面中一系列使用緊湊行格記錄。
    * ### COMP_LIST_END_DELETE: 刪除一系列記錄直到 COMP_LIST_END_DELETE 為止 (與 COMP_LIST_START_DELETE 呼應)。
    * ### ZIP_PAGE_COMPRESS: 壓縮一個資料頁。
* ### redo 記錄檔的兩個層面
    * ### 物理: 指名對表格空間的哪個頁進行修改。
    * ### 邏輯: 系統崩潰重啟後，呼叫預先準備函數，後透過 redo 記錄檔恢復系統至崩潰前狀態。
* ### MLOG_COMP_REC_INSERT 記錄檔結構
    ```
    (type)(space ID)(page number)(n_fields)(n_uniques)(field1_len)(field2_len)(...)(fieldn_len)(offset)(end_seg_len)(一些記錄標頭資訊)(extra_size)(mismatch index)(記錄的真實資料)

    n_fields: 該筆記錄欄位數量。
    n_uniques: 決定該筆記錄唯一欄位數量。
    field＿len: 各個欄位佔用儲存空間大小。
    offset: 前一筆記錄地址。
    end_seg_len: 透過此欄位計算目前記錄總共佔用儲存空間大小。
    一些記錄標頭資訊: 表示記錄標頭的前 4 位元 (info bits) 的值及 record_type 的值。
    extra_size: 額外資訊佔用儲存空間大小。
    mismatch index: 為節省 redo 記錄檔大小而存在的欄位，嘿嘿。
    ```
    * ### n_uniques 表示在一筆記錄中，需要多少欄位才能確保記錄唯一性，如此在插入一筆記錄時，可以按照前 n_uniques 欄位進行排序，聚簇索引的 n_uniques 為主鍵列數，二級索引 (包含唯一二級索引，因可能接受 NULL) 的 n_uniques 為索引列數 + 主鍵列數。
    * ### field＿len 為欄位佔用儲存空間大小，且無論是固定長度還是可變長度都要寫入。
    * ### end_seg_len 是一個魔法，有效減少直接記錄儲存空間佔用大小所佔用的大小。
    * ### mismatch index 也是一種魔法...。
* ### redo 記錄檔格式小節
    * ### 把交易在執行過程中對資料庫所做的所有修改都記錄下來。
    * ### 用於系統崩潰後的恢復作業。
* ### 在執行敘述的過程中產生的 redo 記錄檔是 "不可分割的"。
    * ### 更新 Max Row ID 產生的 redo 記錄檔為一組。
    * ### 向聚簇索引對應的 B+ 樹插入一筆記錄產生的 redo 記錄檔為一組。
    * ### 向二級索引對應的 B+ 樹插入一筆記錄產生的 redo 記錄檔為一組。
* ### 插入記錄時，在定位完該筆記錄的插入位置後:
    * ### 資料頁剩餘空間充足 (樂觀插入)，直接插入 (後生成 MLOG_COMP_REC_INSERT)。
    * ### 資料頁剩餘空間不足 (悲觀插入)，執行頁分裂，將原先資料頁一部分記錄 (約一半左右，類似 Chapter05 中操作) 複製到新資料頁，再將新記錄插入，還有一些針對新申請頁面相關操作 (放入葉節點鏈結串列、增加目錄項等)，後產生非常多 redo 記錄檔 (二三十筆)。
* ### redo 記錄檔為 "不可分割的" 並以組的方式呈現，可以保持原子性。
* ### 一組 redo 記錄檔最後會加上一筆特殊類型 redo 記錄檔，名為 "MLOG_MULTI_REC_END"，其只有一個 type 欄位。
* ### 在進行重啟恢復時，只有解析到 MLOG_MULTI_REC_END 才算解析一組完整的 redo 記錄檔，否則就放棄該組恢復。
* ### 獨自一筆就可以進行恢復的 redo 記錄檔，檔頭中的 type 第一個位元會為 1，否則就是系列 (組) 的記錄檔。
* ### Mini - Transaction 概念
    * ### 對底層頁面進行一次原子存取的過程稱為一個 Mini - Transaction (MTR)。
    * ### 一個 MTR 包含一組不可分割的 redo 記錄檔。
    * ### 一筆交易有多句敘述，一句敘述包含多個 MTR，一個 MTR 包含多項 redo 記錄檔。
* ### redo log block
    * ### 透過 MTR 生成的 redo 記錄檔被存放在大小為 512 位元組的頁中，這種頁稱為 "block"。
    * ### redo log block 結構
        ```
        (log block header)(log block body)(log block trailer)

        log block header: 管理資訊。
        log block body: 共 496 位元組以儲存 redo 記錄檔。
        log block trailer: 管理資訊。
        ```
    * ### log block header
        * ### LOG_BLOCK_HDR_NO: 編號。
        * ### LOG_BLOCK_HDR_DATA_LEN: 以使用位元組數，初始為 12，寫滿為 512。
        * ### LOG_BLOCK_FIRST_REC_GROUP: 一筆 redo 記錄檔可稱為一筆 redo 記錄檔記錄 (redo log record)，一個 MTR 會生成多筆 redo 記錄檔記錄，被稱為記錄檔記錄組 (redo log record group)，LOG_BLOCK_FIRST_REC_GROUP 表示第一個 redo log record group 偏移量。
        * ### LOG_BLOCK_CHECKPOINT_NO: checkpoint 序號。
        * ### LOG_BLOCK_CHECKSUM: block 驗證值。
* ### redo 記錄檔緩衝區
    * ### redo 記錄檔也不是直接寫入磁碟。
    * ### 伺服器啟動時會向作業系統申請一大片稱為 "redo log buffer (redo 記錄檔緩衝區)" 的連續記憶體空間，簡稱 log buffer (被劃分成許多連續的 redo log block)。
    * ### 可以透過啟動選項 innodb_log_buffer_size 指定大小，預設為 16 MB。
* ### redo 記錄檔寫入 log buffer
    * ### 順序寫入。
    * ### 透過 buf_free 全域變數定位 redo 記錄檔應寫入 block 哪個偏移量位置。
    * ### 一次是插入一組 redo 記錄檔 (在這之前會先暫存於某處)。
    * ### 不同交易可能併發執行，所以不同交易 MTR 對應的 redo 記錄檔組可以是交替寫入的。
* ### redo 記錄檔寫入磁碟時機
    * ### log buffer 空間不足: 當前寫入 log buffer 的 redo 記錄檔量已經佔滿 log buffer 總量的 50 % 左右，就會進行刷新。
    * ### 交易提交時: 為了保持持久性。
    * ### 後臺執行緒約每秒刷新一次。
    * ### 伺服器被正常關閉。
    * ### 做 checkpoint 時。
* ### redo 記錄檔組
    * ### log buffer 記錄檔預設是被刷新到 MySQL 資料目錄下的 ib_logfile0 和 ib_logfile1 檔案中。
    * ### innodb_log_group_home_dir: 指定 redo 記錄檔所在目錄，預設為資料目錄。
    * ### innodb_log_file_size: 每個 redo 記錄檔大小，預設為 48 MB。
    * ### innodb_log_files_in_group: 指定 redo 記錄檔個數，預設為 2 最大 100。
    * ### ib_logfile0 寫滿了寫 ib_logfile1，ib_logfile1 寫滿了回去寫 ib_logfile0。
    * ### redo 記錄檔總大小為 ```innodb_log_file_size x innodb_log_files_in_group```。
    * ### 按照寫入邏輯，"追尾" 會造成 "覆蓋"，所以有了 checkpoint 概念。
* ### redo 記錄檔格式
    * ### redo 記錄檔每個檔案大小相同，格式也相同。
    * ### 前 2048 位元組為管理資訊。
    * ### 2048 位元組後為 log buffer 中的 block 映像檔。
    * ### 前 2048 位元組包含: log file header、checkpoint1、沒用、checkpoint2。
    * ### log file header 為該 redo 記錄檔整體屬性 (版本、lsn、創建者、驗證值)。
    * ### checkpoint1 為 checkpoint 屬性 (編號、lsn、上個屬性 lsn 偏移量、執行 checkpoint 操作對應 log buffer 大小、驗證值)。
    * ### checkpoint2 與 checkpoint1 相同。
    * ### 註: checkpoint 只儲存在 redo 記錄檔組的第一個記錄檔中。
* ### lsn, log sequence number (詳細內容請參閱書籍 19-27 頁)
    * ### lsn 為全域變數，用於記錄總共寫入的 redo 記錄檔量。
    * ### 預設為 8704。
    * ### buf_free 是位置、lsn 是量。
    * ### buf_free 和 lsn 是一起長大的。
    * ### 結論: "lsn 越小，說明 redo 記錄檔產生的越早"，這才是 "重點"。
* ### flushed_to_dosk_lsn (詳細內容請參閱書籍 19-30 頁)
    * ### 用於標記當前 log buffer 已經有哪些記錄被刷新到記錄檔中。
    * ### 也就是表示刷新到磁碟中的 redo 記錄檔量。
    * ### 系統第一次啟動時，flushed_to_dosk_lsn 與 lsn 相同。
    * ### 慢慢的就同了，嘿嘿。
* ### flush 鏈結串列中的 lsn (詳細內容請參閱書籍 19-32 頁)
    * ### 在 MTR 執行過程中修改的頁面會被加入 Buffer Pool 的 flush 鏈結串列。
    * ### 控制區塊中也記錄了以下兩項資訊:
        * ### oldset_modification: 第一次修改 Buffer Pool 某個緩衝頁時，會將該頁面的 MTR 開始對應的 lsn 寫入。
        * ### newest_modification: 每修改一次頁面該頁面 MTR 結束時對應 lsn 會被寫入。
    * ### 結論: flush 鏈結串列中的髒頁會按照第一次修改發生的時間順序排序，也就是按照 oldset_modification 排序，被多次修改的頁面不會被重複插入，只會被更新 newest_modification。
* ### checkpoint (詳細內容請參閱書籍 19-35 頁)
    * ### 當對應髒頁已經寫入磁碟，則該 redo 記錄檔就沒用了。
    * ### 判斷 redo 記錄檔是否為可覆蓋，就是判斷髒頁是否已經被刷新至磁碟。
    * ### 全域變數 checkpoint＿lsn 用於表示當前系統可被覆蓋的 redo 記錄檔總量。
    * ### checkpoint＿lsn 初始值也是 8704。
* ### 查看 lsn
    ```
    SHOW ENGINE INNODB STATUS\G
    ```
    * ### Log sequence number: lsn。
    * ### Log flushed up to: flush_to_disk。
    * ### Pages flushed up to: oldest_modification。
    * ### Last checkpoint at: checkpoint_lsn。
* ### innodb_flush_log_at_trx_commit 用法
    * ### 為了保證持久性，真的把交易過程中產生的所有 redo 記錄檔都刷新到磁碟，說實話，挺累 der。
    * ### innodb_flush_log_at_trx_commit 的值與解釋如下。
    * ### 0: 不立即同步，後台自行處理，可以用於加速，但伺服器掛了沒寫入的就掰了。
    * ### 1: 提交交易就刷新。
    * ### 2: 提交交易寫入緩衝區，資料庫掛了作業系統沒掛就是虛驚一場，都掛了就...耗子尾汁。
* ### 崩潰恢復 (詳細內容請參閱書籍 19-41 頁)
    * ### 資料庫沒掛 redo 記錄檔就跟你一樣，一點用都沒有，資料庫掛了，redo 記錄檔就跟你不一樣，非常有用。
    * ### 恢復過程: 確定恢復起點 > 確定恢復終點 > 怎麼恢復 (雜湊表) > 跳過已刷新頁面。
* ### LOG_BLOCK_HDR_NO 計算方式
    ```
    LOG_BLOCK_HDR_NO = ((lsn / 512) & 0x3FFFFFFF) + 1
    ```
<br /> 
