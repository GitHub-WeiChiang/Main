04 - Aggregation 進階查詢
=====
* ### Aggregation vs. Find
    * ### Find 只能對資料進行一次的運算處理。
    * ### Aggregation 可以對資料進行多次運算後才取得結果 (例如某 Collection 中特定的 Field 平均值)。
* ### Aggregation 利用 Pipeline 的方式處理資料。
* ### Pipeline 包含一或數個資料處理階段 Stage，每一個 Stage 會將上一個 Stage 輸出資料經過處理後傳給下一個 Stage，直到最後。
* ### 若想計算 AQI 欄位的平均值，可以設計ｓ第一個 Stage 將 AQI 型態由字串轉為數字，第二個 Stage 進行分群後平均值計算。
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
<br />

範例程式
=====
* ### 4_3.py: 生成各縣市平均 AQI 指標與 View 的讀取。
<br />
