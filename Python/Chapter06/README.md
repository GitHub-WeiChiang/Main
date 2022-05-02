Chapter06
=====
* ### vars() 函數返回對象 object 的屬性和屬性值的字典對象。
* ### 若希望子類別在繼承後，一定要實作的方法，可以在父類別中指定 metaclass 為 abc 模組的 ABCMeta 類別，並在指定的方法上標註 abc 模組的 \@abstractmethod。
* ### 定義方法時使用無引數的 super() 呼叫，等同於 super(\_\_class\_\_, \<first argument\>)，\_\_class\_\_ 代表著目前所在類別，而 \<first argument\> 指目前所在方法的第一個引數，相當於 super(\_\_class\_\_, self>)。
* ### super(\_\_class\_\_, \<first argument\>) 會查找 \_\_class\_\_ 的父類別中，是否有指定的方法，若有就將 \<first argument\> 作為呼叫方法時的第一個引數。
* ### 想要使用 == 來比較物件，需定義 \_\_eq\_\_() 方法，而 \_\_ne\_\_() 預設也會呼叫 \_\_eq\_\_() 並反相其結果，因此定義 \_\_eq\_\_() 等於定義 \_\_ne\_\_()，便可使用 != 比較物件。
* ### object 定義的 \_\_eq\_\_() 方法，預設是使用 is 比較物件。
* ### hasattr(object, 'attrName') 檢查物件上是否有該屬性。
* ### 基本上無需為 \_\_eq\_\_() 加上型態提示。
* ### 實作 \_\_eq\_\_() 通常也會實作 \_\_hash\_\_()。
* ### Note that it is generally necessary to override the hashCode method whenever this method is overridden, so as to maintain the general contract for the hashCode method, which states that equal objects must have equal hash codes.
* ### 當重寫 equals 方法後有必要將 hashCode 方法也重寫，這樣做才能保證不違背 hashCode 方法中 "相同物件必須有相同哈希值" 的約定。
* ### \_\_lt\_\_() 與 \_\_gt\_\_() 互補，\_\_le\_\_() 與 \_\_ge\_\_() 互補，因此只須定義 \_\_gt\_\_() 與 \_\_ge\_\_() 即可。
* ### 使用 functools.total\_ordering，當類別被標註 @total_ordering 時，必需實作 \_\_eq\_\_() 方法以及選擇 \_\_lt\_\_()、\_\_le\_\_()、\_\_gt\_\_()、\_\_ge\_\_() 其中一個實作。
* ### enum 中名稱不可重複，但值可重複，若有上述情形，後者是前者的別名。
* ### 可加上 \@unique 確保 enum 中無重複的值。
* ### Python 支援多重繼承。
* ### 多重繼承時若方法名稱相同，搜尋順序為，該類別 -> 父類別 (左至右) -> 父父類別 (左至右)。
* ### 類別尋找指定屬性或方法時，會依據 \_\_mro\_\_ 屬性的 tuple 中元素順序尋找 (MRO 全名是 Method Resolution Order)。
* ### 可透過 \_\_bases\_\_ 得知與修改該類別繼承的對象。
* ### 判斷抽象方法是否有實作，也是依照 \_\_mro\_\_ 類別的順序。
* ### 多重繼承只建議用於繼承 ABC (Abstract Base Class, 抽象基礎類別)。
* ### 呼叫 super(type, type2) 時，會使用 type2 的 \_\_mro\_\_ 清單，從指定的 type 之下一個類別開始查找。
* ### 在函式、類別或模組定義的一開頭，使用 ''' 包起來的多行字串，會成為函式、類別或模組的 \_\_doc\_\_ 屬性值，也就是 help() 的輸出內容之一。
* ### 套件的 DocStrings，可以在對應資料夾中 \_\_init\_\_.py 撰寫。
