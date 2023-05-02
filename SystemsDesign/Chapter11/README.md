Chapter11 動態訊息系統
=====
* ### 發佈個人動態: 發佈、寫快取予資料庫、推送。
* ### 構建動態訊息: 按時間排序彙整好友動態。
* ### 扇出服務
    * ### 寫入後扇出 (適用於一般使用者): 讀取速度快、朋友太多會有 hotkey 問題、若有幽靈朋友會造成記憶體浪費。
    * ### 讀取時扇出 (適用於網紅): 節省記憶體資源、無 hotkey 問題、讀取速度慢。
* ### 動態訊息快取: 基本上只存放鍵值對應 (post_id, user_id)。
* ### 動態訊息檢索過程
    * ### 發出請求
    * ### 附載平衡
    * ### 伺服器
    * ### 動態快取: 取得相關 key 值。
    * ### 使用者快取 / 貼文快取: 獲取內容資訊。
    * ### 回傳響應
* ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/SystemsDesign/Chapter11/SystemArchitectureDiagram.png)
<br />
