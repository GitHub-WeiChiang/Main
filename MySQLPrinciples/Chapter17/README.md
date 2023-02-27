Chapter17 調節磁碟和 CPU 的矛盾 -- InnoDB 的 Buffer Pool
=====
* ### 資料以頁的形式存放在表格空間中，表格空間是 InnoDB 對一個或多個實際檔案的抽象。
* ### 若需要存取某個資料頁，會將完整的頁從磁碟載入到記憶體 (即便只存取了一筆)。
* ### 載入記憶體的頁會被快取，不會在使用完後馬上被釋放，以節省 I/O 負擔。
* ### 什麼是 Buffer Pool
    * ### MySQL 伺服器啟動時會向作業系統申請一片連續記憶體，稱為 Buffer Pool (緩衝集區)。
    * ### 預設為 128 MB，由變數 innodb_buffer_pool_size 設定，單位為位元組。
* ### Buffer Pool 內部組成
    * ### Buffer Pool 被劃分成很多頁，大小與表格空間的頁相同 (16 KB)，稱為 "緩衝頁"。
    * ### 每一個 "緩衝頁" 都會創建一些控制資訊，包含表個空間編號、頁號、緩衝頁在 Buffer Pool 中的位址與鏈結串列節點資訊等。
    * ### 每個 "控制資訊" 佔用相同記憶體，該佔用區塊稱為 "控制區塊"，"控制區塊" 與 "緩衝頁" 相互一一對應。
    * ### "控制區塊" 位於 Buffer Pool 前面，"緩衝頁" 位於 Buffer Pool 後面，
    * ### Buffer Pool 結構如下:
        ```
        (控制區塊 1)(控制區塊 2)...(控制區塊 n)(碎片)(緩衝頁 1)(緩衝頁 2)...(緩衝頁 n)
        ```
    * ### "控制區塊" 大約佔用 "緩衝頁" 大小的百分之 5，而我們設定的 innodb_buffer_pool_size 並不包含 "控制區塊"，所以實際上，上述的連續記憶體空間會比所設定 innodb_buffer_pool_size 大 5 % 左右。
* ### free 鏈結串列的管理
    * ### 空閒的 "緩衝頁" 所對應的 "控制區塊" 會被作為一個節點放到一個鏈結串列中，稱為 "free 鏈結串列"。
    * ### 一開始所有的緩衝頁控制區塊都會被加入到 free 鏈結串列。
    * ### free 鏈結串列基節點結構: 頭節點、尾節點、節點數量等資訊。
    * ### "控制區塊" 中包含 pre 和 next 指標，所以這是一個 "雙向鏈結串列"。
    * ### 當需要從磁碟載入頁面至 Buffer Pool，就會從 free 鏈結串列中取出 (移出) 一個空閒 "緩衝頁" 對應的 "控制區塊"。
* ### 緩衝頁的雜湊處理
    * ### 判斷某頁是否在 Buffer Pool 中的方法。
    * ### 根據 "表格空間號" + "頁號" 進行定位 (key)。
    * ### 緩衝頁的控制區就是一個 value。
* ### flush 鏈結串列的管理
    * ### 被修改過的緩衝頁，因其內容與磁碟上對應的頁已經不同，該緩衝頁就被稱為 "髒頁 (dirty page)"。
    * ### 被修改過的緩衝頁 (髒頁) 並不會馬上被刷新到磁碟，而是在未來的某一個時間點被刷過去 (就像你現在沒有女朋友，在未來的某一個時間點也不會有...好像不太一樣)。
    * ### 如何知道 "緩衝頁" 是否為 "髒頁" 呢，這時候就出現了儲存髒頁的鏈結串列，被修改過的緩衝頁所對應的控制區塊就會被加入，稱之為 "flush 鏈結串列"。
    * ### flush 鏈結串列構造與 free 鏈結串列大致相同。
    * ### 如果 "緩衝頁" 是 "空閒" 的，那它就不可能是髒頁，如果一個緩衝頁是髒頁，那它就不會是空閒的 "緩衝頁"。
    * ### 總之，一個緩衝頁所對應的控制區塊，不可能同時存在於 free 和 flush 的鏈結串列中。
* ### 緩衝區不夠的窘境
    * ### 若當前需要快取的頁面大小超過了 free 鏈結串列中可用的空間 (空閒緩衝頁)，需要把舊的緩衝頁從 Buffer Pool 中移除。
