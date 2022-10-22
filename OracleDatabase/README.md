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
<br />

Reference
=====
* ### Oracle 資料庫 SQL 學習經典 -- 融入 OCA DBA 國際認證
