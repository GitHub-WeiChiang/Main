Chapter15 查詢最佳化的百科全書 -- EXPLAIN 詳解
=====
```
EXPLAN SELECT ... FROM ...
```
* ### EXPLAN 輸出列
    * ### id: 一個 SELECT 對應一個 id。
    * ### select_type: 查詢類型。
    * ### table: 表名。
    * ### partitions: 匹配的分區資訊。
    * ### type: 存取方法。
    * ### possible_keys: 可能使用索引。
    * ### key: 實際使用索引。
    * ### key_len: 實際使用索引長度。
    * ### ref: 使用索引列相等查詢時，與索引列進行相等匹配的物件資訊。
    * ### rows: 預估所需讀取的記錄筆數。
    * ### filtered: 針對 rows 經過搜索條件過濾後剩餘記錄筆數的百分比。
    * ### Extra: 額外資訊。
* ### 
<br />
