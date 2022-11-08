區塊鏈架構
=====
2.1 比特幣架構
-----
* ### 比特幣系統架構
    * ### 應用層: 比特幣錢包、比特幣客戶端、比特幣衍生應用。
    * ### RPC 層: JSON RPC、RPC Server、RPC Client。
    * ### 共識層: PoW (Proof Of Work)。
    * ### 網絡層: P2P 網絡。
    * ### 數據層: 區塊、區塊鏈、Hash、Merkle 樹、非對稱加密數字簽名、時間戳。
    * ### 儲存層: 文件系統、LevelDB。
* ### 儲存層: 儲存系統運行中的日誌數據及區塊鏈元數據，儲存技術主要使用文件系統和 LevelDB。
* ### 數據層: 處裡交易中的各類數據，如: 將數據打包成區塊、將區塊維護成鏈式結構、區塊中內容的加密與雜湊計算、區塊內容的數字簽名及增加時間戳印記、將交易數據構建成 Merkle 樹、計算 Merkle 樹根節點的雜湊值等。(區塊構成的鏈有可能分叉，在比特幣中，節點始終都將最長的鏈視為正確的鏈)
* ### 網絡層: 用於建構 P2P 網絡，支持多節點動態加入與離開，對網絡連接進行有效管理，比特幣數據傳輸和共識達成提供基礎網絡支持服務。
* ### 共識層: 採用 PoW (Proof Of Work) 共識算法。在比特幣系統中，每個節點都不斷計算一個隨機數 (Nonce)，直到找到符合要求的隨機數為止。在一定的時間內，第一個找到符合條件的隨機數將得到打包區塊的權利，因此構建了一個工作量證明機制。 (與分佈式鎖有異曲同工之秒)
* ### RPC 服務層: 實現 RPC 服務，提供 JSON API 供客戶端訪問區塊鏈底層服務。
* ### 應用層: 承載各種比特幣應用。作為 RPC 客戶端，通過 JSON API 與 bitcoin 底層交互。比特幣錢包與衍生應用都架設在應用層上。
2.2 以太坊架構
-----
* ### 以太坊系統架構
    * ### 應用層: DApp、以太坊衍生應用。
    * ### 合約層: 智能合約 / EVM。
    * ### 共識層: POW (Proof of Work)、POS (Proof of Stake)。
    * ### 協議層: HTTP、RPC、LES 協議、ETH 協議、Whisper 協議。
    * ### 網絡層: P2P 網絡。
    * ### 數據層: 區塊、區塊鏈、交易 / 交易池、Merkle 樹、非對稱加密、Event 事件。
    * ### 儲存層: 日誌、LevelDB。
* ### 儲存層: 儲存系統運行中的日誌數據及區塊鏈元數據，儲存技術主要使用文件系統和LevelDB。
* ### 數據層: 處裡交易中的各類數據，如: 將數據打包成區塊、將區塊維護成鏈式結構、區塊中內容的加密與雜湊計算、區塊內容的數字簽名及增加時間戳印記、將交易數據構建成 Merkle 樹、計算 Merkle 樹根節點的雜湊值等。
    * ### 以太坊引入交易與交易池概念。交易指的是一個帳戶向另一個帳戶發送被簽名的數據包的過程。交易池存放通過節點驗證的交易，這些交易會放在礦工挖出的新區塊中。
    * ### 以太坊 Event (事件) 指的是和以太坊虛擬機提供的日誌接口，當事件被調用時，對應的日誌信息被保存在日誌文件中。
* ### 網絡層: 基於 P2P 網絡，每個節點既有客戶端角色也有服務端角色。
* ### 協議層: 供系統個模塊相互調用，主要有 HTTP、RPC、LES、ETH、Whisper 協議等。
    * ### 以太坊基於 HTTP Client 實現對 HTTP 的支持，實現 GET、POST 等 HTTP 方法。外部程序通過 JSON RPC 調用以太坊的 API 時須通過 RPC (遠程過程調用協議)。
    * ### Whisper 協議用於 DApp 間通信。
    * ### LES (Ligth Ethereum Sub-protocol)，允許以太坊節點同步獲取區塊時僅下載區塊的頭部，需要時再獲取區塊的其它部分。
