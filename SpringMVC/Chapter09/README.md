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
<br />
