Question006 - 什麼是前綴樹 ?
=====
* ### 前綴樹 (prefix tree, trie): 用於提升自動補全文字查詢速度，樹結構如圖所示，前綴樹通常直接採用整顆替換作為更新方式，也可以根據查詢時間加上權重。
* ### 若前綴樹大到需要進行分片對應 (shard map)，要注意 hotkey 開頭字母問題。
* ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/SystemsDesign/Chapter13/SystemArchitectureDiagram.png)
<br />
