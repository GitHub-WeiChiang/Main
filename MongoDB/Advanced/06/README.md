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
* ### MongoDB 跟日期時間有關的函數
    * ### $project - $dateToPart: 將日期時間資料解包，可分離出年、月、日、時、分、秒與毫秒。
        ```
        {
        	"datePart": {
            "$dateToParts": {
              "date": "$$NOW"
              // "timezone": "+08"
            }
          }
        }
        ```
    * ### $project - $year、$month、$dayOfYear、$dayOfMonth、$dayOfWeek、$hour、$minute、$seconds、$millisecond: 指定日期時間資料。
        ```
        {
        	"year": {
            "$year": {
              "date": "$$NOW",
              // "timezone": "+08"
            }
          }
        }
        ```
    * ### $project - $dateFromParts: 組合日期時間數據並傳回 Date 物件 (year 為必要，其餘預設填入 1/1/0/0/0.000)。
        ```
        {
        	"date": {
            "$dateFromParts": {
              "year": 2022,
              "month": 3,
              "day": 1,
              "hour": 6,
              "minute": 10,
              "second": 0,
              "millisecond": 0,
              // "timezone": "+08"
            }
          }
        }
        ```
    * ### $project - $dateFromString: 其它時間格式的標準日期時間格式轉換。
        ```
        {
          "date": {
            "$dateFromString": {
              "dateString": "2022年2月14日5時20分",
              "format": "%Y年%m月%d日%H時%M分",
              // "timezone": "+08"
            }
          }
        }
        ```
        | 符號 | 說明 | 範例              |
        |----|----|-----------------|
        | %d | 日期 | 01-31           |
        | %G | 年份 | 0000-9999       |
        | %H | 小時 | 00-23           |
        | %L | 毫秒 | 000-999         |
        | %m | 月份 | 01-12           |
        | %M | 分鐘 | 00-59           |
        | %S | 秒數 | 00-60           |
        | %u | 星期 | 1-7             |
        | %V | 週數 | 01-53           |
        | %Y | 年份 | 0000-9999       |
        | %z | 時差 | +/-\[hh\]\[mm\] |
        | %Z | 時差 | +/-\[mmm\]      |
        | %% | 很純 | %               |
    * ### $project - $dateToString: 將日期轉成特定格式字串。
        ```
        {
        	"dd": {
            "$dateToString": {
              "date": "$$NOW",
              "format": "%m月%d日"
            }
          }
        }
        ```
        | 符號 | 說明  | 範例      |
        |----|-----|---------|
        | %j | 第幾天 | 001-366 |
        | %w | 星期幾 | 1-7     |
        | %U | 第幾週 | 00-53   |
    * ### $project - $dateDiff: 計算兩個時間的差距 (透過 unit 指定計算單位)。
        ```
        {
          "diff": {
            "$dateDiff": {
              "startDate": {
                "$dateFromString": {
                  "dateString": "2022/9/19"
                }
              },
              "endDate": "$$NOW",
              "unit": "day"
            }
          }
        }
        ```
        * ### unit: year、quarter、week、month、day、hour、minute、second、millisecond。
    * ### $project - $dateAdd、$dateSubtract: 對日期時間進行加減。
        ```
        {
          "newDate": {
            "$dateAdd": {
              "startDate": {
                "$dateFromString": {
                  "dateString": "2022/9/19 21:30:00z"
                }
              },
              "unit": "day",
              "amount": 365
            }
          }
        }
        ```
<br />

範例程式
=====
* ### 6_1_1.py: 在 Python 取得現在日期。
* ### 6_2.py: 從 \_id 取得資料建立日期。
<br />
