JavaSEDomainKnowledgeUpdate
=====
* ### Volume1
    * ### var
    * ### interface
    * ### Functional Interface
    * ### Lambda
* ### Volume2
    * ### of()
    * ### copyOf()
    * ### Arrays.asList()
    * ### JDBC
    * ### Lambda
    * ### Optional&lt;T&gt;
    * ### StreamAPI - 基礎
    * ### StreamAPI2 - 中間作業
    * ### StreamAPI3 - 終端作業
    * ### StreamAPI4 - 短路型終端作業
    * ### StreamAPI5 - 操作平行化
<br />

Note
=====
* ### ![image](https://gitlab.com/ChiangWei/main/-/raw/master/JavaSEDomainKnowledgeUpdate/%E5%9F%B7%E8%A1%8C%E7%B7%92%E7%94%9F%E5%91%BD%E9%80%B1%E6%9C%9F%E6%B5%81%E7%A8%8B%E5%9C%96.jpg)
* ### install
    * ### sudo ln -sfn /opt/homebrew/opt/openjdk@11/libexec/openjdk.jdk /Library/Java/JavaVirtualMachines/openjdk-11.jdk
* ### Java SE 11 已將 JRE 併入 JDK。
* ### UMLet: UML Tool for Fast UML Diagrams.
* ### Integer.valueOf() vs Integer.parseInt(): valueOf() returns an Integer object while Integer, parseInt() returns a primitive int. Both String and integer can be passed a parameter to Integer, valueOf() whereas only a String can be passed as parameter to Integer.
* ### var: SE 10 加入，正式名稱為區域型別推斷 (local variable type inference)，只能套用在區域變數，由右側變數值推斷型別，可用於 lambda、迴圈和 try-with-resources 等區塊。
    * ### var 只可用於區域變數宣告。
    * ### var 可用於簡化程式碼。
* ### interface
    * ### SE 7: 只有 public abstract method (無方法內容)。
    * ### SE 8: 新增 public default, public static (要實作方法內容)。
    * ### SE 9: 新增 private, private static (要實作方法內容)。
    * ### 方法宣告可以是 abstract or default。
    * ### 存取修飾可以是 public or private。
    * ### 若某類別所繼承父類別與實作之介面有相同方法，父類別優先權較高 (該方法在父類別中存取修飾字需為 public)。
    * ### 若某類別實作多個介面中有相同之方法則會導致編譯失敗 (可以透過實作該方法解決編譯失敗問題)。
* ### SE 8 推出 Functional Interface，該介面只可有一個抽象方法，透過 @FunctionalInterface 標記。
* ### Lambda (Lambda expressions are a new and important feature included in Java SE 8)
    * ### 目的為使用匿名方法。
    * ### 無需述明方法名稱、參數與回傳型別。
    * ### 簡化 Functional Interface 的實作內容。
    * ### Lambda 可以快速的建立並回傳一個實作功能性介面 (Functional Interface) 的類別物件實例。
* ### 泛型類別註記
    * ### &lt;T&gt;: Type.
    * ### &lt;E&gt;: Element.
    * ### &lt;K&gt;: Key.
    * ### &lt;V&gt;: Value.
* ### Deque: Double Ended Queue.
* ### SE 9 導入 of() 建立 immutable 物件 (List.of(), Set.of(), Map.of())，類似 Arrays.asList("1", "2", ...)。
* ### SE 10 導入 copyOf() 建立 immutable 的副本物件 (List.copyOf(), Set.copyOf(), Map.copyOf())。
* ### Thread 為求效能，啟動時會將程序裡的 main memory 資料複製在自己的 working memory 作為 cached copies 並於工作後寫回。
* ### 可以透過 volatile 關鍵字避免快取產生，但不產生快取並不等於執行序安全。
* ### 終止執行序可以透過 interrupt() 方法。
* ### 執行緒預設為 non-daemon，non-daemon 執行緒都結束 JVM 才會結束，反之 daemon 執行緒無法影響 JVM 不結束。
* ### \@Deprecated 代表這個方法要被淘汰，不要再使用勒。
* ### 被 read lock 的方法其它執行緒不能 write lock 但可以一直 read lock，被 write lock 的方法其它執行緒請走開。
* ### Java will utilize the underlying OS threads to do the actual job of executing the code on different CPUs, if running on a multi-CPU machine.
* ### Apache Derby
    * ### Java 開發。
    * ### 輕量級。
    * ### 支持 JDBC 和 ANSI SQL。
    * ### 有 Table 與 View。
    * ### 支援 BLOB 和 CLOB 資料類型。
    * ### 支援預存程序。
