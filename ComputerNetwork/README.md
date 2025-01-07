ComputerNetwork
=====
協定
---
| 縮寫 | 英文 | 中文 | 層級 |
| --- | --- | --- | --- |
| DNS | Domain Name System | 網域名稱服務協定 | L5 |
| DHCP | Dynamic Host Configuration Protocol | 動態主機 IP 配置協定 | L5 |
| HTTP | HyperText Transfer Protocol | 超文字傳輸協定 | L5 |
| SMTP | Simple Mail Transfer Protocol | 簡易郵件傳輸協定 | L5 |
| POP | Post Office Protocol | 郵件接收協定 | L5 |
| Telnet | Telnet | 遠端登入協定 | L5 |
| SSH | Secure Shell | 遠端登入協定 | L5 |
| FTP | File Transfer Protocol | 檔案傳輸協定 | L5 |
| TFTP | Trivial File Transfer Protocol | 簡單檔案傳輸協定 | L5 |
| TCP | Transmission Control Protocol | 傳輸控制協定 | L4 |
| UDP | User Datagram Protocol | 使用者資料報協定 | L4 |
| IPv4 | Internet Protocol version 4 | 網際網路通訊協定第四版 | L3 |
| IPv6 | Internet Protocol version 6 | 網際網路通訊協定第六版 | L3 |
| IPX | Internetwork Packet Exchange | 網際網路封包交換協定 | L3 |
| CLNP | Connectionless Network Protocol | 無連接網路協定 | L3 |
| Ethernet Protocol | Ethernet Protocol | 乙太網路協定 | L2 |
| ICMP | Internet Control Message Protocol | 網際網路控制訊息協定 | L3 |
| ARP | Address Resolution Protocol | 位址解析協定 | L3 |
| GARP | Gratuitous Address Resolution Protocol | 無回報位址解析協定 | L3 |
| RARP | Reverse Address Resolution Protocol | 逆位址解析協定 | L3 |
| CDP | Cisco Discovery Protocol | 思科發現協定 | L2 |
| LLDP | Link Layer Discovery Protocol | 鏈路層發現協定 | L2 |
| Routing Protocol | Routing Protocol | 路由協定 | L3 |
| IGP | Interior Gateway Protocol | 內部閘道協定 | L3 |
| EGP | Exterior Gateway Protocol | 外部閘道協定 | L3 |
| RIP | Routing Information Protocol | 路由資訊協定 | L3 |
| EIGRP | Enhanced Interior Gateway Routing Protocol | 增強型內部閘道路由協定 | L3 |
| OSPF | Open Shortest Path First | 開放式最短路徑優先 | L3 |
| IS - IS | Intermediate System To Intermediate System | 中間系統到中間系統 | L2 |
| BGP | Border Gateway Protocol | 邊界閘道協定 | L5 |
| IGMP | Internet Group Management Protocol | 網際網路組管理協定 | L3 |
| NDP | Neighbor Discovery Protocol | 鄰居發現協議 | L3 |
| DTP | Dynamic Trunk Protocol | 動態中繼協定 | L2 |
| VTP | VLAN Trunking Protocol | 虛擬區域網絡中繼協定 | L2 |
| STP | Spanning Tree Protocol | 生成樹協定 | L2 |
| PAgP | Port Aggregation Protocol | 連線埠聚集協定 | L2 |
| LACP | Link Aggregation Control Protocol | 鏈路聚合控制協議 | L2 |
| FHRP | First Hop Redundancy Protocol | 第一跳冗餘協定 | L3 |
| HSRP | Hot Standby Router Protocol | 熱備份路由器協定 | L3 |
| VRRP | Virtual Router Redundancy Protocol | 虛擬路由器冗餘協定 | L3 |
| GLBP | Gateway Load Balancing Protocol | 閘道負載平衡協定 | L3 |
| ATM | Asynchronous Transfer Mode | 非同步傳輸模式 | L2 |
| Frame Relay | Frame Relay | 訊框中繼 | L2 |
| HDLC | High Level Data Link Control | 高級數據鏈路控制 | L2 |
| PPP | Point To Point Protocol | 對等協定 | L2 |
| PAP | Password Authentication Protocol | 通行碼鑑別協定 | L2 |
| CHAP | Challenge Handshake Authentication Protocol | 詢問握手認證協議 | L2 |
| MLPPP | Multilink PPP | 多鏈路對等協定 | L3 |
| PPPoE | Point-to-Point Protocol over Ethernet | 乙太網路對等協定 | L2 |
| ISAKMP | Internet Security Association And Key Management Protocol | 網際網路安全關聯鑰匙管理協定 | L4 |
| NHRP | Next Hop Resolution Protocol | 下一跳解析協定 | L2 |
| NTP | Network Time Protocol | 網路時間協定 | L5 |
| SNMP | Simple Network Management Protocol | 簡單網路管理協定 | L5 |
| RSVP | Resource Reservation Protocol | 資源預留協定 | L4 |
| CAPWAP | Control And Provisioning Of Wireless Access Points | 無線接入點的控制和配置協議 | L3 |
| CHARGEN | Character Generator Protocol | 字元產生器協定 | L4 |
| EAP | Extensible Authentication Protocol | 可擴展身份驗證協議 | L4 |
<br />

