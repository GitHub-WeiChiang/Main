Question031 - Python 中 import 與 from import 的差異為何 ?
=====
* ### import module_name
    * ### 將模塊的全部內容進行導入，包括類別、函數與屬性，使用的是相對路徑。
    * ### 將模塊中的內容直接加載到內存中，多個程序透過該方式使用同一個模塊時 "會" 相互影響。
    * ### 透過 ```module_name.funcname()``` 方式調用。
* ### from module_name import * | class_name | func_name
    * ### 將模塊的部分內容進行導入，例如某個類別、函數與屬性，使用的是絕對路徑。
    * ### 將模塊中內容的副本加載到內存中，多個程序透過該方式使用同一個模塊時 "不會" 相互影響。
    * ### 透過 ```funcname()``` 方式調用。
<br />
