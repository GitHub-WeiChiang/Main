Chapter08 設計短網址生成器
=====
* ### HTTP 狀態碼
    * ### 301 Moved Permanently: 代表永久重定向，瀏覽器會針對這個回應進行快取，爾後若呼叫同一個短網址，請求就不會被送到短網址伺服器，瀏覽器會直接重定向到正確的伺服器 (可以降低伺服器負荷)。
    * ### 302 Found: 臨時的重定向，每一次的請求都會被傳送到短網址伺服器，等待重定向響應 (可以針對用戶行為進行分析)。
* ### 短網址可以透過鍵值對儲存與使用。
* ### 短網址生成方式: 雜湊 + 衝突解決、Base 62 轉換。
* ### 雜湊 + 衝突解決
    * ### 根據需求計算所需雜湊數量求得短網址長度，雜湊是透過數字與大小寫英文字母組成，10 + 26 + 26 = 62，設 n 為短網址長度，其對應的網址數量如下 (1: 62, 2: 3844, 3: 238328, 4: 14776336, 5: 916132832, ..., n: 62 ^ n)。
    * ### 以 CRC32 雜湊函式為例，十六進位表示下該雜湊還數有八位數，我們可以只取前七位數作為網址映射，而這種作法可能導致雜湊的衝突機率升高，相應的解決方案是，如果遇到衝突，在原網址後加上一個預定義字串，重新計算雜湊，直到沒有衝突為止。
    * ### 長網址 -> 雜湊 -> 不存在 (若存在，加上預定義字串後返回上一步驟) -> 儲存成為短網址。
    * ### 短網址是否衝突的檢查會降低效能，可以透過 Bloom Filter 解決。
* ### Base 62 轉換
    * ### 將數字與英文字母大小寫直接對應成數字，0 = 0、a = 10、z = 35、A = 36、Z = 61。
    * ### 透過計數器，對應當下正在進行的網址，若為第 11157 個網址，則將此數取餘數，如下，11157 / 62 = 179...59、179 / 62 = 2...55、2 / 62 = 0...2，餘數 59、55、2 分別對應字符 X、T、2，那麼第 11157 個網址得短網址即為 .../2TX。
* ### 雜湊 + 衝突解決
    * ### 長度固定。
    * ### 需要解決衝突。
    * ### 無法預知短網址。
* ### Base 62 轉換
    * ### 長度不固定。
    * ### 需要唯一 ID 生成器。
    * ### 無衝突可能。
    * ### 若地增值固定，可以預測短網址，有安全疑慮。
* ### 短網址可以存在快取，提升效率。
* ### RESTful API
    * ### "GET /api/files/" 得到所有檔案。
    * ### "GET /api/files/1/" 得到檔案 ID 為 1 的檔案。
    * ### "POST /api/files/" 新增一個檔案。
    * ### "PUT /api/files/1/" 更新 ID 為 1 的檔案。
    * ### "PATCH /api/files/1/" 更新 ID 為 1 的部分檔案內容。
    * ### "DELETE /api/files/1/" 刪除 ID 為 1 的檔案。
    * ### "GET /api/files/search?key=hello" 搜尋檔案名稱為 hello 的檔案。
* ### Bloom Filter: 可以儲存「某一個元素是否存在」的集合。
    * ### 不存在漏報 (False Negative): 有一定會說。
    * ### 但卻可能誤報 (False Positive): 但說了不一定會對。
    * ### 確定某元素是否在集合的代價和元素數目無關: 不管對不對，反正很快。
    * ### 不過只要它說不在就一定不在。
* ### Difference between Bloom filters and Hashtable: In hash table the object gets stored to the bucket(index position in the hashtable) the hash function maps to. Bloom filters doesn't store the associated object. It just tells whether it is there in the bloom filter or not. Hash tables are less space efficient.
<br />
