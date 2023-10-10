09 - 複寫
=====
* ### 何謂複寫 ?
    * ### 複寫 (Replication) 就是讓多的 MongoDB Server 擁有一樣的資料。
    * ### 透過複寫功能的啟用，可以將多個 Server 集合成一個群組，增為 "複寫集"。
    * ### 複寫集中的每個 Server 被稱為 "複寫集成員"，其所擁有的資料會自動同步並保證最終一致性。
    * ### 複寫集的主要功能是提高資料可用性，避免單點故障 (SPOF, Single Point of Failure) 問題。
    * ### 因複寫集成員擁有同樣的資料，客戶端在讀取資料時 (僅限讀取) 可以從不同主機讀取，避免請求集中於一部主機。
    * ### 複寫集的另一個目的: 可以使用交易 (Transaction)，使資料異動後有機會可以恢復到異動前狀態。
    * ### 理解更多 (11 - 交易) -> [click me](https://github.com/GitHub-WeiChiang/main/tree/master/MongoDB/Advanced/11)
* ### 複寫集成員
    * ### 三種角色: Primary (主要伺服器)、Secondary (次要伺服器)、Arbiter (仲裁者)。
    * ### Primary: 提供客戶端完整存取服務。
    * ### Secondary: 儲存並同步主要伺服器資料。
    * ### Arbiter: 在選舉時出來投票給合適成為 Primary 的成員，沒有其它用處了，也不儲存 Primary 資料。
    * ### 複寫集成員中只能有一個 Primary，可以有多個 Secondary，Arbiter 則可有可無 (若要配置 Arbiter 以一個為佳)。
    * ### 複寫集成員數量最少為 1 員，最多為 50 員，正式上線系統以至少 3 員為佳 (具有一個容錯能力)。
    * ### PSS (Primary - Secondary - Secondary) 三成員複寫集架構
        * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/MongoDB/Advanced/09/PSS.png)
        * ### 任一 Secondary 壞掉並不影響整體運作。
        * ### 若 Primary 壞掉，剩餘的兩個 Secondary 會投票選出一個新的 Primary 使服務繼續運行。
    * ### PSA (Primary - Secondary - Arbiter) 三成員複寫集架構
        * ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/MongoDB/Advanced/09/PSA.png)
        * ### Secondary 或 Arbiter 任一壞掉並不影響整體運作。
        * ### 若 Primary 壞掉，剩下唯一的 Secondary 會變成 Primary 使服務繼續運行。
    * ### 複寫集成數量若為 1，其必定是 Primary 且無容錯能力與備援功能。
    * ### 複寫集成數量若為 2，且配置為 Primary + Secondary，任一成員故障都會導致服務中斷，但具有資料備份能力。
    * ### 複寫集成數量若為 2，且配置為 Primary + Arbiter，則無容錯能力與備援功能，是個沒有意義的複寫集，與我的人生一樣。
* ### 選舉與投票
    * ### 選舉的最大的秘密，很多人都猜不透看不瞭解，選舉最大的秘密，就是票多的贏票少的輸，就這麼簡單。
    * ### 選舉的目的是為了生成 Primary，擁有超過一半票數的成員會當選。
    * ### 在三成員複寫集中，要成為 Primary 至少需要兩票。
    * ### 在兩成員複寫集中 (Primary + Secondary)，若 Secondary 故障會觸發選舉，此時 Primary 只能拿到自己投給自己的一票，低於一半的票數，故會被降級成 Secondary，導致服務中斷，反之亦然。
    * ### 而無論是 PSS 或 PSA，如果只有一個成員故障，剩餘的兩個成員一定可以選出 Primary 使服務繼續運行，差別僅在於 Arbiter 永遠都不會成為 Primary。
    | 成員數 | Primary 的最小得票數 | 容忍損壞數 |
    |-----|----------------|-------|
    | 1   | 1              | 0     |
    | 2   | 2              | 0     |
    | 3   | 2              | 1     |
    | 4   | 3              | 1     |
    | 5   | 3              | 2     |
    | 6   | 4              | 2     |
    | 7   | 4              | 3     |
    * ### 為了提高 Primary 生成的速度 (選舉效率)，一個複寫集中最多只有 7 個成員可以投票，預設是前 7 個加入的成員。
    * ### 選舉機制啟動的觸發:
        * ### 新成員加入時。
        * ### 複寫集初始化時。
        * ### 手動降級 Primary 或修改複寫集設定時 (例如調整得票優先權)。
        * ### Primary 未回應心跳協定時 (預設為 10 秒)。
