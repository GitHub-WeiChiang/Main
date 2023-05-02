Chapter10 設計通知系統
=====
* ### 通知 (notification) 的形式
    * ### 手機推送 (push notifiction)
    * ### 手機簡訊 (SMS)
    * ### Email 電子郵件
* ### 通知的類型
    * ### iOS 推送通知
        * ### 提供者 (provider): 負責生成通知，需包含 token 與 payload。
        * ### APNS: Apple 推送通知服務 (Apple Push Notification Service)。
        * ### iOS 設備: 被通知的人。
    * ### Android 推送通知: 採用 FCM (Firebase Cloud Messaging)。
    * ### SMS 手機簡訊: 使用第三方服務 (Twilio, Nexmo, ...)。
    * ### Email 電子郵件: 這我內行的！
* ### 記得要收集使用者手機設備的 token 與電話號碼，或是子郵件帳號！
* ### 資料庫 table 設計
    * ### user: id, email, country, phone_num, created_at.
    * ### device: id, token, user_id, last_logged_in_at.
    * ### 上述為使用者可以使用多設備的場景粗略設計。
* ### 注意事項
    * ### 通知範本: 統一格式。
    * ### 通知過濾: 選擇所接受通知 (尊重使用者)。
    * ### 通知限速: 避免頻繁發送。
    * ### 通知重送: 避免遺漏訊息。
    * ### 通知安全: 認證過客戶端才可發送。
    * ### 通知監視: 效能管理。
    * ### 通知追蹤: 分析！
* ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/SystemsDesign/Chapter10/SystemArchitectureDiagram.png)
<br />
