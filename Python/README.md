Python
=====
* ### Chapter01 Python 起步走
* ### Chapter02 從 REPL 到 IDE
* ### Chapter03 型態與運算子
* ### Chapter04 流程語法與函式
* ### Chapter05 從模組到類別
* ### Chapter06 類別的繼承
* ### Chapter07 例外處理
* ### Chapter08 open() 與 io 模組
* ### Chapter09 資料結構
* ### Chapter10 資料永續與交換
* ### Chapter11 常用內建模組
* ### Chapter12 除錯、測試與效能
* ### Chapter13 並行、平行與非同步
* ### Chapter14 進階主題
<br />

Note
=====
* ### "CPU 密集型" 與 "IO 密集型" 及其應用
	* ### CPU 密集型 (CPU - bound)
		* ### 也叫計算密集型，指的是系統的硬盤、內存性能相對 CPU 要好很多，此時，系統運作 CPU 讀寫 IO (硬盤 / 內存) 時，IO 可以在很短的時間內完成，而 CPU 還有許多運算要處理，因此，CPU 負載很高。
		* ### CPU 密集表示該任務需要大量的運算，而沒有阻塞，CPU 一直全速運行。CPU 密集任務只有在真正的多核 CPU 上才可能得到加速 (通過多線程)，而在單核 CPU 上，無論你開幾個模擬的多線程該任務都不可能得到加速，因為 CPU 總的運算能力就只有這麼多。
		* ### CPU 使用率較高 (例如: 計算圓周率、對視頻進行高清解碼、矩陣運算等情況) 的情況下，通常，線程數只需要設置為 CPU 核心數的線程個數就可以了。這一情況多出現在一些業務複雜的計算和邏輯處理過程中。比如說，現在的一些機器學習和深度學習的模型訓練和推理任務，包含了大量的矩陣運算。
	* ### IO 密集型 (I/O - bound)
		* ### IO 密集型指的是系統的 CPU 性能相對硬盤、內存要好很多，此時，系統運作，大部分的狀況是 CPU 在等 IO (硬盤 / 內存) 的讀寫操作，因此，CPU 負載並不高。
		* ### 密集型的程序一般在達到性能極限時，CPU 佔用率仍然較低。這可能是因為任務本身需要大量 I/O 操作，而程序的邏輯做得不是很好，沒有充分利用處理器能力。
		* ### CPU 使用率較低，程序中會存在大量的 I/O 操作佔用時間，導致線程空餘時間很多，通常就需要開 CPU 核心數數倍的線程。
		* ### 其計算公式為: IO 密集型核心線程數 = CPU 核數 / (1 - 阻塞係數)。
		* ### 當線程進行 I/O 操作 CPU 空閒時，啟用其他線程繼續使用 CPU，以提高 CPU 的使用率。例如: 數據庫交互、文件上傳下載、網絡傳輸等。
	* ### CPU 密集型任務與 IO 密集型任務的區別
		* ### CPU 密集型任務的特點是要進行大量的計算，消耗 CPU 資源，全靠 CPU 的運算能力。這種計算密集型任務雖然也可以用多任務完成，但是任務越多，花在任務切換的時間就越多，CPU 執行任務的效率就越低，所以，要最高效地利用 CPU，計算密集型任務同時進行的數量應當等於 CPU 的核心數，避免線程或進程的切換。
		* ### 計算密集型任務由於主要消耗 CPU 資源，因此，代碼運行效率至關重要。Python 這樣的腳本語言運行效率很低，完全不適合計算密集型任務。對於計算密集型任務，最好用 C 語言編寫。
		* ### IO 密集型任務的特點是 CPU 消耗很少，任務的大部分時間都在等待 IO 操作完成 (因為 IO 的速度遠遠低於 CPU 和內存的速度)。涉及到網絡、磁盤 IO 的任務都是 IO 密集型任務。
		* ### 對於 IO 密集型任務，線程數越多，CPU 效率越高，但也有一個限度。
	* ### 一個計算為主的應用程序 (CPU 密集型程序)，多線程可以充分利用起所有的 CPU 核心數，比如說 16 核的 CPU，開 16 個線程的時候，可以同時跑 16 個線程的運算任務，此時是最大效率。但是如果線程數遠遠超出 CPU 核心數量，反而會使得任務效率下降，因為頻繁的切換線程或進程也是要消耗時間的。因此對於 CPU 密集型的任務來說，線程數等於 CPU 數是最好的了。
	* ### 如果是一個磁盤或網絡為主的應用程序 (IO 密集型程序)，一個線程處在 IO 等待的時候，另一個線程還可以在 CPU 裡面跑，有時候 CPU 閒著沒事幹，所有的線程都在等著 IO，這時候他們就是同時的了，而單線程的話，此時還是在一個一個等待的。我們都知道 IO 的速度比起 CPU 來是很慢的。此時線程數可以是 CPU 核心數的數倍 (視情況而定)。
	* ### CPU 密集型，使用 multiprocessing。
	* ### IO 密集型，使用 multiprocessing.dummy。
	* ### The concurrent.futures module provides a high-level interface for asynchronously executing callables.
	* ### threading 重點摘要
		* ### 透過 context-switch 的方式實現。
		* ### 透過 CPU 的不斷切換 (context-switch)，實現平行的功能。
		* ### 大量使用 threading 執行平行的功能時，會因為大量的 context-switch，「實現了程式平行的功能，但也因為大量的 context-switch，使得程式執行速度更慢」。
	* ### multiprocessing 重點摘要
		* ### multiprocessing 在資料傳遞上，會因為需要將資料轉移至其他 CPU 上進行運算。
		* ### 因此會需要考慮資料搬運的時間，而多核心真正的實現「平行運算的功能」，當任務較為複雜時，效率一定比較好。
	* ### join() 方法可以等待子進程結束後再繼續往下運行 (更準確地說，在當前位置阻塞主進程，待執行 join() 的進程結束後再繼續執行主進程)，通常用於進程間的同步。(進一步地解釋，哪個子進程調用了 join 方法，主進程就要等該子進程執行完後才能繼續向下執行)
	* ### multiprocessing.Pool 可取得回傳結果，並讓系統自動分配資源。
	* ### multiprocessing.Process 不會回傳結果。
	* ### 執行 pool 內的任務的時候，使用「map」將任務一個個分配下去。
	* ### Pool 內可以使用參數 processes = 「想要的 CPU 核數量」，例如: pool = mp.Pool(processes=4) ，就是我們指定了 4個 CPU 核 (預設就是 CPU 的對應核心數量)。
	* ### map 可以傳入一個 list 使其迭代，而 apply_async 不行。
	* ### map 會等待 map 的任務執行完後，才執行接下來的主程式。
	* ### apply_async 不等待 apply_async 的任務執行完，就會執行接下來的主程式。
	* ### thread 可直接使用全域變數 (global) 交換資訊。
	* ### multiprocess 需透過設定特定通道 (多核心執行的中央變數管理) 才能拿到資訊。
	* ### thread 適合小任務、資訊共用的任務 (直接拿 global 資訊來用)。
	* ### multiprocess 適合大任務、資訊獨立的任務 (把相關資訊交由其他核心處理後，不太需要拿取新資訊)。
	* ### python 的 thread 實作使用 GIL (global interpreter lock) 保護程式取用資料衝突的機制。
	* ### ![image](https://raw.githubusercontent.com/GitHub-WeiChiang/main/master/Python/thread%20%E8%88%87%20multiprocess%20%E6%AF%94%E8%BC%83.png)
