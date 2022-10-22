OracleDatabase
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
<br />

Reference
=====
* ### Oracle 資料庫 SQL 學習經典 -- 融入 OCA DBA 國際認證
