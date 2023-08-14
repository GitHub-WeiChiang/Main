01 - NoSQL 與 MongoDB 簡介
=====
* ### NoSQL 資料庫的四種形式: Key - Value、Document - Based、Column、Graph。
* ### Key - Value: Redis、Memcached。
* ### Document - Based
    * ### 儲存複雜鍵值對資料，例如 XML、HTML、JSON。
    * ### 每一份文件具有一個唯一識別碼。
    * ### 不同格式文件可以儲存於同一處。
    * ### 文件格式無需事先定義。
    * ### 代表性資料庫: MongoDB。
* ### Column
    | 學號 | 姓名 | 年級 | 數學 |
    | - | - | - | - |
    | S1 | David | 1 | 80 |
    | S2 | Emma | 1 | 85 |
    | S3 | Eric | 2 | 70 |
    * ### Row 資料庫中: ```[S1][David][1][80][S2][Emma][1][85][S3][Eric][2][70]```。
        * ### 新增資料快速。
        * ### 分析讀取效率較低。
    * ### Column 資料庫中: ```[S1][S2][S3][David][Emma][Eric][1][1][2][80][85][70]```。
        * ### 新增資料緩慢。
        * ### 分析讀取效率較高。
    * ### 代表性資料庫: Cassandra、HBase。
* ### Graph: Neo4j、JanusGraph。
* ### MongoDB 介紹
    * ### MongoDB 將一筆資料稱做是一份文件 (Document)。
    * ### MongoDB Atlas: 雲端資料庫服務，可以在 AWS、Azure 和 Google Cloud 建立託管服務，包含建立高可用性 (replication) 與水平擴展 (sharding) 的功能，除此之外還有對外的防護、自動備份機制、全面的監控和告警。
* ### JSON 與 BSON
    * ### MongoDB 內部會將 JSON 轉成 BSON 進行儲存，讀取時再轉回 JSON。
    * ### JSON 資料型態: String、Number、Object、Array、Boolean、Null。
    * ### BSON 的改進
        * ### 更多的資料型態: Number 被細分為 Double、Int、Long、Decimal 等。
        * ### 將 TEXT 格式轉為 Binary 格式，加快解析速度並可儲存文字無法表示的資料，例如日期物件。
* ### ObjectId
    * ### MongoDB 會為每一筆資料自動加上 "_id"，預設內容為 ObjectId，由 ObjectId() 函數產生。
    * ### ObjectId 的組成: timestamp + random + counter。
    * ### 對同一資料表而言，ObjectId 保證不重複 (重複儲存會產生 error)。
    ```
    mongosh

    ObjectId()
    # ObjectId("64da0d4e22075c9758416829")

    ObjectId().getTimestamp()
    # ISODate("2023-08-14T11:19:02.000Z")
    ```
* ### Timestamp of BSON
    * ### 組成: UNIX epoch time + 流水號。
* ### Date of BSON
    * ### 單位: 豪秒 (milliseconds)。
    ```
    new Date()
    # ISODate("2023-08-14T11:23:49.279Z")

    (new Date()).toString()
    # Mon Aug 14 2023 19:23:34 GMT+0800 (台北標準時間)
    ```
* ### 文件與相關名詞對照
    * ### MongoDB 儲存的資料稱為文件，一份文件指的是字典，若為陣列則表示多份文件。
    * ### 文件中的文件稱為 "子文件"。
    * ### MongoDB 中儲存多份文件的區域稱為聚集 (Collection)，在 RDB 中稱為 Table。
    | RDB | MongoDB | 中文翻譯 |
    | - | - | - |
    | Database | Database | 資料庫 |
    | Table | Collection | 資料表、聚集 |
    | Row | Document | 資料、文件 |
    | Column | Field | 欄位、鍵名 |
    | Primary Key | ObjectId | 主鍵 |
    | View | View | 視觀表 |
<br />