* ### 簡單的 LRU 鏈結串列
    * ### 宗旨是，淘汰掉最近很少使用的緩衝頁。
    * ### 透過 LRU (Least Recently Used) 鏈結串列實作。
    * ### 如果該頁不在 Buffer Pool 中就將其載入，並將該頁對應的控制區塊作為節點塞到 LRU 的頭部。
    * ### 如果該頁已經存在於 Buffer Pool，就將該頁對應的控制區塊移動到LRU 的頭部。
    * ### 這樣在淘汰緩衝頁時，就可以從 LRU 尾部進行淘汰。
* ### 劃分區域的 LRU 鏈結串列
    * ### 情況 1: InnoDB 提供預先讀取 (read ahead)，會將認為當前請求後續可能讀取的頁面，一併載入到 Buffer Pool。
        * ### 線性預先讀取: 當循序存取某個區 (extent) 的頁面超過某個系統變數值，會觸發一次的 "非同步" 讀取下一個區中的全部頁面到 Buffer Pool 中，該系統變數為 innodb_read_ahead_threshold，預設值為 56，這是一個全域變數。
        * ### 隨機預先讀取: 當某個區的 13 個連續頁面都被載入到 Buffer Pool 的 "非常熱 (young) 區"，無論是否為順序讀取，都會觸發一次 "非同步" 讀取本區中的所有其它頁面到 Buffer Pool 中，由系統變數 innodb_random_read_ahead 控制，預設為 OFF，也就是不開啟隨機預先讀取功能，可以透過啟動選項或 ```SET GLOBAL``` 命令修改。
        * ### 有一個問題是，如果預先讀取的頁並沒有被使用，就可能導致為了載入一些沒用的頁，進而移除了一些可能有用但只是沒這麼常用儲存於 LRU 尾部的頁。
    * ### 情況 2: 如果需要執行全資料表掃描，可能導致 Buffer Pool 中一堆的頁面被排擠出去。
    * ### 總結: 可能降低 Buffer Pool 命中率的情況:
        * ### 自動載入了一堆用不到的頁。
        * ### 載入需求過大導致排擠問題。
* ### LRU 鏈結串列的分截
    * ### 熱資料 (young 區域): 儲存使用頻率非常高的緩衝頁。
    * ### 冷資料 (old 區域): 儲存使用頻率較不高的緩衝頁。
    * ### 透過系統變數 innodb_old_blocks_pct 控制 old 區域佔比，預設為 37 %。
    ```
    SHOW VARIABLES LIKE 'innodb_old_blocks_pct'
    ```
    * ### 可以透過啟動選縣更改或是在伺服器運作時直接修改。
    ```
    # 法一
    [server]
    innodb_old_blocks_pct = ?

    # 法二
    SET GLOBAL innodb_old_blocks_pct = ?;
    ```
    * ### 針對預先讀取: 當磁碟上頁面初次載入到 Buffer Pool 中某個緩衝頁時，其對應的控制區塊會放置於 old 截的頭部，如果被預先讀取的資料並未被使用，自然而然就會被擠出。
    * ### 針對全資料表掃描: 某個位於 Buffer Pool 之 old 區域的緩衝頁在第一次被存取時，會被記錄當下時間，後在某個時間間隔內若又被存取一次，不會被移到 young 區，此間隔時間由系統變數 innodb_old_blocks_time 控制。
    ```
    SHOW VARIABLES LIKE 'innodb_old_blocks_time'
    ```
    * ### innodb_old_blocks_time 預設為 1000 (ms)，也就是說 old 區域的緩衝頁在第一次和最後一次的存取時間若小於一秒，並不會被移動到 young 區。
* ### 更進一步最佳化 LRU 鏈結串列
    * ### 只有當被存取的緩衝頁位於 young 區 1 / 4 之後時，才會被移動到 LRU 的頭部，如果本身就位於 young 區的前 1 / 4 (非常熱)，該緩衝頁對應的控制區塊並不會被移動。
* ### 其它一些鏈結串列
    * ### unzip LRU: 用於管理壓縮頁。
    * ### zip clean: 用於管理壓縮頁。
    * ### zip free: 用於壓縮頁記憶體空間提供。
* ### 刷新髒頁到磁碟 (具有專門執行的執行緒，方式如下)
    * ### 從 LRU 鏈結串列的冷資料中刷新一部分頁面到磁碟: 定時從 LRU 尾部掃描些許頁面 (頁面數量透過系統變數 innodb_lru_scan_depth 控制)，若發現髒頁則刷新至磁碟，此種方式稱為 BUF_FLUSH_LRU。
    * ### 從 flush 鏈結串列中刷新一部分頁面到磁碟: 定時從 flush 鏈結串列中刷新一部分頁面到磁碟，此種方式稱為 BUF_FLUSH_LIST。
    * ### 當後台繁忙，刷新速度慢，導致 Buffer Pool 沒有可用的緩衝頁，這時就會查看 LRU 鏈結串列的尾部是否存在可以直接釋放掉的未修改緩衝頁，如果沒有則不得不將 LRU 鏈結串列尾部的髒頁同步刷新到磁碟，此種方式稱為 BUF_FLUSH_SINGLE_PAGE (不過這個操作會影響使用者的操作速度感受)。
