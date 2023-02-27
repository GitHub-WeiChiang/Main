Question029 - 什麼是 InnoDB 預先讀取 (read ahead) ?
=====
* ### InnoDB 提供預先讀取 (read ahead)，會將認為當前請求後續可能讀取的頁面，一併載入到 Buffer Pool。
* ### 線性預先讀取: 當循序存取某個區 (extent) 的頁面超過某個系統變數值，會觸發一次的 "非同步" 讀取下一個區中的全部頁面到 Buffer Pool 中，該系統變數為 innodb_read_ahead_threshold，預設值為 56，這是一個全域變數。
* ### 隨機預先讀取: 當某個區的 13 個連續頁面都被載入到 Buffer Pool 的 "非常熱 (young) 區"，無論是否為順序讀取，都會觸發一次 "非同步" 讀取本區中的所有其它頁面到 Buffer Pool 中，由系統變數 innodb_random_read_ahead 控制，預設為 OFF，也就是不開啟隨機預先讀取功能，可以透過啟動選項或 ```SET GLOBAL``` 命令修改。
* ### 理解更多 -> [click me](https://gitlab.com/ChiangWei/main/-/tree/master/MySQLPrinciples/Chapter17)
<br />
