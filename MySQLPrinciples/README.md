MySQLPrinciples
=====
* ### 守則篇: MySQL Design Principles (從刪庫到跑路)
* ### 番外篇: Stored Procedure (從蒙圈到無限茫然)
* ### 觸發篇: Introduction To MySQL Triggers (從看懂到看開)
* ### 物化篇: Materialized View (還沒入門就奪門而逃)
* ### 約束篇: CHECK Constraint In MySQL Isn't Working (從入門到女裝)
* ### Chapter01 裝作自己是個小白 -- 初識 MySQL
* ### Chapter02 MySQL 的調控按鈕 -- 啟動選項和系統變數
* ### Chapter03 字元集和比較規則
* ### Chapter04 從一筆記錄說起 -- InnoDB 記錄儲存結構
* ### Chapter05 盛放記錄的大盒子 -- InnoDB 資料頁結構
* ### Chapter06 快速查詢的秘笈 -- B+ 樹索引
* ### Chapter07 B+ 樹索引的使用
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
    * ### Query Hinting: Use the OPTIMIZE FOR query hint. This tells SQL Server to use a specified value when compiling the plan. If you can find a value that produces a “good enough” plan each time, and the performance is acceptable for each case, this is a good option for you. But the biggest drawback with OPTIMIZE FOR is on tables where the distribution of data changes.
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
<br />

Reference
=====
* ### 資料庫解剖學：從內部深解 MySQL 運作原理
<br />
