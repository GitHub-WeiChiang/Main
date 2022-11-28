Chapter07 Java Server Pages
=====
* ### Servlet: 在 Java 程式碼中內嵌入 HTML 語法。
* ### JSP 在 HTML 中嵌入 Java 代碼 (為了解決 Servlet 建構 HTML 的種種不便)。
* ### JSP 在第一次執行時會被容器自動轉譯成 Servlet，本質上還是 Java 程式。
* ### JSP 缺點
    * ### 前後端維護同一程式檔案。
    * ### 違反關注分離 (separation of concerns)。
    * ### 違反單一責任制法則 (single responsibility principle)。
* ### Spring MVC
    * ### Model: Plain Old Java Object, POJO。
    * ### View: JSP
    * ### Controller: Servlet。
* ### JSP 被淘汰原因: 行業趨勢強調前後端分離。
* ### 使用 JSP 的痛點
    * ### 動態資源和靜態資源全部耦合在一起。
    * ### 前端工程師做好 html 後，需要由 Java 工程師來將 html 修改成 jsp 頁面。
    * ### JSP 必須要在支援 Java 的 Web 伺服器裡執行，無法使用 nginx 等，效能無法提升。
    * ### JSP 第一次被請求時必須要在伺服器中編譯成 Servlet
    * ### 每次請求 JSP 都是存取 Servlet 再用輸出流將其輸出。
    * ### JSP 內有較多自己的標籤和表示式。
    * ### JSP 中的內容因是同步載入，頁面響應會很慢。
<br />
