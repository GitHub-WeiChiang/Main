設計模式
=====
* ### 監聽模式 (Observer Pattern)
* ### 狀態模式 (State Pattern)
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
* ### 在 Python 中一切都是物件，類是元類 metaclass 的一個實例。
	* ### obj (is instance of) class (is instance of) metaclass。
* ### type 與 object 的關係
	* ### type 是一個 metaclass，而且是一個默認的 metaclass。也就是說，type 是 object 的類型，object 是 type 的一個實例。
	* ### type 是 object 的一個子類，繼承 object 的所有屬性和行為。
	* ### type 還是一個 callable，即實現了 \_\_call\_\_ 方法，可以當成一個函數來使用。
	* ### ![image](https://gitlab.com/ChiangWei/main/-/raw/master/DesignPatterns%20(Python)/type%20%E8%88%87%20object%20%E7%9A%84%E9%97%9C%E4%BF%82.jpg)
* ### 物件的創建過程
	* ### metaclass.\_\_init\_\_ 進行一些初始化的操作 (如全域變數的初始化)。
	* ### metaclass.\_\_call\_\_ 創建實例，在創建的過程中會呼叫 class 的 \_\_new\_\_ 和 \_\_init\_\_ 方法。
	* ### class.\_\_new\_\_ 進行具體的產生實體操作，並返回一個實例物件 obj。
	* ### class.\_\_init\_\_ 對返回的實例物件 obj 進行初始化，如一些狀態和屬性的設置。
	* ### 返回一個使用者真正需要使用的物件 obj。
	* ### ![image](https://gitlab.com/ChiangWei/main/-/raw/master/DesignPatterns%20(Python)/%E7%89%A9%E4%BB%B6%E7%9A%84%E5%89%B5%E5%BB%BA%E9%81%8E%E7%A8%8B.jpg)
* ### [Python UnboundLocalError](https://www.kawabangga.com/posts/2245)
<br />

Reference
=====
* ### Python 設計模式
