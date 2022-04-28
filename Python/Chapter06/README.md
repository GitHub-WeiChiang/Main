Chapter06
=====
* ### vars() 函數返回對象 object 的屬性和屬性值的字典對象。
* ### 若希望子類別在繼承後，一定要實作的方法，可以在父類別中指定 metaclass 為 abc 模組的 ABCMeta 類別，並在指定的方法上標註 abc 模組的 @abstractmethod。
* ### 定義方法時使用無引數的 super() 呼叫，等同於 super(\_\_class\_\_, \<first argument\>)，\_\_class\_\_ 代表著目前所在類別，而 \<first argument\> 指目前所在方法的第一個引數，相當於 super(\_\_class\_\_, self>)。
* ### super(\_\_class\_\_, \<first argument\>) 會查找 \_\_class\_\_ 的父類別中，是否有指定的方法，若有就將 \<first argument\> 作為呼叫方法時的第一個引數。
