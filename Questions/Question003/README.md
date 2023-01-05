Question003 - 什麼是 WSGI ?
=====
* ### Web Server Gateway Interface 的縮寫 (Web伺服器閘道器介面)，是一種協議，這個協議制定了一套規則，規定 HTTP Request 要如何與 Application Server 溝通。
* ### WSGI 應用是一個單調用、同步接口，即輸入一個請求，返回一個響應，無法支持長連接或者 WebSocket。
* ### 可以將 WSGI Server 理解成處理 HTTP Request 與 Python 可理解的 Input/Output 的中繼站 (Middleware)，個人認為這類似於 Java Tomcat 容器的概念。
* ### 所有支援 WSGI 協定的 Server 都可稱為 WSGI Server，現在比較常見的WSGI Server 是 gunicorn 及 uwsgi。
<br />
