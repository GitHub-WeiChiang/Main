Chapter09 存放頁面的大池子 -- InnoDB 的表格空間
=====
* ### 表格空間是一個抽象概念。
    * ### 系統表格空間: 對應檔案系統中一個或多個檔案。
    * ### 獨立表格空間: 對應檔案系統中一個名為 ".bd" 的實際檔案。
    * ### 可視為被切分成許多個頁的池子，插入記錄時從池子中撈出對應頁並寫入。
* ### 頁面的類型 (以下省略 "FILE_PAGE_" 前綴)
    * ### TYPE_ALLOCATED: 未使用。
    * ### UNDO_LOG: undo 記錄頁。
    * ### INODE: 儲存段的資訊。
    * ### IBUF_FREE_LIST: Change Buffer 空閒列表。
    * ### IBUF_BITMAP: Change Buffer 屬性。
    * ### TYPE_SYS: 系統資料。
    * ### TYPE_TRX_SYS: 交易系統資料。
    * ### TYPE_FSP_HDR: 表格空間表頭資訊。
    * ### TYPE_XDES: 儲存區屬性。
    * ### TYPE_BLOB: 溢位頁。
    * ### INDEX: 索引頁 (資料頁)。
* ### 頁面通用部分
    * ### File Header: 頁面通用資訊。 (以下省略 "FILE_PAGE_" 前綴)
        * ### SPACE_OR_CHKSUM: checkssum 校正碼 (MySQL 4.0.14 以下的版本此屬性用於表示表格空間 ID)。
        * ### OFFSET: 頁號。
        * ### PREV: 上一頁頁號 (主要用於 INDEX 頁)。
        * ### NEXT: 下一頁頁號 (主要用於 INDEX 頁)。
        * ### LSN: 該頁面最後修改對應的 LSN (Log Squence Number)。
        * ### TYPE: 頁面類型。
        * ### FILE_FLUSH_LSN: 僅在系統表格空間的第一個頁中定義，代表檔案至少被刷新到了對應的 LSN (Log Squence Number)。
        * ### ARCH_LOG_NO_OR_SPACE_ID: 該頁屬於哪一個表格空間。
    * ### File Trailer: 驗證頁面完整性 (記憶體刷新至磁碟內容是否相同)。
    * ### 表格空間中的每一個頁都對應著一個頁號，頁號在表格空間中可以快速定位到指定的頁面。
    * ### 某些類型的頁可以組成鏈結串列 (雙向)，鏈結串列中相鄰的兩個頁面的頁號可以不連續，也就是可以不按照表格空間中的物理位置相鄰儲存。
* ### 獨立表格空間結構
    * ### 1 組: 256 區。
    * ### 1 區: 64 頁 (1 M)。
    * ### 1 頁: 16 KB。
    * ### 頁 > 區 > 組。
    * ### 段 (邏輯概念): 區的集合 (葉子區集合 & 非葉子區集合) + 存在於碎片區的零散頁。
    * ### 碎片區 (區的一種): 含不同段的頁。
    * ### 區 (extent) 的概念
        * ### 用於管理頁。
        * ### 連續 64 個頁是一個區。
        * ### 一個區佔用 1 MB 大小。
        * ### 表格空間由多個連續的區組成。
        * ### 256 個區被劃分成一組。
    * ### 第一個組的前三個頁面是固定的
        * ### FSP_HDR: 包含整個表格空間的整體屬性與本組所有的區的屬性 (一個表格空間只有一個 FSP_HDR)。
        * ### IBUF_BITMAP: 儲存關於 Change Buffer 資訊。
        * ### INODE: 儲存許多 INODE Entry 資料結構。
    * ### 其餘組前兩個頁面類型是固定的
        * ### XDES (Extent Descriptor): 登記本組 256 個區的屬性 (與 FSP_HDR 類似但不包含額外屬於表格空間的屬性)。
        * ### IBUF_BITMAP: 儲存關於 Change Buffer 資訊。
    * ### 講了這麼多，記住，表格空間被劃分為許多連續的區，每個區預設由 64 個頁組成，每 256 個區劃分為一組，每組的前幾個頁面類型是固定的。
* ### 段的概念
    * ### 如果雙向鏈結串列的兩個頁在實體物理位置上不連續甚至距離非常遠，所產生的隨機 I/O 所造成磁碟的效能影響會非常可觀 (尤其是傳統機械硬碟)，應盡可能使相鄰的頁在物理位置上也相鄰。
    * ### 區 (extent) 是在物理位置上連續的 64 個頁，當資料量很大時，將以一個區或數個區為單位進行硬碟空間分配，進而消除隨機 I/O (當然會耗費一些記憶體，不過...空間換取時間嘛)。
    * ### 葉子節點有自己獨立的區，非葉子節點有自己獨立的區，它們各自的集合都算是一個段 (segment)。
    * ### 所以，一個索引會產生兩個段，"葉子節點段" 與 "非葉子節點段"。
    * ### 預設下，InnoDB 會為一張表產生一個聚簇索引，一個索引有兩個段，而段已區為單位申請儲存空間，一個區佔用 1 MB 空間。
    * ### 理論上，一個區會完全屬於某一個段 (不過當資料量不大的時候，太浪費了)。
    * ### 碎片 (fragment) 區: 解決上述問題，一個碎片區中的頁，彼此是屬於不同的段的，碎片區直屬於表格空間。
        * ### 剛開始插入資料至表中時，段是從某個碎片區以頁為單位分配儲存空間。
        * ### 當佔用 32 個碎片區的頁後，就會以完整的區為單位分配儲存空間，但原本存在於碎片區的資料依舊存在，並不會被移動。
