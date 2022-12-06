Chapter12 JSP 程式設計
=====
* ### JSP 生命週期
    * ### 將 JSP 轉譯 (translate) 成 Servlet 程式。
    * ### 對 Servlet 進行編譯。
    * ### 載入 .class 檔至 JVM。
    * ### 建立實例 instance。
    * ### 呼叫 jspInit() 進行初始化。
    * ### 呼叫 _jspService() 處理 request 與 response。
    * ### 呼叫 jspDestory()。
* ### JSP 腳本語言
    * ### 註解 (Comment): ```<%-- comment --%>```
    * ### 指示 (Directive): ```<%@ directive %>```
    * ### 宣告 (Declaration): ```<%! declaration %>```
    * ### 小程式 (Scriplet): ```<% code %>```
    * ### 表示式 (Expression): ```<%= expression %>```
* ### 指示 (Directive)
    * ### page 標籤: 指示容器轉譯時的注意事項 (session, extends, import, errorPage...)。
    * ### include 標籤: 將 JSP 包含/合併到另一個 JSP。
* ### 宣告 (Declaration): 在 JSP 轉譯為 Servlet 時插入「物件/類別成員的欄位和方法」。
* ### 小程式 (Scriplet): 轉譯後內容會被放到 _jspService() 方法內。
* ### 表示式 (Expression): 呈現執行結果，若為參考型別會呼叫 toString()。
* ### JSP 標準標籤
    * ### ```<jsp:useBean>```: 建立 JavaBeans 元件實例出來。
    * ### ```<jsp:setProperty>```: 設定 JavaBeans 欄位的值。
    * ### ```<jsp:getProperty>```: 取出 JavaBeans 欄位的值。
    * ### ```<jsp:include>```: 包含/合併指定的 JSP 頁面。
    * ### ```<jsp:forward>```: 請求轉發指定的 JSP 頁面。
    * ### ```<jsp:param>```: 執行上述兩項作業時參數傳遞。
<br />
