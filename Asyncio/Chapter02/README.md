Chapter02 Thread 的真相
=====
* ### 執行緒的優點
    * ### 易於閱讀: 因為函數內是執行緒安全的，由上而下執行。
    * ### 共享記憶體: 可以利用多 CPU 特性，並且能夠共享記憶體，當然在 CPU 間的資料交換需要一定的成本。
    * ### 經驗: 可以在遇到問題時從網路查到很多需要的資源。
* ### GIL (Global Interpreter Lock): 雖然說執行緒表面上能夠達到平行化，但如果使用 CPython 直譯器，會遇到 GIL 問題，因為它控制在同一時間內，只有一個原生執行緒執行 Python 位元碼 (可以使用 Cython 或 Numba 避免)。
* ### 執行緒的最佳實踐，建議採用 concurrent.futures 模組的 ThreadPoolExecutor，透過 submit() 傳遞必要資料。
```
from concurrent.futures import ThreadPoolExecutor

def worker(data):
    # 資料處理

...

with ThreadPoolExecutor(max_workers=10) as exe:
    future = exe.submit(worker, data)
```
* ### 上述程式碼中，可以透過將 ThreadPoolExecutor (並行) 修改為 ProcessPoolExecutor (平行) 以使用子行程池，484 非常的方便勒。
* ### 應盡量避免執行緒存取全域變數。
* ### 執行緒的缺點
    * ### 難以處理: 臭蟲與競速問題，如果從頭開始好好設計還好說，如果接到一個為了趕時間而不講武德亂寫的專案，耗子尾汁...
    * ### 資源密集: 簡單說就是，作業系統需要資源建立執行緒，比如為執行緒配置堆疊空間 (會消耗虛擬記憶體)，這是個大問題，因為它會佔用比與其還要多非常多的空間。
    * ### 影響產能: 大規模並行會因為 context switch 影響 throughput (吞吐量)。
    * ### 缺乏彈性: 應該說，在執行緒的世界中，OS 排班器有點笨，無論執行緒是否因為 I/O 作業在進行等待，OS 排班器會在執行緒間來回不斷切換。
    * ### 總結: 不良的執行緒設計反而更加難以理解，且對於大規模並行作業而言，執行緒不一定比較有效率。
* ### 範例程式碼中的狀況
    * ### 閱讀理解難易度基本上還算可接受。
    * ### 測試上幾乎也都成功。
    * ### 但有可能因為競速導致結果不如預期。
    * ### 不如預期的結果難以重現。
```
# 問題出在這
def change(self, knives, forks):
    self.knives += knives
    self.forks += forks
    
# 當然可以透過以下方法修正
def change(self, knives, forks):
    with self.lock:
        self.knives += knives
        self.forks += forks
```
* ### 當代碼在可控制範圍內，修補這個錯誤並不困難，但不是所有應用場景都這麼容易除錯。
* ### 要找到問題所在，往往可能需要看完並理解所有的程式碼才行。
* ### 在範例中當然也可以只使用一隻機器人完成所有工作。
* ### 不過更棒的是使用 Asyncio !!
<br />
