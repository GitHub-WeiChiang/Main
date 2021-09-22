SpringBoot
=====
* ### Chapter03 使用開發工具
* ### Chapter04 Spring Boot 基礎
* ### Chapter05 分層開發 Web 應用程式
* ### Chapter06 響應式程式設計
* ### Chapter07 Spring Boot 進階
* ### Chapter08 用 ORM 操作 SQL 資料庫
* ### 其它
	* ### RESTful API
	* ### JWT
		* header
		* payload
		* signature
	* ### Redis
		* 數據一致性: 資料庫與快取間雙重寫入數據一致性問題。
		* 快取穿透: 訪問一個不存在的 key，快取不起作用，請求會穿透到 DB，流量大時 DB 會掛掉。
		* 快取雪崩: 快取因高峰請求當機，所有請求直接轉向資料庫導致資料庫故障，即便重啟又馬上故障。
		* 快取擊穿: 某 key 訪問頻繁，處於集中式高併發訪問的情況，當這個 key 在失效的瞬間，大量的請求就擊穿了快取，直接請求資料庫。
		* 快取平行處理競爭問題
		* 為甚麼比較快: 純記憶體操作、單執行續操作、非阻塞 I/O 多工機制
	* ### RabbitMQ
	* ### Elasticsearch
	* ### PUT: 提交完整需更新物件。
	* ### PATCH: 對已知資源進行局部更新。
	* ### GET 與 POST 區別
		* GET 在瀏覽器中可以回退，POST 造訪同一位址時只是再次提交請求。
		* GET 會被瀏覽器快取，POST 不會。
		* GET 中的參數會被完整保留於瀏覽器歷史紀錄，POST 不會。
		* GET 只能進行 URL 編碼，POST 支援多種編碼方式。
		* GET 只接收 ASCII 字元，POST 無限制。
		* GET 安全性相較於 POST 低，因其參數暴露在 URL 上，不可用於傳遞敏感資訊。
		* GET 參數透過 URL 傳遞，POST 存放於 request body 中。
<br />

Reference
=====
### * 極速開發 Java 大型系統：Spring Boot 又輕又快又好學
