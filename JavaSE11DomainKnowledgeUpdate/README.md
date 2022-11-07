JavaSE11DomainKnowledgeUpdate
=====
* ### Volume1
    * ### var
    * ### interface
    * ### Functional Interface
    * ### Lambda
* ### Volume2
    * ### of()
<br />

Note
=====
* ### ![image](https://gitlab.com/ChiangWei/main/-/raw/master/JavaSE11DomainKnowledgeUpdate/%E5%9F%B7%E8%A1%8C%E7%B7%92%E7%94%9F%E5%91%BD%E9%80%B1%E6%9C%9F%E6%B5%81%E7%A8%8B%E5%9C%96.jpg)
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
* ### 泛型類別註記
    * ### <T>: Type.
    * ### <E>: Element.
    * ### <K>: Key.
    * ### <V>: Value.
* ### Deque: Double Ended Queue.
* ### SE 9 導入 of() 建立 immutable 物件 (List.of(), Set.of(), Map.of())，類似 Arrays.asList("1", "2", ...)。
* ### SE 10 導入 copyOf() 建立 immutable 的副本物件 (List.copyOf(), Set.copyOf(), Map.copyOf())。
<br />

Reference
=====
### * OCP：Java SE 11 Developer 認證指南 (上) -- 物件導向設計篇
### * OCP：Java SE 11 Developer 認證指南 (下) -- API 剖析運用篇
