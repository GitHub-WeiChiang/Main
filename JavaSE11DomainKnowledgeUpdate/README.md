JavaSE11DomainKnowledgeUpdate
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
<br />

Note
=====
* ### ![image](https://gitlab.com/ChiangWei/main/-/raw/master/JavaSE11DomainKnowledgeUpdate/%E5%9F%B7%E8%A1%8C%E7%B7%92%E7%94%9F%E5%91%BD%E9%80%B1%E6%9C%9F%E6%B5%81%E7%A8%8B%E5%9C%96.jpg)
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
    * ### <T>: Type.
    * ### <E>: Element.
    * ### <K>: Key.
    * ### <V>: Value.
* ### Deque: Double Ended Queue.
* ### SE 9 導入 of() 建立 immutable 物件 (List.of(), Set.of(), Map.of())，類似 Arrays.asList("1", "2", ...)。
* ### SE 10 導入 copyOf() 建立 immutable 的副本物件 (List.copyOf(), Set.copyOf(), Map.copyOf())。
* ### Thread 為求效能，啟動時會將程序裡的 main memory 資料複製在自己的 working memory 作為 cached copies 並於工作後寫回。
* ### 可以透過 volatile 關鍵字避免快取產生，但不產生快取並不等於執行序安全。
* ### 終止執行序可以透過 interrupt() 方法。
* ### 執行緒預設為 non-daemon，non-daemon 執行緒都結束 JVM 才會結束，反之 daemon 執行緒無法影響 JVM 不結束。
* ### @Deprecated 代表這個方法要被淘汰，不要再使用勒。
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
<br />

Reference
=====
* ### OCP：Java SE 11 Developer 認證指南 (上) -- 物件導向設計篇
* ### OCP：Java SE 11 Developer 認證指南 (下) -- API 剖析運用篇
