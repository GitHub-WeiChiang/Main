MySQLPrinciples
=====
* ### 守則篇: MySQL Design Principles (從刪庫到跑路)
* ### 番外篇: Stored Procedure (從蒙圈到無限茫然)
* ### 觸發篇: Introduction To MySQL Triggers (從看懂到看開)
* ### 物化篇: Materialized View (還沒入門就奪門而逃)
* ### 約束篇: CHECK Constraint In MySQL Isn't Working (從入門到女裝)
* ### 鎖頭篇: 徹底搞懂 MySQL 的鎖機制 (從入門到入墳)
* ### 公共篇: MySQL Common Table Expression 公共表表示式 (從入門到改行)
* ### 遞回篇: MySQL 遞回 Common Table Expression 公共表表示式 (樓上改行是對的)
* ### 回傳篇: PostgreSQL 的 RETURNING 子句 (嗯...這個滿簡單的)
* ### 函數篇: MySQL 自定義函數 (從呼叫函數到呼叫破喉嚨)
* ### 更新篇: PostgreSQL 9.4 引入特性: FILTER 子句 (夜深了...)
* ### 分頁篇: 有的時候總是會遇到要分頁的情況 (人生迷茫中...)
* ### 正規篇: 資料庫正規化 (就像埋在霧區裡的地雷，只要誤踩瞬間便會粉身碎骨。)
* ### 視圖篇: Creating PostgreSQL Updatable Views (MBTI 我是 ISFJ-T)
* ### Chapter01 裝作自己是個小白 -- 初識 MySQL
* ### Chapter02 MySQL 的調控按鈕 -- 啟動選項和系統變數
* ### Chapter03 字元集和比較規則
* ### Chapter04 從一筆記錄說起 -- InnoDB 記錄儲存結構
* ### Chapter05 盛放記錄的大盒子 -- InnoDB 資料頁結構
* ### Chapter06 快速查詢的秘笈 -- B+ 樹索引
* ### Chapter07 B+ 樹索引的使用
* ### Chapter08 MySQL 的資料目錄
* ### Chapter09 存放頁面的大池子 -- InnoDB 的表格空間
* ### Chapter10 條條大路通羅馬 -- 表單存取方法
* ### Chapter11 兩個表的親密接觸 -- 連接的原理
* ### Chapter12 誰最便宜就選誰 -- 基於成本的最佳化
* ### Chapter13 兵馬未動，糧草先行 -- InnoDB 統計資料是如何收集的
* ### Chapter14 基於規則的最佳化 (內含子查詢最佳化二三事)
* ### Chapter15 查詢最佳化的百科全書 -- EXPLAIN 詳解
* ### Chapter16 神兵利器 -- optimizer trace 的神奇功效
* ### Chapter17 調節磁碟和 CPU 的矛盾 -- InnoDB 的 Buffer Pool
* ### Chapter18 從貓爺借錢說起 -- 交易簡介
* ### Chapter19 說過的話就一定要做到 -- redo 記錄檔
* ### Chapter20 後悔了怎麼辦 -- undo 記錄檔
* ### Chapter21 一筆記錄的多副面孔 -- 交易隔離等級和 MVCC
* ### Chapter22 工作面試老大難 -- 鎖
<br />

守則篇: MySQL Design Principles (從刪庫到跑路)
=====
* ### 先說好，這些僅是透過 "理論推算" 的 "參考"。
* ### 非變長欄位資料格式適用於修改頻率較高的欄位。 / Chapter04
* ### 變長欄位資料格式適用於修改頻率較低的欄位。 / Chapter04
* ### 不要為所欲為的肆意創建索引。 / Chapter07
* ### 為 ORDER BY 子句中的欄位建立索引有機會提高效能。 / Chapter07
* ### ORDER BY 升冪 (ASC) 排列的效能優於降冪 (DESC) 排列。 / Chapter07
* ### 聯合索引的建立對於含有 GROUP BY 的查詢可以有效提升效率。 / Chapter07
* ### 索引使用與創建注意事項 / Chapter07
    * ### 適用於 "搜索"、"排序" 與 "分組" 的列。
    * ### 適用於 "欄位值不重複比例較高" 的列。
    * ### 索引列資料型態 "越小越好"。
    * ### 可針對 "字串" 型態 "列字首" 創建索引。
    * ### 盡可能執行 "覆蓋索引" (索引下推)。
    * ### 索引列應 "單獨出現" 於搜索條件。
    * ### 新插入記錄 "主鍵" 盡可能 "遞增" 呈現。
    * ### 避免出現 "容錯索引" 與 "重複索引" 的場景。
* ### 連接查詢最佳化 1 / Chapter11
    * ### 為 "被驅動表" 加上高效率的索引。
    * ### 透過 "啟動選項" 或 "系統變數" 調大 join_buffer_size 的值進而優化 "基於區塊的巢狀結構迴圈連接 (Block Nested - Loop Join)" 演算法的執行。
* ### 連接查詢最佳化 2 / Chapter12
    * ### 儘量減少驅動表的扇出。
    * ### 存取被驅動表的成本要儘量低: 簡單說就是，被驅動表的連接列最好是該表的主鍵或唯一二級索引列，如此可以把存取被驅動表的成本降至更低。
* ### 儘量刪除那些用不到的索引 / Chapter15
    * ### 執行計畫中會包含 possible_keys 與 key 兩欄位。
    * ### 透過比對，應儘量刪除那些用不到的索引。
<br />

番外篇: Stored Procedure (從蒙圈到無限茫然)
=====
* ### SQL Server Management Studio (Stored Procedure)
    * ### Database -> Programmibility -> Stored Procedure
    ```
    /* 創建預存程序 */
    CREATE PROCEDURE (STORED PROCEDURE NAME)
    AS
    BEGIN
        /* SQL 查詢 */
        SELECT * FROM (TABLE NAME);
    END 

    /* 調用 */
    EXEC (STORED PROCEDURE NAME)

    /* 修改 */
    ALTER PROCEDURE (STORED PROCEDURE NAME)
    AS
    BEGIN
        /* 關閉影響筆數回傳 */
        SET NOCOUNT ON;
        /* SQL 查詢 */
        SELECT * FROM (TABLE NAME);
    END

    /* 傳入變數 */
    CREATE PROCEDURE (STORED PROCEDURE NAME)
        @(ATTRIBUTE NAME) (ATTRIBUTE TYPE)
    AS
    BEGIN
        SELECT *
        FROM (TABLE NAME)
        WHERE (ATTRIBUTE NAME) = @(ATTRIBUTE NAME);
    END

    /* 調用 */
    EXEC (STORED PROCEDURE NAME) (ATTRIBUTE)

    /* 傳入兩個變數 */
    CREATE PROCEDURE (STORED PROCEDURE NAME)
        @(ATTRIBUTE NAME 1) (ATTRIBUTE TYPE)
        @(ATTRIBUTE NAME 2) (ATTRIBUTE TYPE)
    AS
    BEGIN
        SELECT *
        FROM (TABLE NAME)
        WHERE
            (ATTRIBUTE NAME 1) = @(ATTRIBUTE NAME 1)
            AND
            (ATTRIBUTE NAME 2) = @(ATTRIBUTE NAME 2);
    END
    ```
* ### Execute SQL Server Stored Procedure From Python (示意用，僅供參考。)
```
import pyodbc
 
# Connection variables.
server = 'ip'
database = 'database name'
username = 'user name'
password = 'password'

try:
    # Connection string.
    cnxn = pyodbc.connect("DRIVER={ODBC Driver 17 for SQL Server};SERVER=" + server + ";DATABASE=" + database + ";UID=" + username + ";PWD=" + password)
    cursor = cnxn.cursor()
 
    # Prepare the stored procedure execution script and parameter values.
    storedProc = "Exec (PROCEDURE NAME) @(ATTRIBUTE NAME) = ?, @(ATTRIBUTE NAME) = ?"
    params = ("ATTRIBUTE", "ATTRIBUTE")
 
    # Execute Stored Procedure With Parameters.
    cursor.execute(storedProc, params)
 
    # Iterate the cursor.
    row = cursor.fetchone()
    while row:
        # Print the row.
        print(str(row[0]) + " : " + str(row[1] or '') )
        row = cursor.fetchone()
 
    # Close the cursor and delete it.
    cursor.close()
    del cursor
 
    # Close the database connection.
    cnxn.close()
 
except Exception as e:
    print("Error: %s" % e)
```
* ### Stored Procedure 優點
    * ### 減少網路流量 (不用在網路上傳輸大量的 inline SQL code)。
    * ### 提升安全性 (賦予 EXEC 權限，無須存取資料表，並可避免 SQL injection)。
    * ### 優化效能 (避免每次查詢的 CPU 編譯資源消耗與等待時間及大量執行計畫對快取的佔用，並可供 DBA 能優化每一隻 SP)。
    * ### 可以接受參數 (可以參數化查詢條件)。
    * ### 封裝並隱藏複雜商業邏輯 (分離數據與業務邏輯)。
    * ### 預存程序可以將多項作業結合成單一的程序呼叫。
