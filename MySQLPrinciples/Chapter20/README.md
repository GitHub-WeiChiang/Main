Chapter20 後悔了怎麼辦 -- undo 記錄檔
=====
* ### 後悔了怎麼辦 ? 後悔了活該啦，後悔了怎麼辦。
* ### 破壞原子性的原因
    * ### 伺服器錯誤、作業系統錯誤、斷電。
    * ### 被修人下了 ROLLBACK 指令。
* ### 怎麼辦呢 ? 為了保證原子性，要把此次交易的改動都改回去，好像什麼事都沒發生一樣，這個操作也稱為 "回覆"。
* ### 做事留一手，做人也一樣。
    * ### 插入: 記錄主鍵，回覆時刪除。
    * ### 刪除: 記錄內容，回覆時插入。
    * ### 修改: 記錄舊值，回覆時更新。
* ### 為了回覆而記錄的東西，稱之為 "取消記錄檔 (undo log)"，也稱 "undo 記錄檔"。
* ### SELECT 操作是沒有對應的 undo 記錄檔的。
* ### 分配交易 id 的時機
    * ### 當該交易執行了增刪改操作，就會被分配一個獨一無二的交易 id。
    * ### 即便是唯讀交易，對臨時表進行增刪改，也會被分配 id。
    * ### 但如果是 SELECT 敘述執行時，使用到內部臨時表，並不會被分配 id。
    * ### 即便是開啟讀寫交易，沒有執行增刪改操作，就不會被分配 id。
* ### 交易 id 生成方式: 與 row_id 大致相同，由系統表格空間頁號為 5 的屬性 "Max Trx ID" 管理。
* ### 聚簇索引中記錄的行格式隱藏列也包過以下項目
    * ### trx_id: 交易 id。
    * ### rill_pointer: 稍後說明。
* ### undo log 從編號 0 開始，並被記錄於 FIL_PAGE_UNDO_LOG 頁面中。
* ### INSERT 操作對應的 undo 記錄檔結構 (詳細內容請參閱書籍 20-6 頁)
    * ### end of record: 此記錄檔結束，下一筆記錄檔開始的位址。
    * ### undo type: "TRX_UNDO_INSERT_REC"。
    * ### undo no: 編號。
    * ### table id: 記錄檔對應記錄所在 table id。
    * ### 主鍵各列資訊 (len, value) 列表: 主鍵每個列佔用空間大小與值。
    * ### start of record: 上一筆記錄檔結束，本筆記錄檔開始的位址。
* ### "roll_pointer" 本質上是一個指向記錄對應 undo log 的指標 (只需要針對 "聚簇索引" 來記錄 undo log)。
* ### DELETE 操作對應的 undo 記錄檔 (詳細內容請參閱書籍 20-9 頁)
    * ### 被刪除的記錄也會被串成鏈結串列，稱為 "垃圾鏈結串列"。
    * ### 刪除二階段
        * ### 將 deleted flag 標示為 1，這個操作稱為 delete mark。
        * ### 將該記錄加入垃圾鏈結串列 (當該刪除敘述所在交易被提交時)。
    * ### 結構
        * ### end of record
        * ### undo type: "TRX_UNDO_DEL_MARK_REC"。
        * ### undo no
        * ### table id
        * ### info bits: 記錄標頭資訊的前四個位元值。
        * ### trx_id: 舊記錄的 trx_id 值。
        * ### roll_pointer: 舊記錄的 roll_pointer 值。
        * ### 主鍵各列資訊 (len, value) 列表
        * ### len of index_col_info: 索引各列資訊和本部分佔用儲存空間大小。
        * ### 索引各列資訊 (len, value) 列表: 被索引的列的各列資訊。
        * ### start of record
* ### 每當新插入記錄時，首先判斷垃圾鏈結串列頭節點代表的已刪除紀錄所佔用的儲存空間是否足夠容納這筆新插入的紀錄，如果無法容納，就直接向頁面申請新的空間，來儲存這筆紀錄，並不會嘗試遍歷整個垃圾鏈結串聯，如果可以容納，那麼直接重用這筆已刪除紀錄的儲存空間。
* ### UPDATE 操作對應的 undo 記錄檔 (詳細內容請參閱書籍 20-17 頁)
    * ### 不更新主鍵
        * ### 就地更新 (in - place update): 更新前後所有列佔用 "空間大小一致"。
        * ### 先刪除舊記錄 (真刪除，不是 delete mark )，在插入新記錄。
    * ### 結構
        * ### end of record
        * ### undo type: "TRX_UNDO_UPD_EXIST_REC"。
        * ### undo no
        * ### table id
        * ### info bits
        * ### trx_id
        * ### roll_pointer
        * ### 主鍵各列資訊 (len, value) 列表
        * ### u_updated: 多少列被更新。
        * ### 被更新的列更新前資訊 (pos, old_len, old_value): 就是被更新的列更新前資訊。
        * ### len of index_col_info
        * ### 索引各列資訊 (len, value) 列表
        * ### start of record
    * ### 更新主鍵
        * ### 將舊記錄進行 delete mark 操作。
        * ### 將新記錄插入聚簇索引。