* ### 多個 Buffer Pool 實例
    * ### 在多執行緒環境下，Buffer Pool 會被加鎖處理。
    * ### 當 Buffer Pool 特別大時，會將其拆分為數個 Buffer Pool 實例。
    * ### Buffer Pool 實例會獨立申請記憶體空間、獨立管理相關鏈結串列等。
    * ### 可以透過系統變數修改 Buffer Pool 實例個數。
    ```
    [server]
    innodb_buffer_pool_instances = ?
    ```
    * ### Buffer Pool 實例實際佔用記憶體空間:
    ```
    innodb_buffer_pool_size (總大小) / innodb_buffer_pool_instances (實例個數)
    ```
* ### innodb_biffer_pool_chunk_size
    * ### 一個 Buffer Pool 實例由多個 chunk 組成，可以避免一次申請過大連續記憶體空間，而是由 chunk 為單位項作業系統申請。
    * ### 一個 chunk 代表一片連續記憶體空間 (innodb_biffer_pool_chunk_size 預設為 128 MB)。
    * ### innodb_biffer_pool_chunk_size 不包含緩衝頁所對應的控制區塊記憶體大小，所以每一個 chunk 實際的大小會比 innodb_biffer_pool_chunk_size 大 5 % 左右。
* ### 設定 Buffer Pool 注意事項
    * ### innodb_buffer_pool_size 必須是 innodb_biffer_pool_chunk_size x innodb_buffer_pool_instances 的倍數。
* ### 查看 Buffer Pool 的狀態資訊
    ```
    SHOW ENGINE INNODB STATUS\G
    ```
    * ### Total memory allocated: 代表 Buffer Pool 向作業系統申請的連續記憶體空間大小 (真實值，全部包含，沒錯...是全部)。
    * ### Dictionary memory allocated: 資料字典分配的記憶體空間大小。
    * ### Buffer pool size: Buffer Pool 可容納緩衝頁數。
    * ### Free buffers: Buffer Pool 剩餘空閒緩衝頁數。
    * ### Database pages: LRU 鏈結串列中頁的數量 (young + old)。
    * ### Old database pages: LRU old 區節點數量。
    * ### Modified db pages: 髒頁數量，等同於 flush 鏈結串列中節點數量。
    * ### Pending reads: 等待從磁碟載入到 Buffer Pool 中的頁面數量 (載入時會先生成控制區塊並置於 LRU old 區頭部，此值為對應前述)。
    * ### Pending writes LRU: 即將從 LRU 刷新到磁碟的頁面數量。
    * ### Pending writes flush list: 即將從 flush 鏈結串列刷新到磁碟的頁面數量。
    * ### Pending writes single page: 即將以單一頁面形式刷新到磁碟的頁面數量。
    * ### Pages made young: 代表 LRU 中曾從 old 移動到 young 的節點數量。
    * ### Page made not young: 處於 old 的節點應不符合時間間隔未被移動到 young 的數量。
    * ### youngs / s: 每秒從 old 移動到 young 頭部的節點數量。
    * ### non-youngs / s: 每秒由不符合時間間隔未從 old 移動到 young 頭部的節點數量。
    * ### Pages read、created、written: 代表讀取、創建、寫入了多少頁面，後面跟著讀取、創建、寫入的速率。
    * ### Buffer pool hit rate: 過去某段時間內，平均存取 1000 次頁面時，該頁面有多少次已經被快取到 Buffer Pool 中。
    * ### young - making rate: 過去某段時間內，平均存取 1000 次頁面時，有多少次存取使頁面移動到 young 頭部。
    * ### not (young - making rate): 過去某段時間內，平均存取 1000 次頁面時，有多少次存取沒有使頁面移動到 young 頭部。
    * ### LRU len: LRU 中節點數量。
    * ### unzip_LRU: unzip_LRU 中節點數量。
    * ### I / O sum: 最近 50 s 讀取磁碟總頁數。
    * ### I / O cur: 正在讀取的磁碟頁數量。
    * ### I / O unzip sum: 最近 50 s 解壓的頁面數量。
    * ### I / O unzip cur: 正在解壓的頁面數量。
<br /> 