* ### 關於底線
	* ### 單底線: 這個回傳值我不要了。
	* ### 前單底線: 表示 private，不要碰我。
	* ### 後單底線: 如果非得用保留字當變數名，加上去吧。
	* ### 前雙底線: 我自己是用這個表示 private 啦。
	* ### 前後雙底線: 這個方法是內建原有的，你可以覆寫它。
* ### 關於底線 2 (Protected, Private Members)
	* ### Python's convention to make an instance variable protected is to add a prefix _ (single underscore) to it. This effectively prevents it from being accessed unless it is from within a sub-class.
	* ### The double underscore __ prefixed to a variable makes it private. It gives a strong suggestion not to touch it from outside the class.
* ### \_\_call\_\_()
	* ### Python 中的函数是一级对象，这意味着 Python 中的函数的引用可以作为输入传递到其它的函数中并被执行。
	* ### 而 Python 中类的实例可以被当做函数对待，也就是说，可以将它们作为输入传递到其它的函数中并调用他们，正如我们调用一个正常的函数那样。
	* ### 而类中 \_\_call\_\_() 函数的意义正在于此，为了将一个类实例当做函数调用，我们需要在类中实现 \_\_call\_\_() 方法。
	```
	class Sample(object):
		def __init__(self):
			self.a = 0
			self.b = 0

		def __call__(self, a, b):
			self.a = a
			self.b = b
			print('__call__ with （{}, {}）'.format(self.a, self.b))
	

	>>> sample = Sample()
	>>> sample(1,2)
	__call__ with (1, 2)
	```