* ### 區的分類
    * ### 空閒的區 (FREE): 沒用到這個區的任何頁面 (獨立直屬表格空間)。
    * ### 有剩餘空閒頁的碎片區 (FREE_FRAG): 還有可被分配的空閒頁 (獨立直屬表格空間)。
    * ### 沒剩餘空閒頁的碎片區 (FULL_FRAG): 沒有可被分配的空閒頁 (獨立直屬表格空間)。
    * ### 附屬於某個段的區 (FSEG): 就...附屬於某個段的區... (屬於某個段)。
* ### XDES Entry (Extent Descriptor Entry) 結構 (方便管理區)
    * ### 一個區對應一個 XDES Entry。
    * ### 由四個部分組成 (按序依次為): Segment ID + List Node + State + Page State Bitmap。
    * ### Segment ID: 段的唯一編號，表示該區所在的段，前提是該區是屬於某一個段。
    * ### List Node: 用於將多個 XDES Entry 組成鏈結串列 (包含以下結構)。
        * ### Prev Node Page Number
        * ### Prev Node Offset (此兩組合是指向前一個 XDES Entry 的指標)
        * ### Next Node Page Number
        * ### Next Node Offset (此兩組合是指向後一個 XDES Entry 的指標)
    * ### State: 表明區的狀態 (FREE, FREE_FRAG, FULL_FRAG, FSEG)。
    * ### Page State Bitmap: 對應區中的 64 個頁 (一個對應佔用兩個位元，第一個位元用於表示對應的頁是否為空閒，第二個位元是冗員，跟我一樣沒用)。
* ### XDES Entry 鏈結串列
    * ### 申請頁面的過程 (插入資料時)
        * ### 資料量少，檢查表格空間是否有狀態為 FREE_FRAG 的區，有就插入。
        * ### 否則申請一個狀態為 FREE 的區，把它變成 FREE_FRAG，取一個零散頁插入。
        * ### 之後不同段所使用的零散頁就從上面申請的區中取得，直到沒有空閒頁，該區狀態就會變成 FULL_FRAG。
    * ### 透過 XDES Entry 的 List Node 可以判斷區的狀態。
        * ### 狀態為 FREE 的區對應的 XDES Entry 會是一個 FREE 鏈結串列。
        * ### 狀態為 FREE_FRAG 的區對應的 XDES Entry 會是一個 FREE_FRAG 鏈結串列。
        * ### 狀態為 FULL_FRAG 的區對應的 XDES Entry 會是一個 FULL_FRAG 鏈結串列。
        * ### 狀態的改變意味著所對應的 XDES Entry 會被移動到相應的鏈結串列。
    * ### 如何知道區屬於哪一個段
        * ### 針對每個段中的區對應的 XDES Entry 結構建立 3 個鏈結串列。
        * ### FREE 鏈結串列: 同一個段中所有頁面都是空閒頁的區對應的 XDES Entry 會被加進來。
        * ### NOT_FULL 鏈結串列: 仍有空閒頁面的區對應的 XDES Entry 會被加入。
        * ### FULL 鏈結串列: 沒有空閒頁面的區對應的 XDES Entry 會被放到這。
        * ### 記住，一個索引會有兩個段，每個對都會維護上述三個鏈結串列。
    * ### 鏈結串列的基節點
        * ### List Base Node 結構用於找到某個鏈結串列的頭尾節點。
        * ### 結構依序為: List Length + First Node Page Number + First Node Offset + Last Node Page Number + Last Node Offset。
        * ### List Length: 有多少個節點。
        * ### 後兩兩一組，分別表示該鏈結串列頭與尾節點在表格空間中的位置。
    * ### 小結
        * ### 表格空間由區組成，每個區對應一個 XDES Entry 結構。
        * ### 直屬表格空間的區對應的 XDES Entry 結構可分為 FREE、FREE_FRAG、FULL_FRAG 三個鏈結串列。
        * ### 段可以擁有許多區，每個段中的區對應的 XDES Entry 結構可分為 FREE、NOT_FULL、FULL 三個鏈結串列。
        * ### 每個鏈結串列對應一個 List Base Node，記錄了節點數與該鏈結串列頭與尾節點在表格空間中的位置。
