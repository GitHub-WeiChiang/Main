設計模式
=====
* ### test
<br />

補充
=====
* ### 關聯 (Association): ClassA 中並沒有資料型態為 ClassB 的屬性，但有使用到 ClassB 的屬性或方法。
* ### 聚合 (Aggregation): ClassA 中有資料型態為 ClassB 的屬性，但其 ClassB 的實例是從外部取得，非內部生成。
* ### 組合 (Composition): ClassA 中有資料型態為 ClassB 的屬性，且為 ClassA 自己內部生成。
* ### Python3 中所有類別都繼承 object 類別。
* ### 存取權限
	* ### \_\_foo\_\_: 定義的是特殊方法，一般是系統定義名字，類似 \_\_init\_\_()。
	* ### \_foo: 以單底線開頭時表示的是 protected 類型的變數，即保護類型只允許其本身與子類別進行存取，不能用於 from module import *。
	* ### \_\_foo: 以雙底線開頭時，表示的是私有類型 (private) 的變數，即只允許這個類別本身進行存取。
* ### \_\_new\_\_: 負責物件的創建，是一個類別方法。
* ### \_\_init\_\_: 負責物件初始化，是一個物件方法。
* ### \_\_call\_\_: 聲明這個類別的物件是可呼叫的 (callable)，是一個物件方法。
* ### 創建物件時，先呼叫 \_\_new\_\_ 方法，才呼叫 \_\_init\_\_ 方法。
* ### \_\_new\_\_ 是構造函數，需要返回一個實例。
* ### \_\_init\_\_ 不允許有返回值。
* ### \_\_init\_\_ 的參數除 self 外需與 \_\_new\_\_ 除 cls 外其餘參數一致或等效。
* ### type()
	* ### 查看變數或物件的類型。
	* ### 創建一個 (class)。
```
ClassVaribale = type('ClassA', (object, ), dict(name = "type test"))
a = ClassVaribale()
print(type(a))
print(a.name)
```
<br />

Reference
=====
* ### Python 設計模式
