OracleDatabase
=====
* ### Oracle Database (19c), 資料庫軟體。
* ### SQL Developer, 圖形整合發展軟體。
* ### Data Modeler, 建模工具軟體。
* ### Database Performance Tuning
    * ### Index 建立
    * ### I/O 流量減少
    * ### Stored Procedure
* ### Schema, 泛指 Table、View、Index、Row 等, 是形式描述語言的一種結構 (不包含資料)。
* ### DDL, Data Definition Language, 無需 commit (CREATE、DROP、ALTER)。
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
* ### 資料庫的其它物件
    * ### 物件同義詞 SYNONYM: 物件別名，簡化物件冗長名稱。
    * ### 序列 SEQUENCE: 獨立於資料表外，可被共用，並循環的按指定起始值、遞增值與最終值產生一序列的整數值，可應用於產生不重複整數值場合。
    * ### 視觀表 VIEW: 由一到多個 SELECT 語句組成，方便檢索無需每次下達複雜指令，可用於併表操作場景。
    * ### 索引 INDEX: 當針對沒有建立索引的資料表檢索時，系統會透過掃描整張表 (Full table scan) 方式找尋資料，若在欄位上建立索引，系統則以指標 (Pointer) 方式，索引化路徑 (Indexed path) 快速尋找資料。
    * ### 用戶自訂類型 User - defined Data Type: 將具有複雜屬性的實體表達成單個物件。
* ### 建議使用索引
    * ### 欄位儲存值範圍大。
    * ### 欄位有大量空值。
    * ### 欄位常用於 WHERE 子句。
    * ### 預期檢索資料量經常 < 4% 的大量資料表。
 * ### 不建議使用索引
    * ### 欄位不經常用於條件式。
    * ### 需要經常更新的資料表。
    * ### 小資料量資料表。
    * ### 預期檢索資料量經常 > 4% 的大量資料表。
* ### Oracle 資料庫存取權限
    * ### 系統權限 System Privilege，如登入資料庫或建立資料表。
    * ### 物件權限 Object Privilege，如對某資料表進行 SELECT。
    * ### 角色權限 Role Privilege，System Privilege + Object Privilege, 組合包。
* ### 檢索控制資訊 (資料字典): 資料字典 (Data Dictionary) 貯存資料庫邏輯、物理結構和正在進行操作的相關資料之 meta 數據。具體的說，Oracle 資料庫的資料字典是由基本表格和使用者可存取的資料字典視觀表組成 (如可透過其查詢用戶、用戶狀態與帳號過期時間等)。
<br />

Reference
=====
* ### Oracle 資料庫 SQL 學習經典 -- 融入 OCA DBA 國際認證
