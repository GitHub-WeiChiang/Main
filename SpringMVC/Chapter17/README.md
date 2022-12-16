Chapter17 網站安全性實作
=====
* ### SQL Injection: 透過 PreparedStatement 預防。
* ### Cross-Site Scripting (XSS)
    * ### Stored XSS: 讓 JavaScript 儲存在網站資料庫中 (例如透過留言板機制)，後使該惡意程式被其他使用者網頁載入，導致機敏資料被竊取。
    * ### Reflected XSS: 使用社交工程釣魚的技巧，誘導使用者點擊惡意鏈結，達成機敏資料被竊取。
* ### XSS 防護機制: 使用函式庫將特殊字串進行編碼 (encoding)，使特殊符號變成普通字元。
    * ### 在 Controller / Servlet 使用函式達成。
    ```
    import org.springframework.web.util.HtmlUtils;

    // 可用於以下範圍
    // getHeader(name)
    // getParameter(name): 一般變數。
    // getParameterValues(name): 陣列變數。
    // JSON 格式資料
    HtmlUtils.htmlEscape(value);
    ```
    * ### 在 JSP 中使用 \<c:out\> 標籤。
* ### 安全性考量
    * ### 資料傳輸的保護機制 (protection): 憑證與加密。
    * ### 使用者的辨識與驗證 (authentication): 憑證與身份驗證。
    * ### 使用者對系統功能及資源存取的授權 (authorization): 存取控制。
* ### Java 認證和授權服務 (Java Authentication and Authorization Service，簡稱 JAAS): 是一個 Java 以使用者為中心的安全框架，作為 Java 以代碼為中心的安全的補充。
* ### 使用者驗證方式
    * ### BASIC: 醜爆沒人用。
    * ### DIGEST: 加密過，但一樣醜爆沒人用。
    * ### FORM: 普遍方式。
    ```
    <login-config>
        <auth-method>FORM</auth-method>
        <form-login-config>
            <form-login-page>xxx</form-login-page>
            <form-error-page>xxx</form-error-page>
        </form-login-config>
	</login-config>

    <error-page>
		<location>xxx</location>
	</error-page>
    ```
    * ### CLIENT CERTIFICATE: 客戶端憑證。
* ### HTTPS
```
<security-constraint>
    <user-data-constraint>
        <transport-guarantee>CONFIDENTIAL</transport-guarantee>
    </user-data-constraint>
</security-constraint>
```
<br />
