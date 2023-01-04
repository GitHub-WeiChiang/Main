MySQLPrinciples
=====
* ### 番外篇: Stored Procedure (從蒙圈到無限茫然)
* ### Chapter01 裝作自己是個小白 -- 初識 MySQL
* ### Chapter02 MySQL 的調控按鈕 -- 啟動選項和系統變數
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

Reference
=====
* ### 資料庫解剖學：從內部深解 MySQL 運作原理
<br />