![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/ComputerNetwork/InternetProtocol.png)
<br />

* ### EMS (Element Management System，網元管理系統)，是管理特定類型的一個或多個電信 NE (Network Element，網路單元) 的系統。
* ### NMS (Network Management System，網路管理系統)，也稱為綜合網管系統，可以同時對多種專業網進行管理，也可以同時管理由多個廠家設備構成的電信網路。
* ### API vs. SNMP vs. CLI
    * ### There are a variety of ways to communicate, configure, and manage network devices. The first way of managing network equipment is through the console. The console is a command-line environment that network admins connect to through a remote connection. Though SSH is commonly used today, that remote connection can be made through the Telnet or SSH protocols.
    * ### SNMP is another way to communicate with network devices. SNMP is more universal than console commands. SNMP has a limited ability to perform configurations, though, and is commonly used to collect metrics for networks instead. These metrics are collected and displayed by management information bases.
    * ### Finally, network engineers can also use APIs. Again, APIs are specific to each vendor, though common languages like OpenConfig attempt to make those APIs more universal. Network admins can create a much more automated, scalable, and robust network by using vendor APIs.
* ### Whats The Difference Between A Port And An Interface ?
    * ### The port is where you plug in the physical cable connector. The interface is what you configure in the Cisco IOS, therefore is the software representation of the physical port.
* ### "ip default-gateway" vs. "ip default-network"
    * ### "ip default-gateway" is to be used in L2 devices.
    * ### "ip default-network" would be used in L3 devices, but works slightly different from the usual static default route configured with "ip route 0.0.0.0 0.0.0.0 <next_hop>". Let's say you configure "ip default-network 172.31.0.0". Then, if the device already knows a route for 172.31.0.0, this route will be flagged as a default route candidate. "ip default-network" command is classful.
* ### The difference between VLANs and VLAN interfaces.
    * ### A VLAN itself is not an interface. It is a division of the broadcast domain within an Ethernet segment.
    * ### To initiate a VLAN in a network switch, this command can be used: "(config)#vlan 10".
    * ### A VLAN interface is a logical interface that represents a VLAN in all Layer 3 activities the unit may participate in.
    * ### A VLAN interface has an IP address that is used for any management operations, or as an IP next-hop for routes.
    ```
    (config)#Interface vlan 10
    (config-vlan-10)#ip address 10.10.10.1 255.255.255.0
    (config-vlan-10)#no shutdown
    ```
<br />

QoS 流量策略 Policing 詳解
---
* ### CIR = Bc / Tc
* ### 承诺信息速率 (CIR, Committed Information Rate)，單位為 Bits Per Second。
* ### 承诺突发速率 (Bc, Committed Burst)，單位為 Bytes。
* ### 单位时间间隔 (Tc, Committed Time Interval)，單位為 Seconds。
* ### 举例
    * ### 假设想算出驾车时的平均速度 (V)，有个很简单的公式: V = S / T (S = 行驶距离，T = 行驶时间)，
    * ### 驾车 1 个小时行驶了 100 公里，平均速度是 100 公里/小时，
    * ### 如果半个小时行驶了 50 公里，平均速度也是 100 公里/小时，
    * ### 两种算法得到的结果相同，都是 100 公里/小时这个平均速度，
    * ### 唯一不同的地方是 "单位时间间隔 (Tc)"。
* ### 在现实生活中，不可能一直保持 100 公里/小时的速度来行驶一个小时。
* ### 举例
    * ### 假设前 15 分钟行驶了 50 公里，
    * ### 后 45 分钟也行驶了 50 公里，
    * ### 这时平均速度依然是 100 公里/小时，
    * ### 但是前 15 分钟的平均速度达到了 200 公里/小时，
    * ### 之所以出现这种情况，完全是因为计算平均速度时所使用的 "单位时间间隔 (Tc)" 不同，
    * ### 造成前 15 分钟计算出来的平均速度更像是达到峰值的 "瞬时速度 (instant speed)"，
    * ### 而非真正的平均速度。
