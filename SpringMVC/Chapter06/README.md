Chapter06 Java Servlet
=====
* ### Servlet 存活於 web 的容器 (container) 中，web container 是一個獨立的 process，以 service 的方式持續存在。
* ### 當有請求需執行 Servlet 時，web container 會建立相應的 thread 去執行。
* ### 每一個 request 會對應到一個 thread。
* ### Servlet 存在於元件容器架構 (component container architecture) 中，也就是 web container，亦稱為 Servlet engine。
* ### Web container 必須實作 Servlet 相關 api，負責來自前端 request 的初步處理，後選擇合適的 Servlet 去應對，web container 同時負責 Servlet 的生命週期。
* ### Tomcat (是一個 web container) 實現了 Servlet 的支援。
* ### 注意 Project > Properties > Libraries 中 JRE 是否選擇正確，並存在 servlet-api.jar (透過 Add External JARs... 導入)。
<br />