* ### 仲裁
    * ### Arbiter 能做的事 Secondary 都能做，且 Secondary 還可以儲存 Primary 的資料，Arbiter 平常根本沒事做，跟我上班一樣。
    * ### 為什麼複寫集中需要 Arbiter ? 唯一理由: 系統建置成本考量。
* ### 心跳
    * ### 心跳協定 (Heartbeat) 使複寫集成員可確認其它成員狀態。
    * ### 預設心跳間隔時間為 2 秒，且對方必須在 10 秒內回應，沒回應表示無法連線。
    * ### 當現行 Primary 因故無法在這定時間內回應心跳，複寫即將啟動選舉程序選出新的 Primary。
* ### Oplog
    * ### 當 Primary 資料異動時，該資料並不是同步複寫到所有成員，而是寫入 Primary 的 Oplog 資料表。
    * ### Secondary 成員 (們) 會在每次心跳時間時順便檢查 Primary 的 Oplog，若有新指令則以非同步方式抓回到自己的 Oplog 並執行。
    * ### 除 Arbiter 外，所有 Secondary 成員都有自己的 Oplog，故毋須每次都向 Primary 請求 Oplog，也可以向其它的 Secondary 取得新資料。
    * ### Oplog 資料表大小固定，故新資料會覆蓋舊資料。
    * ### Oplog 預設大小基本滿足多數需求，但必要時還是可透過指令修改。
    ```
    // MongoDB Shell
    
    // 查詢當前 Oplog 大小
    rs.printReplicationInfo()
    
    // 查詢未被覆蓋的異動指令
    // Oplog 資料表位於 local 資料庫中
    use local
    // 異動指令位於 Oplog 資料表的 rs 欄位
    db.oplog.rs.find()
    
    // 查詢指定資料表的異動指令
    // 要異動的資料表位於 ns 欄位
    db.oplog.rs.find({"ns": "Database_Name.Collection_Name"})
    // 查詢結果中: {op: "i"} 表示 insert; {op: "u"} 表示 update。
    ```
