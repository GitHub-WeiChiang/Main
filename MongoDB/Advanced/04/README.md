04 - Aggregation 進階查詢
=====
* ### Aggregation vs. Find
    * ### Find 只能對資料進行一次的運算處理。
    * ### Aggregation 可以對資料進行多次運算後才取得結果 (例如某 Collection 中特定的 Field 平均值)。
* ### Aggregation 利用 Pipeline 的方式處理資料。
* ### Pipeline 包含一或數個資料處理階段 Stage，每一個 Stage 會將上一個 Stage 輸出資料經過處理後傳給下一個 Stage，直到最後。
* ### 若想計算 AQI 欄位的平均值，可以設計，第一個 Stage 將 AQI 型態由字串轉為數字，第二個 Stage 進行分群後平均值計算。
* ### 4_3.py: 生成各縣市平均 AQI 指標與 View 的讀取。
    * ### Stage 1: 將 AQI 欄位的字串型態轉成 Int 型態後放到 iAQI 欄位中，iAQI 是一個新增欄位，不會改變原始資料內容，且只暫存於記憶體中，執行完即棄用。
        * ### 開啟 Compass 的 Aggregation 分頁。
        * ### 點擊 Add Stage 並選擇 $addFields。
        * ### 填入下方內容
            ```
            {
              "iAQI": {
                "$toInt": "$AQI"
              }
            }
            ```
            * ### iAQI: 新欄位名稱。
            * ### $toInt: 型別轉換運算子。
            * ### $AQI: 要轉換成整數的欄位 (雙引號代表這是一個欄位而非內建系統函數、比索符號若省略則代表被轉換的資料來源為字串 AQI)。
        * ### 點擊 EXPORT TO LANGUAGE。
    * ### Stage 2: 將 County 名稱一樣的資料圈在一起，計算各個群組中 iAQI 欄位的平均值。
        * ### 開啟 Compass 的 Aggregation 分頁。
        * ### 點擊 Add Stage 並選擇 $group (會將 _id 欄位內容一樣的資料群組起來)。
        * ### 填入下方內容
            ```
            {
              "_id": "$County",
              "averageAQI": {
                "$avg": "$iAQI"
              }
            }
            ```
            * ### $County: 分群的依據。
            * ### averageAQI: 運算結果的欄位。
            * ### $avg: 平均值運算子。
            * ### $iAQI: 要被計算的欄位。
        * ### 點擊 EXPORT TO LANGUAGE。
        * ### 備註: 若想計算所有資料的 $iAQI 欄位平均值，只要將 _id 欄位設定為 1 或是 null 即可。
    * ### Stage 3: 顯示資料時，averageAQI 欄位只顯示整數部分。
        * ### 開啟 Compass 的 Aggregation 分頁。
        * ### 點擊 Add Stage 並選擇 $project (用於輸出結果欄位選擇與格式設定)。
        * ### 填入下方內容
            ```
            {
              "averageAQI": {
                "$round": ["$averageAQI", 0]
              }
            }
            ```
            * ### averageAQI: 運算結果的欄位。
            * ### $round: 四捨五入運算子。
            * ### $averageAQI: 要被計算的欄位。
            * ### 0: 只取整數部分。
        * ### 點擊 EXPORT TO LANGUAGE。
    * ### Stage 4: 按照各縣市平均 AQI 數值由小到大進行排序。
        * ### 開啟 Compass 的 Aggregation 分頁。
        * ### 點擊 Add Stage 並選擇 $sort。
        * ### 填入下方內容
            ```
            {
              "averageAQI": 1
            }
            ```
            * ### averageAQI: 排序的依據。
            * ### 1: 由小到大 (-1 則為由大到小)。
        * ### 點擊 EXPORT TO LANGUAGE。
* ### 將設計的 Pipeline 存成 View。
    * ### 按下 SAVE。
    * ### 按下 Create view。
    * ### 取名為 vw_average_aqi。
    * ### 按下 Create。