* ### MySQL 安裝與執行
    * ### brew install mysql
    * ### brew install --cask mysqlworkbench
    * ### brew services start mysql
    * ### brew services stop mysql
    * ### mysqladmin -u root -p --ssl-mode=required password
    * ### 下載並匯入 IDEA: JDBC Driver for MySQL (Connector/J)
* ### JDBC fetch number 優化 - fetch size
    * ### JDBC 默認每執行一次檢索，會從游標中提取 10 行記錄。
    * ### 通過設置 fetch size 可以改變每次和數據庫交互所提取出來的記錄行總數。
    * ### Fetch 相當於讀緩存，默認 Fetch Size 值是 10。
    * ### 緩存因不會有網路消耗，效率相對較高，但需要注意 Fetch Size 值越高則佔用內存越高，要避免出現 OOM (Out of Memory) 錯誤。
    * ### fetch size 需要在獲得檢索結果集之前設置。
    ```
    Connection con = DriverManager.getConnection(url, name, password);
    Statement stmt = con.createStatement();

    stmt.setFetchSize(1000);

    ResultSet rs = stmt.executeQuery(query);
    ```
* ### 資料庫會針對收到的 SQL 語句編譯，產生執行計畫 (execution plan)，若想讓執行計畫重複使用可以透過繫結變數 (bind variables) 方式執行，且可同時避免 SQL injection。
* ### JDBC 的交易
    * ### 預設為 auto commit。
    ```
    con.setAutoCommit(false);
    con.commit();
    con.rollback();
    ```
* ### SE 7 導入新版 RowSetProvider 和 RowSetFactory。
```
RowSetFactory rsf = RowSetProvider.newFactory();
JdbcRowSet jrs = rsf.createJdbcRowSet();

jrs.setUrl(url);
jrs.setUsername(username);
jrs.setPassword(password);
jrs.setCommand(sql);

jrs.execute();

while (jrs.next()) {
    ...
}
```
* ### SE 8 在套件 java.util.function 下內建多種功能性介面，其中包含以下四種基礎型供使用。
    * ### 判斷型 (predicate): 回傳 boolean。
    * ### 消費型 (consumer): 回傳 void。
    * ### 功能型 (function): 型別轉換。
    * ### 供應型 (supplier): 提供物件。
* ### 若 Lambda 內容只是呼叫另一個方法，如同委派 (delegation)，可將其表示簡化為方法參照 (method reference)。
* ### SE 8 支援泛型的 Optional&lt;T&gt;。
* ### SE 8 在介面 Collection 中新增宣告為 default 的 stream() 方法，具備許多可以使用方法鏈結 (method chaining) 的方法，使語法流暢 (fluent) 化。
    * ### filter(): 對集合物件成員使用 Predicate 介面的 test() 方法進行篩選，符合的才可以往下流。
    * ### forEach(): 使流入的集合物件逐一操作 Consumer 介面的 accept() 方法。
* ### 管線操作 (pipeline operations) 的分段
    * ### 來源 (Source): Collection Object, File, Stream Object.
    * ### 中間作業 (Intermediate Operation): 零個以上。
    * ### 終端作業 (Terminal Operation): Only one.
    * ### 短路型終端作業 (Short-Circuit Terminal Operation): Only one.
* ### HashMap 四大重點: 哈希函数、哈希衝突、擴容方案、線程安全。
* ### 哈希函数
    * ### 通過高 16 位與低 16 位進行異或運算來讓高位參與散列，提高散列效果。
    * ### 控制數組的長度為 2 的整數次冪來簡化取模運算，提高性能。
    * ### 通過控制初始化的數組長度為 2 的整數次冪、擴容為原來的 2 倍來控制數組長度一定為 2 的整數次冪。