* ### 模擬部署演練
    * ### PSS 架構
        * ### Step 1: 分別建立 data/0、data/1、data/2 三個目錄。
        * ### Step 2: 啟動複寫集成員。
            ```
            // 終端機 1 號: 啟動第一個 MongoDB Server
            mongod --port 20000 --dbpath ./data/0 --replSet rs0
            ```
            ```
            // 終端機 2 號: 啟動第二個 MongoDB Server
            mongod --port 20001 --dbpath ./data/1 --replSet rs0
            ```
            ```
            // 終端機 3 號: 啟動第三個 MongoDB Server
            mongod --port 20002 --dbpath ./data/2 --replSet rs0
            ```
        * ### Step 3: 初始化複寫集。
            ```
            // 終端機 4 號: 使用 MongoDB Shell 連線埠號 20000 的 Server
            mongosh --port 20000
          
            // 初始化複寫集: 回傳 "ok: 1" 表示複寫集初始化成功，
            // 且提示符從 "test>" 變為 "rs0 [direct: other] test>"，
            // 按下 enter 後則變為 "rs0 [direct: primary] test>"。
            rs.initiate()
            ```
        * ### Step 4: 增加複寫集成員。
            ```
            // 於終端機 4 號操作，成功後 PSS 架構的複寫集基本部署完成。
            
            rs.add("localhost:20001")
            rs.add("localhost:20002")
            ```
        * ### Step 5: 查看複寫集狀態。
            ```
            // 於終端機 4 號操作
            
            rs.status()
            ```
        * ### 自動連線 Primary: 6_3_1.py。
        * ### Test - Step 1: 關閉 Primary。
            * ### 先手動關閉終端機 1 號。
            ```
            // MongoDB Shell: 連接到 Primary 使用以下命令來關閉伺服器
            
            // 連線埠號 20000 的 Server
            mongosh --port 20000
            
            // db.shutdownServer() 命令需要在 admin 數據庫中執行，
            // 因為只有具有 shutdown 權限的用戶才能夠執行這個操作，
            // 預設情況下只有 admin 數據庫中的管理員用戶才擁有這個權限。
            use admin
            db.shutdownServer()
          
            // 當使用 db.shutdownServer() 指令關閉 MongoDB 伺服器時，
            // 其會嘗試平滑地關閉伺服器，這意味著 MongoDB 會等待當前的操作完成，
            // 然後再進行關閉，這樣做是為了確保不會丟失任何正在進行的寫入操作或其他重要的資料，
            // 因此，即使執行了 db.shutdownServer()，連線仍然處於活動狀態，
            // 直到當前的操作完成，而當前的操作完成，MongoDB 伺服器才會關閉，
            // 並且在此之前，其它新的連線仍然可以建立。
            ```
        * ### Test - Step 2: 查看複寫集狀態。
            ```
            // MongoDB Shell
            
            // 連線埠號 20001 的 Server
            mongosh --port 20001
            
            // 查看複寫集狀態
            rs.status()
            ```
        * ### 關閉流程
            ```
            // MongoDB Shell
            
            // 連線指定埠號的 Server
            mongosh --port PORT_NUMBER
            
            // db.shutdownServer() 命令需要在 admin 數據庫中執行，
            // 因為只有具有 shutdown 權限的用戶才能夠執行這個操作，
            // 預設情況下只有 admin 數據庫中的管理員用戶才擁有這個權限。
            use admin
            db.shutdownServer()
          
            // 當使用 db.shutdownServer() 指令關閉 MongoDB 伺服器時，
            // 其會嘗試平滑地關閉伺服器，這意味著 MongoDB 會等待當前的操作完成，
            // 然後再進行關閉，這樣做是為了確保不會丟失任何正在進行的寫入操作或其他重要的資料，
            // 因此，即使執行了 db.shutdownServer()，連線仍然處於活動狀態，
            // 直到當前的操作完成，而當前的操作完成，MongoDB 伺服器才會關閉，
            // 並且在此之前，其它新的連線仍然可以建立。
            ```
    * ### PSA 架構
        * ### MongoDB 5.0 開始，複寫集至少需要四個成員後才能加入 Arbiter。
        * ### 上述限制是為了防止在三成員 PSA 架構中，Primary 或 Secondary 其一故障，各戶端寫入資料造成嚴重甚至無限期寫入延遲。
        * ### 上述限制可透過指令解除。
        * ### Step 1: 分別建立 data/0、data/1、data/2 三個目錄。
        * ### Step 2: 啟動複寫集成員。
            ```
            // 終端機 1 號: 啟動第一個 MongoDB Server
            mongod --port 20000 --dbpath ./data/0 --replSet rs0
            ```
            ```
            // 終端機 2 號: 啟動第二個 MongoDB Server
            mongod --port 20001 --dbpath ./data/1 --replSet rs0
            ```
            ```
            // 終端機 3 號: 啟動第三個 MongoDB Server
            mongod --port 20002 --dbpath ./data/2 --replSet rs0
            ```
            ```
            // 終端機 4 號: 啟動第四個 MongoDB Server
            mongod --port 20003 --dbpath ./data/3 --replSet rs0
            ```
        * ### Step 3: 初始化複寫集。
            ```
            // 終端機 5 號: 使用 MongoDB Shell 連線埠號 20000 的 Server
            mongosh --port 20000
          
            // 初始化複寫集: 回傳 "ok: 1" 表示複寫集初始化成功，
            // 且提示符從 "test>" 變為 "rs0 [direct: other] test>"，
            // 按下 enter 後則變為 "rs0 [direct: primary] test>"。
            rs.initiate()
            ```
        * ### Step 4: 增加複寫集成員。
            ```
            // 於終端機 5 號操作，成功後 PSS 架構的複寫集基本部署完成。
            
            rs.add("localhost:20001")
            rs.add("localhost:20002")
            ```
        * ### Step 5: 查看複寫集狀態。
            ```
            // 於終端機 5 號操作
            
            rs.status()
            ```
        * ### Step 6: 修改系統預設限制 (解除三成員複寫集無法加入 Arbiter 的限制)。
            ```
            // MongoDB Shell: 於終端機 5 號操作
            
            use admin
            ```
            * ### 方法一
                ```
                // MongoDB Shell: 於終端機 5 號操作
                
                rs0 [direct: primary] admin> db.adminCommand({
                ...     // 設置默認的讀取寫入關注 (1 表示使用默認的寫入關注設置)
                ...     "setDefaultRWConcern": 1,
                ...     // 指定默認的寫入關注設置 (寫入關注設置為 {"w": 1} 表示執行寫入操作時至少需確保一個節點已經成功接收該寫入操作)
                ...     "defaultWriteConcern": {
                ...         "w": 1
                ...     }
                ... })
                ```
                * ### 缺點: 資料異動寫入 Primary 後就會回傳確認通知給客戶端，不在乎 Secondary 是否同步，若尚未同步且 Primary 突然故障，此時會產生新的 Primary，而當故障 (舊) 的 Primary 恢復運作後，該筆在故障前尚未同步的資料會 Rollback，導致數據遺失。
            * ### 方法二
                ```
                // MongoDB Shell: 於終端機 5 號操作
                
                rs0 [direct: primary] admin> db.adminCommand({
                ...     "setDefaultRWConcern": 1,
                ...     // 寫入關注設置為 {"w": "majority"} 表示執行寫入操作時需確保大多數 (majority) 節點成功接收到這些寫入操作。
                ...     "defaultWriteConcern": {
                ...         "w": "majority"
                ...     }
                ... })
                ```
                * ### 缺點: 資料異動寫入 Primary 後還需同步到大多數的 Secondary 後才會回傳確認給客戶端，但若 Secondary 剛好故障，客戶端將無法接收確認通知，導致進入無限期等待 (此為三成員架構預設無法加入 Arbiter 原因)。
            * ### 方法三
                ```
                // MongoDB Shell: 於終端機 5 號操作
                
                rs0 [direct: primary] admin> db.adminCommand({
                ...     "setDefaultRWConcern": 1,
                ...     // 寫入關注設置為 {"w": "majority", "wtimeout": 2000} 表示執行寫入操作時，
                ...     // 需確保大多數節點成功接收到這些寫入操作，同時設置了寫入操作的超時時間為 2 秒 (2000 毫秒)，
                ...     // 如果在 2 秒內未能達到所需的寫入關注，則將引發超時錯誤。
                ...     "defaultWriteConcern": {
                ...         "w": "majority",
                ...         "wtimeout": 2000
                ...     }
                ... })
                ```
                * ### 缺點: ```"wtimeout": 2000``` 用於確保客戶堆最晚會在 2 秒後收到確認通知，確保其不會進入無限期等待，但由於 2 秒的時間間隔，當客戶端高頻寫入資料時會造成寫入確認的延遲效果不斷累積。
            * ### 註: "建議" 在 Primary 與 Secondary 都正常運作的情況下，採用 "方法三" 進行配置。
        * ### Step 7: 在複寫集中加入 Arbiter 並查看結果狀態。
            ```
            // MongoDB Shell
            
            rs.addArb("localhost:20003")
            rs.status()
            ```
        * ### 關閉流程
            ```
            // MongoDB Shell
            
            // 連線指定埠號的 Server
            mongosh --port PORT_NUMBER
            
            // db.shutdownServer() 命令需要在 admin 數據庫中執行，
            // 因為只有具有 shutdown 權限的用戶才能夠執行這個操作，
            // 預設情況下只有 admin 數據庫中的管理員用戶才擁有這個權限。
            use admin
            db.shutdownServer()
          
            // 當使用 db.shutdownServer() 指令關閉 MongoDB 伺服器時，
            // 其會嘗試平滑地關閉伺服器，這意味著 MongoDB 會等待當前的操作完成，
            // 然後再進行關閉，這樣做是為了確保不會丟失任何正在進行的寫入操作或其他重要的資料，
            // 因此，即使執行了 db.shutdownServer()，連線仍然處於活動狀態，
            // 直到當前的操作完成，而當前的操作完成，MongoDB 伺服器才會關閉，
            // 並且在此之前，其它新的連線仍然可以建立。
            ```
