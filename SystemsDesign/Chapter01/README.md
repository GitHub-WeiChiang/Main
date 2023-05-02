Chapter01 使用者人數 - 從零到百萬規模
=====
* ### 何時選擇非關聯式資料庫
    * ### 超低 latency
    * ### 非結構化資料
    * ### 資料只需進行 serialize 與 deserialize
* ### vertical scaling (scale up): 升級伺服器硬體，低流量適用，不支援 failover and redundancy。
* ### horizontal scaling (scale out): 添加更多伺服器 (poll of resource)，配合 load balancer，提升 availability。
* ### vertical scaling 缺點
    * ### 硬體升級終究有限制
    * ### 單點故障風險大
    * ### 成本高
* ### horizontal scaling 採用分片 (sharding / partition key) 策略的挑戰
    * ### 資料重新分片 (空間不足新增分片與分佈不均)
    * ### 名人 (celebrity) 問題 / 熱點 (hotspot) 問題
    * ### JOIN 聯結與去正規化 (de - normalization)
* ### database replication: 將資料庫區分 master 與 slave，master 只支援寫入，slave 會向 master 取得副本並只支援讀取，當 master 掛了，將由一 slave 代替之 。
* ### database replication 優點
    * ### 效能更好
    * ### 可靠性高
    * ### 可用性高
* ### 快取注意事項
    * ### 讀取頻繁不常寫入使用 (Redis 是具有持久儲存功能的)。
    * ### 過期策略定義。
    * ### 數據一致性。
    * ### 減輕故障影響。
    * ### Eviction Policy。
* ### CDN 注意事項
    * ### 成本
    * ### 過期時間
    * ### 退守做法 (fallback)
    * ### 檔案無效化 (invalidating)
* ### 多資料中心配置
    * ### 流量重定向
    * ### 資料同步
    * ### 測試與部署
* ### 日誌紀錄: 錯誤日誌紀錄。
* ### 衡量指標
    * ### 主機級別: CPU, Memory, Disk I/O.
    * ### 整合級別: 資料庫與快取效能表現。
    * ### 關鍵業務: 活躍使用者、滯留率 (retention)、營業收入。
* ### 百萬使用者系統架構摘要
    * ### web 層 stateless
    * ### 每一層需具備 redundancy
    * ### 使用 cache
    * ### 支援多資料中心
    * ### CDN 管理靜態資料
    * ### 使用分片擴展資料層
    * ### 每一層都是單一服務
    * ### 監控系統並善用自動化工具
* ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/SystemsDesign/Chapter01/SystemArchitectureDiagram.png)
<br />