* ### Stored Procedure 缺點
    * ### 移植性差，客製化於特定的資料庫上。
    * ### 預存程式的效能調校，受限於各種資料庫系統。
* ### 什麼時候會發生 Parameter Sniffing ?
    * ### SQL Server uses a process called parameter sniffing when it executes stored procedures that have parameters.
* ### What is parameter sniffing in SQL Server ?
    * ### When we invoke a stored procedure for the first time the query optimizer generates an optimal execution plan for this stored procedure according to its input parameters.
* ### 參數探測 (Parameter Sniffing): SQL Server 為避免 Cache 中有許多重覆的執行計畫，當語法是參數化且沒有任何的 Plan 在 Cache 中，會根據當時的參數產生一份最恰當的執行計畫，爾後除非 recompile stored procedure，否則就會一直重用這份執行計畫。
    * ### 讓 Plan 可以重複使用，避免每次執行 Stored Procedure 都必須耗費 CPU 編譯語法來選擇最佳查詢算法。
    * ### 若第一次執行所選擇的是資料分布非常極端的情況，可能造成之後在執行此 Stored Procedure 時效能低落。
* ### 如何解決 Parameter Sniffing 問題
    * ### Recompile: 極少執行，但每次所進行查詢的資料量差異極大 (可針對整個 Procedure 層級或個別的 WHERE 查詢子句，但這會嚴重增加 CPU 的負擔 "Recompiling is a CPU-intensive operation.")。
    ```
    CREATE PROCEDURE ...
    @...
    WITH RECOMPILE
    AS
    BEGIN
        查詢區塊
    END

    --

    CREATE PROCEDURE ...
    @...
    AS
    BEGIN
        ...
        WHERE ... = @... OPTION(RECOMPILE)
    END
    ```
    * ### OPTIMIZE FOR UNKNOWN: 面對頻繁執行的情況，將查詢子句的參數設定為未知，使 Query Optimizer 在編譯時針對未知參數賦予中庸值，這個方法所選擇的執行計劃不會針對每次執行選擇最完美的做法，但其所選擇的中庸值可以避免大部分的查詢有效能問題，要注意，若使用於不均勻資料效能將非常低落 (適用 2008 之後的版本)。
    ```
    CREATE PROCEDURE ...
    @...
    AS
    BEGIN
        ...
        WHERE ... = @... OPTION(OPTIMIZE FOR UNKNOWN)
    END
    ```
    * ### Local Variable: 2008 之前的版本適用，透過 Local Variable 承接參數，亦可達到與 OPTIMIZE FOR UNKNOWN 一樣的效果，亦不可用於不均勻資料。
    ```
    CREATE PROCEDURE ...
    @...(variable)
    AS
    BEGIN
        DECLARE ...(local variable)
        SET ...(local variable) = ...(variable)
        ...
        WHERE ... = ...(local variable)
    END
    ```
    * ### Query Hinting: Use the OPTIMIZE FOR query hint. This tells SQL Server to use a specified value when compiling the plan. If you can find a value that produces a "good enough" plan each time, and the performance is acceptable for each case, this is a good option for you. But the biggest drawback with OPTIMIZE FOR is on tables where the distribution of data changes.
    ```
    CREATE PROCEDURE ...
    AS
    BEGIN
        ...
        WHERE ... = @...
        OPTION (OPTIMIZE FOR (@...='good good value !'));
    END
    ```
    * ### 為每個獨特的情況寫一個 Stored Procedure: 適合頻繁查詢，且追求每次查詢都能有近乎完美效能的解法 (如果能夠清楚掌握每次查詢的特性且資料表不易變動時可以使用，但理論上不建議使用)。
* ### The Elephant and the Mouse, or, Parameter Sniffing in SQL Server
    * ### SQL Server uses a process called parameter sniffing when it executes stored procedures that "have parameters".
    * ### When using "literal values", SQL Server will "compile each separately", and "store a separate execution plan for each".
    * ### 如何判斷是同一句 literal values query ? 在 MySQL (版本 8.0 已徹底移除緩存功能) 還具備缓存功能時，查詢內容多一個空格或變一個大小寫都被認為是不同的語句，在這邊可能也是這樣判斷。
* ### 執行計畫的生命週期
    * ### The SQL Execution Plan will not be kept in the Plan cache forever, where the SQL Server Engine will remove the plan from the Plan Cache if the system requires more memory or the age of the plan, that depends on the number of times this plan is called.
    * ### The system process that is responsible for cleaning these aged plans is called the Lazy Writer process.
* ### 註記
    * ### Literal Values 不會有 Parameter Sniffing 的事情發生，每一個查詢語句會對應一個獨立的執行計畫，也就是每次都需進行編譯。
    * ### Parameterized 的查詢語句，則會發生 Parameter Sniffing，所以需要注意效能調適。
* ### 問題
    * ### Q1: 若針對整個 Stored Procedure 層級進行 Recompile，預存程序是不是就沒意義了 ?
    * ### A1: 不完全正確，Stored Procedure 除了增加效能外還有其它優點，且可以將多項作業結合成單一的程序呼叫，所以並不會讓預存程序的使用變得沒有意義。
    * ### Q2: 為什麼 MySQL 不推薦使用資料庫的除緩存功能甚至要徹底移除 ?
    * ### A2: (1)自帶的緩存系統應用場景有限，因其要求SQL語句必須一模一樣。 (2)緩存失效頻繁，只要表的數據有任何修改，針對該表的所有緩存都會失效，導致對於更新頻繁的數據表而言，緩存命中率非常低。 (3)緩存功能應交給獨立的緩存服務執行較為合適。
    * ### Q3: Stored Procedure 除了上述的優勢外，是否還有其它的適用場景 ?
    * ### A3: 如果某個資料庫會被多種後端程式語言架構所存取，Stored Procedure 會是一個很好的選擇，因為相關的業務邏輯只需要撰寫一次即可。
<br />

觸發篇: Introduction To MySQL Triggers (從看懂到看開)
=====
* ### Trigger 設計目的是讓 DB 在特定事件發生後，執行指定的操作，例如某資料表新增了一筆資料後，將該筆資料記錄到另一張表。
* ### 來個簡單的案例，當使用者註冊成功以後，在日誌表留下使用者名稱和註冊的時間。
* ### 建表
```
CREATE TABLE `user` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_name` VARCHAR(200) NOT NULL,
    `mail` VARCHAR(255) NOT NULL
);