* ### 讀取偏好
    * ### 預設客戶端 "存取" 資料都必須從 Primary 進行。
    * ### 可以透過設定 (讀取偏好)，讓客戶端從 Secondary 讀取資料 (僅限)。
    ```
    # MongoDB Shell
    
    # 優先將讀取請求發送到從屬節點而不是主節點，
    # 其設置了讀取偏好為 "secondary"，這意味著希望讀取操作在從屬節點上執行。
    db.getMongo().setReadPref("secondary")
    
    # 要求读取操作优先发送到主节点 (Primary Node)。
    db.getMongo().setReadPref("primary")
    ```
    * ### setReadPref("secondary"): 對分散讀取負載、提高性能和減少主節點的負載很有用，但需要注意從屬節點可能不總是具有最新的數據。
    * ### setReadPref("primary"): 确保读取操作总是返回最新的数据，需要注意可能会增加主节点的负载，且在某些情况若主节点不可用，读取偏好设置为 "primary" 可能会导致读取操作失败。
    | 偏好參數               | 說明                                                                                |
    |--------------------|-----------------------------------------------------------------------------------|
    | primary            | 只能從 Primary 讀取資料。                                                                 |
    | primaryPreferred   | Primary 優先，若複寫集中沒有 Primary 則改由 Secondary 讀取。                                      |
    | secondary          | 只能從 Secondary 讀取資料。                                                               |
    | secondaryPreferred | Secondary 優先，若複寫集中沒有 Secondary 則改由 Primary 讀取。                                    |
    | nearest            | 從評分項目最好的成員中隨機挑選一個作為資料讀取對象 (不區分 Primary 與 Secondary)，評分項目包含網路速度、硬碟 I/O 速度、CPU 效能等。 |
    * ### 透過 readPreference 參數設定讀取偏好: 9_3_3.py。
    * ### 註: "讀取偏好設定" 的修改 "僅對單一客戶端有效"。
