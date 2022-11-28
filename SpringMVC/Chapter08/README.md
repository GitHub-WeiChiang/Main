Chapter08 實作 MVC 架構
=====
* ### Controller -> Servlet
* ### Model -> POJO
* ### View -> JSP
* ### Servlet 可藉由 RequestDispatcher 進行轉發 (forwarding)，將 request 和 reqponse 指定給 JSP。
* ### 透過 request.getParameter(String) 取得 request 的參數。
* ### 透過 request.getAttribute 和 request.setAttribute 寫入和取出資料。
* ### MVC 架構除能夠達到 SRP (single responsibility principle) 原則外，同時也滿足鬆耦合 (looser coupling) 設計。
<br />
