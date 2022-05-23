Chapter11
=====
* ### time 模組提供一層介面，用於呼叫各平台上的 C 程式庫函式。
* ### UNIX 時間，或稱 POSIX 時間是 UNIX 系統使用的時間表示方式: 從 UTC 1970 年 1 月 1 0 時 0 分 0 秒起至現在的總秒數，不考慮閏秒修正 (epoch 的一種)。 
* ### time 模組提供低階機器時間觀點，也就是從 epoch 起經過的秒數。
* ### datetime 模組提供以人類觀點表達的時間。
* ### datetime 預設沒有時區資訊，可透過 timezone (tzinfo 的子類) 提供基本 UTC 偏移時區實作。
* ### 通常以 UTC 進行時間儲存，因其為絕對時間，不考量日光節約時間等問題。
* ### 通常一個模組只需要一個 Logger 實例，雖然可以直接建構 Logger 實例，但建議透過 logging.getLogging() 取得 Logger 實例。
* ### 呼叫 getLogger() 時，可以指定名稱，相同名稱下取得的 Logger 會是同一個實例。
* ### 日誌等級與其值 (預設為大於 30 才輸出)
    * ### NOTSET = 0
    * ### DEBUG = 10
    * ### INFO = 20
    * ### WARNING = 30
    * ### ERROR = 40
    * ### CRITICAL = 50
* ### setLevel() 可以調整日誌層級，logging.basicConfig() 可以調整根 Logger 的組態 (日誌層級)。
* ### 可以透過 debug()、info()、warning()、error() 與 critical() 等方法直接指定日誌等級。
