七大編程原則
=====
* ### SingleResponsibility: 一個類別應該只專注於一項事物。
* ### OpenClose: 類別架構應該對架構應該對擴展開放而對修改封閉。
* ### LawOfDemeter: 類別應只和自己關係密切的類別溝通。
* ### DependencyInversion: 高階類別與低階類別間應該要有一個抽象的中介接口。
* ### CompositeReuse: 應該多使用關聯、聚合與組合，少使用繼承。
* ### InterfaceSegregation: 客戶 (類別) 不應該依賴 (實作) 它不需要的接口，且接口的設計應要符合單一職責原則。
* ### LiskovSubstitutionPrinciple: 任何父類別可以出現的地方，其子類別一定也可以出現。
<br />

編成原則整理
=====
* ### 面對對象設計 (高層設計)
    * ### 開閉 (目標): 對擴展開放，對修改關閉。
    * ### 依賴倒置 (手段): 依賴於抽象而非具體。
* ### 拆分解構
    * ### 單一職責 (業務上): 類的職責要明確且功能要單一。
    * ### 接口隔離 (架構上): 類應該只依賴真正有關聯的接口。
* ### 類之間的通信
    * ### 合成復用: 關聯、聚合與組合都優於繼承。
    * ### 里氏替換: 子類別應該可以取代服類別，反之則否。
    * ### 迪米特法則: 類應該只和真正有關聯的類溝通。
<br />

設計模式分類
=====
| 行為型 | 結構性 | 創建型 |
| --- | --- | --- |
| Chain of Responsibility | Adapter | Abstract Factory |
| Command | Bridge | Builder |
| Interpreter | Composite | Factory Method |
| Iterator | Decorator | Prototype |
| Mediator | Facade | Singleton |
| Memento | Flyweight |  |
| Observer | Proxy |  |
| State |  |  |
| Strategy |  |  |
| Template Method |  |  |
| Visitor |  |  |
<br />

創建型模式
=====
* ### 幫助創建類或是對象。
* ### 將創建與使用分離，使兩者相互獨立。
<br />

結構性模式
=====
* ### 涉及對象的組合，獲得更好與靈活的結構。
* ### 更多的透過組合與運行期的動態結合實現。
<br />

行為型模式
=====
* ### 描述類或是對象如何交互分配職責。
* ### 涉及算法與對象間職責分配，描述一組對象應如何協作完成一個整體功能。
<br />

設計模式
=====
* ### 抽象工廠 Abstract Factory: 創建一系列相互依賴的類。
* ### 生成器 Builder: 創建各實例生成所需不同的類。
* ### 工廠方法 Factory Method: 創建需要使用大量重複代碼對象。
* ### 原型 Prototype: 支持相同物件的大量複製。
* ### 單例 Singleton: 保證一個類只有一個實例。
* ### 適配器 Adapter: 讓接口不兼容的對象能夠相互合作。
* ### 橋接 Bridge: 將抽象與實現分離，在抽象和現實間搭建橋樑。
* ### 組合 Composite: 實現遞歸樹狀結構。
* ### 裝飾器 Decorator: 在運行時動態添加新功能。
* ### 外觀 Facade: 為複雜系統提供簡單接口。
* ### 享元 Flyweight: 節省內存使用。
* ### 代理 Proxy: 讓一個類代表另一個類。
<br />

Reference
=====
* ### 图灵星球 Turing Planet: 设计模式快速入门
<br />
