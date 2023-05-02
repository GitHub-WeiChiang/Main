Chapter15 設計 Google Drive
=====
* ### 檔案上傳: 簡單上傳、斷點上傳。
* ### 同步衝突: 先處理為準，後處理判定為衝突，衝突點個別顯示雲端與本機版本。
* ### 差異同步 (delta sync): 將檔案切塊後，若檔案資訊更新，只需更新變動區塊，不用全部更新。
* ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/SystemsDesign/Chapter15/SystemArchitectureDiagram.png)
<br />
