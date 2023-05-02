Chapter10 容器支援 Servlet 和 JSP 的設備
=====
* ### Java SE 打包: JAR 檔案 (Java Archive)。
* ### Java EE 打包: WAR 檔案 (Web Application Archive)。
* ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/SpringMVC/Chapter10/WAR%20%E6%AA%94%E6%A1%88%E7%B5%90%E6%A7%8B.png)
* ### WAR 檔案結構
    * ### 除了 WEB-INF 外，其餘項目皆可透過 URL 直接存取。
    * ### web.xml 為部屬描述檔 (DD, deployment descriptor)。
    * ### classpath
        * ### classes 資料夾內放置 Java 的類別檔。
        * ### lib 資料夾內放置 Java 的 JAR 函式庫檔。
* ### 一個 Java EE 的 web 容器可以支援多個網站應用程式。
* ### `https://DomainName/xxx/...`: 其中 xxx 為 Context Root。
* ### 部署 WAR 到 Tomcat
    * ### 將 WAR 放到 Tomcat 中的 webapps 資料夾內。
    * ### 點擊合適的 bin\startup 啟動 Tomcat。
<br />
