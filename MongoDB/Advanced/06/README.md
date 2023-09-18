06 - 日期時間處理
=====
* ### MongoDB 的日期型態
    * ### Date: 處理常見的年月日時分秒。
    * ### Timestamp: 時間戳記。
* ### MongoDB 中的日期，其時區固定為 UTC (Coordinated Universal Time)，所有的日期都會自動轉成 UTC (世界標準時間) 時區儲存。
* ### 把 Timestamp 內容轉成容易閱讀的字串: Aggregation -> $set - $dateToString。
* ### 從 \_id 取得資料建立日期: Aggregation -> $set - $toDate。
* ### 字串與 Date 型態轉換
    * ### Sample 1 - $project - $toDate: 簡單轉換。
        ```
        {
          "_id": 0,
          "ori_date": "$PublishTime",
          "reg_date": {
            "$toDate": "$PublishTime"
          }
        }
        ```
    * ### Sample 1 - $project - $toDate: 轉換為 UTC 時區。
        ```
        {
          "_id": 0,
          "ori_date": "$PublishTime",
          "reg_date": {
            "$add":[
              {"$toDate": "$PublishTime"},
              -8 * 60 * 60 * 1000
            ]
          }
        }
        ```
<br />

範例程式
=====
* ### 6_1_1.py: 在 Python 取得現在日期。
* ### 6_2.py: 從 \_id 取得資料建立日期。
<br />
