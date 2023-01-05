Question009 Redis 持久不持久 ?
=====
* ### Redis 預設是持久化的鍵值對儲存資料庫 !
* ### 默认开启 RDB，默认關閉 AOF。
* ### 也因為預設是開啟的，如果關閉了持久化功能，記得刪掉 dump.rdb 呦。
```
# redis.conf

# 這樣就關閉持久化勒。
save ""

# save 900 1
# save 300 10
# save 60 10000
```
* ### RDB 持久化: 在指定的時間間隔內將內存中的數據集快照寫入磁盤(默認 15 分鐘有一次修改，6 分鐘內有 10 次修改，1 分鐘內有 10000次 修改，將會將快照數據集集中寫入 dump.rdb 文件)。
* ### AOF 持久化: 該機制將以日誌的形式記錄服務器所處理的每一個寫操作，在 Redis 服務器啟動之初會讀取該文件來重新構建數據庫，以保證啟動後數據庫中的數據是完整的。
```
# redis.conf

# 默認關閉
appendonly no
```
<br />