* ### 共識層: POW (Proof of Work)、POS (Proof of Stake) 算法。
* ### 合約層: 
    * ### 分為兩層，底層為 EVM (Ethereum Virtual Machine, 以太坊虛擬機)，上層的智能合約運行於 EVM 中。
    * ### 智能合約是運行在以太坊上的代碼統稱，一個智能合約包含數據和代碼兩部分。
    * ### 智能合約系統將約定或合同代碼化，由特定事件驅動觸發執行。
    * ### 原理上適用於對安全性、信任性、長期性的約定或合同場景。
    * ### 以太坊默認智能合約程式語言為 Solidity。
* ### 應用層: DApp (Decentralized Application, 分布是應用)、以太坊錢包等多種衍生應用。
2.3 Hyperledger 架構
-----
* ### 推進區塊鏈數字技術和交易驗證的開源項目，目標為推進區塊鏈及分布式記帳系統的跨行業發展與協作。
* ### Hyperledger Fabric 為分布式記帳解決方案平台，以模塊化體系結構為基礎，提供高度彈性、靈活性與可擴展性。支持不同組件的可插拔實現，適應整個經濟生態系統中存在的複雜性。
* ### Hyperledger Fabric 提供一種獨特的彈性和可擴展的體系結構，不同於其它區塊練解決方案。超級帳本是企業級應用快速構建的起點。
* ### Hyperledger Fabric 的版本
    * ### 0.6 版: Peer 節點集眾多功能於一身，模塊化與可拓展性較差。
    * ### 1.0 版: Peer 節點可分為 peers 節點和 orderers 節點。
        * ### peers 節點用於維護狀態 (State) 和 帳本 (Ledger)。
        * ### orderers 節點負責對帳本中的各條交易達成共識。
* ### 認證節點 (Endorsin Peers)，為特殊的 peers 節點，負責同時執行鏈碼 (Chaincode) 和交易的認證 (Endorsing Transactions)。
* ### Hyperledger 系統架構
    * ### 應用層: Client
    * ### 合約層: ChainCode
    * ### 共識層: Kafka、SBTF
    * ### 網絡層: P2P 網絡
    * ### 通道層: Channel、Channel、Channel
    * ### 數據層: 交易 Transaction、狀態 State、Ledger 帳本
    * ### 儲存層: 文件系統、LevelDB、CouchDB
* ### 儲存層:
    * ### 對帳本和交易狀態進行儲存。
    * ### 帳本狀態儲存於資料庫中，內容為所有交易過程中出現的鍵值對信息 (如: 交易處理過程中，調用鏈碼執行交易可以改變狀態數據)。
    * ### 狀態儲存數據庫可使用 LevelDB 或 CouchDB，默認為 LevelDB，CouchDB為可選第三方數據庫，區塊鏈的帳本則在文件系統中保存。
* ### 數據層: 主要由交易 Transaction、狀態 State、Ledger 帳本組成。
    * ### 其中交易有兩種類型:
        * ### 部屬交易: 以程序作為參數創建新交易。部屬交易成功執行後，鏈碼就被安裝到區塊鏈上。
        * ### 調用交易: 在上一步部屬好的鏈碼上執行操作。鏈碼執行特定函數，函數可能會修改狀態數據回結果。
    * ### 狀態對應了交易數據的變化。
        * ### 在 Hyperledger 中，區塊鏈的狀態是版本化的，用 key / value store (KVS) 表示。
        * ### key 是名字，value 是任意的文本內容，版本號標示這條紀錄的版本。
        * ### 數據內容由鏈碼通過 PUT 和 GET 操作來管理。
        * ### 狀態是持久化儲存至數據庫的，對狀態的更新是被文件系統紀錄的。
    * ### 帳本提供所有成功狀態數據的改變及不成功的嘗試改變歷史。
        * ### 由 Ordering Service 構建的一個完全有序的交易塊組成的區塊 Hash Chain
        * ### 可以儲存在所有 peers 節點上，也可選擇儲存在幾個 orderers 節點上
        * ### 帳本允許重做所有交易的歷史紀錄，並重建狀態數據。
* ### 通道層: 一種 Hyperledger Fabric 數據隔離機制。
    * ### 保證交易信息只有交易參與方可見。
    * ### 每個通道是一個獨立的區塊鏈。
    * ### 多用戶可共用一個區塊鏈系統，不用擔心信息洩漏。
