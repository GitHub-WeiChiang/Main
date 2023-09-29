08 - 索引
=====
* ### 索引的目的
    * ### 索引的目的是為了加快資料搜尋速度。
    * ### 在完全沒有索引的情況下，只能採用 "線性搜尋"，時間複雜度為 O(n)。
    * ### 搜尋效率遠高於線性搜尋的方式為 "二位元搜尋 (建立索引)"，時間複雜度為 O(log n)。
    * ### 二位元搜尋資料時，會先將資料排序後建立樹狀結構。
        * ### MongoDB 官方文件指出，其採用 B Tree。
        * ### 儲存引擎 WiredTiger 官方文件指出，其採用 B+ Tree。
        * ### 理解更多 -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/Questions/Question045)
    * ### 理解更多 -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/MySQLPrinciples)
* ### 建立方式
    * ### MongoDB Compass (推薦)
        * ### 左側選擇 Database。
        * ### 左側選擇 Collection。
        * ### 點擊 Indexes。
        * ### 點擊 Create Index。
    * ### Python: 8_2.py。
    * ### 註: 預設的 "_id" 欄位會自動建立索引，不可修改且無法刪除。
* ### 索引種類
    * ### 單一欄位索引: 針對查詢中經常會拿來做查詢條件的欄位設定索引。
        * ### 建立索引時，索引名稱可省略 (MongoDB 自己會想辦法)。
        * ### 設定索引方向: 順向為 1 (asc)，逆向為 -1 (desc)。
        * ### MongoDB Compass 中可以查看索引佔用硬碟空間與使用次數。
        ```
        // 測試索引使用次數
        
        test> use opendata
        switched to db opendata
        opendata> db.AQI.find({"SiteName": "豐原"})
        ```
    * ### 複合欄位索引
<br />

範例程式
=====
* ### 8_2.py: 在 Python 程式中建立索引。
<br />