* ### Python 魔法方法 \_\_getattr\_\_
	```
	class MyClass:
		def __init__(self, x):
			self.x = x

		def __getattr__(self, item):
			print('找不到 {} 啦'.format(item))
			return None


	>>> obj = MyClass(1)
	>>> obj.x
	1
	>>> obj.y
	找不到 y 啦
	None
	```
	* ### 定義一個 MyClass 類，設定一個例項屬性為 x，值為 1，obj 為這個類的例項，獲取 obj.x 返回 1，而獲取 obj.y 發現屬性找不到，原因是 obj 的例項變數中不包含 y，找不到某屬性時會呼叫 \_\_getattr\_\_ 方法。
	* ### 呼叫 \_\_getattr\_\_ 詳細過程如下
		* ### 在物件的實例項屬性中尋找 (找不到執行第二步)
		* ### 來到物件所在的類中查詢類屬性 (找不到執行第三步)
		* ### 來到物件的繼承鏈上尋找 (找不到執行第四步)
		* ### 呼叫 \_\_getattr\_\_ 方法，如果使用者沒有定義或者還是找不到，丟擲 AttributeError 異常，屬性查詢失敗。
		```
		class MyClass:
			def __init__(self, x):
				self.x = x


		>>> obj = MyClass(1)
		>>> obj.y

		AttributeError: 'MyClass' object has no attribute 'a'
		```
* ### Python 魔法方法 \_\_getattribute\_\_
	* ### 當我們呼叫物件的屬性時，首先會呼叫 \_\_getattribute\_\_ 魔法方法。
	```
	obj.x
	obj.__getattribute__(x)
	```
	* ### 上兩行代碼為等價，當 \_\_getattribute\_\_ 查詢失敗，就會去呼叫 \_\_getattr\_\_ 方法。
	```
	class MyClass:
		def __init__(self, x):
			self.x = x

		def __getattribute__(self, item):
			print('正在獲取屬性 {}'.format(item))
			return super(MyClass, self).__getattribute__(item)


	>>> obj = MyClass(2)
	>>> obj.x
	正在獲取屬性 x
	2
	```
	* ### 使用 \_\_getattribute\_\_ 魔法方法時，要返回父類的方法。
	* ### 內建的 getattr 和 hasattr 也會觸發這個魔法方法。
	```
	>>> getattr(obj, 'x', None)
	正在獲取屬性 x
	2
	>>> hasattr(obj, 'x', None)
	正在獲取屬性 x
	True
	```
* ### if __name__ == "__main__":
	* ### 建立一個 Module (tool.py) 與主程式 (main.py)
		```
		# tool.py

		def func1():
			print("In func1")

		def func2():
			print("In func2")

		print("in tool.py")

		# -------------------------

		# main.py

		import tool

		tool.func1()
		tool.func2()
		```
	* ### 執行上述代碼
		```
		python3 main.py

		in tool.py
		In func1
		In func2
		```
	* ### Python 在引入 Module 時做了什麼事情 ?
		```
		# main.py

		import tool

		tool.func1()
		tool.func2()
		```
		* ### 替這一個 Module 建立一些特別的變數 (例如: __name__)。
		* ### 執行 Module 中的每一行程式碼。
		* ### 如果只是想使用 tool 中定義的 func1() 與 func2() 並不希望執行 tool 最後的 print，這時候就可以透過 ```if __name__ == "__main__"``` 達到目的。
	* ### 了解 __name__ 的值
		* ### 當一個 Module 是直接被執行時 (python3 module_name.py)，則 __name__ 為 "__main__"。
		* ### 當一個 Module 是被引入時，則 __name__ 設為 "檔案名稱"。
	* ### 透過 if __name__ == "__main__": 可避免 Module 中的部分程式碼在 "被引入" 時執行。
<br />

Reference
=====
* ### Python 3.7 技術手冊
