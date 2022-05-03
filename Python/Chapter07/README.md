Chapter07
=====
* ### 只要具有 \_\_iter\_\_() 方法的物件，曾為 iterable 物件，都可使用 for in 來迭代。
* ### 迭代器具有 \_\_next\_\_() 方法，每次迭代時就會傳回下一個物件，若沒有下一個元素，會引發 StopIteration 例外。
* ### 函式的型態提示，以 Callable[[paramType1, paramType2, ...], returnType] 方式標註。
* ### except 右方可以使用 tuple 指定多個物件，也可以有多個 except，如果沒有指定 except 後的物件型態，表示捕捉所有引發的物件。
* ### 在 Python 中，例外都是 BaseException 的子類別，當使用 except 而沒有指定例外型態時，實際上就是比對 BaseException。
* ### 可使用 raise 來引發例外。
* ### 可利用 traceback 模組 (堆疊追蹤)，得知例外發生根源及多重呼叫下例外的傳播過程。
* ### traceback.print_exc() 可以指定 file 參數。
* ### traceback.print_exc() 的 limit 參數預設為 None，不限制堆疊個數，可指定正數或負數，正數為顯示最後幾次堆疊追蹤個數，負數則相反。
* ### 只想取得堆疊追蹤的字串描述可使用 traceback.format_exc()。
* ### 警告訊息通常作為一種提示，用來告知程式有一些潛在性問題，例如使用了被棄用 (Deprecated) 的功能、以不適當的方式存取資源等。
* ### Warning 不會直接透過 raise 引發，而是透過 warnings 模組的 warn() 函式提出警告。
* ### try、except 語法可與 else、finally 搭配，try 沒發生例外才執行 else，無論 try 有無發生例外都執行 else。
* ### 若程式撰寫流程中同時有 return 與 finally，finally 區塊會先執行完才回傳 return 值。
* ### with 之後銜接的資源實例，可以透過 as 來指定給一個變數，之後就可以在區塊中進行資源的處裡，當離開 with as 區塊之後，就會自動做清除資源的動作。
* ### 支援情境管理協定的物件，必須實作 \_\_enter\_\_() 與 \_\_exit\_\_() 兩個方法，這樣的物件被稱為情境管理器 (Context Manager)。
* ### 可以使用 contextlib 模組的 @contextmanager 來實作 Context Manager，讓資源得設定與清除更為直覺。
* ### 可以透過 Context Manager 抑制一個意外 (實作範例: context_manager_demo4.py)。
* ### contextlib 有提供 suppress() 函式抑制意外。
* ### 在不實作 Context Manager 的情況下，可以透過實作 close() 方法搭配 contextlib 模組的 closing() 函式使用 with as。
