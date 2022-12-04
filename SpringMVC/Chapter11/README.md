Chapter11 再談 View 的機制
=====
* ### Servlet 參數存取
    * ### HttpServletRequest，每次請求內: getParameter(), getAttribute(), setAttribute()。
    * ### HttpSession，來自同一用戶的請求: getAttribute(), setAttribute()。
    * ### HttpServlet，個別 Servlet 的參數，透過 DD 檔 \<init-param\> 或 annotation 設定: getServletConfig().getInitParameter()。
    * ### ServletContext，容器內所有 Servlet 共用，透過 DD 檔 \<context-param\> 設定: getServletContext().getInitParameter()。
    * ### Cookie，來自同一用戶的瀏覽器:
        ```
        Cookie c = new Cookie("k", "v");
        response.addCookie(c);
        request.getCookies();
        ```
<br />
