Chapter13 設計搜尋文字自動補全系統
=====
* ### 自動補全文字 (autocomplete) 又稱為
    * ### 提前輸入 (typeahead)
    * ### 隨打搜尋 (search-as-you-type)
    * ### 漸增搜尋 (incremental search)
* ### 自動補全文字主要目標為找出最常被搜尋的前 k 個查詢結果。
* ### 系統組成: 資料收集 (data gathering) 服務、查詢 (query) 服務。
* ### 若透過關聯式資料庫查詢頻域最高單詞並不是很有效率的做法，可以使用 trie 資料結構 (甚至可以使用 CDN) 並把快取保存在瀏覽器。
* ### 前綴樹 (prefix tree, trie): 提升查詢速度，樹結構如圖所示，前綴樹通常直接採用整顆替換作為更新方式，也可以根據查詢時間加上權重。
* ### 若前綴樹大到需要進行分片對應 (shard map)，要注意 hotkey 開頭字母問題。
* ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/SystemsDesign/Chapter13/SystemArchitectureDiagram.png)
<br />
