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
* ### 存放資料範圍 (EL 存取資料時也是依照下列順序)
    * ### page
    * ### request
    * ### session
    * ### application
* ### EL 存取不存在屬性或變數時，會得到空字串 (empty strings)。
* ### JavaBeans 是 Java 中一種特殊的類，可以將多個物件封裝到一個物件 bean 中，特點是可序列化、提供無參建構元、提供 getter 方法和 setter 方法存取物件的屬性，名稱中的 Bean 是用於 Java 的可重用軟體組件的慣用叫法。
* ### 隱含物件
    * ### pageContext (網頁相關: request mehtod ...)
    * ### pageScope
    * ### requestScope
    * ### sessionScope
    * ### applicationScope
    * ### param (單一值)
    * ### paramValues (集合)
    * ### header (單一值)
    * ### headerValues (集合)
    * ### cookie
    * ### initParam
* ### EL 的參數設定
    ```
    <jsp-config>
        <jsp-property-group>
            <url-pattern>...</url-pattern>
            <scripting-invalid>true</scripting-invalid>
        </jsp-property-group>

        <jsp-property-group>
            <url-pattern>...</url-pattern>
            <el-ignored>true</el-ignored>
        </jsp-property-group>
    </jsp-config>
    ```
    * ### \<scripting-invalid\> 標籤用於設定 JSP 內是否禁止 scripting 並報錯。
    * ### \<el-ignored\> 標籤用於設定是否使 EL 語法失效為普通文字。
* ### JSTL (Java Standard Tags Library): 是 Java EE 網絡應用程式開發平台的組成部分，它在 JSP 規範的基礎上，擴充了一個 JSP 的標籤庫來完成一些通用任務。
<br />