CREATE TABLE `log` (
    `id` BIGINT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `user_name` VARCHAR(200) NOT NULL,
    `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP()
);
```
* ### Trigger 的種類
    * ### BEFORE INSERT
    * ### BEFORE UPDATE
    * ### BEFORE DELETE
    * ### AFTER INSERT
    * ### AFTER UPDATE
    * ### AFTER DELETE
* ### 當 user 新增後，將 user_name 複製到 log 中。
```
CREATE TRIGGER `trigger_name` AFTER INSERT ON `user`
FOR EACH ROW
    .... ;
```
* ### 若 trigger 中需要的動作超過一個時。
```
CREATE TRIGGER `trigger_name` AFTER INSERT ON `user`
FOR EACH ROW
BEGIN
    .... ;
    .... ;
END;
```
* ### 完整版的當 user 新增後，將 user_name 複製到 log 中。
```
-- 這個範例會報錯

CREATE TRIGGER `trigger_name`
AFTER INSERT ON `user`
FOR EACH ROW
BEGIN
    -- 找出最新的 user name，存在變數 @name 中
    SET @name = (
        SELECT `user_name`
        FROM `user`
        WHERE `id` = last_insert_id()
    );

    -- 將 user name 存進 log 中
    INSERT INTO `log` (
        `user_name`
    ) VALUES (
        @name
    );
END;
```
* ### 新增上方的 trigger 時，MySQL 會報錯誤，因其寫法會讓 MySQL 搞不清楚哪些是 trigger 要做的動作而哪些又是與 trigger 無關的 SQL 語句。
* ### 使用 DELIMITER 暫時將原本代表語句結束的 ";" 換成 "$$" (符號自訂)
```
DELIMITER $$

CREATE TRIGGER `trigger_name`
AFTER INSERT ON `user`
FOR EACH ROW
BEGIN
    SET @name = (
        SELECT `user_name`
        FROM `user`
        WHERE `id` = last_insert_id()
    );
    INSERT INTO `log` (
        `user_name`
    ) VALUES (
        @name
    );
END;
$$

DELIMITER ;
```
* ### 雖然能夠成功建立，但存在一個問題，last_insert_id() 只能抓到 insert 成功以後的最後一個 ID，但若有一個 transaction 裡面包含多個 insert 時，AFTER INSERT 這個 trigger 裡面就只會抓到一個 ID (transaction 中最後一個 insert 的 user ID)。
* ### MySQL 特別提供了一個 row 的 alias "NEW" 和 "OLD" (僅能在 trigger 中使用)，當 table user 一口氣新增 3 筆資料時，會觸發 trigger 執行三次，這時在 trigger 中使用 NEW 就會自動指向特定的 row。
```
DELIMITER $$

CREATE TRIGGER `trigger_name`
AFTER INSERT ON `user`
FOR EACH ROW
BEGIN
    -- 使用 NEW 來改寫
    SET @name = NEW.user_name;

    INSERT INTO `log` (
        `user_name`
    ) VALUES (
        @name
    );
END;
$$

DELIMITER ;
```
* ### \@name 只被用了一次，優化一下。
```
DELIMITER $$

CREATE TRIGGER `trigger_name`
AFTER INSERT ON `user`
FOR EACH ROW
BEGIN
    -- 直接從 NEW 來指定要 insert 的資料即可
    INSERT INTO `log` (
        `user_name`
    ) VALUES (
        NEW.user_name
    );
END;
$$

DELIMITER ;
```
<br />

物化篇: Materialized View (還沒入門就奪門而逃)
=====
* ### View
    * ### 由一個查詢指令所做成，並存放在資料庫來 "代表這個指令" 的物件，每次使用他都會觸發這個指令來做查詢。
    * ### 建立檢視表。
    ```
    create view 檢視表名稱 as 想要的指令
    ``` 
    * ### 每次使用 View 查詢其實都會重跑一次所撰寫的指令。
    * ### 一般的 View 並不會有任何效能提升。
* ### Materialized View
    * ### 又稱 "實體化檢視表" 以下簡稱 MView。
    * ### 與 View 一樣是將一個查詢存起來，但建立的同時會先執行一次所撰寫的指令，並且把結果用資料表的形式存起來。
    * ### 建立實體化檢視表。
    ```
    create materialized view 檢視表名稱 as 想要的指令
    ```
    * ### MView 就是一個真的有存資料的表，甚至可以加 Index 來加速搜尋。
    * ### 必須透過 "refresh" 來刷新資料，使其再執行一次所撰寫的指令，並用新的結果覆蓋舊的結果。
    ```
    refresh materialized view 檢視表名稱
    ```
    * ### 如果這個表很常被查詢，若擔心查詢當下此表正在被整個 refresh 更新，使資料處於被鎖住的狀況，可以用 "concurrently" 的方式來 refresh。
    ```
    refresh materialized view concurrently 檢視表名稱
    ```
    * ### "concurrently" 會讓 PostgresQL 不會直接把整張表鎖住，而是會另外產生一份新的表來做比對，針對有更動的列來更新 (使用 concurrently 有一個前提: 表內要有一或多個 unique index)。
    * ### 適用場景: 假設每日需查詢 (顯示) "前一天有多少特定新用戶"，當時間到了該日，這個資料一天內就完全不會改變，一天只需計算一次，透過這種 MView 的方式，進而改善服務的效能。
    * ### 如果服務需要用到運算量較大的查詢 (併表操作)，就可以把它寫成一個 Materialized View，並決定 refresh 頻率，而非每次都重新執行運算。
<br />

約束篇: CHECK Constraint In MySQL Isn't Working (從入門到女裝)
=====
* ### 讓我們來討論一下 Mysql 中 Check 约束无效的原因以及解决方法吧 !
```
mysql> create table checkDemoTable(a int, b int, id int, primary key(id));
Query OK, 0 rows affected

mysql> alter table checkDemoTable add constraint checkDemoConstraint check(a > 0);
Query OK, 0 rows affected
Records: 0 Duplicates: 0 Warnings: 0

mysql> insert into checkDemoTable values(-2, 1, 1);
Query OK, 1 row affected

mysql> select * from checkDemoTable;
+----+---+----+
| a | b | id |
+----+---+----+
| -2 | 1 | 1 |
+----+---+----+
1 row in set
```
* ### 很明显，CHECK 语句在声明中并未起到作用。
* ### 在 MYSQL 中，CHECK 只是一段可调用但无意义的子句，MySQL 会直接忽略。
* ### CHECK 子句会被分析但是会被忽略: 接受这些子句但又忽略子句的原因是为了提高兼容性，以便更容易地从其它 SQL 服务器中导入代码，并运行应用程序，创建带参考数据的表。
* ### 解决这个问题有两种办法
    * ### 如果需要设置 CHECK 约束的字段范围小，并且比较容易列举全部的值，就可以考虑将该字段的类型设置为枚举类型 enum() 或集合类型 set()，比如性别字段可以这样设置，插入枚举值以外值的操作将不被允许。
    ```
    mysql> create table checkDemoTable(a enum('男', '女'), b int, id int, primary key(id));
    Query OK, 0 rows affected

    mysql> insert into checkDemoTable values('男', 1, 1);
    Query OK, 1 row affected

    mysql> select * from checkDemoTable;
    +----+---+----+
    | a | b | id |
    +----+---+----+
    | 男 | 1 | 1 |
    +----+---+----+
    1 row in set
    ```
    * ### 如果需要设置 CHECK 约束的字段是连续的，或者列举全部值很困难，比如正实数或正整数，那就只能用触发器来代替约束实现数据有效性了。
    ```
    DELIMITER $$

    CREATE TRIGGER TestField1_BeforeInsert BEFORE INSERT ON checkDemoTable
    FOR EACH ROW
    BEGIN
    IF NEW.a < 0 THEN
    SET NEW.a = 0;
    END IF;
    
    END $$
    ```
<br />

鎖頭篇: 徹底搞懂 MySQL 的鎖機制 (從入門到入墳)
=====
* ### 锁对 MySQL 的数据访问并发有着举足轻重的影响。
* ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/MySQLPrinciples/Lock.png)
* ### 锁的解释
    * ### 计算机协调多个进程或线程并发访问某一资源的机制。
* ### 锁的重要性
    * ### 在数据库中，除传统计算资源 (CPU、RAM、I/O) 的争抢，数据也是一种供多用户共享的资源。
    * ### 如何保证数据并发访问的一致性，有效性，是所有数据库必须要解决的问题。
    * ### 锁冲突也是影响数据库并发访问性能的一个重要因素，因此锁对数据库尤其重要。
* ### 锁的缺点
    * ### 加锁是消耗资源的，锁的各种操作，包括获得锁、检测锁是否已解除、释放锁等，都会增加系统的开销。
* ### 简单的例子
    * ### 现如今网购已经特别普遍了，比如淘宝双十一活动，当天的人流量是千万及亿级别的，但商家的库存是有限的。
    * ### 系统为了保证商家的商品库存不发生超卖现象，会对商品的库存进行锁控制。
    * ### 当有用户正在下单某款商品最后一件时，系统会立马对该件商品进行锁定，防止其他用户也重复下单，直到支付动作完成才会释放 (支付成功则立即减库存售罄，支付失败则立即释放)。
* ### 表锁
    * ### 读锁 (read lock)，也叫共享锁 (shared lock)，针对同一份数据，多个读操作可以同时进行而不会互相影响 (select)。
    * ### 写锁 (write lock)，也叫排他锁 (exclusive lock)，当前操作没完成之前，会阻塞其它读和写操作 (update、insert、delete)。
    * ### 存储引擎默认锁: MyISAM。
    * ### 特点
        * ### 对整张表加锁。
        * ### 开销小。
        * ### 加锁快。
        * ### 无死锁。
        * ### 锁粒度大，发生锁冲突概率大，并发性低 (相對效能差)。
    * ### 结论
        * ### 读锁会阻塞写操作，不会阻塞读操作。
        * ### 写锁会阻塞读和写操作。
    * ### 建议: MyISAM 的读写锁调度是写优先，这也是 MyISAM 不适合做写为主表的引擎，因为写锁以后，其它线程不能做任何操作，大量的更新使查询很难得到锁，从而造成永远阻塞。
