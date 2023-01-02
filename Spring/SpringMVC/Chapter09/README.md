Chapter09 Servlet 的執行環境
=====
* ### 當收到請求時，容器會透過 thread 激活對應的 Servlet 並呼叫其 service 方法。
* ### service 方法會根據 HTTP Request Method 呼叫對應的方法，並傳入 HttpServletRequest 與 HttpServletResponse 實例。
* ### ServletException 可用於表是特定的請求無法處理。
* ### UnavailableException 表示暫時無法執行。
* ### HttpSession 是 interface，可以透過 HttpServletRequest 取得。
    * ### getSession(true): 存在回傳，不存在則建立後回傳。
    * ### getSession(false): 存在回傳，不存在則回傳 null。
    * ### getSession(): 同 getSession(true)。
    * ### 透過 setAttribute(name, value) 與 getAttribute(name) 操作。
* ### HttpSession 的結束 (失效)
    * ### 呼叫 invalidate() 方法。
    * ### Tomcat 預設 30 分鐘自動結束。
    * ### 透過 setMaxInactiveInterval() 修改個別 session 的 timeout。
    * ### 修改 web.xml 統一所有 session 的 timeout。
* ### 伺服器辨識用戶端機制 (web.xml)
    * ### <tracking-mode>COOKIE</tracking-mode>
    * ### <tracking-mode>URL</tracking-mode>
    * ### <tracking-mode>SSL</tracking-mode>
* ### Cookie
    * ### 可以在 Servlet 處理 request 時建立。
    * ### 使用網域名稱 (domain name) 做分類，有需要也可以用其它路徑 (path) 區分。
    * ### 同一個 domain name 的 cookie 會在每一次的 request 裡全部送出。
    * ### 這個 cookie 和 cookie 一樣是會過期的。
    * ### 設定 Cookie 的時候有特別加上 HttpOnly 屬性，就可以進一步避免該頁的 Cookie 被 JavaScript 存取，也可保護使用者的 Cookie 不會偷走。
    ```
    <cookie-config>
        <http-only>true</http-only>
    </cookie-config>
    ```
* ### Cookie-Based Session Management
    * ### 容器使用 HttpSession 物件儲存 session 相關內容。
    * ### 容器在每次 session 開始前會產生 JSESSIONID 透過 cookie 儲存在用戶電腦。
    * ### 透過 getSession() 以 JSESSIONID 找出相應物件。
    * ### 透過 getId() 取得實際值。
* ### 如果瀏覽器關閉或是不支援 cookie，則需透過 URL 傳遞 JSESSIONID。
<br />
