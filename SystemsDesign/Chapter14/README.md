Chapter14 設計 YouTube
=====
* ### 使用 CDN 與 BLOB (二進位大型物件，在資料庫管理系統中，將二進位資料儲存為一個單一個體的集合，BLOB 通常是影像、聲音或多媒體檔案。) 雲端服務。
* ### 串流協定
    * ### MPEG - DASH: 動態圖像專家群組 (Moving Picture Experts Group)，透過 HTTP 進行動態自適應串流 (Dynamic Adaptive Streaming over HTTP)。
    * ### Apple 的 HLS: HTTP Live Streaming (HTTP 即時串流)。
    * ### Microsoft 的 Smooth Streaming (平順串流)。
    * ### Adobe 的 HDS (HTTP Dynamic Streaming, HTTP 動態串流)。
* ### 影片轉碼: 將影片編碼為相容的比特率 (bitrate, 一定時間內處理 bit 資料的速度) 與格式。
    * ### 原始影片會佔用較大記憶體。
    * ### 便於設備相容。
    * ### 只提供高解析影片給網路頻寬較好的使用者。
    * ### 根據情況自動或人工切換影片品質。
* ### 透過有向非循環圖模型執行影片轉碼 (DAG, Directed Acyclic Graph)
    * ### 影片: 檢查、影片編碼、縮圖、浮水印。
    * ### 音軌: 聲音編碼。
    * ### 詮釋資料
* ### 影片轉碼架構
    * ### 預處理器: 進行影片分割。
    * ### DAG 排程器
    * ### 資源管理工具: Task, Worker, Running Queue.
    * ### 任務工作程序: 執行 DAG 定義任務。
    * ### 已編碼影片
* ### 預簽名上傳網址
    * ### 請求上傳
    * ### 獲得預簽名網址
    * ### 上傳影片
* ### 影片保護
    * ### DRM (Digital Rights Management, 數位版權管理) 系統。
    * ### AES 加密。
    * ### 浮水印。
* ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/SystemsDesign/Chapter14/SystemArchitectureDiagram.png)
<br />
