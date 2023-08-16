Question046 - Monolithic Architecture 與 Microservices Architecture 的差異為何 ?
=====
* ### 什麼是單體式架構 (Monolithic Architecture) ?
    * ### 將系統所需的所有元件整合到同一份程式裡，讓此應用程式不只處理單一任務，而是能負責所需的所有功能。
    * ### 以 Web Application 來說，其設計方向就是將 Web 所需邏輯 (例如: 前端 + 後端) 全部寫進同一份程式裡，最後打包起來就是一套擁有完整功能的系統。
    * ### 優點
        * ### 部屬容易: 只需部屬一份執行檔就能運作。
        * ### 設計簡單: 功能都寫在同一份程式，不用思考各元件交互的方式。
        * ### 初期成本低: 開發與學習成本較低，上手速度較快，適合小規模的開發團隊。
    * ### 缺點
        * ### 未來成本高: 程式碼龐大，除錯與功能新增可能較為困難。
        * ### 程式碼依賴性高: 畢盡一整包，任何層面的依賴性都會比較高。
        * ### 擴展服務困難: 單一功能遇到瓶頸，只能對整個應用程式擴展。
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/Questions/Question046/Monolithic.png)
* ### 什麼是微服務架構 (Microservices Architecture) ?
    * ### 將應用程式依據功能拆解成獨立元件，彼此透過合適的傳輸協定互相通訊。
    * ### 以 Web Application 來說，其設計方向就是將 Web 所需邏輯 (例如: 前端 + 後端) 都拆解成獨立程式，後互相使用合適的傳輸協定相互溝通，組合在一起即可成為完整的系統。
    * ### 優點
        * ### 故障風險降低: 功能獨立運作，若其中一項服務故障，系統也不會全面停擺。
        * ### 易於平行擴展: 可根據個別功能調整資源，以滿足應用程式需求。
        * ### 開發自由度高: 每個功能都是彼此獨立，可以天馬行空，無拘無束。
    * ### 缺點
        * ### 開發時注意事項較多，若 API 定義不清楚，或元件拆分方式不佳，都會導致整個系統衍生出很多的問題。
    * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/Questions/Question046/Microservices.png)
<br />