* ### 哈希衝突
    * ### 採用鏈地址法，當發生衝突時會轉化為鏈表，當鏈表過長會轉化為紅黑樹提高效率。
    * ### 對紅黑樹進行了限制，讓紅黑樹只有在極少數極端情況下進行抗壓。
* ### 擴容方案
    * ### 裝載因子決定了擴容的閾值，需要權衡時間與空間，一般情況下保持 0.75 不作改動。
    * ### 擴容機制結合了數組長度為 2 的整數次冪的特點，以一種更高的效率完成數據遷移，同時避免頭插法造成鍊錶環。
* ### 線程安全
    * ### HashMap 並不能保證線程安全，在多線程並發訪問下會出現意想不到的問題，如數據丟失等。
    * ### HashMap 1.8 採用尾插法進行擴容，防止出現鍊錶環導致的死循環問題。
    * ### 解決並發問題的的方案有 Hashtable、Collections.synchronizeMap()、ConcurrentHashMap，其中最佳解決方案是 ConcurrentHashMap。
    * ### 上述解決方案並不能完全保證線程安全。
    * ### 快速失敗是 HashMap 迭代機制中的一種並發安全保證。
    * ### Note: ConcurrentHashMap 通過降低鎖粒度 + CAS 的方式來提高效率。簡單來說，ConcurrentHashMap 鎖的並不是整個對象，而是一個數組的一個節點。
* ### ConcurrentHashMap
    * ### CAS (compare and swap) 和自旋鎖在 ConcurrentHashMap 應用地非常廣泛，在原始碼中我們會經常看到他們的身影，同時這也是 ConcurrentHashMap 的設計核心所在 (自旋鎖是利用 CAS 而設計的一種應用層面的鎖)。
    * ### CAS 的思路並不複雜，當需要對變數進行自增時，先儲存一個變數副本，再對變數進行自增，然後把變數副本和變數本身進行比較，如果兩者相同，證明沒有發生併發衝突，修改變數的值；如果不同，說明變數在自增的過程中被修改了，把上述整個過程重新來一遍，直到修改成功為止 (比較賦值的操作作業系統會保證的原子性)。
    ```
    // 常見的 CAS 方法
    .compareAndSwapInt();
    .compareAndSwapLong();
    .compareAndSwapObject();
    ```
    * ### CAS 在併發度過高的場景，若處理時間過長，會導致某些執行緒一直在迴圈自旋，浪費 cpu 資源。
    * ### Hashtable 與 SynchronizeMap 採取的併發策略是對整個陣列物件加鎖，導致效能及其低下。
    * ### JDK 1.7 前 ConcurrentHashMap 採用的是鎖分段策略來優化效能。
    * ### JDK 1.8 後 ConcurrentHashMap 鎖的不是 segment，而是節點。
* ### 管線作業若沒有定義終端作業，peek() 將不會被啟動。
* ### 指令式編程 (Imperative Programming)。
* ### 流暢式編程 (Streaming Programming)。
* ### 管線操作變數必須是沒有狀態 (stateless)。
* ### 對 Stream 發動平行處理可能讓結果不同。
* ### 管線平行化處理，底層是使用 Fork / Join 框架。
* ### 平行化處理注意事項
    * ### 不一定比較快。
    * ### 拆解和合併是否適用該場景。
    * ### boxing / unboxing 會降低執行效率。
* ### 標註型別 (Annotation) 功能
    * ### 再不改變繼承結構下分類類別。
    * ### 讓 metadata 維護工作變得容易。
    * ### 將 metadata 標註在完全不同目標，即便是不相關的類別、實例變數或方法。
    * ### 單純作為 marker。 
* ### 常用內建標註型別
    * ### \@Override: 標註覆寫的方法。
    * ### \@FunctionalInterface: 宣告 Functional Interface。
    * ### \@Deprecated: 停用程式碼。
    * ### \@SuppressWarnings: 忽略警告。
    * ### \@SafeVarargs: 程序員認定帶有註釋的主體或者構造函數不會對其執行潛在的不安全操作。
<br />

Reference
=====
* ### OCP：Java SE 11 Developer 認證指南 (上) -- 物件導向設計篇
* ### OCP：Java SE 11 Developer 認證指南 (下) -- API 剖析運用篇
