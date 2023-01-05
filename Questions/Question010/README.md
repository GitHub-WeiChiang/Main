Question010 - Redis 記憶體資料滿了怎麼辦 ?
=====
* ### Redis 有自己的記憶體淘汰策略 (如下) !
* ### noeviction (預設): 對於寫請求不再提供服務，直接返回錯誤。
* ### allkeys-lru: 從所有 key 中使用 LRU 演算法進行淘汰。
* ### volatile-lru: 從設定了過期時間的 key 中使用 LRU 演算法進行淘汰。
* ### allkeys-random: 從所有 key 中隨機淘汰資料。
* ### volatile-random: 從設定了過期時間的 key 中隨機淘汰。
* ### volatile-ttl: 在設定了過期時間的 key 中，根據 key 的過期時間進行淘汰，越早過期的越優先被淘汰。
<br />