* ### 增刪改操作對二級索引的影響
    * ### INSERT 與 DELETE 就是像對聚簇索引列那樣。
    * ### UPDATE 敘述內容如果未涉及二級索引的列，就不會對二級索引有任何操作。
    * ### 相反的，先對舊記錄進行 delete mark 操作，後插入新記錄到二級索引對應的 B+ 樹中。
* ### 通用鏈結串列結構 (12 位元組)
    * ### Prev Node Page Number 和 Prev Node Offset 組合為指向前一節點的指標。
    * ### Next Node Page Number 和 Nexy Node Offset 組合為指向後一節點的指標。
    * ### 基節點多了 "List Length" 記錄總節點數。
* ### FIL_PAGE_UNDO_LOG 頁面 (Undo Page)
    * ### 儲存 undo log。
    * ### Undo Page Header (詳細內容請參閱書籍 20-25 頁)
        * ### TRX_UNDO_PAGE_TYPE
        * ### TRX_UNDO_PAGE_START
        * ### TRX_UNDO_PAGE_FREE
        * ### TRX_UNDO_PAGE_NODE
* ### 單一交易中的 Undo Page 鏈結串列
    * ### insert undo 鏈結串列 (FIL_PAGE_UNDO_LOG 組成)
    * ### update undo 鏈結串列 (FIL_PAGE_UNDO_LOG 組成)
    * ### 普通表與臨時表會各自維護上述鏈結串列。
    * ### 一個交易中最多有 4 個 Undo Page 組成的鏈結串列。
    * ### 有用到才會分配對應的鏈結串列。
    * ### 不同交易維護各自的 Undo Page 鏈結串列。
    * ### 第一個 Undo Page 稱為 first undo page，其餘的稱為 normal undo page。
* ### Undo Log Segment Header (詳細內容請參閱書籍 20-32 頁)
    * ### 一個 Undo 頁面鏈結串列對應一個段，稱為 Undo Log Segment。
    * ### "Undo Page 鏈結串列" 的 "第一個頁面 (first undo page)" 會具有 "Undo Log Segment Header"。
    * ### 結構
        * ### TRX_UNDO_STATE: Undo Page 鏈結串列狀態。
        * ### TRX_UNDO_LAST_LOG: 此 Undo Page 鏈結串列中最後一個 Undo Log Header 位置。
        * ### TRX_UNDO_FSEG_HEADER: 此 Undo Page 鏈結串列對應的段的 Segment Header 資訊。
        * ### TRX_UNDO_PAGE_LIST: Undo Page 鏈結串列基節點。
* ### Undo Log Header: 該組 Undo log 的屬性 (詳細內容請參閱書籍 20-34 頁)。
* ### 對沒有被重用的 undo page 鏈結串列來說，第一個頁面 (first undo page) 在真正寫入 undo 記錄檔前，會填充 undo page header、undo log segment header、undo log header 三個部分，之後才開始寫入 undo 紀錄檔，對於其它頁面 (normal undo page)，真正在寫入 undo log 前，只會填充 undo page header。
* ### 鏈結串列基節點存放到 first undo page 的 undo log segment header，鏈結串列節點資訊放到每一個 undo 頁面的 undo page header 部分。
* ### 重用 Undo Page (詳細內容請參閱書籍 20-37 頁)
    * ### 該鏈結串列中只包含一個 Undo Page。
    * ### 該 Undo 頁面已經使用的空間小於整個頁面空間的 3/4。
* ### undo page 鏈結串列可分為 insert 與 update 兩種，重用策略如下 (詳細內容請參閱書籍 20-38 頁)
    * ### insert undo 鏈結串列: 提交之後即可清除。
    * ### update undo 鏈結串列: 提交之後不可清除，需用於 MVCC。
* ### Rollback Segment Header (詳細內容請參閱書籍 20-40 頁)
    * ### 存放各個 Undo 頁面鏈結串列的 first undo page 頁號 (undo slot)。
    * ### 每個 Undo Page 鏈結串列都相當於是一個班，這個鏈結串列的 first undo page 就相當於這個班的班長，這些班長被召集在會議室，Rollback Segment Header 就是那個會議室。
<br /> 