* ### 行锁
    * ### 读锁 (read lock)，也叫共享锁 (shared lock)，允许一个事务去读一行，阻止其他事务获得相同数据集的排他锁。
    * ### 写锁 (write lock)，也叫排他锁 (exclusive lock)，允许获得排他锁的事务更新数据，阻止其他事务取得相同数据集的共享锁和排他锁。
    * ### 意向共享锁 (IS)，一个事务给一个数据行加共享锁时，必须先获得表的 IS 锁。
    * ### 意向排它锁 (IX)，一个事务给一个数据行加排他锁时，必须先获得该表的 IX 锁。
    * ### 存储引擎默认锁: InnoDB。
    * ### 特点
        * ### 对一行数据加锁。
        * ### 开销大。
        * ### 加锁慢。
        * ### 会出现死锁。
        * ### 锁粒度小，发生锁冲突概率最低，并发性高 (相對效能佳)。
    * ### 事务并发带来的问题
        * ### 更新丢失，解决: 让事务变成串行操作，而不是并发的操作，即对每个事务开始---对读取记录加排他锁。
        * ### 脏读，解决: 隔离级别为 Read uncommitted。
        * ### 不可重读，解决: 使用 Next-Key Lock 算法来避免。
        * ### 幻读，解决: 间隙锁 (Gap Lock)。
* ### 页锁: 开销、加锁时间和锁粒度介于表锁和行锁之间，会出现死锁，并发处理能力一般。
* ### 表锁上锁
    * ### 隐式上锁 (默认，自动加锁自动释放)
        ```
        # 上读锁
        select

        # 上写锁
        insert、update、delete
        ```
    * ### 显式上锁
        ```
        # 读锁
        lock table tableName read;
        # 写锁
        lock table tableName write;
        ```
    * ### 显式解锁
        ```
        # 释放被当前会话持有的任何锁
        unlock tables;
        ```
    | session 1 | session 2 |
    | -- | -- |
    | lock table teacher read; // 上读锁 |  |
    | select * from teacher; // 可以正常读取 | select * from teacher; // 可以正常读取 |
    | update teacher set name = 3 where id = 2; // 报错因被上读锁不能写操作 | update teacher set name = 3 where id = 2; // 被阻塞 |
    | unlock tables; // 解锁 |  |
    |  | update teacher set name = 3 where id = 2; // 更新操作成功 |

    | session 1 | session 2 |
    | -- | -- |
    | lock table teacher write; // 上写锁 |  |
    | select * from teacher; // 可以正常读取 | select * from teacher; // 被阻塞 |
    | update teacher set name = 3 where id = 2; // 可以正常更新操作 | update teacher set name = 4 where id = 2; // 被阻塞 |
    | unlock tables; // 解锁 |  |
    |  | select * from teacher; // 读取成功 |
    |  | update teacher set name = 4 where id = 2; // 更新操作成功 |
* ### 行锁上鎖
    * ### 隐式上锁 (默认，自动加锁自动释放)
        ```
        # 不会上锁
        select

        # 上写锁
        insert、update、delete
        ```
    * ### 显式上锁
        ```
        # 读锁
        select * from tableName lock in share mode;

        # 写锁
        select * from tableName for update;
        ```
    * ### 显式解锁
        * ### 提交事务 (commit)
        * ### 回滚事务 (rollback)
        * ### kill 阻塞进程
    | session 1 | session 2 |
    | -- | -- |
    | begin; |  |
    | select * from teacher where id = 2 lock in share mode; // 上读锁 |  |
    |  | select * from teacher where id = 2; // 可以正常读取 |
    | update teacher set name = 3 where id = 2; // 可以更新操作 | update teacher set name = 5 where id = 2; // 被阻塞 |
    | commit; |  |
    |  | update teacher set name = 5 where id = 2; // 更新操作成功 |

    | session 1 | session 2 |
    | -- | -- |
    | begin; |  |
    | select * from teacher where id = 2 for update; // 上写锁 |  |
    |  | select * from teacher where id = 2; // 可以正常读取 |
    | update teacher set name = 3 where id = 2; // 可以更新操作 | update teacher set name = 5 where id = 2; // 被阻塞 |
    | rollback; |  |
    |  | update teacher set name = 5 where id = 2; // 更新操作成功 |
    * ### 为什么上了写锁，别的事务还可以读操作 ? 因为 InnoDB 有 MVCC 机制 (多版本并发控制)，可以使用快照读，而不会被阻塞。
* ### 行锁的实现算法
    * ### Record Lock: 单个行记录上的锁，Record Lock 总是会去锁住索引记录，如果 InnoDB 存储引擎表建立的时候没有设置任何一个索引，这时 nnoDB 存储引擎会使用隐式的主键来进行锁定。
    * ### Gap Lock: 当我们用范围条件而不是相等条件检索数据，并请求共享或排他锁时，InnoDB 会给符合条件的已有数据记录的索引加锁，对于键值在条件范围内但并不存在的记录。
        * ### 优点: 解决了事务并发的幻读问题。
        * ### 不足: 因为 query 执行过程中通过范围查找的话，他会锁定争个范围内所有的索引键值，即使这个键值并不存在。
        * ### Gap Lock 有一个致命的弱点，就是当锁定一个范围键值之后，即使某些不存在的键值也会被无辜的锁定，而造成锁定的时候无法插入锁定键值范围内任何数据。在某些场景下这可能会对性能造成很大的危害。
    * ### Next - key Lock: 同时锁住数据 + 间隙锁，在 Repeatable Read 隔离级别下，Next - key Lock 算法是默认的行记录锁定算法。
* ### 行锁的注意点
    * ### 只有通过索引条件检索数据时，InnoDB 才会使用行级锁，否则会使用表级锁 (索引失效，行锁变表锁)。
    * ### 即使是访问不同行的记录，如果使用的是相同的索引键，会发生锁冲突。
    * ### 如果数据表建有多个索引时，可以通过不同的索引锁定不同的行。
* ### 如何排查锁
    * ### 表鎖
        ```
        # 查看表鎖情況
        show open tables;

        # 表锁分析
        show status like 'table%';
        ```
        * ### table_locks_waited: 出现表级锁定争用而发生等待的次数 (不能立即获取锁的次数，每等待一次值加 1)，此值高说明存在着较严重的表级锁争用情况。
        * ### table_locks_immediate: 产生表级锁定次数，不是可以立即获取锁的查询次数，每立即获取锁加 1。
    * ### 行锁
        ```
        # 行鎖分析
        show status like 'innodb_row_lock%';
        ```
        * ### innodb_row_lock_current_waits: 当前正在等待锁定的数量。
        * ### innodb_row_lock_time: 从系统启动到现在锁定总时间长度。
        * ### innodb_row_lock_time_avg: 每次等待所花平均时间。
        * ### innodb_row_lock_time_max: 从系统启动到现在等待最长的一次所花时间。
        * ### innodb_row_lock_waits: 系统启动后到现在总共等待的次数。
* ### information_schema 库
    * ### innodb_lock_waits 表
    * ### innodb_locks 表
    * ### innodb_trx 表
* ### 优化建议
    * ### 尽可能让所有数据检索都通过索引来完成，避免无索引行锁升级为表锁。
    * ### 合理设计索引，尽量缩小锁的范围。
    * ### 尽可能较少检索条件，避免间隙锁。
    * ### 尽量控制事务大小，减少锁定资源量和时间长度。
    * ### 尽可能低级别事务隔离。
