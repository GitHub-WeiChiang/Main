Chapter12
=====
* ### Step Over: 執行下一步。
* ### Step Into: 進入函式。
* ### Step Out: 執行完當前函式後返回上一層。
* ### 無開發環境可使用 pdb 模組除錯。
* ### 使用 assert 安插斷言。
* ### doctest 模組可用於測試程式碼。
* ### unittest 模組有時亦稱為 "PyUnit"，是 JUnit 的 Python 語言實現，JUnit 是個 Java 實現的單元測試 (Unit test) 框架，單元測試指的是測試一個工作單元 (a unit of work) 的行為。
* ### 測試一個單元，基本上要與其它的單元獨立，否則會是在同時測試兩個單元的正確性，或是兩個單元之間的行為。
* ### 單元測試通常指的是測試某個函式 (方法)。
* ### unitest 模組
    * ### 測試案例 (Test case): 測試的最小單元。
    * ### 測試設備 (Test fixture): 執行一個或多個測試前必要的預備資源，以及相關的清除資源動作。
    * ### 測試套件 (Test suite): 一個測試案例、測試套件或者是兩者的組合。
    * ### 測試執行器 (Test runner): 負責執行測試並提供測試結果的原件。
* ### timeit 可用於量測一個小程式片段的執行時間。
* ### cProfile (profile) 用來蒐集程式執行時的一些時間數據，提供各種統計數據，對大多數的使用者來說是不錯的工具，這是用 C 撰寫的擴充模組，在評測時有較低的額外成本，但並非所有系統都提供，profile 介面上仿造了 cProfile，是用純 Python 實現的模組，有較高的互通性。
    * ### ncalls (number of calls): 針對特定函式的呼叫次數。
    * ### tottime (total time): 花費在函式上的執行時間 (不包括子函數呼叫的時間)。
    * ### percall: tottime / ncalls。
    * ### cumtime (cumulative time): 花費在函式與所有子函式的時間 (從呼叫至離開)。
    * ### percall: cumtime / ncalls。
    * ### filename:lineno(function): 提供程式碼執行時的位置資訊。