* ### 常用 Stage 介紹
    * ### 桶型計算: 將資料按照特定範圍進行群組。
        * ### 使用 AQI 作為來源資料，並且按到 AQI 數值所定義的污染程度來群組資料。
        * ### Stage 1 - $addFields: 將字串型態的 AQI 轉成整數型態放到 iAQI 欄位 (AQI 值為空則設定為 -1)。
            ```
            {
            	"iAQI": {
                "$cond": {
                  "if": {
                    "$eq": ["$AQI", ""]
                  },
                  "then": -1,
                  "else": {
                    "$toInt": "$AQI"
                  }
                }
              }
            }
            ```
        * ### Stage 2 - $bucket: 根據 AQI 的污染程度分類，進行桶型計算。
            ```
            {
              "groupBy": "$iAQI",
              "boundaries": [0, 51, 101, 151, 201, 301, 1000],
              "default": "error",
              "output": {
                "count": {
                  "$sum": 1
                },
                "location": {
                  "$push": {
                    "County": "$County",
                    "SiteName": "$SiteName",
                    "iAQI": "$iAQI"
                  }
                }
              }
            }
            ```
            * ### groupBy: 群組依據。
            * ### boundaries: 群組區段。
            * ### default: 不在群組區段內的其它數值。
            * ### output: 輸出資料。
                * ### count: 群組區段內資料筆數。
                * ### location: 透過 $push 運算子放置原始資料的欄位數值。
    * ### 資料筆數: 用於計算上一個 Stage 輸出的資料筆數。
        * ### $count: 計算資料筆數。
            ```
            "total"
            ```
        * ### $group: 計算每個縣市有多少空氣品質檢測站。
            ```
            {
              "_id": "$County",
              "count": {
                "$sum": 1
              }
            }
            ```
    * ### 依經緯度排序: 根據經緯度座標產生由近到遠的資料排序。
        * ### 使用條件
            * ### 符合 GeoJSON 格式，先經度後緯度。
            * ### 需建立經緯度座標索引。
            * ### 必需為 Pipeline 的第一個 Stage。
            * ### 無法在 View 上使用。
        * ### Stage 1.1 - $addFields: 將 AQI 中的經緯度欄位內容轉成 GeoJSON 格式。
            ```
            {
              "geometry": {
                "type": "Point",
                "coordinates": [
                  {
                    "$toDouble": "$Longitude"
                  },
                  {
                    "$toDouble": "$Latitude"
                  }
                ]
              }
            }
            ```
        * ### Stage 1.2 - $project: 留下需要的欄位 (SiteName、County、AQI 與 geometry)。
            ```
            {
              "_id": 0,
              "County": 1,
              "SiteName": 1,
              "geometry": 1,
              "AQI": {
                "$toInt": "$AQI"
              }
            }
            ```
        * ### Stage 1.3 - $out: 將資料儲存到另一個資料表 AQI_geo (按下 RUN)。
            ```
            "AQI_geo"
            ```
            * ### 建立型態為 2dsphere 索引
                * ### 選擇 AQI_geo 資料表。
                * ### 按下 Indexes。
                * ### 按下 Create Index。
                * ### 選擇 geometry + 2dsphere
                * ### 按下 Create Index。
        * ### Stage 2 - $geoNear: 針對資料表的經緯度資訊進行排序 (選擇 AQI_geo 資料表)。
            ```
            {
              "near": {
                "type": "Point",
                "coordinates": [121.5466, 25.15532]
              },
              "distanceField": "distance",
              "maxDistance": 5000,
              "includeLocs": "geometry",
              "query": {
                "County": {
                  "$in": ["臺北市", "新北市"]
                }
              }
            }
            ```
            * ### near: 基準點座標 (可能為使用者所在位置，上述以陽明山遊客中心為例)。
            * ### distanceField: 存放與基準點間的距離，欄位名稱為 distance (單位為公尺)。
            * ### maxDistance: 搜尋的最大範圍 (單位為公尺)。
            * ### includeLocs: 存放原本的經緯度座標資訊，欄位名稱為 geometry。
            * ### query: 設定搜尋條件 (上述僅搜尋臺北市與新北市，省略則代表搜尋全部資料)。
    * ### 限制與忽略: 用於限制與忽略所需輸出的資料筆數與位置 (熟悉的分頁功能)。
        * ### 目標: 顯示從第四筆開始的連續四筆資料。
        * ### Stage 1 - $skip: 忽略指定筆數後再進行輸出。
            ```
            4
            ```
        * ### Stage 2 - $limit: 限制輸出的資料筆數。
            ```
            4
            ```
    * ### 外部尋找: 連結兩個資料表 (在驅動表上選擇 Aggregations 並設置相關 Stage)。
        * ### Stage 1.1 - $lookup: 類似於關聯式資料庫的 left outer join。
            ```
            {
              "from": "forecast",
              "localField": "SiteName",
              "foreignField": "SiteName",
              "as": "result"
            }
            ```
            * ### from: 要尋找的資料表 (外部資料表 or 被驅動表)。
            * ### localField: 驅動表的欄位。
            * ### foreignField: 被驅動表的欄位。
            * ### as: 存放找到的資料。
        * ### Stage 1.2 - $lookup - pipeline: 可用於下一個 Stage 的 aggregation 前處理。
            ```
            {
              "from": "forecast",
              "localField": "SiteName",
              "foreignField": "SiteName",
              "as": "result",
              "pipeline": [
                {
                  "$project": {
                    "_id": 0, "Status": 1
                  }
                }
              ]
            }
            ```
        * ### Stage 2 - $match: 將區域限制在淡水、新店與萬里。
            ```
            {
              "SiteName": {
                "$in": ["新店", "淡水", "萬里"]
              }
            }
            ```
        * ### Stage 3 - $project: 去除不需要的欄位。
            ```
            {
              "SiteName": 1, "result": 1, "_id": 0
            }
            ```
        * ### 極端值查詢 Stage 1 - $group: 群組後找出 value 的最大值。
            ```
            {
              "_id": "null",
              "max_value": {
                "$max": "$value"
              }
            }
            ```
        * ### 極端值查詢 Stage 2 - $lookup: 透過上一個 Stage 所輸出的最大值，至被驅動表中尋找符合的資料。
            ```
            {
              "from": "color",
              "localField": "max_value",
              "foreignField": "value",
              "as": "result"
            }
            ```
    * ### 設定查詢條件: 用於 Aggregation 中的查詢條件設定。
        * ### Stage 1 - $match: 限定 County 欄位只有臺中市。
            ```
            {
              "County": "臺中市"
            }
            ```
        * ### Stage 2 - $addFields: 產生整數型態的 iAQI 欄位。
            ```
            {
              "iAQI": {
                "$toInt": "$AQI"
              }
            }
            ```
        * ### Stage 3 - $group: 群組後算平均值。
            ```
            {
              "_id": "$County",
              "averageAQI": {
                "$avg": "$iAQI"
              }
            }
            ```
        * ### 順序與執行效率
            * ### 順序 1 (較高效): $match -> $addFields -> $group。
            * ### 順序 2 (較低效): $addFields -> $match -> $group。
            * ### 將 $match 放置於第一個 Stage 可以將資料量先縮小，減少後續 Stage 所需處理的資料量與記憶體佔用，進而提升處理速度。
            * ### MongoDB 限制每一筆資料量最大記憶體使用量為 16 MB。
            * ### 除了 $match 外，$project 與 $unset 也可以減少不需要的欄位，此類型的操作應盡可能放置於 Pipeline 的前幾個 Stage。
        * ### 運算式結合: $match 可以透過 $expr 運算子執行一個布林運算式，$match 會透過迴圈檢視所有資料，當該筆資料的 $expr 傳回 true 就輸出，反之傳回 false 則不輸出。
            * ### $match: 列出所有資料。
                ```
                {
                  "$expr": true
                }
                ```
            * ### $match: 列出 AQI 指數大於 100 的縣市資料。
                ```
                {
                  "$expr": {
                    "$gte": [{"$toInt": "AQI"}, 100]
                  }
                }
                ```
    * ### 輸出到新資料表: 將上一個 Stage 的結果複製到另外一個資料表中 (_id 相同的資料會被新的資料覆蓋，且新資料表或資料庫無需事先建立，若不存在 MongoDB 會自動建立)。
        * ### $out: 複製到指定資料表。
            ```
            "AQI_backup"
            ```
        * ### $out: 複製到指定資料庫中的資料表。
            ```
            {
              "db": "backup",
              "coll": "AQI"
            }
            ```
    * ### 文件修訂: 修剪文件內容 (根據一個判斷式來決定是否要將文件中的每個子文件都巡過一遍)。
        * ### Sample 1 - $redact: 判斷式永遠回傳 true，文件中的所有子文件都會巡一遍，最後取得此文件的所有文件。
            ```
            {
              "$cond": {
                "if": "true",
                "then": "$$DESCEND",
                "else": "$$PRUNE"
              }
            }
            ```
            * ### $$DESCEND: 保留該子文件並且繼續檢查同曾與內部其它的子文件。
            * ### $$PRUNE: 刪除這份子文件，然後繼續檢查同層的文件，但不會繼續檢查該層的子文件。
            * ### $$KEEP: 保留該曾並且包含子文件所有內容，然後停止檢查子文件內容。
        * ### Sample 2 - $redact: 使查詢結果只能看到 level 3 的文件。
            ```
            {
              "$cond": {
                "if": {"$eq": ["$level", 3]},
                "then": "$$DESCEND",
                "else": "$$PRUNE"
              }
            }
            ```
        * ### Sample 3 - $redact: 使查詢結果只能看到 level 1 的文件。
            ```
            {
              "$cond": {
                "if": {"$eq": ["$level", 1]},
                "then": "$$DESCEND",
                "else": "$$PRUNE"
              }
            }
            ```
        * ### Sample 4 - $redact: 使查詢結果只能看到 level 大於等於 1 的文件。
            ```
            {
              "$cond": {
                "if": {"$gte": ["$level", 1]},
                "then": "$$DESCEND",
                "else": "$$PRUNE"
              }
            }
            ```
        * ### 備註: 只要上曾被擋掉，即使內層有符合條件的子文件，也會一併修剪掉 (與全文檢索搜尋方式不同)。
    * ### 文件取代: 將文件的內容由該文件中的某個子文件取代。
        * ### Sample 1 - $replaceWith: 將該文件由其子文件 records 取代。
            ```
            "$records"
            ```
        * ### Sample 2 - $replaceRoot: 將該文件由其子文件 records 取代。
            ```
            {
              "newRoot": "$records"
            }
            ```
    * ### 新增與移除欄位: 功能與 $addFields 和 $project 相同。
        * ### Sample 1 - $set: 將 AQI 的字串型態轉型為整數型態 (亦可透過 $addFields 達成)。
            ```
            {
            	"AQI": {"$toInt": "$AQI"}
            }
            ```
        * ### Sample 2 - $unset: 刪除 SiteName 欄位。
            ```
            "SiteName"
            ```
        * ### Sample 3 - 移除 _id、SiteName 與 Pollutant。
            ```
            ["_id", "SiteName", "Pollutant"]
            ```
        * ### 備註: 欄位很多輸出很少時使用 $project 較為方便。
    * ### 與其它資料結合: 將目前的結果與另外一個資料表或另外一個 Aggregation 的結果結合起來後一起輸出。
        * ### Stage 1 - $addFields: 將 AQI 的字串型態轉型為整數型態。
            ```
            {
            	"iAQI": {"$toInt": "$AQI"}
            }
            ```
        * ### Stage 2 - $sort: 根據 iAQI 值做順向排序。
            ```
            {
              "iAQI": 1
            }
            ```
        * ### Stage 3 - $limit: 取得第一筆 (AQI 最低那筆)。
            ```
            1
            ```
        * ### Stage 4 - $unionWith: 結合其 Pipeline 的計算結果，輸出 AQI 最低與最高的區域。
            ```
            {
              "coll": "AQI",
              "pipeline": [
                {"$addFields": {"iAQI": {"$toInt": "$AQI"}}},
                {"$sort": {"iAQI": -1}},
                {"$limit": 1}
              ]
            }
            ```
            * ### coll: 集合（Collection）的名称。
            * ### pipeline: 取得 AQI 最高的那筆資料。
        * ### 備註: 合併另一個資料表的全部資料 ($unionWith)。
            ```
            "another_collection"
            ```
    * ### 陣列解構: 將陣列欄位解構。
        * ### Sample 1 - $unwind: 解構 size 欄位，其資料在解構後將從一筆變成三筆。
            ```
            "$size"
            ```
            * ### 資料
                ```
                {"name": "襯衫", "size": ["S", "M", "L"]}
                ```
            * ### size 欄位將從陣列變成陣列的內容 (各一筆，共三筆)。
        * ### Sample 2 - $unwind - includeArrayIndex: 顯示解構後的資料是在原本陣列中的哪個位置。
            ```
            {
              "path": "$size",
              "includeArrayIndex": "index"
            }
            ```