* ### 死锁
    * ### 指两个或者多个事务在同一资源上相互占用，并请求锁定对方占用的资源，从而导致恶性循环的现象。
    * ### 产生的条件
        * ### 互斥条件: 一个资源每次只能被一个进程使用。
        * ### 请求与保持条件: 一个进程因请求资源而阻塞时，对已获得的资源保持不放。
        * ### 不剥夺条件: 进程已获得的资源，在没有使用完之前，不能强行剥夺。
        * ### 循环等待条件: 多个进程之间形成的一种互相循环等待的资源的关系。
    * ### 解决
        * ### 查看死锁：show engine innodb status \G。
        * ### 自动检测机制，超时自动回滚代价较小的事务 (innodb_lock_wait_timeout，默认 50 s)。
        * ### 人为解决，kill 阻塞进程 (show processlist)。
        * ### wait for graph 等待图 (主动检测)。
    * ### 如何避免
        * ### 加锁顺序一致，尽可能一次性锁定所需的数据行。
        * ### 尽量基于primary (主键) 或 unique key 更新数据。
        * ### 单次操作数据量不宜过多，涉及表尽量少。
        * ### 减少表上索引，减少锁定资源。
        * ### 尽量使用较低的隔离级别。
        * ### 尽量使用相同条件访问数据，这样可以避免间隙锁对并发的插入影响。
        * ### 精心设计索引，尽量使用索引访问数据。
        * ### 借助相关工具: pt-deadlock-logger。
* ### 乐观锁与悲观锁
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/MySQLPrinciples/GLockBLock.png)
    * ### 悲观锁
        * ### 解释: 假定会发生并发冲突，屏蔽一切可能违反数据完整性的操作。
        * ### 实现机制: 表锁、行锁等。
        * ### 实现层面: 数据库本身。
        * ### 适用场景: 并发量大。
    * ### 乐观锁
        * ### 解释: 假设不会发生并发冲突，只在提交操作时检查是否违反数据完整性。
        * ### 实现机制: 提交更新时检查版本号或者时间戳是否符合。
        * ### 实现层面: 业务代码。
        * ### 适用场景: 并发量小。
<br />

公共篇: MySQL Common Table Expression 公共表表示式 (從入門到改行)
=====
* ### MySQL 8.0 開始支援 !
* ### 什麼是公用表表示式 ?
    * ### 公用表表示式是一個命名的臨時結果集，僅存在於單個 SQL 語句 (如 SELECT、INSERT、UPDATE 或 DELETE) 的執行範圍。
    * ### 與衍生表 (派生表) 類似，CTE 不作為物件儲存，僅在查詢執行期間持續。
    * ### 與衍生表 (派生表) 不同，CTE 可以是自參照 (遞回 CTE)，也可以在同一查詢中多次參照。
    * ### 與衍生表 (派生表) 相比，CTE 提供了更好的可讀性和效能。
* ### MySQL CTE 語法
    * ### CTE 的結構包括名稱，可選列列表和定義 CTE 的查詢。
    * ### 定義 CTE 後，可以像 SELECT、INSERT、UPDATE、DELETE 或 CREATE VIEW 語句中的檢視一樣使用。
    ```
    # CTE 的基本語法
    # 查詢中的列數必須與 column_list 中的列數相同。
    # 如果省略 column_list，CTE 將使用定義 CTE 的查詢的列列表。

    WITH cte_name (column_list) AS (
        query
    )
    SELECT * FROM cte_name;
    ```
* ### 簡單的 MySQL CTE 範例
    ```
    # 使用 CTE 查詢範例資料庫 (yiibaidb) 中的 customers 表中的資料。

    WITH customers_in_usa AS (
        SELECT customerName, state
        FROM customers
        WHERE country = 'USA'
    )
    SELECT customerName
    FROM customers_in_usa
    WHERE state = 'CA'
    ORDER BY customerName;
    ```
    * ### 此範例中，CTE 的名稱為 customers_in_usa，定義 CTE 的查詢返回兩列: customerName 和 state。
    * ### 因此，customers_in_usa CTE 返回位於美國的所有客戶。
    * ### 在定義美國 CTE 的客戶之後，可在 SELECT 語句中參照它，例如僅查詢選擇位於 California 的客戶。
* ### 再來一個範例
    ```
    WITH topsales2013 AS (
        SELECT
            salesRepEmployeeNumber employeeNumber,
            SUM(quantityOrdered * priceEach) sales
        FROM orders
        INNER JOIN orderdetails USING (orderNumber)
        INNER JOIN customers USING (customerNumber)
        WHERE YEAR(shippedDate) = 2013 AND status = 'Shipped'
        GROUP BY salesRepEmployeeNumber
        ORDER BY sales DESC
        LIMIT 5
    )
    SELECT employeeNumber, firstName, lastName, sales
    FROM employees JOIN topsales2013 USING (employeeNumber);
    ```
    * ### 在這個例子中，CTE 返回了在 2013 年前五名的銷售代表。
    * ### 之後參照了 topsales2013 CTE 來獲取有關銷售代表的其他資訊，包括名字和姓氏。
* ### 更高階的 MySQL CTE 範例
    ```
    WITH salesrep AS (
        SELECT
            employeeNumber,
            CONCAT(firstName, ' ', lastName) AS salesrepName
        FROM employees
        WHERE jobTitle = 'Sales Rep'
    ), customer_salesrep AS (
        SELECT customerName, salesrepName
        FROM customers
        INNER JOIN salesrep ON employeeNumber = salesrepEmployeeNumber
    )
    SELECT *
    FROM customer_salesrep
    ORDER BY customerName;
    ```
    * ### 這個例子在同一查詢中有兩個 CTE。
    * ### 第一個 CTE (salesrep) 獲得職位是銷售代表的員工。
    * ### 第二個 CTE (customer_salesrep) 使用 INNER JOIN 子句與第一個 CTE 連線來獲取每個銷售代表負責的客戶。
    * ### 使用第二個 CTE 之後，透過帶有 ORDER BY 子句的簡單 SELECT 語句來查詢來自該 CTE 的資料。
* ### WITH 子句用法
    * ### 在 SELECT、UPDATE 和 DELETE 語句的開頭使用 WITH 子句。
        ```
        WITH ... SELECT ...
        WITH ... UPDATE ...
        WITH ... DELETE ...
        ```
    * ### 在子查詢或衍生表 (派生表) 子查詢的開頭使用WITH子句。
        ```
        SELECT ... WHERE id IN (WITH ... SELECT ...);
        SELECT * FROM (WITH ... SELECT ...) AS derived_table;
        ```
    * ### 在 SELECT 語句之前立即使用 WITH 子句 (包括 SELECT 子句)。
        ```
        CREATE TABLE ... WITH ... SELECT ...
        CREATE VIEW ... WITH ... SELECT ...
        INSERT ... WITH ... SELECT ...
        REPLACE ... WITH ... SELECT ...
        DECLARE CURSOR ... WITH ... SELECT ...
        EXPLAIN ... WITH ... SELECT ...
        ```
<br />

遞回篇: MySQL 遞回 Common Table Expression 公共表表示式 (樓上改行是對的)
=====
* ### MySQL 8.0 開始支援 !
* ### MySQL 遞回 CTE 簡介
    * ### 遞回公用表表示式 (CTE) 是一個具有參照 CTE 名稱本身的子查詢的 CTE。
    ```
    WITH RECURSIVE cte_name AS (
        initial_query  -- anchor member
        UNION ALL
        recursive_query -- recursive member that references to the CTE name
    )
    SELECT * FROM cte_name;
    ```
    * ### 遞回CTE由三個主要部分組成
        * ### 形成 CTE 結構的基本結果集的初始查詢 (initial_query)，初始查詢部分被稱為 "錨成員"。
        * ### 遞回查詢部分是參照 CTE 名稱的查詢，因此稱為遞回成員。
        * ### 遞回成員由一個 UNION ALL (保留表中重复行) 或 UNION DISTINCT (消去表中重复行) 運算子與錨成員相連。
        * ### 終止條件是當遞回成員沒有返回任何行時，確保遞回停止。
    * ### 遞回 CTE 的執行順序
        * ### 將成員分為兩個: "錨點" 和 "遞回" 成員。
        * ### 執行錨成員形成基本結果集 (R0)，並使用該基本結果集進行下一次疊代。
        * ### 將 Ri 結果集作為輸入執行遞回成員，並將 Ri+1 作為輸出。
        * ### 重複第三步，直到遞回成員返回一個空結果集，換句話說，滿足終止條件。
        * ### 使用 UNION ALL 運算子將結果集從 R0 到 Rn 組合。
* ### 遞回成員限制
    * ### 遞回成員不能包含以下結構
        * ### 聚合函式，如 MAX、MIN、SUM、AVG、COUNT 等。
        * ### GROUP BY 子句。
        * ### ORDER BY 子句。
        * ### LIMIT 子句。
        * ### DISTINCT。
    * ### 上述約束不適用於錨定成員。
    * ### 只有在使用 UNION 運算子時，不能包含 DISTINCT。
    * ### 如果使用 UNION DISTINCT 運算子，則允許使用 DISTINCT。
    * ### 遞回成員只能在其子句中參照 CTE 名稱，而不是參照任何子查詢。