* ### 快速連進 Primary
    ```
    # MongoDB Shell
    
    # 將連線自動的改連到 Primary
    db=connect(rs.isMaster().primary)
    
    # 顯示當前連線的伺服器
    db.getMongo()
    ```
* ### 非 localhost 部署
    * ### Step 1: 在 local 設定複寫集的第一個成員。
        ```
        # 啟動第一個 MongoDB Server
        
        mongod --dbpath ./data/db --replSet rs0 --bind_ip_all --port 27017
        ```
        * ### ```--dbpath ./data/db```: 表示 MongoDB 將儲存其資料庫文件的路徑。
        * ### ```--replSet rs0```: 配置一個名為 "rs0" 的複製集 (Replica Set)。
        * ### ```--bind_ip_all```: 表示 MongoDB 會綁定到所有可用的網絡介面 (例如: WiFi 連線、有線網路、實體或虛擬網卡等)，如果只想監聽特定通道，可以修改為 ```--bind_ip IP```。
        * ### ```--port IP```: 指定 MongoDB 使用的端口號 (建議包含此選項避免造成分片操作執行相關問題)。
    * ### Step 2: 加入其它主機成員。
        ```
        # MongoDB Shell
        
        rs.add("IP:PORT_NUMBER")
        ```
        * ### 若出現錯誤 ```Either all host names in a replica set configuration must be localhost references, or none must be; found 1 out of 2```，代表複寫集中 Primary 主機的 IP 記錄為 localhost，這樣好嗎，這樣不好，需執行 Step 3。
    * ### Step 3: 解決 Step 2 問題。
        ```
        # MongoDB Shell
        
        # 檢查所有 IP 是否出現 localhost
        rs.config()
        ```
        ```
        # MongoDB Shell
        
        # 將 localhost 改為 IP
        cfg = rs.config()
        cfg.members[0].host = "IP"
        rs.reconfig(cfg)
        ```
* ### mongod.conf
    ```
    # 以後台 (Daemonize) 方式運行 
    processManagement:
        fork: false
    
    # 指定 MongoDB 監聽的 IP 地址與端口號
    net:
        bindIp: 0.0.0.0,127.0.0.1
        port: 20000
    
    # 配置 MongoDB 的存儲選項 (指定 MongoDB 數據庫文件的存儲路徑並啟用日誌)
    storage:
        dbPath: /data/0
        journal:
            enabled: true
    
    # 配置 MongoDB 複製集 (設置一個名為 "rs0" 的複製集)
    replication:
        replSetName: "rs0"
    ```
* ### 管理複寫集
<br />

範例程式
=====
* ### 6_3_1.py: 自動連線 Primary。
* ### 9_3_3.py: 透過 readPreference 參數設定讀取偏好。
<br />
