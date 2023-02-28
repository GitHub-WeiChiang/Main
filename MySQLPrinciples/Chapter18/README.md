Chapter18 從貓爺借錢說起 -- 交易簡介
=====
* ### 原子性 (Atomicity)
    * ### 不可分割操作，不能存在中間狀態。
    * ### 不是全做，就是全不做。
    * ### 如果在執行操作的過程中發生了錯誤，就把已經執行的操作恢復成沒執行之前的樣子。
* ### 隔離性 (Isolation)
    * ### 兩次狀態的轉換應該互不影響。
* ### 一致性 (Consistency)
    * ### 資料庫中的資料全部符合現實世界中的約束，就稱這些資料是一致的，符合一致性。
    * ### 可以透過主鍵、唯一索引、外鍵、NOT NULL、CHECK 等方式實施。
    * ### MySQL 的 CHECK 約束沒有任何作用，不同於 SQL Server 和 Oracle DB。
    * ### 理解更多 (約束篇) -> [click me](https://gitlab.com/ChiangWei/main/-/tree/master/MySQLPrinciples)
    * ### 更多的一致性需求主要是在程式業務邏輯實現。
* ### 持久性 (Durability)
    * ### 狀態轉換完成後，這個轉換的結果將永久保留，稱為持久性。
    * ### 某次轉換對應的資料庫操作所修改的資料都應該在磁碟中保留下來，無論發生什麼事故，該次轉換造成的影響都不應該遺失。
* ### 交易的概念
    * ### ACID: 上述原子性、隔離性、一致性與持久性的統稱。
    * ### 交易 (transaction): 需要保證 ACID 的資料庫操作。
    * ### 交易是一種抽象的概念。
* ### 交易的狀態
    * ### 活動的 (active): 該交易對應的資料庫操作正在執行。
    * ### 部分提交的 (partially committed): 該交易對應的資料庫操作已完成，但尚未將結果從記憶體刷新到資料庫。
    * ### 失敗的 (failed): 當該交易狀態處於 "活動的" 或 "部分提交的" 時，因遇到某些事故 (資料庫錯誤、作業系統錯誤、斷電、人為停止) 而無法繼續執行。
    * ### 中止的 (aborted): 當交易狀態為 "失敗的"，需要將當前造成的影響復原，在此稱之為 "回覆"，在 "回覆" 後資料庫就復原至執行交易之前的狀態，該交易狀態就稱為 "中止的"。
    * ### 提交的 (committed): 當交易所進行的資料庫操作順利執行完畢並刷新至磁碟中。
* ### 交易的生命週期正式結束: 狀態需為 "中止的 (aborted)" 或 "提交的 (committed)"。
    * ### 已提交的交易其修改將為永久生效。
    * ### 被中止的交易其影響已被完全復原。
* ### 開啟交易
    ```
    # 法一
    BEGIN [WORK];

    # 法二
    START TRANSACTION;
    ```
    * ### START TRANSACTION 後可以加上修飾符號。
        * ### READ ONLY: 唯讀交易，不可進行增刪改操作 (臨時表不受此限)。
        * ### READ WRITE: 讀寫交易，可以進行增刪改查操作 (預設)。
        * ### WITH CONSISTENT SNAPSHOT: 一致性讀取。
* ### 提交交易
    ```
    COMMIT [WORK];
    ```
* ### 手動中止交易
    ```
    ROLLBACK [WORK];
    ```
* ### 支援交易的儲存引擎
    * ### InnoDB
    * ### NDB
    * ### 如果某儲存引擎不支援 ROLLBACK 操作，並不會引發報錯，但也不會進行 "回覆"，總之就是沒有任何事情發生。
* ### 自動提交
    * ### 透過系統變數 autocommit 控制。
    ```
    SHOW VARIABLES LIKE 'autocommit';
    ```
    * ### 預設為 ON，也就是說若不使用 BEGIN 或 START TRANSACTION 開啟交易，每一行敘述都會是一個獨立的交易被自動提交。
* ### 觸發隱式提交的條件 (將之前的交易悄悄的提交，就像偷偷下 COMMIT 指令一樣)
    * ### 定義或修改資料庫物件的資料定義語言 (Data Definition Language, DDL)。
        * ### 資料庫物件泛指 "資料庫"、"表"、"視圖"、"預存程序" 等。
        * ### DDL 包含 CREATE、DROP、ALTER。
    * ### 隱式使用或修改 mysql 資料庫中的表
        * ### 包含 ALTER USER、CREATE USER、DROP USER、GRANT、RENAME USER、REVOKE、SET PASSWORD 等。
    * ### 交易控制或關於鎖定的敘述
        * ### 上一個交易尚未提交或回覆就下了 BEGIN 或 START TRANSACTION 指令。
        * ### 使用 LOCK TABLES、UNLOCK TABLES 等鎖定相關敘述。
    * ### 載入資料的敘述
        * ### LOAD DATA。
    * ### 關於 MySQL 複製的一些敘述
        * ### 使用 START SLAVE、STOP SLAVE、RESET SLAVE、CHANGE MASTER TO 等敘述。
    * ### 其它
        * ### ANALYZE TABLE、CACHE INDEX、CHECK TABLE、FLUSH、LOAD INDEX INTO CACHE、OPTIMIZE TABLE、PEPAIR TABLE、RESET 等敘述。
* ### 保存點 (savepoint)
    ```
    # 定義保存點
    SAVEPOINT save_point_name;

    # 回覆到指定保存點
    ROOLBACK [WORK] TO [SAVEPOINT] save_point_name;

    # 回覆到交易執行前 (略過保存點)
    ROLLBACK [WORK];

    # 刪除保存點
    RELEASE SAVEPOINT save_point_name;
    ```
<br /> 