* ### 簡單的 MySQL 遞回 CTE 範例
    ```
    WITH RECURSIVE cte_count (n) AS (
        SELECT 1
        UNION ALL
        SELECT n + 1
        FROM cte_count
        WHERE n < 3
    )
    SELECT n
    FROM cte_count;
    ```
    * ### 作為基本結果集返回 1 的錨成員: ```SELECT 1```。
    * ### 遞迴成員，參照了 cte_count 的 CTE 名稱: ```SELECT n + 1 FROM cte_count WHERE n < 3```。
    * ### 遞回成員中的表示式 "< 3" 是終止條件。
    * ### 當 n 等於 3，遞回成員將返回一個空集合，將停止遞回。
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/MySQLPrinciples/Recursive.png)
    * ### 遞回 CTE 返回以下輸出: n | 1 2 3。
    * ### 遞回CTE的執行步驟如下
        * ### 分離錨和遞回成員。
        * ### 錨定成員形成初始行 (SELECT 1)，因此第一次疊代在 n = 1 時產生 1 + 1 = 2。
        * ### 第二次疊代對第一次疊代的輸出 (2) 進行操作，並且在 n = 2 時產生 2 + 1 = 3。
        * ### 在第三次操作 (n = 3) 之前，滿足終止條件 (n < 3)，因此查詢停止。
        * ### 使用 UNION ALL 運算子組合所有結果集 1, 2 和 3。
* ### 使用 MySQL 遞回 CTE 遍歷分層資料
    ```
    # 使用 CTE 查詢範例資料庫 (yiibaidb) 中的 customers 表中的資料。
    # employees 表具有參照 employeeNumber 欄位的 reportsTo 欄位。
    # reportsTo 列儲存經理的 ID。
    # 總經理不會向公司的組織結構中的任何人報告，因此 reportsTo 列中的值為 NULL。

    WITH RECURSIVE employee_paths AS (
        SELECT employeeNumber, reportsTo managerNumber, officeCode, 1 lvl
        FROM employees
        WHERE reportsTo IS NULL
        UNION ALL
        SELECT
            e.employeeNumber,
            e.reportsTo,
            e.officeCode,
            lvl+1
        FROM employees e
        INNER JOIN employee_paths ep ON ep.employeeNumber = e.reportsTo
    )
    SELECT employeeNumber, managerNumber, lvl, city
    FROM employee_paths ep
    INNER JOIN offices o USING (officeCode)
    ORDER BY lvl, city;
    ```
    ```
    # 首先使用以下查詢形成錨成員，此查詢 (錨成員) 返回 reportTo 為 NULL 的總經理。

    SELECT employeeNumber, reportsTo managerNumber, officeCode
    FROM employees
    WHERE reportsTo IS NULL
    ```
    ```
    # 其次通過參照 CTE 名稱來執行遞回成員，在這個範例中為 employee_paths。
    # 此查詢 (遞回成員) 返回經理的所有直接上級，直到沒有更多的直接上級。
    # 如果遞回成員不返回直接上級，則遞回停止。

    SELECT e.employeeNumber, e.reportsTo, e.officeCode
    FROM employees e
    INNER JOIN employee_paths ep ON ep.employeeNumber = e.reportsTo
    ```
    ```
    最後使用 employee_paths 的查詢將 CTE 返回的結果集與 offices 表結合起來，以得到最終結果集合。
    ```
<br />

回傳篇: PostgreSQL 的 RETURNING 子句 (嗯...這個滿簡單的)
=====
* ### 有時在修改資料列的操作過程中取得資料是很方便的。
* ### INSERT、UPDATE 和 DELETE 指令都有一個選擇性的 ```RETURNING``` 子句來支持這個功能。
* ### 使用 ```RETURNING``` 可以避免執行額外的資料庫查詢來收集資料，特別是在難以可靠地識別修改的資料列時尤其有用。
* ### "RETURNING" 子句允許的語法與 SELECT 指令的輸出列表相同，它可以包含命令目標資料表的欄位名稱，或者包含使用這些欄位的表示式。
* ### 常用的簡寫形式是 ```RETURNING *```，預設是資料表的所有欄位，且相同次序。
* ### 在 INSERT 中，可用於 RETURNING 的資料是新增的資料列，這在一般的資料新增中並不是很有用，因為它只會重複用戶端所提供的資料，但如果是計算過的預設值就會非常方便，例如當使用串列欄位 (serial) 提供唯一識別時，RETURNING 可以回傳分配給新資料列的 ID:
    ```
    CREATE TABLE users (firstname text, lastname text, id serial primary key);

    INSERT INTO users (firstname, lastname)
    VALUES ('Joe', 'Cool')
    RETURNING id;
    ```
* ### 對於 INSERT ... SELECT，RETURNING 子句也非常有用。
* ### 在 UPDATE 中，可用於 RETURNING 的資料是被修改的資料列新內容，例如:
    ```
    UPDATE products
    SET price = price * 1.10
    WHERE price <= 99.99
    RETURNING name, price AS new_price;
    ```
* ### 在 DELETE 中，可用於 RETURNING 的資料是已刪除資料列的內容，例如:
    ```
    DELETE FROM products
    WHERE obsoletion_date = 'today'
    RETURNING *;
    ```
* ### 但是有一件很遺憾的事情: RETURNING is supported by Oracle and PostgreSQL but not by MySQL。
<br />

函數篇: MySQL 自定義函數 (從呼叫函數到呼叫破喉嚨)
=====
* ### 定義
    * ### 如果有一些复杂的业务逻辑在数据库层面就可以完成，无需在程序层面完成的时候，这时候就可以写成 MySQL 自定义函数。
    * ### 函数是指一组预编译好的 sql 语句集合，理解成批处理语句，必须有返回值，调用函数等于一次性执行了这些语句，有利降低语句重复编写和调用。
* ### 作用
    * ### 可以高度抽象业务逻辑，前置到数据库层面，而不是应用层面。
    * ### 相比于从数据库查询出来，然后程序操作数据，数据库操作一定程度上提高效率。
    * ### 高度可复用性，数据库层面的方法封装，不只是应用在多个同样业务场景，还可以应用到多个不同语言中。
* ### 函数的使用
    ```
    # 创建函数

    CREATE FUNCTION func_name([param_list]) RETURNS TYPE
    BEGIN
        -- Todo:function body
    END 
    ```
    ```
    # 调用函数

    SELECT func_name([param_list]);
    ```
    ```
    # 查看函数创建脚本

    SHOW CREATE FUNCTION func_name;
    ```
    ```
    # 查看函数信息

    SHOW FUNCTION STATUS;
    ```
    ```
    # 删除函数

    DROP FUNCTION IF EXISTS func_name;
    ```
* ### 示例
    ```
    # 数据基础

     1 mysql> select * from students;
     2 +-----------+-------------+-------+---------+
     3 | studentid | studentname | score | classid |
     4 +-----------+-------------+-------+---------+
     5 |         1 | brand       | 105.5 |       1 |
     6 |         2 | helen       | 98.5  |       1 |
     7 |         3 | lyn         | 97    |       1 |
     8 |         4 | sol         | 97    |       1 |
     9 |         5 | b1          | 89    |       2 |
    10 |         6 | b2          | 90    |       2 |
    11 |         7 | c1          | 76    |       3 |
    12 |         8 | c2          | 73.5  |       3 |
    13 |         9 | lala        | 73    |       0 |
    14 |        10 | A           | 100   |       3 |
    15 |        16 | test1       | 100   |       0 |
    16 |        17 | trigger2    | 107   |       0 |
    17 |        22 | trigger1    | 100   |       0 |
    18 +-----------+-------------+-------+---------+
    19 13 rows in set
    ```
    ```
    # 无参函数: 获取有班级号的所有同学的平均成绩

    DROP FUNCTION IF EXISTS fun_test1;
    
    DELIMITER $

    CREATE FUNCTION fun_test1() RETURNS DECIMAL(10, 2)
    BEGIN
        DECLARE avg_score DECIMAL(10, 2) DEFAULT 0;
        SELECT AVG(score) INTO avg_score
        FROM students
        where classid != 0;
        return avg_score;
    END $

    DELIMITER ;
    ```
    ```
    # 使用 select 调用，无需传入参数

    1 mysql> select fun_test1();
    2 +-------------+
    3 | fun_test1() |
    4 +-------------+
    5 | 91.83       |
    6 +-------------+
    7 1 row in set
    ```
    ```
    # 有参函数: 获取班级号为 1 的同学的平均成绩，参数 cid 为班级号

    DROP FUNCTION IF EXISTS fun_test2;

    DELIMITER $

    CREATE FUNCTION fun_test2(cid INT) RETURNS DECIMAL(10, 2)
    BEGIN
        DECLARE avg_score DECIMAL(10, 2) DEFAULT 0;
        SELECT AVG(score) INTO avg_score
        FROM students
        where classid = cid;
        return avg_score;
    END $

    DELIMITER ;
    ```
    ```
    # 使用 select 调用，传入参数 1 

    1 mysql> select fun_test2(1);
    2 +--------------+
    3 | fun_test2(1) |
    4 +--------------+
    5 | 99.5         |
    6 +--------------+
    7 1 row in set
    ```
