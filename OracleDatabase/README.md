OracleDatabase
=====
* ### Oracle Database (19c), 資料庫軟體。
* ### SQL Developer, 圖形整合發展軟體。
* ### Data Modeler, 建模工具軟體。
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
* ### Database Performance Tuning
    * ### Index 建立
    * ### I/O 流量減少
    * ### Stored Procedure
* ### Stored Procedure 優點
    * ### 減少流量
    * ### 提升安全
    * ### 效能優化
    * ### 可以接受參數
* ### Execute SQL Server Stored Procedure From Python
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
* ### Schema, 泛指 Table、View、Index、Row 等, 是形式描述語言的一種結構 (不包含資料)。
* ### DDL, Data Definition Language, 無需 commit (CREATE、DROP)。
* ### DML, Data Manipulation Language, 需 commit (SELECT、INSERT、UPDATE、DELETE)。
* ### DCL, Data Control Language, 授權相關。
* ### TCL, Transaction Control Language (SAVEPOINT、ROLLBACK)。
* ### 實體關聯圖 ERD (Entity Relation Diagram)。
* ### 鳥爪模型 (Crow's Foot Model)。
* ### 順向工程: ERD to SQL。
* ### 交易的開始與結束
    * ### 執行 COMMIT 或 ROLLBACK 命令。
    * ### 執行一個 DDL 或 DCL。
    * ### 用戶退離 SQL Developer。
    * ### 系統當機。
* ### COMMIT: 確認異動資料，寫入硬碟，執行前皆可透過 ROLLBACK 反悔。
* ### ROLLBACK: 取消當前異動。
* ### SAVEPOINT: 標記 ROLLBACK 倒回點。
* ### 交易自動 COMMIT
    * ### 一個 DDL 或 DCL 命令。
    * ### 正常退出 SQL Developer。
* ### 交易自動 ROLLBACK
    * ### SQL Developer 異常關閉。
    * ### 系統當機。
* ### 交易確認前的狀態
    * ### 交易在主記憶體資料緩衝區內進行，可被復原。
    * ### 其他用戶 SELECT 所查詢的是尚未 COMMIT 資料。
    * ### 當前用戶 SELECT 所查詢的是緩衝區內資料。
    * ### 受交易影響的資料列會被鎖住，其他人同時間無法針對該資料列進行異動。
* ### 交易確認後的狀態
    * ### 新資料將覆蓋舊資料。
    * ### 異動資料被永久寫入硬碟。
    * ### 所有被授權用戶皆可查詢異動結果。
    * ### 系統釋放鎖住的資料列。
    * ### 所有 SAVEPOINT 被清除。
* ### 倒回注意事項
    * ### 單一的一個 DML 命令執行發生錯誤，只有受該命令影響的資料列會被倒回。
    * ### Oracle Server 在 DDL 命令前後均會自動執行隱性 COMMIT，故無法再進行 ROLLBACK。
<br />

Reference
=====
* ### Oracle 資料庫 SQL 學習經典 -- 融入 OCA DBA 國際認證