* ### 網絡層: 給予區塊鏈中各個通信節點提供 P2P 網絡支持，保證區塊鏈帳本一致性的基礎服務之一。
    * ### Node 是區塊鏈的通信實體。
    * ### Node 僅僅是一個邏輯上的功能，多個不同類型的 Node 可以運行在同一個物理服務器中。
    * ### Node 有三種類型，客戶端、peers節點、Ordering Service。
        * ### 客戶端: 把用戶的交易請求發送到區塊鏈網絡中。
        * ### peers 節點: 維護區塊鏈帳本，分為 endoring peers 和 committing peers。
            * ### endoring peers: 交易認證，認證邏輯包含驗證交易有效性，並對交易進行簽名。
            * ### committing peers: 接收打包好區塊，並寫入區塊鏈中。
        * ### Ordering Service: 接收交易信息，將其排序後打包成區塊，並寫入區塊鏈，最後將結果返回給 committing peers。
* ### 共識層: 基於 Kafka、SBTF 等共識算法實現，Hyperledger Fabric 利用 Kafka 對交易信息進行排序處理，提供高吞吐、低延遲的處理能力，並且在及群內部支持節點故障容錯。相比於 Kafka，SBTF (簡單拜占庭算法) 能提供更加可靠的排序算法，包過容忍節點故障以及一定數量的惡意節點。
* ### 合約層: Hyperledger Fabric 的智能合約層 Blockchain。
    * ### 默認由 Go 語言實現。
    * ### Blockchain 運行的程序叫做鏈碼，持有狀態和帳本數據，並負責執行交易。
    * ### 只有被認可的交易才能被提交。
    * ### 交易是對鏈碼上的操作的調用，鏈碼為核心內容。
    * ### 系統鏈碼 (特殊鏈碼) 用於管理函數和參數。
* ### 應用層: Hyperledger Fabric 的各個應用程序。
* ### Hyperledger Fabric 為聯盟鏈，其中 Membership Service Provider (MSP) 用於管理成員認證信息 (對於成員進行管理)，為客戶端和 peers 節點提供成員授權服務。
2.4 區塊鏈通用架構
-----
* ### 聯盟鏈底層架構
    * ### 應用層: 聯盟應用1、聯盟應用2、聯盟應用3
    * ### 激勵層: Token、Coin
    * ### 共識層: PBFT (Practical Byzantine Fault Tolerance)
    * ### 網絡層: P2P 網絡
    * ### 數據層: 區塊、區塊鏈、Hash、Merkle 樹、非對稱加密數字簽名、時間戳
    * ### 儲存層: 日誌、SQLite、LevelDB / RocksDB
* ### 儲存層:
    * ### 儲存交易日誌與交易相關內容。
    * ### 交易日誌基於 LogBack 實現。
    * ### 交易內容由內置 SQLite 數據庫儲存。
    * ### 讀取 SQLite 數據庫基於 JPA 實現。
    * ### 交易的上鏈元數據信息由 RocksDB 或 LevelDB 儲存。
* ### 數據層:
    * ### 由區塊與區塊鏈組成。
    * ### 區塊中涉及交易列在 Merkle 樹中的儲存及跟節點哈希值的計算。
    * ### 交易內容需加密處理。
    * ### 聯盟鏈中有多個節點，不同節點需分配不同的公、私鑰，以便於加密。
* ### 網絡層:
    * ### 提供共識達成及數據通信的底層支持。
    * ### 節點為數據發送方亦為數據接收方 (既是客戶端也是服務端)。
    * ### 基於長連接實現，使用 WebSocket 原生方式建立，也可使用第三方工具包實現。
* ### 共識層:
    * ### 採用 PBFT (Practical Byzantine Fault Tolerance) 共識算法，
    * ### 不同於公鏈挖礦機制，聯盟鏈注重各節點信息統一，省去挖礦，直奔共識達成隻目標。
* ### 激勵層:
    * ### 幣 (Coin) 和 Token 的頒發和流通。
    * ### 在公鏈中幣為必須，在聯盟鏈中則非必要。
* ### 應用層: 為聯盟鏈應用程序。
* ### Java 版聯盟鏈的部屬架構
    * ### |-------------------- 聯盟節點 1 -------------------|
    * ### |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
    * ### |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
    * ### 聯盟節點 2 ------------------------------ 聯盟節點 N
    * ### |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
    * ### |&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
    * ### |--------------------------|--------------------------|
    * ### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|
    * ### &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<聯盟超級節點> <聯盟監控和管理>
* ### 聯盟鏈
    * ### 由一個超級節點和若干個普通節點組成。
    * ### 超級節點除具備普通節點的功能外，還具備在聯盟中實施成員管理、權限管理、數據監控等工作。
    * ### 相較於完全去中心化的公鏈，聯盟鏈為部份去中心化。
    * ### 聯盟的鏈為去中心化，但聯盟的管理是中心化的。