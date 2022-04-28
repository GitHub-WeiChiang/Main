Chapter06
=====
* ### vars() 函數返回對象 object 的屬性和屬性值的字典對象。
* ### 若希望子類別在繼承後，一定要實作的方法，可以在父類別中指定 metaclass 為 abc 模組的 ABCMeta 類別，並在指定的方法上標註 abc 模組的 @abstractmethod。
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