* ### 结论: Tc 越短，计算出来的平均速度越接近 "瞬时速度"，Tc 越长，计算出来的平均速度越接近真实的 "平均速度"。
* ### 这个道理也同样运用在流量策略中，
* ### 流量策略只有一个目的，那就是将 Tc 内测得的平均速度和 CIR 做比较，
* ### 超出 CIR 的部分被丢弃或者标记（marking)，
* ### 因为 Tc = Bc / CIR，如果 Bc 越大，Tc 也就越大，
* ### 那么最终靠该 Tc 计算出来的平均速度就越接近 "真实平均速度"，
* ### 反之则越接近 "瞬时速度"。
* ### 举例
    * ### 假设 CIR 是 100Mbps，
    * ### 将 Bc 设为 12.5MB，那么 Tc = (12.5MB x 8) / 100Mbps = 1s，
    * ### 如果在 Tc (1s) 內下载了 13MB 的文件，
    * ### 这时测得的平均速度為 (13MB x 8) / 1s = 104Mbps，
    * ### 大於 CIR 的 100Mbps，超出的包就会被丢弃或者被重新标记，
    * ### 也就是說在這樣的設定下，CIR 設為 100Mbps，Bc 设为 12.5MB，
    * ### 所達到的效果就是每 Tc (1s) 內最高接受 12.5MB 的平均傳輸量。
    * ### 假设 CIR 還是 100Mbps，但將 Bc 设置为 25MB，
    * ### 那么 Tc = (25MB x 8) / 100Mbps = 2s，
    * ### 这时如果在 Tc (2s) 的第一秒下载了 13MB 的文件，
    * ### 这一秒的瞬时速度和刚才一样达到了 104Mbps，
    * ### 但若后一秒没有下载任何东西，
    * ### 那么 (13MB x 8) / 2s = 52Mbps，
    * ### 因小於所設定之 CIR，所以流量會順利通過，
    * ### 也就是說在這樣的設定下，CIR 設為 100Mbps，Bc 设为 25MB，
    * ### 所達到的效果就是每 Tc (2s) 內最高接受 25MB 的平均傳輸量。
    * ### 由此可见，Bc 设置的越大，那么 Tc 相對越大，
    * ### 测得的平均速度越接近真实的平均速度。
    * ### 不过至于 Bc 是越大越好，还是越小越好，这没有定论，要根据实际的需求来制定。
* ### Cisco 設備只能夠設定 CIR 與 Bc，無法設定 Tc。
* ### 實作示例: Cisco Switch 端口限速 (QoS)
    ```
    # 透過命名方式設定 ACL
    conf t
    ip access-list extended ACL_NAME
    permit ip any any
    exit

    # 指定 CLASS 套用 ACL: CLASS 透過 class-map 定義一個類與 ACL 綁定
    class-map match-all CLASS_NAME
    match access-group name ACL_NAME
    exit

    # 指定 POLICY 套用 CLASS 並設定 CIR 和 Bc，
    # POLICY 為策略，透過 policy-map 建立策略文件與 CLASS 綁定並對應至介面，
    # 上述 CIR 為承諾信息速率 (Bits Per Second)，
    # Bc 為承諾突發速率 (Bytes)，
    # 最後設定當流量超过了配置的限速值，超出部分的数据包将被丢弃，
    # 在默认情况下，流量超出限速时会被标记为 "exceed"，
    # 並預設實施 exceed-action drop 行為 (故下方此行指令可不輸入)，
    # 这意味着當流量超出了限速配置，系统会將其直接的丢弃。
    policy-map POLICY_NAME
    class CLASS_NAME
    police CIR Bc
    exceed-action drop
    exit
    exit
    exit

    # 當然，設備本身並不笨，也可以只設定 CIR，
    # 而 Bc 則讓設備自動推算，示例如下:
    # 1. 當 CIR 為 16000000 時，設備會將 Bc 會自動設定為 500000。
    # 2. 當 CIR 為 32000000 時，設備會將 Bc 會自動設定為 1000000。
    # 由前述計算公式可知，在沒有指定 Bc 的場景下，
    # 設備將以 0.25 秒作為一個流量限制的单位时间间隔 (Tc)。

    # 對端口進行限速套用: 以流出為例
    int INTERFACE_NAME
    service-policy output POLICY_NAME
    exit

    # 查詢端口套用
    sh policy-map
    sh policy-map int
    sh policy-map INTERFACE_NAME

    # 徹底刪除 QoS
    no service-policy
    no policy-map
    no class-map
    no ip access-list extended
    ```
    * ### 使用 CIR 和 Bc 进行配置可以更精确地控制流量限速，确保设备的平稳运行和容忍短期突发。
<br />

三層網路架構
---
* ### 三層網路架構是現代網路構成的一種分層結構，將複雜的網路設計劃分為三個層次——接入層、匯聚層與核心層。核心層主要負責實現網路的高速交換骨幹；匯聚層則側重於提供基於策略的連接，位於接入層與核心層之間；而接入層的功能則是將工作站（如電腦、AP等設備）接入網路。這種設計可以將龐大且複雜的網路劃分為三個層次，從而實現有序的管理。
* ### 核心層：核心層的主要功能是實現骨幹網路之間的高效傳輸。其設計任務的重點通常集中在冗餘能力、可靠性和高速傳輸方面。核心層被視為所有流量的最終承載者與匯聚點。
* ### 匯聚層：匯聚層作為網路接入層與核心層之間的“中介”，在工作站接入核心層之前進行匯聚，以減輕核心層設備的負擔。匯聚層具備多項功能，包括實施策略管理、安全控制、工作群組接入、虛擬區域網（VLAN）之間的路由、以及源地址或目的地址之間的過濾等。
* ### 接入層：接入層通常是網路中直接面向使用者連接或訪問的部分。它通過光纖、雙絞線、同軸電纜及無線接入技術等傳輸媒介，實現與使用者的連接，並負責業務和頻寬的分配。接入層交換機具有低成本和高端口密度的特性。
<br />

Reference
=====
* ### 網路規劃與管理實務 - 協助考取國際網管證照, 3e