* ### 存储过程和函数的区别
    * ### 存储过程的关键字为 procedure，返回值可以有多个，调用时用 call，一般用于执行比较复杂的的过程体、更新、创建等语句。
    * ### 函数的关键字为 function，返回值必须有一个，调用用 select，一般用于查询单个值并返回。
|  | 存储过程 | 函数 |
| -- | -- | -- |
| 返回值 | 可以有 0 个或者多个 | 必须有一个 |
| 关键字 | procedure | function |
| 调用方式 | call | select |
<br />

更新篇: PostgreSQL 9.4 引入特性: FILTER 子句 (夜深了...)
=====
* ### filter 子句可以对聚集函数增加过滤功能，仅对符合条件的子集进行聚集。
* ### 假设需要对一组数据执行 count 统计，同时需要统计奇数和偶数，可以在一个查询中使用 filter 进行实现:
    ```
    test=# SELECT
    test-#     count(*) count_all,
    test-#     count(*) FILTER(WHERE value % 2 = 1) count_1,
    test-#     count(*) FILTER(WHERE value % 2 = 0) count_2
    test-# FROM generate_series(1, 100, 1) as t(value);

    count_all | count_1 | count_2
    -----------+---------+---------
        100 |      50 |      50
    (1 行记录)
    ```
* ### FILTER 子句將实现簡單化，且提升了代码可读性，甚至優化了查询性能。
* ### FILTER 子句帮助过滤满足某些条件的数据子集，从而避免不必要的聚合函数。
* ### 註
    * ### 函數: generate_series(start, stop, step)
    * ### 参数类型: int 或 bigint
    * ### 返回类型: setof int 或 setof bigint (与参数类型相同)
    * ### 描述: 生成一个数值序列，从 start 到 stop，步进为 step
<br />

分頁篇: 有的時候總是會遇到要分頁的情況 (人生迷茫中...)
=====
* ### 今日主角: ROW_NUMBER()
* ### 用於排序的函數，可實作分頁功能，其會將查詢出的每一列資料加上一個序號 (從 1 開始遞增)，依次排序且不會重複。
* ### 使用時必須搭配 OVER 子句選擇對某一列進行排序才能生成序號。
* ### 初階使用
    ```
    # 根據 ID 進行排序並依序生成流水號 (從 1 開始)。

    SELECT
        ROW_NUMBER() OVER (
            ORDER BY ID ASC
        ) AS ROW_ID,
        *
    FROM CUSTOMERS
    ```
* ### 中階使用
    ```
    # 以 ADDRESS 為分組依據，
    # 並透過 ID 進行排序後依序生成流水號 (從 1 開始)。

    SELECT
        ROW_NUMBER() OVER (
            PARTITION BY ADDRESS
            ORDER BY ID ASC
        ) AS ROW_ID,
        *
    FROM CUSTOMERS
    ```
* ### 進階使用
    ```
    # 以 ADDRESS 為分組依據，
    # 並透過 ID 進行排序後依序生成流水號 (從 1 開始)，
    # 後印出每組的第一筆資料。

    SELECT *
    FROM (
        SELECT
            ROW_NUMBER() OVER (
                PARTITION BY ADDRESS
                ORDER BY ID ASC
            ) AS ROW_ID,
            *
        FROM CUSTOMERS
    ) AS RNC
    WHERE RNC.ROW_ID = 1 
    ```
* ### 使用 OFFSET ROWS
    ```
    # ORDER BY 是必須的。
    # OFFSET N ROWS 表示略過前 N 行，從第 N + 1 行開始。

    SELECT *
    FROM CUSTOMERS
    ORDER BY CUSTOMERS_ID 
    OFFSET 5 ROWS
    ```
* ### 使用 OFFSET ROWS 搭配 FETCH NEXT ROWS ONLY
    ```
    # ORDER BY 是必須的。
    # OFFSET N ROWS 表示略過前 N 行，從第 N + 1 行開始。
    # FETCH NEXT M ROWS ONLY 列出從第  N + 1 行開始的 M 筆資料。
    # 這個方法在 MSSQL 2012 版本 (含) 以上適用，以下怎麼辦呢，請看下去。

    SELECT *
    FROM CUSTOMERS
    ORDER BY CUSTOMERS_ID
    OFFSET 2 ROWS
    FETCH NEXT 8 ROWS ONLY
    ```
* ### 使用 ROW_NUMBER() 搭配 OVER (ORDER BY)
    ```
    # 在 MSSQL 2012 版以下的實作方法，
    # 等同於上一個範例的效果。

    SELECT *
    FROM (
        SELECT
            ROW_NUMBER() OVER (
                ORDER BY CUSTOMERS_ID
            ) AS ROW_ID,
            *
        FROM CUSTOMERS
    ) AS RNC
    WHERE RNC.ROW_ID > 2 AND RNC.ROW_ID <= 2 + 8
    ```
<br />

正規篇: 資料庫正規化 (就像埋在霧區裡的地雷，只要誤踩瞬間便會粉身碎骨。)
=====
* ### 資料庫正規化 (Database Normalization)，又稱正規化、標準化，是資料庫設計的一系列原理和技術，以減少資料庫中數據冗餘，增進數據的一致性。
* ### 正規化的過程就是將一些實體的描述資料，透過一定的程序將表單簡化，直到一張表單只單純描述一個事實為止。
* ### 去除資料庫中冗餘的內容，讓資料能夠井然有序且有效率的儲存。
* ### 執行正規化的理由
    * ### 提昇儲存資料與資料庫操作效率
    * ### 減少資料異常
    * ### 使資料庫維護更容易
* ### 經正規化後的特性
    * ### 欄位唯一性: 每個欄位只儲存一項資料。
    * ### 主關鍵欄位: 每筆資料都擁有一個主鍵，來區別這些資料。
    * ### 功能關聯性: 欄位之間的關聯應該要明確。
    * ### 欄位獨立性: 欄位之間不應存在遞移相依。
* ### 不符合正規化特性的資料表
    | 姓名 | 性別 | Gender | 項目 | 價格 | 數量 | 商店 | 地址 | 日期 | 訂單編號 |
    | - | - | - | - | - | - | - | - | - | - |
    | 阿寶 | 女 | F | 鉛筆、橡皮擦 | 20, 50 | 1, 2 | 久成久 | 東區大學路 | 12/17 | 1 |
    | 豆芽 | 女 | F | 牛奶、三明治 | 70, 10 | 2, 1 | 全家 | 東區北門路 | 12/18 | 2 |
    | 豆芽 | 女 | F | 牛奶、三明治 | 70, 10 | 3, 4 | 全家 | 東區北門路 | 12/19 | 3 |
    | 老皮 | 男 | M | 蛋餅、奶茶 | 30, 40 | 1, 2 | 日蝕 | 東區成功路 | 12/19 | 4 |
    * ### 此表儲存使用者的消費紀錄。
    * ### 問題: 項目和價格欄位中儲存了兩項以上的資料，且分隔這些資料的符號並不統一。
    * ### 問題: 性別和 Gender 這兩個欄位是重複的。
    * ### 問題: 沒有 Primary Key。
* ### 問題小記
    * ### 一個欄位儲存多筆資料
    * ### 出現意義上重複的欄位
    * ### 缺乏主鍵 (Primary Key)
