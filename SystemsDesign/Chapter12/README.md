Chapter12 設計聊天系統
=====
* ### 持續保持連接 (keep-alive)
    * ### 輪詢 (polling): 一問一答，頻率高代價高，消耗伺服器資源。
    * ### 長輪詢 (long polling): 問了開始等回覆，或是等到不耐煩 (超時)。
    * ### WebSocket: 從 HTTP 開始，透過明確定義的交握過程，升級成 WebSocket。
* ### 聊天系統分類: 無狀態、有狀態、第三方整合。
* ### 無狀態 (通用功能): 登入、註冊、使用者資訊查詢。
* ### 有狀態: 持久型網路連接。
* ### 第三方整合: 通知系統。
* ### 關聯式資料庫: 儲存通用型資料 (個人檔案、設定、使用者好友列表)。
* ### NoSQL: 聊天相關資料。
    * ### 近期聊天記錄會被頻繁存取。
    * ### 讀寫比例約為 1:1。
* ### 資料模型
    * ### 一對一: message_id、from、to、content、time。
    * ### 群組: channel_id、message_id、user_id、content、time。
* ### 訊息 ID 唯一不可重複且可依照時間排序 (Chapter07)。
* ### 服務探索: 依據客戶端地理位置與伺服器容量等條件選擇合適聊天伺服器。
* ### 訊息流量: 一對一
    * ### 使用者 1 發送訊息給使用者 2。
    * ### 聊天伺服器接收訊息。
    * ### 訊息 ID 生成器產生訊息 ID。
    * ### 訊息進入同步佇列。
    * ### 儲存訊息。
    * ### 判斷使用者 2 是否在線。
        * ### 離線將進行推送通知。
    * ### 將訊息傳送至使用者 2 所連接之聊天伺服器。
    * ### 使用者 2 接收訊息。
* ### 單一使用者跨越多設備訊息同步
    * ### 每一個設備維護各自的 cur_max_message_id 以追蹤最新訊息。
* ### 訊息流量: 群組
    * ### 針對每一個使用者產生一個獨立的訊息同步佇列。
    * ### 並將佇列依群組識別統一接收資訊。
* ### 連線狀態透過心跳包實現。
* ### 好友連線狀態的傳遞，可以透過監聽訊息佇列 (RabbitMQ, Kafka, ...) 實現 (發佈 / 訂閱)，若好友人數太多，可以改為使用者手動刷新方式。
* ### 其它
    * ### 檔案種類擴充。
    * ### 訊息加密。
    * ### 訊息快取。
    * ### 載入時間優化。
    * ### 錯誤處理。
    * ### 訊息重發機制。
* ### ![image](https://gitlab.com/ChiangWei/main/-/raw/master/SystemsDesign/Chapter12/SystemArchitectureDiagram.png)
<br />