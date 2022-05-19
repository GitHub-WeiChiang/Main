Chapter10
=====
* ### 保留程式運算結果，稱為永續化 (Persistence)。
* ### 物件資訊的保留與讀取稱為物件序列化 (Object serialization)與反序列化 (Deserialization)。
* ### Python 內建 pickle 模組用於序列化物件。
* ### 序列化時會將 Py 物件轉為 bytes，這個過程稱為 pickling，相反的操作則稱為 unpickling。
* ### 物件轉 bytes 透過 dumps() 函式，反之透過 loads() 函式。
* ### 無法 pickling 或 unpickling 時會引發 PicklingError 或 UnpicklingError (父類別為 PickleError)。
* ### .pickle 是 Python 專屬格式，保證向後相容。
* ### Import 的 try / except 範例。
```
try:
    # 速度快但非所有平台都有 (如 Windows 沒有)。
    import cPickle
except Import Error:
    import pickle
```
* ### shelve 物件行為上像是字典物件，key 必須為字串，value 可以是 pickle 模組可處裡的 Python 物件，其直接與檔案關聯，使用上如同資料庫介面。
* ### Python 內建 SQlite 資料庫，此為用 C 語言撰寫的輕量級資料庫。
* ### sqlite3.connect(:memory:)，此行程式可在記憶體中建立一個資料庫。
* ### sqlite3.connect 實作情境管理器，可搭配 with 陳述使用，with 區塊結束後會自動 commit() 與 close()，若發生例外會自動 rollback()。
* ### 使用 execute 方法執行一條 SQL 語句，如果帶有參數可以使用佔位符來傳遞參數，使用佔位符已經考慮到轉碼的問題，不需要自己單獨處理，不用去管 SQL 注入的問題。不過佔位符只是針對 value，不能用於設置表名與字段等。
* ### sqlite3 的交易有四個基本要求 (ACID)，原子性 (Atomicity)、一致性 (Consistency)、隔離行為 (Isolation behavior)、持續性 (Durability)。
* ### sqlite3 模組預設不會自動提交，必須透過 Connection 的 commit() 提交，過程若有錯誤需使用 Connection 的 rollback() 撤回操作。
* ### sqlite3 交易時預設會鎖定資料庫。
* ### sqlite3 若不設隔離可能引發的問題有，更新遺失 (Lost update)、髒讀 (Dirty read)、無法重複的讀取 (Unrepeatable read)、幻讀 (Phantom read)。
    * ### 更新遺失: 某個交易對欄位進行更新，因另一個交易導致更新無效 (交叉提交一方確認一方撤銷)。
    * ### 髒讀: 兩個交易同時進行，其中一個交易更新資料但尚未確認，另一個交易就讀取，此時前一個交易又進行撤銷。
    * ### 無法重複的讀取: 某個交易兩次讀取同一欄位資料不一致 (途中被另一個交易更新欄位值)。
    * ### 幻讀: 同一時間讀取到資料筆數不同 (有一筆交易在前一筆交易讀取後馬上新增並讀取)。
* ### CSV 的全名是 Comma Separated Values，是一種通用的試算表、資料庫間的交換格式。
* ### Python 提供 csv 模組，可以隱藏讀寫細節。
* ### JSON 全名為 JavaScript Object Notation，為 JavaScript 物件實字 (Object literal) 的子集。
* ### Python 內建 json 模組，API 的使用上類似 pickle。
* ### Json 資料再進行網路傳輸時，可以移除不必要的空白，省去不必要的流量開銷。
* ### 處裡 XML 時建議使用 xml.etree.ElementTree，相對於 DOM，ElementTree 更為簡單與快速，相對於 SAX 也有 iterparse() 可以使用，可以在讀取 XML 文件的過程中即時進行處理。
