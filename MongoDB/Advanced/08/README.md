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
    * ### 複合欄位索引: 讓一個索引中包含多個欄位 (多欄位同時作為搜索條件時)。
        * ### 建立索引時，按下旁邊的符號 "+"，生成複合欄位索引。
    * ### 索引前綴與索引排序
        * ### 面對 "複合欄位索引"，即便查詢條件沒有使用到索引中的所有欄位，還是有可能啟動該 "複合欄位索引"，這就是 "索引前綴 (Index Prefixes)"。
        * ### 當複合索引為 ```[("a", 1), ("b", 1), ("c", -1)]``` 時，索引前綴為 "a" 與 "ab"。
        * ### 當查詢結果需要排序，不論順向或逆向，"單一欄位索引" 都有可能被觸發。
        * ### "複合欄位索引" 的觸發時機
            * ### 狀況一: 當查詢結果需要排序且為下述六種狀況之一，有機會觸發 "複合欄位索引"。
                ```
                # 索引與索引前綴
                
                [("a", 1), ("b", 1), ("c", -1)]
                [("a", 1), ("b", 1)]
                [("a", 1)]
                ```
                ```
                # 列出反向排序
                
                [("a", -1), ("b", -1), ("c", 1)]
                [("a", -1), ("b", -1)]
                [("a", -1)]
                ```
            * ### 狀況二: 當搜索條件或排序可以使用索引時，合在一起就有機會觸發 "複合欄位索引"。
                ```
                db.test.find({"a": "on"}).sort("c", 1)
                
                db.test.find({"a": "on"}).sort("b", -1)
                
                db.test.find({"c": "light"}).sort([("a", -1), ("b", -1)])
                ```
    * ### 多鍵索引: 當欄位資料型態為陣列，由該欄位建立的索引稱為 "多鍵索引"。
        * ### 可以透過萬用字元 "$**" 建立子文件中所有鍵值索引。
    * ### 文字索引: 針對文件中的字串欄位建立索引，提升原文搜尋的速度。
        * ### 暫時不支援中文。
        ```
        # 全文檢索 (預設不區分大小寫)
        
        {"$text": {"$search": "..."}}
        ```
        ```
        # 全文檢索 (區分大小寫)
        
        {
            "$text": {
                "$search": "...",
                "$caseSensitive": True
            }
        }
        ```
        * ### 執行檢索時，英文中常見的定冠詞或介系詞會被忽略。
        * ### $search 支援多關鍵字檢索 (透過空白鍵區隔即可) 且可透過 "-" 表示否定。
        ```
        # 搜尋關鍵字但排除指定文字
        
        {
            "$text": {
                "$search": "... -..."
            }
        }
        ```
    * ### 2dsphere 球體座標索引: 用於格式符合 GeoJSON 的經緯度座標資料索引建立。
        * ### 用於經緯度座標查詢指令功能
            * ### 距離指定坐標最近的資料。
            * ### 指定坐標範圍內所有資料。
            * ### 指定坐標範圍內所有資料並按近遠排序。
        * ### GeoJSON 格式範例
            ```
            "geometry": {
                "type": "Point",
                "coordinates": [..., ...]
            }
            ```
            * ### type: 表示 coordinates 是代表點、線或區域。
            * ### Point: 表示點。
            * ### coordinates: 表示經緯度座標，先經度後緯度。
            ```
            # 表示直線
            
            "geometry": {
                "type": "LineString",
                "coordinates": [
                    [..., ...], [..., ...]
                ]
            }
            ```
            ```
            # 表示區域範圍: 以三角形區域為例，座標頭尾需重疊。
            
            "geometry": {
                "type": "Polygon",
                "coordinates": [
                    # 第一個角的座標
                    [..., ...],
                    # 第二個角的座標
                    [..., ...],
                    # 第三個角的座標
                    [..., ...],
                    # 第一個角的座標
                    [..., ...]
                ]
            }
            ```
            ```
            # 表示多個座標點
            
            "geometry": {
                "type": "MultiPoint",
                "coordinates": [
                    [..., ...],
                    [..., ...],
                    [..., ...]
                ]
            }
            ```
    * ### 2d 平面座標索引: 用於非 GeoJSON 格式或座標並不在球體上時的座標資料 2d 類型索引建立。
        ```
        db.collection.create_index([("point", "2d")])
        ```
    * ### 特定語系索引 (針對中文的第一個字進行筆畫數排序)
        * ### 左側選擇 Database。
        * ### 左側選擇 Collection。
        * ### 點擊 Indexes。
        * ### 點擊 Create Index。
        * ### 點擊 Options。
        * ### 勾選 Use Custom Collation。
        * ### 輸入 Collation Document:
            ```
            {
               locale: <string>,
               caseLevel: <boolean>,
               caseFirst: <string>,
               strength: <int>,
               numericOrdering: <boolean>,
               alternate: <string>,
               maxVariable: <string>,
               backwards: <boolean>
            }
            ```
            ```
            // 以針對中文的第一個字進行筆畫數排序為例
            
            {
               "locale": "zh_Hant"
            }
            ```
    * ### 萬用字元索引
        * ### 透過 "$**" 表示針對該文件的所有欄位 (包含子文件中的所有欄位) 全部建立單一欄位索引。
        * ### 可以透過勾選 Options 中的 Wildcard Projection 排除不需要建立索引的欄位。
            ```
            // 排除某些欄位
            
            {"...": 0, "...": 0, ...}
            ```
            ```
            // 僅建立某些欄位
            
            {"...": 1, "...": 1, ...}
            ```
* ### 索引屬性
<br />

範例程式
=====
* ### 8_2.py: 在 Python 程式中建立索引。
<br />