* ### 常用運算子
    * ### $add、$subtract、$multiply、$divide
        * ### 用途: 加減乘除。
        * ### 資料
            ```
            {value: 10.3}
            ```
        * ### $project
            ```
            {
              "newValue": {"$add": ["$value", 5, 3]}
            }
            ```
    * ### $round
        * ### 用途: 四捨五入。
        * ### 資料
            ```
            [
              {"value": 1.52},
              {"value": 3.27}
            ]
            ```
        * ### $project
            ```
            {
              "value": {"$round": ["$value", 0]},
              "_id": 0
            }
            ```
        * ### 0: 小數點第一位四捨五入。
        * ### 1: 留下小數一位，且小數第二位四捨五入。
    * ### $sum
        * ### 用途: 陣列中各元素加總或自訂陣列中各元素加總。
        * ### 資料
            ```
            [
                {"name": "s1", "history": [25, 20, 31], "current": 21},
                {"name": "s2", "history": [31, 35], "current": 27}
            ]
            ```
        * ### $project
            ```
            {
              "sumOfHistory": {"$sum": "$history"},
              "newCurrent": {"$sum": ["$current", -5.7]},
              "_id": 0
            }
            ```
        * ### sumOfHistory: history 陣列內容加總。
        * ### newCurrent: current 欄位值與 -5.7 加總 (相當於減 5.7)。
        * ### 上方代碼自訂陣列為 ```["$current", -5.7]```。
    * ### $avg
        * ### 用途: 計算陣列中各元素平均值或自訂陣列中各元素平均值。
        * ### 資料
            ```
            [
                {"name": "s1", "history": [25, 20, 31], "current": 21},
                {"name": "s2", "history": [31, 35], "current": 27}
            ]
            ```
        * ### $project
            ```
            {
              "avgOfHistory": {"$avg": "$history"},
              "newCurrent": {"$avg": ["$current", -10]},
              "_id": 0
            }
            ```
        * ### avgOfHistory: history 陣列內容平均。
        * ### newCurrent: current 欄位值與 -10 平均。
        * ### $project: 增加一個 Stage 使輸出四捨五入。
            ```
            {
              "avgOfHistory": {"$round": ["$avgOfHistory", 1]},
              "newCurrent": {"$round": ["$newCurrent", 0]},
            }
            ```
    * ### $ceil、$floor
        * ### 用途: 給定一個值。$ceil 傳回比給定值大的最小整數；$floor 傳回比給定值小的最大整數。
        * ### 資料
            ```
            [
                {"value": 4},
                {"value": 2.3},
                {"value": -5.4}
            ]
            ```
        * ### $project
            ```
            {
              "_id": 0,
              "value": 1,
              "cellValue": {"$ceil": "$value"},
              "floorValue": {"$floor": "$value"},
            }
            ```
    * ### $strLenCP、$strLenBytes
        * ### 用途: 字算字串中的字元數與位元組數。
        * ### 資料
            ```
            {"s": "Hi，大家好"}
            ```
        * ### $project
            ```
            {
              "_id": 0,
              "strLenCP": {"$strLenCP": "$s"},
              "strLenBytes": {"$strLenBytes": "$s"}
            }
            ```
    * ### $trim、$ltrim、$rtrim
        * ### 用途: 字串去空白 (前後、左、右)。
        * ### 資料
            ```
            {"str": " \t abc \n "}
            ```
        * ### $project
            ```
            {
              "_id": 0,
              "ltrim": {"$ltrim": {"input": "$str"}},
              "rtrim": {"$rtrim": {"input": "$str"}},
              "trim": {"$trim": {"input": "$str"}},
            }
            ```
            * ### 可以透過參數 chars 設定要刪除的字元集。
    * ### $split
        * ### 用途: 將字串分割成陣列。
        * ### 資料
            ```
            {"s": "10,20,30"}
            ```
        * ### $project
            ```
            {
              "_id": 0,
              "result": {"$split": ["$s", ","]}
            }
            ```
    * ### $substrCP
        * ### 用途: 取子字串。
        * ### 資料
            ```
            {"s": "Hi，大家好"}
            ```
        * ### $project
            ```
            {
              "_id": 0,
              "result": {"$substrCP": ["$s", 0, 3]}
            }
            ```
            * ### $substrCP: ```[原始字串, 起始索引, 長度]```。
    * ### $concat
        * ### 用途: 字串合併。
        * ### 資料
            ```
            {"s1": "hello", "s2": "world"}
            ```
        * ### $project
            ```
            {
              "_id": 0,
              "result": {"$concat": ["$s1", "<-->", "$s2"]}
            }
            ```
            * ### 將 $concat 後的陣列內容全部合併。
    * ### $cond
        * ### 用途: 為 if - then - else 形式的條件判斷式。
        * ### 資料
            ```
            [
              {"name": "s1", "score": 70},
              {"name": "s2", "score": 93},
              {"name": "s3", "score": 45}
            ]
            ```
        * ### $project
            ```
            {
              "_id": 0,
              "name": 1,
              "score": 1,
              "status": {
                "$cond": {
                  "if": {"$gte": ["$score", 60]},
                  "then": "pass",
                  "else": "fail"
                }
              }
            }
            ```
    * ### $ifNull
        * ### 用途: 若欄位內容為 null，輸出時可以用別的資料取代。
        * ### 資料
            ```
            {"name": "Tom", "email": "null", "tel": "null"}
            ```
        * ### $project
            ```
            {
              "_id": 0,
              "name": 1,
              "email": {"$ifNull": ["$email", "unknown"]},
              "tel": {"$ifNull": ["$tel", "unknown"]}
            }
            ```
    * ### $switch
        * ### 用途: 多條件判斷，相當於許多程式語言中的 switch - case 語法。
        * ### 資料
            ```
            [
              {"cart": [100]},
              {"cart": [200, 400]},
              {"cart": [500, 200, 300]},
              {"cart": [300, 700, 500, 500]}
            ]
            ```
        * ### Stage 1 - $project: 計算陣列中元素個術後放到 amount 欄位。
            ```
            {
              "_id": 0,
              "cart": 1,
              "amount": {"$size": "$cart"}
            }
            ```
        * ### Stage 1 - $project: 根據陣列中的數值加總，並根據陣列中元素個數乘上一個比重。
            ```
            {
              "amount": 1,
              "origin": {"$sum": "$cart"},
              "total": {
                "$switch": {
                  "branches": [
                    {"case": {"$eq": ["$amount", 1]}, "then": {"$sum": "$cart"}},
                    {"case": {"$eq": ["$amount", 2]}, "then": {"$multiply": [{"$sum": "$cart"}, 0.9]}},
                    {"case": {"$gte": ["$amount", 3]}, "then": {"$multiply": [{"$sum": "$cart"}, 0.8]}}
                  ]
                }
              }
            }
            ```
<br />

範例程式
=====
* ### 4_3.py: 生成各縣市平均 AQI 指標與 View 的讀取。
<br />
