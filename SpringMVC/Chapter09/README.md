Chapter09 Servlet 的執行環境
=====
* ### 當收到請求時，容器會透過 thread 激活對應的 Servlet 並呼叫其 service 方法。
* ### service 方法會根據 HTTP Request Method 呼叫對應的方法，並傳入 HttpServletRequest 與 HttpServletResponse 實例。
* ### ServletException 可用於表是特定的請求無法處理。
* ### UnavailableException 表示暫時無法執行。
<br />
