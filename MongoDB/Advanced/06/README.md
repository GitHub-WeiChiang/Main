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
        * ### unit: year、quarter、week、month、day、hour、minute、second、millisecond。
    * ### $group - $dateTrunc: 將時間去零頭 (透過 unit 指定計算單位)。
        * ### 資料: 6_4.py。
        ```
        // 計算每季的 price 總和
        
        {
          "_id": {
            "quarter": {
              "$dateTrunc": {
                "date": "$date",
                "unit": "quarter",
                // 指定每個時間單位的大小，設置為 1 表示每季度一個時間單位。
                "binSize": 1
              }
            }
          },
          "sumOfPrice": {
            "$sum": "$price"
          }
        }
        ```
        ```
        // 計算上半年與下半年的 price 總和
        
        {
          "_id": {
            "quarter": {
              "$dateTrunc": {
                "date": "$date",
                "unit": "quarter",
                "binSize": 2
              }
            }
          },
          "sumOfPrice": {
            "$sum": "$price"
          }
        }
        ```
        * ### unit: year、quarter、week、month、day、hour、minute、second。
        * ### 當 unit 被設定為 week 時: 可以透過參數 startOfWeek 決定每星期由星期幾開始。
            * ### mon
            * ### tue
            * ### wed
            * ### thu
            * ### fri
            * ### sat
            * ### sun
        ```
        // 將 ObjectId 中的時間部分從 "月" 去零頭
        
        {
          "dd": {
            "$dateTrunc": {
              "date": ObjectId(),
              "unit": "month"
            }
          }
        }
        ```
* ### MongoDB 的时间戳 (timestamp) 由两个部分组成: 时间戳值 + 时间戳增量。
    * ### 时间戳值 (Timestamp Value): 时间戳值表示一个特定时间点的信息，它通常是一个以秒为单位的整数，表示自 UNIX 纪元以来的秒数。
    * ### 时间戳增量 (Timestamp Increment): 时间戳增量是一个表示事件发生在特定时间点内的顺序号或计数器，通常是一个整数，每次事件发生时都会增加，如果多个事件具有相同的时间戳值，时间戳增量允许对它们进行排序，以确定它们的发生顺序。
    * ### 在 MongoDB 中，时间戳通常用于记录文档的创建时间或修改时间，例如: 如果两个文档具有相同的时间戳值，但不同的时间戳增量，那么可以根据时间戳增量来确定哪个文档先创建或修改。
    * ### 时间戳对象表示特定事件发生的时间，而增量为 1 表示这个事件是这个时间点内的第一个事件，增量通常是自动增加的，以确保同一时间戳值的事件可以按顺序进行排序。
<br />

範例程式
=====
* ### 6_1_1.py: 在 Python 取得現在日期。
* ### 6_2.py: 從 \_id 取得資料建立日期。
* ### 6_4.py: "MongoDB 跟日期時間有關的函數" 中 "$group - $dateTrunc" 所需範例資料。
* ### 6_5_1.py: 將字串轉成 Date 型態。
* ### 6_5_2.py: Date 型態解析。
* ### 6_5_3.py: BSON 的時間戳記。
* ### 6_5_4.py: 儲存伺服器日期。
<br />
