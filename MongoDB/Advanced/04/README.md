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
              _id: "$County",
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
<br />

範例程式
=====
* ### 4_3.py: 生成各縣市平均 AQI 指標與 View 的讀取。
<br />
