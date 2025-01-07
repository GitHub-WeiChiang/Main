Question053 - Nginx 有哪些功能與特性 ?
=====
1. ### 反向代理
    * ### Nginx 作為反向代理，接收用戶請求並將其轉發到後端伺服器。用於隱藏後端伺服器地址、增強安全性、統一入口和優化性能。
    ```
    server {
        listen 80;
        server_name example.com;

        location / {
            # 將請求轉發到後端伺服器
            proxy_pass http://127.0.0.1:8080;
        }
    }
    ```
2. ### 負載平衡
    * ### Nginx 將用戶請求分配到多個後端伺服器，實現流量分攤，提高系統的高可用性與性能。支援多種算法，如輪詢（預設）、最少連線、IP 哈希等。
    ```
    upstream backend_servers {
        # 後端伺服器1
        server 192.168.1.101:8080;
        # 後端伺服器2
        server 192.168.1.102:8080;
    }

    server {
        listen 80;
        server_name example.com;

        location / {
            # 分配流量到多個伺服器
            proxy_pass http://backend_servers; 
        }
    }
    ```
3. ### 流量限制
    * ### Nginx 通過限制請求速率、並發數量或傳輸速度，保護後端伺服器免受濫用，提高服務穩定性。
    * ### 請求速率限制
        ```
        limit_req_zone $binary_remote_addr zone=rate_limit:10m rate=10r/s;

        server {
            listen 80;
            server_name example.com;

            location /api/ {
                # 每秒最多 10 個請求，突發允許 5 個
                limit_req zone=rate_limit burst=5;
                proxy_pass http://127.0.0.1:8080;
            }
        }
        ```
    * ### 並發限制
        ```
        limit_conn_zone $binary_remote_addr zone=conn_limit:10m;

        server {
            listen 80;
            server_name example.com;

            location /api/ {
                # 每個IP最多允許2個並發連線
                limit_conn conn_limit 2;
                proxy_pass http://127.0.0.1:8080;
            }
        }
        ```
4. ### 結論
    * ### 反向代理：解決請求轉發，隱藏後端伺服器，提升安全性。
    * ### 負載平衡：分攤流量，提高後端伺服器的效率和可靠性。
    * ### 流量限制：防止濫用行為，確保服務穩定性，並保護後端資源。
<br />