* ### 第一正規化 (First Normal Form)
    * ### 需達成以下目標
        * ### 一個欄位只能有單一值
        * ### 消除意義上重複的欄位
        * ### 決定主鍵
    | 姓名 | 性別 | 項目 | 價格 | 數量 | 總金額 | 商店 | 地址 | 日期 | 訂單編號 |
    | - | - | - | - | - | - | - | - | - | - |
    | 阿寶 | 女 | 鉛筆 | 20 | 1 | 20 | 久成久 | 東區大學路 | 12/17 | 1 |
    | 阿寶 | 女 | 橡皮擦 | 50 | 2 | 100 | 久成久 | 東區大學路 | 12/17 | 1 |
    | 豆芽 | 女 | 牛奶 | 70 | 3 | 210 | 全家 | 東區北門路 | 12/18 | 2 |
    | 豆芽 | 女 | 三明治 | 10 | 1 | 10 | 全家 | 東區北門路 | 12/18 | 2 |
    | 豆芽 | 女 | 牛奶 | 70 | 3 | 210 | 全家 | 東區北門路 | 12/19 | 3 |
    | 豆芽 | 女 | 三明治 | 10 | 4 | 40 | 全家 | 東區北門路 | 12/19 | 3 |
    | 老皮 | 男 | 蛋餅 | 30 | 1 | 30 | 日蝕 | 東區成功路 | 12/19 | 4 |
    | 老皮 | 男 | 奶茶 | 40 | 2 | 80 | 日蝕 | 東區成功路 | 12/19 | 4 |
    * ### 問題: 每一筆消費紀錄皆儲存消費者的性別和商店的名稱與地址 (重複內容過多)。
    * ### 衍伸問題: 過多的重複內容，在插入與修改資料上會變得很複雜。
* ### 問題小記
    * ### 出現過多重複資料
* ### 第二正規化 (Second Normal Form)
    * ### 需達成以下目標
        * ### 消除部分相依
    * ### 實作方法
        * ### 新建獨立的表來儲存一直重複出現的欄位，後透過 Foreign Key 進行關聯。
    | ID | 姓名 | 性別 |
    | - | - | - |
    | 1 | 阿寶 | 女 |
    | 2 | 豆芽 | 女 |
    | 3 | 老皮 | 男 |
    
    | ID | 商店 | 地址 |
    | - | - | - |
    | 1 | 久成久 | 東區大學路 |
    | 2 | 全家 | 東區北門路 |
    | 3 | 日蝕 | 東區成功路 |
    
    | ID | 項目 | 價格 | 商店 ID |
    | - | - | - | - |
    | 1 | 鉛筆 | 20 | 1 |
    | 2 | 橡皮擦 | 50 | 1 |
    | 3 | 牛奶 | 70 | 2 |
    | 4 | 三明治 | 10 | 2 |
    | 5 | 蛋餅 | 30 | 3 |
    | 6 | 奶茶 | 40 | 3 |
    
    | ID | 消費者 ID | 商品 ID | 數量 | 總金額 | 日期 | 訂單編號 |
    | - | - | - | - | - | - | - |
    | 1 | 1 | 1 | 1 | 20 | 12/17 | 1 |
    | 2 | 1 | 2 | 2 | 100 | 12/17 | 1 |
    | 3 | 2 | 3 | 3 | 210 | 12/18 | 2 |
    | 4 | 2 | 4 | 1 | 10 | 12/18 | 2 |
    | 5 | 2 | 3 | 3 | 210 | 12/19 | 3 |
    | 6 | 3 | 4 | 4 | 40 | 12/19 | 3 |
    | 7 | 3 | 5 | 1 | 30 | 12/19 | 4 |
    | 8 | 3 | 6 | 2 | 80 | 12/19 | 5 |
    * ### 問題: 遞移關係 (總金額依賴商品及數量資訊，而商品 ID 和數量又和主鍵直接相關)
    * ### 衍伸問題: 可能發生數量改變而總金額沒改變的資料錯誤。
* ### 問題小記
    * ### 存在主鍵以外的欄位與主鍵間接 (遞移) 相依
* ### 第三正規化 (Third Normal Form)
    * ### 需達成以下目標
        * ### 消除遞移相依
    * ### 實作方法
        * ### 非主鍵屬性的欄位都只能和候選鍵相關，非主鍵屬性的欄位彼此間應該要是獨立無關的。
    * ### 名詞解釋
        * ### 遞移相依: 欄位 1 和主鍵相關，欄位 2 和欄位 1 相關，欄位 2 和主鍵為遞移相依。
        * ### 候選鍵: 欄位組合讓資料能是唯一的，並且是最小唯一。
    | ID | 消費者 ID | 單價 | 數量 | 商品 ID | 日期 | 訂單編號 |
    | - | - | - | - | - | - | - |
    | 1 | 1 | 20 | 1 | 1 | 12/17 | 1 |
    | 2 | 1 | 50 | 2 | 2 | 12/17 | 1 |
    | 3 | 2 | 70 | 3 | 3 | 12/18 | 2 |
    | 4 | 2 | 10 | 1 | 4 | 12/18 | 2 |
    | 5 | 2 | 70 | 3 | 3 | 12/19 | 3 |
    | 6 | 3 | 10 | 4 | 4 | 12/19 | 3 |
    | 7 | 3 | 30 | 1 | 5 | 12/19 | 4 |
    | 8 | 3 | 40 | 2 | 6 | 12/19 | 4 |
* ### 資料庫正規化要進行到的程度，應視對資料庫操作的需求和資料量而定，而非每次建表都需完全符合正規化的規範。
* ### Database Normalization 步驟參考
    * ### 第一正規化 (First Normal Form): 一個欄位只能有單一值、消除意義上重複的欄位、決定主鍵。
    * ### 第二正規化 (Second Normal Form): 消除部分相依。
    * ### 第三正規化 (Third Normal Form): 消除遞移相依。
<br />

視圖篇: Creating PostgreSQL Updatable Views (MBTI 我是 ISFJ-T)
=====
* ### Summary: in this tutorial, we will discuss the requirements for updatable views and show you how to create updatable views in PostgreSQL.
* ### A PostgreSQL view is updatable when it meets the following conditions:
    * ### The defining query of the view must have exactly one entry in the ```FROM``` clause, which can be a table or another updatable view.
    * ### The defining query must not contain one of the following clauses at the top level: GROUP BY, HAVING, LIMIT, OFFSET, DISTINCT, WITH, UNION, INTERSECT, and EXCEPT.
    * ### The selection list must not contain any window function, any set-returning function, or any aggregate function such as SUM, COUNT, AVG, MIN, and MAX.
* ### An updatable view may contain both updatable and non-updatable columns. If you try to insert or update a non-updatable column, PostgreSQL will raise an error.
* ### When you execute an update operation such as INSERT, UPDATE or DELETE, PosgreSQL will convert this statement into the corresponding statement of the underlying table.
* ### In case you have a WHERE condition in the defining query of a view, you still can update or delete the rows that are not visible through the view. However, if you want to avoid this, you can use ```CHECK OPTION``` when you define the view.
* ### When you perform update operations, you must have corresponding privilege on the view, but you don’t need to have privilege on the underlying table. However, view owners must have the relevant privilege of the underlying table.
* ### PosgreSQL updatable views example
    * ### First, create a new updatable view name ```usa_cities``` using ```CREATE VIEW``` statement. This view contains all cities in the ```city``` table locating in the USA whose country id is 103.
        ```
        CREATE VIEW usa_cities AS
        SELECT city, country_id
        FROM city
        WHERE country_id = 103;
        ```
    * ### Next, check the data in the ```usa_cities``` view by executing the following ```SELECT``` statement:
        ```
        SELECT *
        FROM usa_cities;
        ```
    * ### Then, insert a new ```city``` to the city table through the ```usa_cities``` view using the following ```INSERT``` statement:
        ```
        INSERT INTO usa_cities (city, country_id) VALUES ('San Jose', 103);
        ```
    * ### After that, check the contents of the ```city``` table:
        ```
        SELECT city, country_id
        FROM city
        WHERE country_id = 103
        ORDER BY last_update DESC;
        ```
    * ### We have a newly entry added to the ```city``` table.
    * ### Finally, delete the entry that has been added through the ```usa_cities``` view.
        ```
        DELETE FROM usa_cities
        WHERE city = 'San Jose';
        ```
    * ### The entry has been deleted from the ```city``` table through the ```usa_cities``` view.
    * ### In this tutorial, we have shown how to create PostgreSQL updatable views and introduced you to conditions that views must satisfy to become automatically updatable
<br />

Reference
=====
* ### 資料庫解剖學：從內部深解 MySQL 運作原理
<br />