* ### 段的結構
    * ### 段是邏輯概念，由零散頁及完整區組成，每個區都有對應的 XDES Entry。
    * ### 而每個段都被定義了一個 INODE Entry，結構如下:
        * ### Segment ID: 該 INODE Entry 對應的段編號。
        * ### NOT_FULL_N_USED: NOT_FULL 鏈結串列中使用頁面數。
        * ### List Base Node: 分別為 FREE、NOT_FULL、FULL 定義了各自的 List Base Node，用於對應。
        * ### Magic Number: 標記 INODE Entry 是否被初始化。
        * ### Fragment Array Entry: 段是邏輯概念，由零散頁及完整區組成，每一個 Fragment Array Entry 都對應一個零散頁面。
* ### 各類型頁面詳細情況 (詳細內容參閱書籍 9-16 頁)
    * ### FSP_HDR 類型: 第一個組的第一個頁面類型，也是表個空間的第一個頁面，頁號為 0，儲存表格空間整體屬性與第一個組內 256 個區對應的 XDES Entry 結構。
    * ### XDES 類型: 其餘組的第一個頁面類型，沒有記錄表格空間整體屬性，其餘與 FSP_HDR 相同。
    * ### IBUF_BITMAP 類型: 每個組的第二個頁面類型，記錄有關 Change Buffer 資訊 (修改非唯一二級索引頁面時，若該頁面尚未被載入記憶體，修改會先被暫時快取到 Change Buffer)。
    * ### INODE 類型: 此類型頁面用於儲存 INODE Entry 結構。
* ### Segment Header (用於建立索引和對應的段之間關係)
    * ### 結構
        * ### Space ID of the INODE Entry: INODE Entry 所在表格空間 ID。
        * ### Page Number of the INODE Entry: INODE Entry 所在頁面頁號。
        * ### Byte Offset of the INODE Entry: INODE Entry 在該頁面中偏移量。
    * ### Page Header 中包含 PAGE_BTR_SEG_LEAF (葉子節點段表頭資訊，僅在 B+ 樹的根頁中定義) 與 PAGE_BTR_SEG_TOP (非葉子節點段表頭資訊，僅在 B+ 樹的根頁中定義)，分別各自對應一個 Segment Header 結構。
* ### 真實表格空間是自擴充的，所以覺得足夠儲存上面提到的資訊。
* ### 系統表格空間 (詳細內容參閱書籍 9-26 頁)
    * ### 整個 MySQL 處理程序只有一個系統表格空間。
    * ### 系統表格空間記錄一些與整個系統相關的資訊。
    * ### 它是大哥，表格空間 ID 為 0。
    * ### 特有頁面 (頁號、類型、描述)
        * ### 3, SYS, Insert Buffer Header, 儲存 Change Buffer 表頭資訊。
        * ### 4, INDEX, Insert Buffer Root, 儲存 Change Buffer 根頁面。
        * ### 5, TRX_SYS, Transaction System, 交易系統相關資訊。
        * ### 6, SYS, First Rollback Segment, 第一個回覆段資訊。
        * ### 7, SYS, Data Dictionary Header, 資料字典表頭資訊。
    * ### InnoDB 資料字典
        * ### 插入資料時，需要進行很多驗證，例如: 表是否存在、插入格式是否符合、聚簇索引與所有二級索引對應的跟頁面在表格空間的哪個頁面。
        * ### 因此除需保存使用者資料還需額外保存許多資訊 (列數、列類型、索引相關資訊、外鍵相關資訊、檔案路徑)。
        * ### 為了近一步管理上述資訊 (也稱為中繼資料)，InnoDB 定義了一系列內部系統表 (internal system table) 來記錄。
    * ### 內部系統表 (internal system table)，以下省略表名前綴 SYS_。
        * ### TABLES: 所有表資訊。
        * ### COLUMNS: 所有列資訊。
        * ### INDEXES: 所有索引資訊。
        * ### FIELDS: 所有索引對應的列的資訊。
        * ### FOREIGN: 所有外鍵資訊。
        * ### FOREIGN_COLS: 所有外鍵對應的列的資訊。
        * ### TABLESPACES: 所有表格資訊。
        * ### DATAFILES: 所有表格對應檔案系統的檔案路徑資訊。
        * ### VIRTUAL: 所有虛擬生成的列的資訊。
        * ### 前四項被稱為基本系統表 (basic system table)，也可以稱為 "表中之表"，較為重要，書中有詳細說明。
        * ### 表中之表的資訊是強制寫入程式中的，它們所對應的 B+ 樹位置被記錄在頁號為 7 的頁面 Data Dictionary Header 結構中，頁面類型是 SYS。
    * ### Data Dictionary Header 重要欄位 (其餘欄位請參閱書籍)
        * ### Max Row ID: 當不顯性定義主鍵時，表中也沒有不允許儲存 NULL 值的 UNIQUE 鍵，InnoDB 會預設生成一個名為 row_id 的列作為主鍵，Max Row ID 用於達成 row_id 生成的功能。
<br />
